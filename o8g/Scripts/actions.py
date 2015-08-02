    # Python Scripts for the Doomtown CCG definition for OCTGN
    # Copyright (C) 2012  Konstantine Thoukydides

    # This python script is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this script.  If not, see <http://www.gnu.org/licenses/>.

#---------------------------------------------------------------------------
# Global variables
#---------------------------------------------------------------------------

playerside = None # Variable to keep track on which side each player is
playeraxis = None # Variable to keep track on which axis the player is
strikeCount = 0 # Used to automatically place strikes
posSideCount = 0 # Used to automatically place in-town deeds 
negSideCount = 0 # Same as above
handsize = 5 # Used when automatically refilling your hand
OutfitCard = None
PlayerColor = "#" # Variable with the player's unique colour.

harrowedDudes = {} # Which dudes are harrowed
ValueMemory = {} # Which cards have amodified value
AttachedCards = {} # A dictionary which holds a coutner for each card, numbering how many attached cards each card has.
InfluenceRAM = {} # Which cards have extra influence
ControlRAM = {} # Which cards have extra cp

#---------------------------------------------------------------------------
# Phases
#---------------------------------------------------------------------------
   
def showCurrentPhase(phase = 1): # Just say a nice notification about which phase you're on.
   notify(phases[phase].format(me))
   
def nextPhase(group = table, x = 0, y = 0):  
# Function to take you to the next phase. 
   mute()
   if getGlobalVariable('Shootout') == 'True':
      if not confirm("There's still a shootout ongoing. Do you want to end it and move to the next phase?"): return
      else: goToShootout()
   phase = int(getGlobalVariable('Phase'))
   if phase == 4: phase = 1 # In case we're on the last phase (Nightfall), go back to the first game phase (Gamblin')
   else: phase += 1 # Otherwise, just move up one phase
   if phase == 1: goToGamblin()
   elif phase == 2: goToUpkeep()
   elif phase == 3: goToHighNoon()
   elif phase == 4: goToNightfall()

def goToGamblin(group = table, x = 0, y = 0): # Go directly to the gamblin' phase
   mute()
   if getGlobalVariable('Phase') != '1': # We double check someone hasn't moved us to the gamblin' phase by now
      setGlobalVariable('Phase','1')
      showCurrentPhase(1)
      clearShootout() # Clear any Shootout and/or Draw Hand Cards remaining on the table.
      getPotCard() # Create the PotCard to allow the players to bet manually if need be
      for player in getActivePlayers(): remoteCall(player,'atTimedEffects',["Gamblin"])
      for card in table:
         if card.model == '53a212a6-34a6-47b0-bb24-45f1888bebf6': delCard(card)

def goToUpkeep(group = table, x = 0, y = 0): # Go directly to the Upkeep phase
   mute()
   if getPotCard(True) and not confirm("You seem to have not declared the Winner of lowball? (Winner needs to press Ctrl+W)\n\nBypass?"): return
   clearPotCard()
   setGlobalVariable('Phase','2')
   clearShootout() # For clearing any leftover lowball draw hands.
   showCurrentPhase(2)
   for player in getActivePlayers(): remoteCall(player,'atTimedEffects',["Upkeep"])

def goToHighNoon(group = table, x = 0, y = 0): # Go directly to the High Noon phase
   mute()
   if me.getGlobalVariable('UpkeepDone') == 'False':
      if confirm("You do not seem to have completed your upkeep yet. Do so now?\n (Pressing No will remain in the upkeep phase so that you have a chance to discard dudes)"): upkeep()
      return # We always return aftewards because upkeep will anyway come back to High Noon if all players have finished their upkeep.
   for player in getActivePlayers():
      if player != me and player.getGlobalVariable('UpkeepDone') == 'False':
         while not confirm("The other players have not yet finished their upkeep phase. Bypass?\n\nPressing 'No' will prompt them to finish their upkeep"): 
            notify(":> {} is waiting for {} to finish their upkeep phase...".format(me,player))
   clearPotCard()
   setGlobalVariable('Phase','3')
   clearHandRanks() # Just in case it was forgotten
   showCurrentPhase(3)
   for player in getActivePlayers(): remoteCall(player,'atTimedEffects',["High Noon"])

def goToNightfall(group = table, x = 0, y = 0): # Go directly to the Nightfall phase
   mute()
   clearPotCard()
   setGlobalVariable('Phase','4')
   clearHandRanks() # Just in case it was forgotten
   showCurrentPhase(4)   
   for player in getActivePlayers(): remoteCall(player,'atTimedEffects',["Sundown"])

def goToShootout(group = table, x = 0, y = 0, silent = False): # Start or End a Shootout Phase
   mute()
   if getGlobalVariable('Shootout') == 'False': # The shootout phase just shows a nice notification when it starts and does nothing else.
      jobPosse = [c for c in table if c.highlight == InitiateColor]
      if getGlobalVariable('Job Active') != 'False' and len(jobPosse) and jobPosse[0].controller == me: remoteCall(me,'completeJob',[]) # If there's no current shootout but there's a job ongoing with us as the leader, we assume the job just ended without a shootout.
      else:
         if not silent: 
            if getGlobalVariable('Job Active') != 'False': notify("{} is defending against the job. A shootout has broken out!".format(me))
            elif getGlobalVariable('Mark') != 'None': 
               notify("{} accepts the call out. A shootout begins!".format(Card(num(getGlobalVariable('Mark')))))
               joinDefence(Card(num(getGlobalVariable('Mark'))),silent = True)
            else: notify("A shootout is breaking out!".format(me))
         setGlobalVariable('Shootout','True')
         for card in table: 
            if card.highlight == InitiateColor: 
               card.highlight = AttackColor # If a shootout breaks out, all cards in the existing (initiating) posse join the shootout.
               if getGlobalVariable('Job Active') == 'False': executePlayScripts(card, 'PARTICIPATION') # If they were part of a job posse, then these scripts have already been triggered, so we don't do it again.
         atTimedEffects("ShootoutStart")
   else: # When the shootout ends however, any card.highlights for attacker and defender are quickly cleared.
      notify("The shootout has ended.".format(me))
      if getGlobalVariable('Job Active') != 'False': remoteCall(me,'completeJob',[])
      else:
         clearShootout()
         setGlobalVariable('Mark','None') # We also clear the Called Out variable just in case
         atTimedEffects("ShootoutEnd")

def completeJob():
   mute()
   jobResults = eval(getGlobalVariable('Job Active'))
   jobCard = Card(num(jobResults[0]))
   leader = Card(num(jobResults[3]))
   if jobCard.controller != me: remoteCall(jobCard.controller,'completeJob',[])
   else:
      if getGlobalVariable('Shootout') == 'True': jobPosse = [c for c in table if c.highlight == AttackColor]
      else: jobPosse = [c for c in table if c.highlight == InitiateColor]
      iter = 0
      for card in jobPosse: # at the end of jobs, we send the leader's posse home booted
         card.orientation = Rot90
         if playeraxis == Xaxis: card.moveToTable(homeDistance(card) + (playerside * cwidth(card,-4)) + (iter * cardDistance()), 0)
         elif playeraxis == Yaxis: card.moveToTable(0,homeDistance(card) + (playerside * cheight(card,-4)) + (iter * cardDistance()))
         orgAttachments(card)            
         iter += 1
         card.markers[mdict['BulletShootoutPlus']] = 0 # We need to clear these to prevent job effects from taking them into account. E.g. Desolation row.
         card.markers[mdict['BulletShootoutMinus']] = 0 
         card.markers[mdict['ValueShootoutPlus']] = 0 
         card.markers[mdict['ValueShootoutMinus']] = 0 
      if len(jobPosse): notify("{} is successful and the job posse {} goes home booted".format(jobCard,[c.name for c in jobPosse]))
      else: notify("{} is unsuccessful".format(jobCard))
      if confirm("Did the {} job succeed?".format(jobCard.Name)): # If we actually have scripts in the job, we try to execute them.
         if re.search(r'-MarkNotTheTarget',jobResults[1]): targetCards = None
         elif re.search(r'-LeaderIsTarget',jobResults[1]): targetCards = [leader]
         else: targetCards = [Card(eval(getGlobalVariable('Mark')))]
         executeAutoscripts(jobCard,jobResults[1].replace('++','$$'),action = 'USE',targetCards = targetCards) # If the spell is succesful, execute it's effects
      elif jobResults[2] != 'None': # Otherwise we execute the job fail scripts
         if re.search(r'-MarkNotTheTarget',jobResults[1]): targetCards = None
         elif re.search(r'-LeaderIsTarget',jobResults[1]): targetCards = [leader]
         else: targetCards = [Card(eval(getGlobalVariable('Mark')))]
         executeAutoscripts(jobCard,jobResults[2].replace('++','$$'),action = 'USE',targetCards = targetCards) # If the spell is succesful, execute it's effects
      if getGlobalVariable('Shootout') == 'True': 
         if getGlobalVariable('Shootout') == 'True': atTimedEffects("ShootoutEnd")
      setGlobalVariable('Mark','None') # We also clear the Called Out variable just in case
      clearShootout()
#---------------------------------------------------------------------------
# Table group actions
#---------------------------------------------------------------------------

def defaultAction(card, x = 0, y = 0):
   debugNotify(">>> defaultAction()") #Debug
   mute()
   Mark = getGlobalVariable('Mark') # We grab this global variable so that we don't have to check it multiple times and delay them game
   leadingPosse = [c for c in table if c.highlight == InitiateColor]
   if card.model == 'c421c742-c920-4cad-9f72-032c3378191e': # If the player has double-clicked the lowball card, we assume they are the ones that won lowball.
      if confirm("Did you win this round's lowball?"): winLowball()
   if card.model == 'ac0b08ed-8f78-4cff-a63b-fa1010878af9': # If the player has double-clicked the Town Square card, we assume it's a mistake
      pass
   elif card.highlight == DrawHandColor: 
      card.highlight = None
      notify("{} moves {} from their draw hand into play".format(me,card))
      if card.Type == 'Goods' or card.Type == 'Spell':
         hostCard = findHost(card)
         if hostCard: 
            attachCard(card,hostCard)
            notify(":> {} was attached to {}".format(card,hostCard))
      reCalculate(notification = 'silent')
   elif getGlobalVariable('Shootout') == 'True' and card.Type == 'Dude':
      if not participateDude(card): boot(card) # If the dude is already participating, then just boot them.
   elif card.Type == 'Dude' and Mark != 'None' and getGlobalVariable('Job Active') != 'False' and len(leadingPosse):
      if card.controller != leadingPosse[0].controller: defend(card) # if there is a job in progress, anyone but the leader double clicking one of their dudes will defend it or join it.
      elif not participateDude(card): boot(card) 
   elif card.Type == 'Dude' and len([c for c in table if c.Type == 'Dude' and c.targetedBy and c.targetedBy == me and c.controller != me]) and Mark == 'None': # If the player has an opposing dude targeted when they doubled clicked, we assume they want to call out
      callout(card)
   elif Mark != 'None' and Card(num(Mark)) == card: # if there is a callout in progress and we just double clicked the callout's target, we assume they want to accept it.
      defend(card)
   elif card.Type == 'Spell' and card.orientation != Rot90 and confirm("Are you trying to cast this spell?"):
      if CardsAA.get(card.model,None): useAbility(card)
      else: 
         pull()
         boot(card)
   else: boot(card)
   debugNotify("<<< defaultAction()") #Debug

def setup(group,x=0,y=0):
# This function is usually the first one the player does. It will setup their home and cards on the left or right of the playfield 
# It will also setup the starting Ghost Rock for the player according to the cards they bring in play, as well as their influence and CP.
   global OutfitCard # Import some necessary variables we're using around the game.
   debugNotify(">>> setup()")
   mute()
   if me.getGlobalVariable('playerOutfit') != 'None' and not confirm("Are you sure you want to setup for a new game? (This action should only be done after a table reset)"): return # We make sure the player intended to start a new game
   resetAll()
   for player in getPlayers(): # We check that all players have loaded a deck before proceeding to choose side
      if len(player.Deck) == 0:
         if not confirm("Have all non-spectators loaded a deck? (If not, the game sides will not setup correctly)"): return
         else: break
   chooseSide() # The classic place where the players choose their side.
   me.Deck.shuffle() # First let's shuffle our deck now that we have the chance.
   if len([c for c in table if c.name == 'Town Square']) == 0: # Only create a Town Square token if there's not one in the table until now
      TSL = table.create("ac0b08ed-8f78-4cff-a63b-fa1010878af9",-170,-50, 1, True) # Create a Town Square card in the middle of the table.
      TSL.anchor = True
      #TSR = table.create("72f6c0a9-e4f6-4b17-9777-185f88187ad7",-1,0, 1, True) # Create a Right Town Square card in the middle of the table.
   for card in me.hand: # For every card in the player's hand... (which should be an outfit and a bunch of dudes usually)
      if card.Type == "Outfit" :  # First we do a loop to find an play the outfit, (in case the player managed to mess the order somehow)
         placeCard(card,'SetupHome')
         me.GhostRock += num(card.properties['Cost']) # Then we add its starting Ghost Rock to the bank
         me.setGlobalVariable('playerOutfit',card.Outfit)
         OutfitCard = card # We make a note of the outfit the player is playing today (used later for upkeep)
         concat_home = '{}'.format(card) # And we save the name.
   if me.getGlobalVariable('playerOutfit') == 'None': # If we haven't found an outfit in the player's hand, we assume they made some mistake and break out.
      whisper(":::ERROR:::  You need to have an outfit card in your hand before you try to setup the game. Please reset the board, load a valid deck and try again.")
      return
   debugNotify("About to place Dudes",2)
   dudecount = 0
   concat_dudes = 'and has the following starting dudes: ' # A string where we collect the names of the dudes we bring in
   concat_other = '' # A string to remember any other card (like sweetrock's mine)
   for card in me.hand: # For every card in the player's hand... (which should a bunch of dudes now)
      debugNotify("Placing {}".format(card),4)
      if card.Type == "Dude" : # If it's a dude...
         placeCard(card,'SetupDude',dudecount)
         dudecount += 1 # This counter increments per dude, ad we use it to move each other dude further back.
         payCost(card.Cost) # Pay the cost of the dude
         #modInfluence(card.Influence, silent) # Add their influence to the total
         concat_dudes += '{}. '.format(card) # And prepare a concatenated string with all the names.
      else: # If it's any other card...
         placeCard(card,'SetupOther')
         payCost(card.Cost) # We pay the cost 
         modControl(card.Control) # Add any control to the total
         #modInfluence(card.Influence) # Add any influence to the total
         concat_other = ', brings {} into play'.format(card) # And we create a special concat string to use later for the notification.
   reCalculate(notification = 'silent')
   if dudecount == 0: concat_dudes = 'and has no starting dudes. ' # In case the player has no starting dudes, we change the notification a bit.
   refill() # We fill the player's play hand to their hand size (usually 5)
   notify("{} is playing {} {} {}Starting Ghost Rock is {} and starting influence is {}.".format(me, concat_home, concat_other, concat_dudes, me.GhostRock, me.Influence))  
   # And finally we inform everyone of the player's outfit, starting dudes & other cards, starting ghost rock and influence.
   
def Pass(group, x = 0, y = 0): # Player says pass. A very common action.
   notify('{} Passes.'.format(me))

def Ready(group, x = 0, y = 0): # Player says ready. A very common action.
   notify('{} is Ready!'.format(me))

def clearShootout(remoted = False):
   if not remoted:
      setGlobalVariable('Shootout','False')
      for player in getActivePlayers():
         if player != me: remoteCall(player,'clearShootout',[True])
      clearHandRanks()  # Clear the Hand Ranks, in case one is leftover.
      setGlobalVariable('Mark','None')
      setGlobalVariable('Job Active','False')
   announcedLeader = False
   for card in table:
      if card.controller == me:
         if card.highlight == DefendColor or card.highlight == AttackColor or card.highlight == InitiateColor:
            if card.highlight == AttackColor:
               if not announcedLeader: notify(":::INFO::: {} was the Leader in this shootout.".format(card.controller))
               announcedLeader = True
            card.highlight = None
            executePlayScripts(card, 'UNPARTICIPATE')
         card.markers[mdict['BulletShootoutPlus']] = 0 
         card.markers[mdict['BulletShootoutMinus']] = 0 
         card.markers[mdict['ValueShootoutPlus']] = 0 
         card.markers[mdict['ValueShootoutMinus']] = 0 
         if card.model == '94fe7823-077c-4abd-9278-6e64bda6dc64' or card.model == 'c4689399-c350-46b3-a79a-f8c62d926cd5': delCard(card) # If it's a gunslinger or nature token, we remove it from the game.
   clearDrawHandonTable()
   clearRemainingActions(True) # Clear any shootout actions used (common mistake)
   me.setGlobalVariable('RevealReady','False')
      
def boot(card, x = 0, y = 0, silent = False, forced =  None): # Boot or Unboot a card. I.e. turn it 90 degrees sideways or set it straight.
   mute()
   if card.controller != me: 
      remoteCall(card.controller,'boot',[card,0,0,silent,forced])
      return
   result = 'OK'
   if forced == 'boot':
      if card.orientation == Rot90: 
         if not silent: notify(":> Tried to boot {} but it was already booted.".format(card))
         result = 'FAIL'
      else: card.orientation = Rot90
   elif forced == 'unboot':
      if card.orientation == Rot0: 
         if not silent: notify(":> Tried to unboot {} but it was already unbooted.".format(card))
         result = 'FAIL'
      else: card.orientation = Rot0
   else: card.orientation ^= Rot90 # This function rotates the card +90 or -90 degrees depending on where it was.
   if card.orientation == Rot90: # if the card is now at 90 degrees, then announce the card was booted
      if not silent: notify('{} boots {}'.format(me, card))
   else: # if the card is now at 0 degrees (i.e. straight up), then announce the card was unbooted
      if not silent: notify('{} unboots {}'.format(me, card))
   debugNotify("<<< boot(). {} result for {}".format(result,card))
   return result

def ace(card, x = 0, y = 0, silent = False): # Ace a card. I.e. kill it and send it to the boot hill (i.e.graveyard)
   debugNotify(">>> ace()") #Debug
   mute()
   cardowner = card.owner # We need to save the card onwer for later
   if card.highlight != DrawHandColor: # We don't want to do anything else except move cards when they're not really in play.
      if card.markers[mdict['Bounty']]: notify("{} was wanted! Don't forget to collect {} bounty.".format(card,card.markers[mdict['Bounty']])) # Remind the player to take a bounty for wanted dudes.
      #cardRMsync(card) # This function removes any Influence and Control Points that card had from your total. 
                       # We need to do it before the card is moved to the boot hill because by then, the markers are removed.
   # Remind the player to take a bounty for wanted dudes. In the future this will be automated.
   if not silent: 
      if card.highlight != DummyColor: notify("{} has aced {}.".format(me, card))
      else: notify("{} has cleared the resident effect of {}.".format(me, card))
   clearAttachLinks(card,'Ace')
   card.moveTo(cardowner.piles['Boot Hill']) # Cards aced need to be sent to their owner's boot hill
   reCalculate(notification = 'silent')
   debugNotify("<<< ace()") #Debug


def aceTarget(table = table, x = 0, y = 0, silent = False, targetCards = None):
   mute()
   if not targetCards: targetCards = [c for c in table if c.targetedBy and c.targetedBy == me]
   if not len(targetCards): notify(":::ERROR::: You need to target the card you're trying to ace with this action")
   for card in targetCards:
      if card.controller != me: 
         if card.markers[mdict['Bounty']]:
            me.GhostRock += card.markers[mdict['Bounty']]
            notify(":> {} gains {} Ghost Rock for acing {}".format(me,card.markers[mdict['Bounty']],card))
         remoteCall(card.controller,'ace',[card,0,0,silent])
      else: ace(card, silent = silent)
      
def discard(card, x = 0, y = 0, silent = False): # Discard a card.
   if card.model == 'ac0b08ed-8f78-4cff-a63b-fa1010878af9': return
   if card.controller != me: 
      remoteCall(card.controller,"discard",[card])
      return
   debugNotify(">>> discard()") #Debug
   mute()
   cardowner = card.owner
   if card.highlight != DrawHandColor and card.highlight != EventColor: # If the card being discarded was not part of a draw hand
      if getGlobalVariable('Shootout') == 'True' and card.markers[mdict['Bounty']]: notify("{} was wanted! Don't forget to collect {} bounty.".format(card,card.markers[mdict['Bounty']])) # Remind the player to take a bounty for wanted dudes.
      #cardRMsync(card) # Then remove it's influence / CP from the player's pool
      if not silent: 
         if card.highlight != DummyColor: notify("{} has discarded {}.".format(me, card))
         else: notify("{} has cleared the resident effect of {}.".format(me, card))
   clearAttachLinks(card,'Discard')
   reCalculate(notification = 'silent')
   if (card.highlight == EventColor and re.search('Ace this card', card.Text)) or (card.Type == 'Joker' and card.highlight == DrawHandColor): # If the card being discarded was an event in a lowball hand or a joker in a draw hand
                                                                                                        # And that card had instructions to be aced
      card.moveTo(cardowner.piles['Boot Hill'])                                                         # Then assume player error and ace it now        
      if card.Type == 'Joker': notify("{} has been aced as per card instructions.".format(card)) # And inform the players.
      else: notify("{} was the active event and has been aced as per card instructions.".format(card)) 
   else: card.moveTo(cardowner.piles['Discard Pile']) # Cards aced need to be sent to their owner's discard pile
   debugNotify("<<< discard()") #Debug

def discardTarget(table = table, x = 0, y = 0, silent = False, targetCards = None):
   mute()
   if not targetCards: targetCards = [c for c in table if c.targetedBy and c.targetedBy == me]
   if not len(targetCards): notify(":::ERROR::: You need to target the card you're trying to discard with this action")
   for card in targetCards:
      if card.controller != me: 
         if card.markers[mdict['Bounty']]:
            me.GhostRock += card.markers[mdict['Bounty']]
            notify(":> {} gains {} Ghost Rock for discarding {}".format(me,card.markers[mdict['Bounty']],card))
         remoteCall(card.controller,'discard',[card,0,0,silent])
      else: discard(card,silent = silent)
   
   
def upkeep(group = table, x = 0, y = 0): # Automatically receive production and pay upkeep costs
# This function goes through each of your cards and checks if it provides production or requires upkeep, then automatically removes it from your bank.
   if getGlobalVariable('Phase') != '2': #One can only call for upkeep during the upkeep phase
      if not confirm(":::WARNING::: It is not yet the Upkeep phase. Do you want to jump to upkeep now?"): return
      goToUpkeep()
   mute()
   gr = 0 # Variable used to track each cards production/upkeep
   concat_prod = '' # A string which we will use to provide a succint notification at the end
   concat_upk = '' # Same as above
   upkeep_concats_dict = {}
   prod = 0 # Variable to track total production received.
   upk = 0 # Variable to track total upkeep paid.
   cards = (card for card in table # Create a group with all the cards you own and control on the table.
                 if (card.owner == me or card.highlight == me.color) # you cannot pay or produce from cards you do not own.
                 and card.controller == me  # you cannot pay or produce from cards you do not control.
                 and card.highlight != DrawHandColor) # And avoid counting lowball cards
   for card in cards: # For each card...
      TownHall = findMarker(card, 'Town Hall')
      cardUpkeep = num(card.Upkeep)
      if TownHall: # If the card is affected by the town hall, then we want to reduce its upkeep by its influence
         cardUpkeep -= compileCardStat(card, stat = 'Influence')
         if cardUpkeep < 0: cardUpkeep = 0
         card.markers[TownHall] = 0
      gr = num(card.Production) - cardUpkeep + card.markers[mdict['ProdPlus']] - card.markers[mdict['ProdMinus']]
      # Grab its production value (usually 0 for most non-deeds) then 
      # add the amount of any +production markers you have on the card and remove the amount of any -production markers you have on the card.
      if (card.Outfit != me.getGlobalVariable('playerOutfit') and # If a non-drifter dude is not from the player's outfit, 
         card.Outfit != 'Drifter' and 
         card.Outfit != 'DR' and  # they need to play an extra GR upkeep per influence.
         card.Type == 'Dude' and
         num(card.Influence) + card.markers[mdict['InfluencePlus']] - card.markers[mdict['InfluenceMinus']] > 0): 
         gr -= (num(card.Influence) + card.markers[mdict['InfluencePlus']] - card.markers[mdict['InfluenceMinus']])
      if gr > 0: # If we still have any production left after removing jailbroken penalties, 
                 # then we increment the total production we have for this turn 
                 # and add the name of the card to our concatenated string of all the cards that produced this turn
         prod += gr
         concat_prod += '{} GR from {}. '.format(str(gr),card) # This is where the concatenation happens
      elif gr < 0: # Much like production, we only add the name to the string if it's having any upkeep
         if gr < -3:
            if not confirm("{} has {} upkeep. Are you sure you want to pay their upkeep this turn? (Pressing No will discard them)".format(card.name,abs(gr))): 
               discard(card)
               continue
         upk += abs(gr) # Add the negative gr as a positive amount to the variable, so that we can compare it later to  our remaining GR.
         #concat_upk += '{} GR for {}. '.format(str(gr),card)
         upkeep_concats_dict[card] = ('{} GR for {}. '.format(str(gr),card), abs(gr)) # We make a tuple of the string to add and the money we have to pay
   if upk > 0 and me.GhostRock + prod - upk < 0: 
      upkDudes = [(dude, upkeep_concats_dict[dude][1]) for dude in upkeep_concats_dict]
      while len(upkDudes) and me.GhostRock + prod - upk < 0:
         choice = SingleChoice("You do not have enough money to pay your upkeep this turn. Choose one of your dudes with upkeep to discard.\n\n(You need to reduce your upkeep by {}. Close this window to discard nobody else.)".format(abs(me.GhostRock + prod - upk)),["{} - {} upk".format(dude[0].name,dude[1]) for dude in upkDudes])
         if choice == None: break # If they close the window, we assume they're going to keep their dudes, even if they cannot pay them (card effects?)
         unpaid_dude = upkDudes.pop(choice)
         discard(unpaid_dude[0])
         upk -= unpaid_dude[1]
         upkeep_concats_dict[unpaid_dude[0]] = ('Discarded {}. '.format(unpaid_dude[0]),0)
   for dude in upkeep_concats_dict: concat_upk += upkeep_concats_dict[dude][0]
   notify("{} has produced {} ghost rock this turn: {}".format(me, prod, concat_prod)) # Inform the players how much they produced and from where.
   me.GhostRock += prod # Then add the money to their Ghost Rock counter.
   if upk > 0: # If we need to pay any upkeep, we do it after receiving production for the turn.
      if me.GhostRock < upk: # If we cannot pay with the money we have, then put the player's money to negative and let them fix it manually.
         notify("{} has {} GR in their bank but needs to pay {} GR for upkeep ({}). Their Ghost Rock stash is now negative and they'll need to fix it manually before proceeding.".format(me, me.GhostRock, upk, concat_upk))
      else: # If we can pay the upkeep, do so.
         notify("{} has paid {} upkeep in total this turn. {}".format(me, upk, concat_upk)) #Inform the players how much they paid and for what.
      me.GhostRock -= upk # Finally take the money out of their bank
   notify("-- {} has {} Ghost Rock in their stash after upkeep".format(me,me.GhostRock))
   me.setGlobalVariable('UpkeepDone','True')
   leftOverUpk = False
   for player in getActivePlayers():
      if player != me and player.getGlobalVariable('UpkeepDone') == 'False': leftOverUpk = True
   if not leftOverUpk: goToHighNoon() # If all players have now done their upkeep, we automatically proceed to high noon.
   
def HNActivate(card, x = 0, y = 0): # A function to add or remove High Noon (HN) markers. 
                                    # Those markers are used to signify when a high noon ability has been used, 
                                    # as printed abilities can only ever be used once per turn, even if they do not require booting.
                                    # These markers are only removed at the end of the turn.
   mute()
   useAbility(card)

def SHActivate(card, x = 0, y = 0): # Same process as the HN markers above
   mute()
   if card.markers[SHActivatedMarker] == 0:
      notify("{} uses {}'s Shootout ability.".format(me, card))
      card.markers[SHActivatedMarker] += 1
   else:
      notify("{} Wanted to use {}'s Shootout ability but it has already been used this turn.".format(me, card))		
      return False
   return True

def nightfall(card, x = 0, y = 0): # This function "refreshes" each card for nightfall.
                                   # This practically means that we remove any High Noon and Shootout ability markers and unboot the card
                                   # But only if it's not marked as a card that does not unboot
   mute()
   card.markers[mdict['UsedAbility']] = 0 # Remove the markers.
   card.markers[SHActivatedMarker] = 0
   card.markers[mdict['ControlMinus']] = 0 # Remove temporary bullet, contol, value and influence modifications
   card.markers[mdict['ControlPlus']] = 0 
   card.markers[mdict['InfluenceMinus']] = 0
   card.markers[mdict['InfluencePlus']] = 0 
   card.markers[mdict['BulletNoonPlus']] = 0 
   card.markers[mdict['BulletNoonMinus']] = 0 
   card.markers[mdict['ValueNoonMinus']] = 0 
   card.markers[mdict['ValueNoonPlus']] = 0 
   card.markers[mdict['Traded']] = 0
   reCalculate(notification = 'silent')
   if not card.markers[mdict['NoUnboot']] and card.name != 'Town Square': # We do not unboot the Town Square card.
      card.orientation = Rot0 # And if we can unboot the card, turn it to 0 degrees.
   elif card.markers[mdict['NoUnboot']]: card.markers[mdict['NoUnboot']] -= 1 # If the card does not unboot for any number of turns, we

def NightfallUnboot(group, x = 0, y = 0): # This function simply runs all the cards the player controls through the nigtfall function.
   mute()
   if getGlobalVariable('Phase') != '4': #One can only call for refresh during the Nighfall phase
      if not confirm(":::WARNING::: It is not yet the Sundown phase. Do you want to jump to Sundown now?"): return
      goToNightfall()
   if not confirm("Have you remembered to discard any cards you don't want from your play hand?"): return
   handsize = refill()
   cards = (card for card in table
                 if card.controller == me)
   for card in cards: nightfall(card)
   notify("Sundown refreshes {} cards and refills their hand back to {}.".format(me, handsize))
   
def doesNotUnboot(card, x = 0, y = 0): # Mark a card as "Does not unboot" and increase the duration. We use a card marker to do this.
   mute()
   card.markers[mdict['NoUnboot']] += 1
   notify("{}'s {} will not unboot during the next {} Sundowns.".format(me, card, card.markers[mdict['NoUnboot']]))
      
def spawnGunslinger(group, x = 0, y = 0): # Simply put a fake card in the game.
   table.create("94fe7823-077c-4abd-9278-6e64bda6dc64", x, y, 1)

def spawnNature(group, x = 0, y = 0): # Simply put a fake card in the game.
   table.create("c4689399-c350-46b3-a79a-f8c62d926cd5", x, y, 1)

def spawnAncestor(group, x = 0, y = 0): # Simply put a fake card in the game.
   table.create("53a212a6-34a6-47b0-bb24-45f1888bebf6", x, y, 1)
   reCalculate()

def HandRankGuide(group, x = 0, y = 0): # Put the Hand Rank guide onto the table, in case player need help to remember.
   HRG = table.create("851b726b-3b0c-43df-bbd7-710b5a0ffbf6", x, y, 1)   
    
def inspectCard(card, x = 0, y = 0): # This function shows the player the card text, to allow for easy reading until High Quality scans are procured.
   if card.Text == '': information("{} has no text".format(card.name))
   else: information("{}".format(card.Text))
   if len(getPlayers()) == 1: confirm("{}".format(CardsAA.get(card.model,'')))
   
def inspectTarget(table, x = 0, y = 0): # This function shows the player the card text, to allow for easy reading until High Quality scans are procured.
   for c in table:
      if c.targetedBy and c.targetedBy == me: 
         if c.Text == '': information("{} has no text".format(c.name))
         else: information("{}".format(c.Text))
   
def reCalculate(group = table, x = 0, y = 0, notification = 'loud'): 
# This function will calculate the amount of influence and Control you have on the table and update your counters. 
   mute()
   influence = 0 
   control = 0
   count = 0
   i = 0
   c = 0
   concat_inf = ' (' # We start our concatenated list of the cards with influence. We're going to put them in parenthesis for easy reading.
   concat_cp = ' ('
   cards = (card for card in table # We only care for cards we control. 
            if card.controller == me
            and card.highlight != DrawHandColor
            and card.highlight != DummyColor)
   for card in cards:
      count = num(card.Influence) + card.markers[mdict['InfluencePlus']] + card.markers[mdict['PermInfluencePlus']] - card.markers[mdict['InfluenceMinus']] # Put the card's total influence on a temp marker.
      if count > 0: # We only care to do anything if the card had any influence
         if i > 0: concat_inf += ', ' # We separate with comma only after we have at least 1 card in the list
         concat_inf += '{} from {}'.format(str(count),card) # Add the count as a string to the concatenated list before the name, e.g. "3 from Black Jack"
         i += 1 # Once we have found at least one card with influence, we separate the rest with commas
         influence += count # We add this card's total influence to our tally.
      count = num(card.Control) + card.markers[mdict['ControlPlus']] + card.markers[mdict['PermControlPlus']] - card.markers[mdict['PermControlMinus']] - card.markers[mdict['ControlMinus']] # Put the card's total influence on a temp marker.
      if count > 0: # Same as influence but for control this time
         if c > 0: concat_cp += ', '
         concat_cp += '{} from {}'.format(str(count),card)
         c += 1
         control += count
   concat_inf += ')' # We close our concatenated list
   if concat_inf == ' ()': concat_inf = '' # To avoid opening an empty parethesis if the player has no influence.
   concat_cp += ')'
   if concat_cp == ' ()': concat_cp = '' # To avoid opening an empty parethesis if the player has no control points.
   if notification == 'loud': # We only want to say the result if we're not explicitly asked to be silent (i.e. from the table action)
      notify('{} has recalculated and found their influence to to be {}{} and their Control Points to be {}{}.'.format(me, influence, concat_inf, control, concat_cp))
   me.Influence = influence # Make the player's total influence and control equal to the sum we've just calculated.
   me.Control = control

def setWinner(winner):
   outfits = (card for card in table
              if card.Type == 'Outfit')
   for outfit in outfits:
      if outfit.owner == winner: outfit.markers[mdict['Winner']] = 1
      else: outfit.markers[mdict['Winner']] = 0

#---------------------------------------------------------------------------
# Marker functions
#---------------------------------------------------------------------------

def plusPermControl(card, x = 0, y = 0, silent = False, count = 1): # Adds an extra control marker to cards (usually deeds)
   mute()
   if not silent:
      notify("{} marks that {} permanently provides {} more control.".format(me, card, count))
   for i in range(0,count):
      if mdict['PermControlMinus'] in card.markers: # If we have a -CP counter already, just remove one of those.
         card.markers[mdict['PermControlMinus']] -= 1
      else: # Otherwise just add an extra +CP
         card.markers[mdict['PermControlPlus']] += 1
   reCalculate(notification = 'silent')        
   
def minusPermControl(card, x = 0, y = 0, silent = False, count = 1): # Adds an extra control marker to cards (usually deeds)
   mute()
   if not silent:
      notify("{} marks that {} permanently provides {} less control.".format(me, card, count))
   for i in range(0,count):
      if mdict['PermControlPlus'] in card.markers: 
         card.markers[mdict['PermControlPlus']] -= 1
      else: 
         card.markers[mdict['PermControlMinus']] += 1
   reCalculate(notification = 'silent')        
   
def plusControl(card, x = 0, y = 0, silent = False, count = 1): # Adds an extra control marker to cards (usually deeds)
   mute()
   if not silent:
      notify("{} marks that {} provides {}  more control.".format(me, card, count))
   for i in range(0,count):
      if mdict['ControlMinus'] in card.markers: # If we have a -CP counter already, just remove one of those.
         card.markers[mdict['ControlMinus']] -= 1
      else: # Otherwise just add an extra +CP
         card.markers[mdict['ControlPlus']] += 1
   reCalculate(notification = 'silent')        
   
def minusControl(card, x = 0, y = 0, silent = False, count = 1): # Similar to adding Control but we remove instead.
   mute()
   if not silent:
      notify("{} marks that {} provides {} less control.".format(me, card, count))
   for i in range(0,count):
      if mdict['ControlPlus'] in card.markers:
         card.markers[mdict['ControlPlus']] -= 1
      else:
         card.markers[mdict['ControlMinus']] += 1     
   reCalculate(notification = 'silent')
   
def plusPermInfluence(card, x = 0, y = 0, silent = False, count = 1): # The same as pluControl but for influence
   mute()
   if not silent: notify("{} marks that {} permanently has {} more influence".format(me, card, count))
   for i in range(0,count):
      if mdict['PermInfluenceMinus'] in card.markers:
         card.markers[mdict['PermInfluenceMinus']] -= 1
      else:
         card.markers[mdict['PermInfluencePlus']] += 1         
   reCalculate(notification = 'silent')
        
def minusPermInfluence(card, x = 0, y = 0, silent = False, count = 1): # The same as pluControl but for influence
   mute()
   if not silent: notify("{} marks that {} permanently has {} less influence".format(me, card, count))
   for i in range(0,count):
      if mdict['PermInfluencePlus'] in card.markers:
         card.markers[mdict['PermInfluencePlus']] -= 1
      else:
         card.markers[mdict['PermInfluenceMinus']] += 1         
   reCalculate(notification = 'silent')
        
def plusInfluence(card, x = 0, y = 0, silent = False, count = 1): # The same as pluControl but for influence
   mute()
   if not silent:
      notify("{} marks that {}'s influence has increased by {}".format(me, card, count))
   for i in range(0,count):
      if mdict['InfluenceMinus'] in card.markers:
         card.markers[mdict['InfluenceMinus']] -= 1
      else:
         card.markers[mdict['InfluencePlus']] += 1         
   reCalculate(notification = 'silent')        
   
def minusInfluence(card, x = 0, y = 0, silent = False, count = 1): # The same as minusContorl but for influence
   mute()
   if not silent:
      notify("{} marks that {}'s influence has decreased by {}.".format(me, card, count))
   for i in range(0,count):
      if mdict['InfluencePlus'] in card.markers:
         card.markers[mdict['InfluencePlus']] -= 1
      else:
         if num(card.Influence) - card.markers[mdict['InfluenceMinus']] + card.markers[mdict['PermInfluencePlus']] > 0: modInfluence(-1)
         card.markers[mdict['InfluenceMinus']] += 1 
   reCalculate(notification = 'silent')
        
def plusProd(source, x = 0, y = 0): # Very much like plus Influence and control, but we don't have to worry about modifying the player's totals
   mute()
   if source == table:
      targetCards = [card for card in table if card.targetedBy and card.targetedBy == me]
      if not len(targetCards): modProd(source)
      else:
         for card in targetCards: modProd(card)
   else: modProd(source)
        
def minusProd(card, x = 0, y = 0): 
   mute()
   modProd(card, -1)

def modProd(card, count = 1, silent = False):
   if count > 0:
      for iter in range(count):
         if mdict['ProdPlus'] in card.markers or mdict['ProdMinus'] in card.markers: # Putting the clarification about upkeep 
                                                                                     # only the first time this is changed
                                                                                     # to make the message more readable
            if not silent: notify("{} marks that {}'s production has increased by 1 GR.".format(me, card)) 
         else: 
            if not silent: notify("{} marks that {}'s production has increased by 1 GR (This will be automatically taken into account during upkeep).".format(me, card))
         if mdict['ProdMinus'] in card.markers:
            card.markers[mdict['ProdMinus']] -= 1
         else:
            card.markers[mdict['ProdPlus']] += 1         
   else:
      for iter in range(abs(count)):
         if mdict['ProdPlus'] in card.markers or mdict['ProdMinus'] in card.markers:
            if not silent: notify("{} marks that {}'s production has decreased by 1 GR.".format(me, card))
         else:
            if not silent: notify("{} marks that {}'s production has decreased by 1 GR (This will be automatically taken into account during upkeep).".format(me, card))
         if mdict['ProdPlus'] in card.markers:
            card.markers[mdict['ProdPlus']] -= 1
         else:
            card.markers[mdict['ProdMinus']] += 1  
        
def plusVP(card, x = 0, y = 0, notification = 'loud', count = 1): # Adds an extra VP marker to cards (usually dudes)
   mute()
   if notification == loud:
      notify("{} marks that {} provides {} extra victory points (Their total has been adjusted accordingly).".format(me, card, count))
   for i in range(0,count):
      if mdict['VPMinus'] in card.markers: # If we have a -VP counter already, just remove one of those.
         card.markers[mdict['VPMinus']] -= 1
      else: # Otherwise just add an extra +VP
         card.markers[mdict['VPPlus']] += 1
      modVP() 
        
def minusVP(card, x = 0, y = 0, notification = 'loud', count = 1): # Similar to adding VP but we remove instead.
   mute()
   if notification == loud and card.markers[mdict['VPPlus']]:
      notify("{} marks that {} provides {} less VP (Their total has been adjusted accordingly).".format(me, card, count))
   for i in range(0,count):
      if mdict['VPPlus'] in card.markers:
         card.markers[mdict['VPPlus']] -= 1
         modVP(-1)
   # if the card doesn't have VP, then we don't do anything as it cannot go negative (at least according to the current card pool. Maybe in the future?)

def plusBulletNoon(card, x = 0, y = 0,count = 1, silent = False): # Very much like plus Value
   mute()
   if not silent: notify("{} marks that {}'s bullets have increased by 1 until Sundown.".format(me, card))
   for i in range(0,count):
      if mdict['BulletNoonMinus'] in card.markers:
         card.markers[mdict['BulletNoonMinus']] -= 1
      else:
         card.markers[mdict['BulletNoonPlus']] += 1 

def plusBulletShootout(card, x = 0, y = 0,count = 1, silent = False):
   mute()
   if getGlobalVariable('Shootout') != 'True': notify(":::ERROR::: You can only increase bullets for a shootout within a shootout. Please press F10 to initiate one first")
   else:
      if not silent: notify("{} marks that {}'s bullets have increased by 1 for this shootout.".format(me, card))
      for i in range(0,count):
         if mdict['BulletShootoutMinus'] in card.markers:
            card.markers[mdict['BulletShootoutMinus']] -= 1
         else:
            card.markers[mdict['BulletShootoutPlus']] += 1 

def plusPermBullet(card, x = 0, y = 0, count = 1, silent = False):
   mute()
   if not silent: notify("{} marks that {}'s bullets have permanently increased by 1.".format(me, card))
   for i in range(0,count):
      if mdict['PermBulletMinus'] in card.markers:
         card.markers[mdict['PermBulletMinus']] -= 1
      else:
         card.markers[mdict['PermBulletPlus']] += 1 

def minusPermBullet(card, x = 0, y = 0,count = 1, silent = False): # Very much like plus Value
   mute()
   if not silent: notify("{} marks that {}'s bullets have permanently decreased by 1.".format(me, card))
   for i in range(0,count):
      if mdict['PermBulletPlus'] in card.markers:
         card.markers[mdict['PermBulletPlus']] -= 1
      else:
         card.markers[mdict['PermBulletMinus']] += 1 
         
def minusBulletNoon(card, x = 0, y = 0,count = 1, silent = False): # Very much like plus Value
   mute()
   if not silent: notify("{} marks that {}'s bullets have decreased by 1 until Sundown.".format(me, card))
   for i in range(0,count):
      if mdict['BulletNoonPlus'] in card.markers:
         card.markers[mdict['BulletNoonPlus']] -= 1
      else:
         card.markers[mdict['BulletNoonMinus']] += 1 

def minusBulletShootout(card, x = 0, y = 0,count = 1, silent = False):
   mute()
   if getGlobalVariable('Shootout') != 'True': notify(":::ERROR::: You can only increase bullets for a shootout within a shootout. Please press F10 to initiate one first")
   else:
      if not silent: notify("{} marks that {}'s bullets have decreased by 1 for this shootout.".format(me, card))
      for i in range(0,count):
         if mdict['BulletShootoutPlus'] in card.markers:
            card.markers[mdict['BulletShootoutPlus']] -= 1
         else:
            card.markers[mdict['BulletShootoutMinus']] += 1 

def plusGR(card, x = 0, y = 0): # Very much like plus Value
   mute()
   notify("{} adds a Ghost Rock counter on {}".format(me, card))
   card.markers[mdict['Ghost Rock']] += 1

def minusGR(card, x = 0, y = 0):
   mute()
   notify("{} removes a Ghost Rock counter on {}".format(me, card))
   if card.markers[mdict['Ghost Rock']] in card.markers: card.markers[mdict['Ghost Rock']] -= 1
   else: notify("There are no Ghost Rock counters to remove")

def plusValue(card, x = 0, y = 0, silent = False, valuemod = None): 
# Very much like plus Influence and control, but we don't have to worry about modifying the player's totals
   mute()
   if valuemod == None: valuemod = askInteger("Increase {}'s value by how much? (Current value is: {})".format(card.name,calcValue(card)), 3)
   if mdict['ValueNoonMinus'] in card.markers:
      if valuemod <= card.markers[mdict['ValueNoonMinus']]:
         card.markers[mdict['ValueNoonMinus']] -= valuemod
      else:
         card.markers[mdict['ValueNoonPlus']] += valuemod - card.markers[mdict['ValueNoonMinus']]
         card.markers[mdict['ValueNoonMinus']] = 0
   else:
      card.markers[mdict['ValueNoonPlus']] += valuemod 
   #if calcValue(card,'raw') > 13: card.markers[mdict['ValueNoonPlus']] = 13 - numrank(card.Rank) # Max value is 13 (King)
   if not silent:
      notify("{} marks that {}'s value has increased by {} and is now {}.".format(me, card, valuemod, calcValue(card)))
        
def minusValue(card, x = 0, y = 0, silent = False, valuemod = None): 
   mute()
   if valuemod == None: valuemod = askInteger("Decrease {}'s value by how much? (Current value is: {})".format(card.name,calcValue(card)), 3)
   if mdict['ValueNoonPlus'] in card.markers:
      if valuemod <= card.markers[mdict['ValueNoonPlus']]:
         card.markers[mdict['ValueNoonPlus']] -= valuemod
      else:
         card.markers[mdict['ValueNoonMinus']] += valuemod - card.markers[mdict['ValueNoonPlus']]
         card.markers[mdict['ValueNoonPlus']] = 0
   else:
      card.markers[mdict['ValueNoonMinus']] += valuemod         
   #if calcValue(card,'raw') < 1: card.markers[mdict['ValueNoonMinus']] = numrank(card.Rank)
   if not silent:
      notify("{} marks that {}'s value has decreased by {} and is now {}.".format(me, card, valuemod, calcValue(card)))

def plusPermValue(card, x = 0, y = 0, silent = False, valuemod = None): 
# Very much like plus Influence and control, but we don't have to worry about modifying the player's totals
   mute()
   if valuemod == None: valuemod = askInteger("Increase {}'s value by how much? (Current value is: {})".format(card.name,calcValue(card)), 3)
   if mdict['ValuePermMinus'] in card.markers:
      if valuemod <= card.markers[mdict['ValuePermMinus']]:
         card.markers[mdict['ValuePermMinus']] -= valuemod
      else:
         card.markers[mdict['ValuePermPlus']] += valuemod - card.markers[mdict['ValuePermMinus']]
         card.markers[mdict['ValuePermMinus']] = 0
   else:
      card.markers[mdict['ValuePermPlus']] += valuemod 
   #if calcValue(card,'raw') > 13: card.markers[mdict['ValuePermPlus']] = 13 - numrank(card.Rank) # Max value is 13 (King)
   if not silent:
      notify("{} marks that {}'s value has permanently increased by {} and is now {}.".format(me, card, valuemod, calcValue(card)))
        
def minusPermValue(card, x = 0, y = 0, silent = False, valuemod = None): 
   mute()
   if valuemod == None: valuemod = askInteger("Decrease {}'s value by how much? (Current value is: {})".format(card.name,calcValue(card)), 3)
   if mdict['ValuePermPlus'] in card.markers:
      if valuemod <= card.markers[mdict['ValuePermPlus']]:
         card.markers[mdict['ValuePermPlus']] -= valuemod
      else:
         card.markers[mdict['ValuePermMinus']] += valuemod - card.markers[mdict['ValuePermPlus']]
         card.markers[mdict['ValuePermPlus']] = 0
   else:
      card.markers[mdict['ValuePermMinus']] += valuemod         
   #if calcValue(card,'raw') < 1: card.markers[mdict['ValuePermMinus']] = numrank(card.Rank)
   if not silent:
      notify("{} marks that {}'s value has permanently decreased by {} and is now {}.".format(me, card, valuemod, calcValue(card)))

def setValue(card, x = 0, y = 0):
   mute()
   currentValue = calcValue(card,'raw')
   newValue = askInteger("What should the new value be? (use direct number format: 1 - 13)", calcValue(card,'numeral'))
   if newValue > currentValue: plusValue(card,0,0,True,(newValue - currentValue))
   if newValue < currentValue: minusValue(card,0,0,True,(currentValue - newValue))
   notify("{} has set the value of {} to {}".format(me,card,calcValue(card)))
    
def addMarker(cards, x = 0, y = 0): # A simple function to manually add any of the available markers.
   mute()
   marker, quantity = askMarker() # Ask the player how many of the same type they want.
   if quantity == 0: return
   for card in cards: # Then go through their cards and add those markers to each.
      card.markers[marker] += quantity
      notify("{} adds {} {} counter to {}.".format(me, quantity, marker[0], card))	
         
#---------------------------------------------------------------------------
# Deed actions
#---------------------------------------------------------------------------
      
def takeOver(card, x = 0, y = 0):
# Set a deed as taken over. This is marked via a card highlight. 
# Same process as doesNotUnboot but only for deeds.
# Taken over deeds are deeds who's ownership has been taken by another player. Since you cannot change owners naturally, we work around that.
   mute()
   if card.Type == "Deed":
      card.highlight = me.color
      notify("Ownership of {} has passed to {}".format(card, me))
         
def locationTarget(card, x = 0, y = 0): # A function to let others know where you are moving. 
                                        # Unfortunately one cannot initiate card actions on cards they do not control.
                                        # Which prevents us from doing much with this. 
                                        # At the future I'd like to automatically read the locations coordinates and move dudes to an appropriate.
                                        # location, but this requires that one can init actions on cards they do not control.
   mute()
   if card.Type == "Deed" or card.Type == "Outfit":
      notify("{} announces {} as the location.".format(me, card))
      card.target
        
#---------------------------------------------------------------------------
# Dude actions
#---------------------------------------------------------------------------

def modWantedMarker(card, x = 0, y = 0): # The old Binary Wanted function. 
   mute()
   if card.Type == "Dude":
      if card.markers[mdict['Bounty']] == 0:
         notify("{} is now wanted by the law.".format(card))
         card.markers[mdict['Bounty']] += 1
      else:
         notify("The name of {} is cleared.".format(card))
         card.markers[mdict['Bounty']] -= 1	
                 
def plusBounty(source, x = 0, y = 0): 
   mute()
   #confirm(source.name) # debug
   if source == table:
      targetCards = [card for card in table if card.targetedBy and card.targetedBy == me and card.Type == "Dude"]
      if not len(targetCards): modBounty(source)
      else:
         for card in targetCards: modBounty(card)
   else: modBounty(source)
         
def minusBounty(card, x = 0, y = 0): 
   mute()
   if card.markers[mdict['Bounty']]:
      card.markers[mdict['Bounty']] -= 1
      if card.markers[mdict['Bounty']] == 0: notify("The name of {} is cleared.".format(card))
      else: notify("{}'s wanted bounty decreases to {}".format(card,card.markers[mdict['Bounty']]))

def modBounty(card, count = 1):
   mute()
   if card.Type == "Dude":
      card.markers[mdict['Bounty']] += count
      if card.markers[mdict['Bounty']] == 1: notify("{} is now wanted by the law.".format(card))
      else: notify("{}'s wanted bounty increases to {}".format(card,card.markers[mdict['Bounty']]))
      
         
def addHarrowedMarker(card, x = 0, y = 0):
   mute()
   if card.Type == "Dude":
      if card.markers[HarrowedMarker] == 1 or re.search(r'\bHarrowed\b\.', card.Text):
         notify("{} is already harrowed! There's only space for one manitou in thar.".format(card))
      else:
         notify("{} has come back from the grave as one of the Harrowed.".format(card))
         card.markers[HarrowedMarker] += 1

def callout(card, x = 0, y = 0, silent = False, targetDudes = None): # Notifies that this dude is calling someone out.
   mute()
   successCallout = False
   if getGlobalVariable('Mark') != 'None' and not confirm(":::WARNING::: There seems to be another call out in progress. Override it?"): return
   if card.Type == "Dude":
      if not targetDudes: targetDudes = [c for c in table if c.Type == 'Dude' and c.targetedBy and c.targetedBy == me and (c.controller != me or len(players) == 1)]
      if not len(targetDudes):
         whisper(":::ERROR::: You need to target the opposing dude you're calling out.")
         return
      targetD = targetDudes[0]
      if targetD == card:
         whisper(":::ERROR::: You cannot call out yourself silly!")
         return
      chkHighNoon()
      if not silent: notify("{} is calling {} out.".format(card,targetD))
      setGlobalVariable('Mark',str(targetD._id)) # We store the called out dude as a global variable so that the owner can easier select their answer.
      if card.orientation == Rot90: notify(":::WARNING::: Remember that you need a card effect to call out someone while booted)".format(card))
      card.highlight = InitiateColor
      successCallout = True
   else: whisper(":::ERROR::: You can only initiate a call-out with a dude")
   return successCallout

def move(card, x = 0, y = 0): # Notifies that this dude is moving without booting
   mute()
   if card.Type == "Dude":
      notify("{} is moving without booting.".format(card))
      if card.orientation == Rot90: notify("(Remember that you need a card effect to move while booted)".format(card))
      
def moveBoot(card, x = 0, y = 0): # Notifies that this dude is moving by booting
   mute()
   if card.orientation == Rot0 and card.Type == "Dude":
         notify("{} is booting to move.".format(card))
         card.orientation = Rot90

def tradeGoods(card, x = 0, y = 0): 
   mute()
   if card.Type != "Dude":
     whisper(":::ERROR::: You can only use this action on a dude")
     return
   newHost = findHost(card) # Seeking for a host for a 'Dude' type of card, will do the same as looking for Goods.
   if not newHost:
      whisper(":::ERROR::: You need to target a dude in the same location to receive the goods")
      return
   chkHighNoon()
   if newHost.orientation != Rot0 and not confirm("You can only trade goods to unbooted dudes. Bypass restriction?"): return
   hostCards = eval(getGlobalVariable('Host Cards'))
   attachedGoods = [Card(att_id) for att_id in hostCards if hostCards[att_id] == card._id and Card(att_id).Type == 'Goods']
   chosenGoods = []
   extraTXT = ''
   if len(attachedGoods) == 0: 
      whisper(":::ERROR::: This dude does not hold any goods they can trade.")
      return
   elif len(attachedGoods) == 1: 
      if attachedGoods[0].markers[mdict['Traded']]:
         if not confirm("This goods has already been traded this turn. Bypass once-per-turn restriction?"): return
         else: extraTXT = ' (Bypassing the once-per-turn restriction)'
      attachCard(attachedGoods[0],newHost)  #If there's only 1 goods attached, we assume that's the one that is going to be moved.
      chosenGoods.append(attachedGoods[0])
      attachedGoods[0].markers[mdict['Traded']] += 1
   else:
      notify("{} is trading some goods between their dudes...".format(me))
      choices = multiChoice("Choose goods to trade to {}".format(newHost.name), makeChoiceListfromCardList(attachedGoods))
      if choices == 'ABORT': 
         notify("{} has aborted the trading action.".format(me))
         return
      debugNotify("About to move choices")
      for choice in choices: 
         if attachedGoods[choice].markers[mdict['Traded']] and not confirm("This goods has already been traded this turn. Bypass once-per-turn restriction?"): continue
         else: extraTXT = ' (Bypassing the once-per-turn restriction)'
         attachCard(attachedGoods[choice],newHost)
         chosenGoods.append(attachedGoods[choice])
         attachedGoods[choice].markers[mdict['Traded']] += 1
   orgAttachments(card)
   notify("{} has traded {} to {}{}".format(card,[c.name for c in chosenGoods],newHost,extraTXT))
   
#---------------------------------------------------------------------------
# Posse actions
#---------------------------------------------------------------------------        

def joinAttack(card, x = 0, y = 0): # Informs that this dude joins an attack posse and highlights him accordingly. 
                                    # This is to help track who is shooting it out. The highlights are cleared by the goToShootout function.
   if card.Type == "Dude" : # This is something only dudes can do
       mute () 
       notify("{} is joining the leader's posse.".format(card))
       card.highlight = AttackColor
       executePlayScripts(card, 'PARTICIPATION')

def joinDefence(card, x = 0, y = 0, silent = False): # Same as above, but about defensive posse.
   if card.Type == "Dude" : 
      mute ()
      if not silent: notify("{} is joining the defending posse.".format(card))
      card.highlight = DefendColor   
      executePlayScripts(card, 'PARTICIPATION')

def defend(card = None, x = 0, y = 0): # Same as the defending posse but with diferent notification.
   mute ()
   if getGlobalVariable('Mark') == 'None': whisper(":::ERROR::: There seems to be no callout in progress")
   elif getGlobalVariable('Shootout') == 'True': whisper(":::ERROR::: Shootout is already in progress. Double click your dudes to make them participate")
   else:
      mark = Card(num(getGlobalVariable('Mark')))
      if card and card != table and card.Type == 'Dude': pass 
      elif mark.Type == 'Dude': card = mark # IF the player just pressed F5 to accept a callout, we set the mark as defending.
      if card and card != table : cardTXT = card # If the player double clicked a card to accept, or there's a dude as a mark, we announce that it's the one defending
      else: cardTXT = me # Otherwise we announce it's the player defending.
      if getGlobalVariable('Job Active') != 'False':
         notify("{} is defending against this job. A shootout is breaking out!".format(cardTXT))
      else:
         notify("{} has accepted the call out. A shootout is breaking out!".format(cardTXT))
      if card and card != table : # If the player just pressed F5 to accept, but the mark is not a dude, then we don't highlight anything.
         joinDefence(card, silent = True)
      goToShootout(silent = True)

def refuseCallout(focus = None, x = 0, y = 0): # Boots the dude and moves him to your home or informs you if they cannot refuse.
   mute ()
   if getGlobalVariable('Shootout') == 'True' and focus != table: runAway(focus)# If the player has moused over a card and pressed ESC while in a shootout, they're trying to run away from the shootout
   elif getGlobalVariable('Mark') == 'None' or getGlobalVariable('Job Active') != 'False': whisper(":::ERROR::: There seems to be no callout in progress")
   else:
      chickenDude = Card(num(getGlobalVariable('Mark')))
      if chickenDude.controller != me: return # Only the owner of the cowardly dude can decide to run away.
      if chickenDude.orientation == Rot90 and not confirm(":::WARNING::: Normally booted dudes cannot refuse callouts. Bypass restriction and refuse anyway?"): 
         return # If the dude is booted, they cannot refuse without a card effect
      else:
         notify("{} has turned yella and run home to hide.".format(chickenDude))
         chickenDude.orientation = Rot90 # If they refure boot them...
         if playeraxis == Xaxis: chickenDude.moveToTable(homeDistance(chickenDude) + (playerside * cwidth(chickenDude,-4)), 0) # ...and move them where we expect the player's home to be.
         elif playeraxis == Yaxis: chickenDude.moveToTable(0,homeDistance(chickenDude) + (playerside * cheight(chickenDude,-4)))
         orgAttachments(chickenDude)
         setGlobalVariable('Mark','None') # Finally we clear the Called Out variable
         clearShootout()

def runAway(card, x = 0, y = 0): # Same as above pretty much but also clears the shootout highlights.
   if card.Type == "Dude" : 
      mute ()
      notify("{} is running away from the shootout.".format(card))
      card.orientation = Rot90
      if playeraxis == Xaxis: card.moveToTable(homeDistance(card) + (playerside * cwidth(card,-4)), 0)
      elif playeraxis == Yaxis: card.moveToTable(0,homeDistance(card) + (playerside * cheight(card,-4)))
      orgAttachments(card)
      card.highlight = None
      
def leavePosse(card, x = 0, y = 0): # Same as above pretty much but also clears the shootout highlights.
   if card.controller != me:
      remoteCall(card.controller,'leavePosse',[card,x,y])
      return
   card.highlight = None
   executePlayScripts(card, 'UNPARTICIPATE')
      
def posseReady (group, x = 0, y = 0):
   notify("{}'s Posse is Ready to throw down!".format(me))     

#---------------------------------------------------------------------------
# Hand and Deck actions
#---------------------------------------------------------------------------
      
def playcard(card,retainPos = False,costReduction = 0): 
# This is the function to play cards from your hand. It's one of the core functions
# It will automatically pay the cost of cards if you can, or inform you if you cannot.
# If the card being played has influence or Control points, those will automatically be added to the player's total.
# Dudes and deeds will be placed at default locations to facilitate quicker play.
   mute()
   reCalculate(notification = 'silent') # We first make sure we have the right totals
   chkcards = [] # Create an empty list to fill later with cards to check
   uniquecards = (tablecard for tablecard in table # Lets gather all the cards from the table that may prevent us from playing our card
                  if tablecard.name == card.name # First the card need to be the same as ours
                  and tablecard != card # In case they played the card by drag & dropping it
                  and tablecard.owner == me # Cards are unique only for each owner.
                  and (tablecard.Type == 'Dude'  # But only dude or deeds...
                        or tablecard.Type == 'Deed' 
                        or (re.search('Unique.', tablecard.Keywords) # ...or cards with an explicit "Unique" in the text that are Goods, Improvements or Spells.
                           and (tablecard.Type == 'Goods'        # Because otherwise those types can be up to 4 per player.
                              or tablecard.Type == 'Improvement' 
                              or tablecard.Type == 'Spell')))) 
   for c in uniquecards: # Append the cards from the table and the cards from the boot hill into one list we can go through.
      chkcards.append(c)
   #for player in players:
   acedcards = (acedcard for acedcard in me.piles['Boot Hill'] # Go through the player's Boot Hill looking for matches 
                  if acedcard.name == card.name
                  and acedcard != card
                  and (acedcard.Type == 'Dude' 
                        or acedcard.Type == 'Deed' 
                        or (re.search('Unique.', acedcard.Keywords) 
                           and (acedcard.Type == 'Goods' 
                              or acedcard.Type == 'Improvement' 
                              or acedcard.Type == 'Spell')))) 
   for c in acedcards:
      chkcards.append(c)
   for chkcard in chkcards: # Now we check the combined list to see if anything will block us from playing our card from the hand.
      if ((chkcard.owner == me and  # First lets see if this is an experienced version that we can play for free.
            chkcard.group == table and
            chkcard.model != card.model and
            (re.search('Experienced', chkcard.Keywords) or re.search('Experienced', card.Keywords)))):
         if confirm("You seem to have another version of {} in play. Do you want to replace it with the version in your hand".format(card.name)):
            xp, yp = chkcard.position            
            card.moveToTable(xp,yp) # We retain position
            if chkcard.orientation == Rot90: card.orientation = Rot90 # We retain orientation
            for key in chkcard.markers: card.markers[key] = chkcard.markers[key] # We transfer the card's markers to the experienced version
            hostCards = eval(getGlobalVariable('Host Cards')) # We transfer any attachments
            if len([att_id for att_id in hostCards if hostCards[att_id] == chkcard._id]) >= 1:
               for attachmentID in hostCards:
                  if hostCards[attachmentID] == chkcard._id:
                     debugNotify("Attachment exists. Trying to move to exp version.", 2) # debug
                     hostCards[attachmentID] = card._id
               setGlobalVariable('Host Cards',str(hostCards))
            chkcard.moveTo(me.piles['Discard Pile'])
            reCalculate(notification = 'silent')
            notify ("{} replaced {} with an experienced version".format(me,card))
            return
         else: return
      elif re.search('Non-Unique', chkcard.Keywords): continue 
            # We can still play our own non-unique cards 
      elif chkcard.owner == me: 
            notify ("{} wanted to bring {} into play they but already have a copy of it in play".format(me,card))     
            return
      else: 
         if chkcard.group == table:
            notify ("{} wanted to bring {} in play but it is already on the table and owned by {}".format(me,card,chkcard.owner))
         else: # if they're not on the table, they're in someone's boothill
            notify ("{} wanted to bring {} in play but it currently RIP in {}'s Boot Hill".format(me,card,chkcard.owner))
         return
   if costReduction > num(card.Cost): costReduction = num(card.Cost)
   reduction = reduceCost(card, action = 'PLAY', fullCost = num(card.Cost))
   if card.Type == "Dude":
      chkHighNoon()
      if chkGadgetCraft(card):
         if not retainPos: 
            if payCost(num(card.Cost) - costReduction - reduction, loud) == 'ABORT' : return # Check if the player can pay the cost. If not, abort.
            placeCard(card,'HireDude')
         notify("{} has hired {}.".format(me, card)) # Inform of the new hire      
   elif card.Type == "Deed" :
      chkHighNoon()
      if chkGadgetCraft(card):
         if not retainPos: 
            if payCost(num(card.Cost) - costReduction - reduction, loud) == 'ABORT' : return # Check if the player can pay the cost. If not, abort.
            placeCard(card,'BuyDeed')
         notify("{} has acquired the deed to {}.".format(me, card))
   elif card.Type == "Goods" or card.Type == "Spell" or (card.Type == "Action" and re.search(r'Condition',card.Keywords) and not re.search(r'(Noon [jJ]ob:|Noon [jJ]ob, Boot:)',card.Text)): # If we're bringing in any goods, just remind the player to pull for gadgets.
      if card.Type != "Action": chkHighNoon()
      hostCard = findHost(card)
      if not hostCard:
         whisper("You need to target the card which is going to attach the card")
         if retainPos: card.moveTo(me.hand)
         return
      else:
         if payCost(num(card.Cost) - costReduction - reduction, loud) == 'ABORT' : return # Check if the player can pay the cost. If not, abort.
         if card.Type == "Goods" or card.Type == "Spell":
            if hostCard.orientation != Rot0 and hostCard.Type == 'Dude' and not confirm("You can only attach goods to unbooted dudes. Bypass restriction?"): 
               me.GhostRock += num(card.Cost)
               return      
            if re.search('Gadget', card.Keywords):
               if hostCard.Type == 'Dude':
                  if confirm("You are trying to create a gadget. Would you like to do a gadget skill check at this point?"): 
                     gadgetPull = pull(silent = True) # pull returns a tuple with the results of the pull
                     hostCard.orientation = Rot90
                     notify("{} attempted to manufacture a {} and pulled a {} {}".format(hostCard,card,fullrank(gadgetPull[0]), fullsuit(gadgetPull[1])))
                  else: notify("{} has created a {} without a gadget skill check.".format(hostCard, card))
               else:
                  if confirm("You are trying to create a gadget. Would you like to do a gadget skill check at this point?"):
                     myDudes = [dude for dude in table if dude.controller == me and dude.orientation == Rot0 and re.search(r'Mad Scientist',dude.Keywords)]
                     if not len(myDudes):
                        if confirm("You do not seem to have an available mad scientist to build this gadget. Abort the build?"): 
                           me.GhostRock += num(card.Cost)
                           notify(":> {} has aborted the purchase. {} Ghost rock was returned".format(me,num(card.Cost)))
                           return
                        else:
                           myDudes = [dude for dude in table if dude.controller == me and re.search(r'Mad Scientist',dude.Keywords)]
                     choice = SingleChoice('Choose one of your available Mad Scientists to build this gadget', makeChoiceListfromCardList(myDudes))
                     if choice != None: 
                        gadgetPull = pull(silent = True) # pull returns a tuple with the results of the pull
                        myDudes[choice].orientation = Rot90
                        notify("{} attempted to manufacture a {} on {} and pulled a {} {}".format(myDudes[choice],card,hostCard,fullrank(gadgetPull[0]), fullsuit(gadgetPull[1])))
                     else: notify("{} has attached a {} on {} without a gadget skill check.".format(me, card, hostCard))
                  else: notify("{} has attached a {} on {} without a gadget skill check.".format(me, card, hostCard))
            elif card.Type == "Spell": 
               if hostCard.Type == 'Dude': notify("{} has learned {}.".format(hostCard, card.Name))
               else: notify("{} been prepared on {}.".format(card.Name,hostCard))
            else: notify("{} has purchased {}.".format(hostCard, card.Name))
         else: notify("{} has attached a {}.".format(hostCard, card.Name))
         attachCard(card,hostCard)
   else: 
      if not retainPos: # We only pay the cost if the card was double-clicked, in case the player tried to play the card for free.
         if chkTargeting(card) == 'ABORT': return 'ABORT'# If it's an Action and has targeting requirements, check with the user first.
         if payCost(num(card.Cost) - costReduction - reduction, loud) == 'ABORT' : return # Check if the player can pay the cost. If not, abort.
         if playeraxis == Xaxis: card.moveToTable(cardDistance(),0) # For anything else, just say they play it.
         else: card.moveToTable(0,cardDistance())
      notify("{} plays {} from their hand.".format(me, card))
   autoscriptOtherPlayers('CardPlayed',card)
   if num(card.Control) + card.markers[mdict['ControlPlus']] - card.markers[mdict['ControlMinus']] > 0:
      # Increase control, if the new card provides is any.
      modControl(num(card.Control) + card.markers[mdict['ControlPlus']] - card.markers[mdict['ControlMinus']], loud) 
   if num(card.Influence) + card.markers[mdict['InfluencePlus']] - card.markers[mdict['InfluenceMinus']] > 0:
      # Increase influence, if the new card provides is any.
      modInfluence(num(card.Influence) + card.markers[mdict['InfluencePlus']] - card.markers[mdict['InfluenceMinus']], loud) 
   # Increase influence, if the new card provides any or any influence markers are remembered
   executePlayScripts(card, 'PLAY')
   
def shuffle(group): # A simple function to shuffle piles
   group.shuffle()

def reshuffle(group = me.piles['Discard Pile']): # This function reshuffles the player's discard pile into their deck.
   mute()
   Deck = group.player.Deck # Just to save us some repetition
   for card in group: card.moveTo(Deck) # Move the player's cards from the discard to their deck one-by-one.
   random = rnd(100, 10000) # Bug 105 workaround. This delays the next action until all animation is done. 
                           # see https://octgn.16bugs.com/projects/3602/bugs/102681
   Deck.shuffle() # Then use the built-in shuffle action
   notify("{} reshuffled their {} into their Deck.".format(me, group.name)) # And inform everyone.

def draw(group = me.Deck): # Draws one card from the deck into the player's hand.
   mute()
   if len(group) == 0: # In case the deck is empty, invoke the reshuffle function.
      notify("{}'s Deck empty. Will reshuffle discard pile".format(me))
      reshuffle()
   group.top().moveTo(me.hand)
   notify("{} draws a card.".format(me))   
   
def pull(group = me.Deck, x = 0, y = 0, silent = False): # Draws one card from the deck into the discard pile and announces its value.
   mute()
   Deck = me.Deck
   if len(Deck) == 0: # In case the deck is empty, invoke the reshuffle function.
      notify("{}'s Deck empty. Will reshuffle discard pile".format(me))
      reshuffle()
      rnd(1, 100) # Bug workaround. We wait a bit so that we are sure the cards are there.
   Deck.top().moveTo(me.piles['Discard Pile']) # Move the top card from the deck into the discard pile
   rnd(1, 100) # Wait a bit more, as in multiplayer games, things are slower.
   rank = me.piles['Discard Pile'].top().Rank # Save the card's rank
   suit = me.piles['Discard Pile'].top().Suit # Save the card's suit
   if not silent: notify("{} Pulled a {} {}.".format(me, fullrank(rank), fullsuit(suit)))  # Announce them nicely to everyone.
   if me.piles['Discard Pile'].top().Type == 'Joker': 
      me.piles['Discard Pile'].top().moveTo(me.piles['Boot Hill'])
      #notify(":> The Joker was aced as per instructions")
   return (rank,suit)

def drawMany(group, count = None, destination = None, silent = False): # This function draws a variable number cards into the player's hand.
   mute()
   if destination == None: destination = me.hand
   if count == None: count = askInteger("Draw how many cards to your Play Hand?", 5) # Ask the player how many cards they want.
   if count == None: return
   for i in range(0, count): 
      if len(group) == 0: reshuffle() # If before moving a card the deck is empty, reshuffle.
      group.top().moveTo(me.hand) # Then move them one by one into their play hand.
   if not silent: notify("{} draws {} cards to their play hand.".format(me, count)) # And if we're "loud", notify what happened.

def setHandSize(group): # A function to modify a player's hand size. This is used during nighfall when refilling the player's hand automatically.
   global handsize
   handsize = askInteger("What is your current hand size?", handsize)
   if handsize == None: handsize = 5
   notify("{} sets their hand size to {}".format(me, handsize))
   
def refill(group = me.hand): # Refill the player's hand to its hand size.
   #global handsize
   handsize = 5 # 5 is the default, then we add any card effects which modify it
   for card in table:
      if card.controller == me:
         handSizeRegex = re.search(r'constantAbility:HandSize(Plus|Minus)([0-9]+)',CardsAS.get(card.model,''))
         if not handSizeRegex: continue
         if handSizeRegex.group(1) == 'Plus': handsize += num(handSizeRegex.group(2))
         else: handsize -= num(handSizeRegex.group(2))
   playhand = len(me.hand) # count how many cards there are currently there.
   if playhand < handsize: drawMany(me.Deck, handsize - playhand, True) # If there's less cards than the handsize, draw from the deck until it's full.
   return handsize

def handDiscard(card, x = 0, y = 0): # Discard a card from your hand.
   mute()
   card.moveTo(me.piles['Discard Pile'])
   notify("{} has discarded {}.".format(me, card))  

def handAce(card, x = 0, y = 0): # Ace a card from your hand.
   mute()
   card.moveTo(me.piles['Boot Hill'])
   notify("{} has aced {}.".format(me, card))  

def handShuffle(group, x = 0, y = 0): # Shuffle your hand back into your deck
   if not confirm("Are you sure you want to shuffle your hand into your deck?"): return
   notify("{} is shuffling their hand back into their deck...".format(me))
   groupToDeck(group,silent = True)
   whisper("Shuffling...")
   shuffle(me.Deck) # We do a good shuffle this time.
   whisper("Shuffle completed.")
       
def groupToDeck (group = me.hand, player = me, silent = False):
   debugNotify(">>> groupToDeck(){}".format(extraASDebug())) #Debug
   mute()
   deck = player.Deck
   count = len(group)
   for c in group: c.moveTo(deck)
   if not silent: notify ("{} moves their whole {} to their {}.".format(player,group.name,deck.name))
   if debugVerbosity >= 3: notify("<<< groupToDeck() with return:\n{}\n{}\n{}".format(group.name,deck.name,count)) #Debug
   else: return(group.name,deck.name,count) # Return a tuple with the names of the groups.
   
def drawDiscard(card, x = 0, y = 0): # Discard a card from your hand.
   mute()
   if card.targetedBy:
      group = card.group
      drawDiscards = [replC for replC in group if replC.targetedBy]
      for c in drawDiscards: c.moveTo(me.piles['Discard Pile'])
      drawhandMany(me.Deck,len(drawDiscards),True)
      notify("{} has redrawn {} cards from their draw hand.".format(me,len(drawDiscards)))
   else:
      card.moveTo(me.piles['Discard Pile'])
      notify("{} has discarded {}.".format(me, card))  

def randomDiscard(group): # Discard a card from your hand randomly.
   mute()
   card = group.random() # Select a random card
   if card == None: return # If hand is empty, do nothing.
   notify("{} randomly discards a card.".format(me)) # Inform that a random card was discarded
   card.moveTo(me.piles['Discard Pile']) # Move the card in the discard pile.

def moveIntoDeck(group): 
   mute()
   Deck = me.Deck
   for card in group: card.moveTo(Deck)
   notify("{} moves their {} into their Deck.".format(me, group.name))
   
def drawhandMany(group = me.Deck, count = None, silent = False, scripted = False): #Same as drawMany, but puts the cards into the player's Draw Hand pile.
   mute()
   if not scripted:
      clearDrawHandonTable() # We clear existing Draw Hands on table as they may be redrawn
      clearRemainingActions() # We also clear action cards on the table as they may be redrawnn
   if count == None: count = askInteger("Draw how many cards to your Draw Hand?", 5)
   if count == None: return
   for i in range(0, count): 
      if len(group) == 0: reshuffle(group.player.piles['Discard Pile'])
      group.top().moveTo(me.piles['Draw Hand'])
   if not silent: notify("{} draws {} cards to their draw hand.".format(me, count))   

def discardDrawHand(group = me.piles['Draw Hand']): # Discards the player's whole Draw Hand.
   mute()
   Discard = me.piles['Discard Pile']
   notify("{} moved their {} ({} cards) to their discard pile.".format(me, group.name, len(group)))    
   for card in group: card.moveTo(Discard)

def aceevents(group = me.piles['Discard Pile']): # Goes through your discard pile and moves all events to the boot hill
   mute()
   notify("{} is going through their discard pile and acing all events".format(me))
   for card in group:
      if card.Type == 'Event': 
         card.moveTo(me.piles['Boot Hill'])
         notify("{} has aced {}".format(me,card))

def harrow(card):  # Returns the top dude card from boot hill, into the table with a harrowed marker.
   mute()
   if card.Type == 'Dude': 
      card.moveToTable(playerside * 200, 0)
      if not re.search(r'\bHarrowed\b\.', card.Text): 
         card.markers[HarrowedMarker] += 1
         notify("{} has brought {} back from the dead as one of the Harrowed".format(me,card))
      else: notify("{} has once again crawled out of a shallow grave.".format(card))
      modInfluence(card.Influence, loud)

def permRemove(card): # Takes a card from the boot hill and moves it to the shared "removed from play" pile.
   mute()
   card.moveTo(me.piles['Removed from Play'])
   notify("{} has permanently removed {} from play".format(me, card))
   
#---------------------------------------------------------------------------
# Draw Hand related actions 
#---------------------------------------------------------------------------
   
def revealHand(group, type = 'lowball', event = None, silent = False): 
# This function moves 5 cards from the player's Draw Hand pile into the table (normally there should be only 5 there when this function is invoked)
# It also highlights those cards, so that they are not confused with the cards in play
# The cards are moved to the table relevant to the player's side and they are placed next to each other so that their suit&ranks are read easily
# Finally their suit and rank are announced
   debugNotify(">>> revealHand()")
   mute()
   i = 0 
   clearDrawHandonTable()
   rank = ['','','','',''] # We create some empty lists for the suits and ranks.
   suit = ['','','','','']
   for card in group: # For each card in the Draw Hand pile...
      debugNotify("Iterating through card {}".format(card))
      foundjoker = 'no'
      if type == 'shootout':
         if card.name == "Fool's Joker": # Check if the card is a joker that is invalid for shootouts. If so, replace it
            card.moveTo(me.piles['Discard Pile'])
            notify ("A {} was revealed in {}'s shootout hand and has been discarded and replaced with a card from the top of the deck".format(card,me))
            if len(me.Deck) == 0: reshuffle()
            card = me.Deck.top() # Replace the card being processed with the top card of the player's deck.
            foundjoker = 'yes' #If we found a joker, make sure we delay the card suit/rank polling a bit.
         if playeraxis == Xaxis: card.moveToTable(homeDistance(card) - cardDistance(card) * 3 + i * (cwidth(card) / 4), cheight(card) * 2) 
         elif playeraxis == Yaxis: card.moveToTable(cwidth(card) / -2 + i * (cwidth(card) / 4), homeDistance(card) - cardDistance(card))
         else: card.moveToTable(i * (cwidth(card) / 4) - cwidth(card), 0) # If the player is not on any side, put the cards in the middle.
         # Move the card to the table, slightly to the right of any other cards from this hand
         if foundjoker == 'yes': # We only delay if we exchanged a joker, otherwise reveal gets too slow.
            random = rnd(100, 10000) # Wait a bit more, as in multiplayer games, things are slower.
      else: 
         if card.name == "Death's Head Joker" or card.name == "Fool's Joker": # Same as in shootouts above, but we don't want Death's Heads either
            if card.name == "Death's Head Joker":card.moveTo(me.piles['Boot Hill']) # Death's Head Jokers are aced
            else: card.moveTo(me.piles['Discard Pile']) # Fool's Jokers are discarded
            notify ("A {} was revealed in {}'s lowball hand and has been replaced with a card from the top of the deck".format(card,me))
            if len(me.Deck) == 0: reshuffle()
            card = me.Deck.top() # Put a new card in the draw hand and process that instead.
            foundjoker = 'yes'
         if playeraxis == Xaxis: card.moveToTable(homeDistance(card) - cardDistance(card) * 3 + i * (cwidth(card) / 4), cheight(card) * -2)
         elif playeraxis == Yaxis: card.moveToTable(cwidth(card) / -2 + i * (cwidth(card) / 4), homeDistance(card) - cardDistance(card))
         else: card.moveToTable(i * (cwidth(card) / 4) - cwidth(card), 0)
         if foundjoker == 'yes': random = rnd(100, 10000)
      if i == 2: cxp, cyp = card.position  # We note down the middle card location, so that we put the cheatin marker precicely.
      card.highlight = DrawHandColor # Highlight them
      if type == 'lowball' and card == event: 
         card.highlight = EventColor # If this is the selected event, highlight it differently
         notify("{} reveals an event this turn: {}".format(me,card)) 
      rank[i] = card.Rank # save their rank into the table
      suit[i] = card.Suit # save their suit into the table
      i += 1 # prepare for the next card.
   cheatResult = cheatinchk(rank,suit)
   if cheatResult != '': 
      if type == 'shootout':
         if playeraxis == Xaxis:
            cheatinNotice = table.create("cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1",cxp, cyp - 30, 1, False)
         elif playeraxis == Yaxis: 
            cheatinNotice = table.create("cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1",cxp, cyp - 30, 1, False)
         else: 
            cheatinNotice = table.create("cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1",cxp, 0, 1, False)
      else:
         if playeraxis == Xaxis:
            cheatinNotice = table.create("cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1",cxp, cyp + 30, 1, False)
         elif playeraxis == Yaxis: 
            cheatinNotice = table.create("cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1",cxp, cyp + 30, 1, False)
         else: 
            cheatinNotice = table.create("cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1",cxp, 30, 1, False)
      #cheatinNotice.highlight = DrawHandColor
   resultTXT = "{}{} ({} {}, {} {}, {} {}, {} {}, {} {})".format(PokerHand(rank,suit,type), cheatResult, fullrank(rank[0]), fullsuit(suit[0]), fullrank(rank[1]), fullsuit(suit[1]), fullrank(rank[2]), fullsuit(suit[2]), fullrank(rank[3]), fullsuit(suit[3]), fullrank(rank[4]), fullsuit(suit[4]))
   handRank = PokerHand(rank,suit,type,'comparison')
   if not silent:
      if type == 'shootout': # Finally, inform the players on what the hand is.
         notify("{}'s Shootout hand is {}. ".format(me, resultTXT))
      else:
         notify("{}'s Lowball Hand is {}. ".format(me, resultTXT))
   else: return resultTXT
   #me.HandRank = PokerHand(rank,suit,type,'comparison')
   me.setGlobalVariable('Hand Rank',str(PokerHand(rank,suit,type,'comparison')))
   #notify("===> Set my Hand Rank to {}".format(me.getGlobalVariable('Hand Rank'))) # Debug
   debugNotify("<<< revealHand()") 
      
def revealShootoutHand(group = me.piles['Draw Hand'], revealReady = False): 
# Simply call the procedure above and then compares hands to see who won. 
# The evaluation works only for 2 players but there can never be more than 2 players shooting it out anyway.
   debugNotify(">>> revealShootoutHand()")
   mute()
   if not revealReady:
      if len(group) > 5: 
         whisper("Please reduce your draw hand to 5 cards before revealing it")
         return
      if me.getGlobalVariable('RevealReady') != 'Shootout': 
         me.setGlobalVariable('RevealReady','Shootout')
         if me._id == 1: checkHandReveal(me) # Because for some reason this event doesn't trigger for the player who's variable changed.
      else: 
         waitingList = [
                        "{} is twitchin' their fingers...".format(me),
                        "{} is eyeballin' the clock...".format(me),
                        "{} is chewin' some tobacco menacingly...".format(me),
                        "{} is movin' their hand...".format(me),
                        "{} is squintin' threatingly...".format(me),
                        "{} is adjustin' their duster...".format(me),
                        "{} is tappin' their holster...".format(me),
                        "{} is shufflin' their foot...".format(me)
         ]
         notify("{}".format(waitingList[rnd(0,len(waitingList) - 1)]))
   else:
      me.setGlobalVariable('RevealReady','False')
      if not len(group): return # IF we have an empty hand just exit silently)
      debugNotify("About to revealHand(). group = {}".format(group.name))
      revealHand(group, shootout)
   debugNotify(">>> revealShootoutHand()")
   
def revealLowballHand(group = me.piles['Draw Hand'], revealReady = False): 
   debugNotify(">>> revealLowballHand()")
   mute()
   if not revealReady:
      if len(group) > 5: 
         whisper("Please reduce your draw hand to 5 cards before revealing it")
         return
      if me.getGlobalVariable('RevealReady') != 'Lowball': 
         me.setGlobalVariable('RevealReady','Lowball')
         if me._id == 1: checkHandReveal(me) # Because for some reason this event doesn't trigger for the player who's variable changed.
      else: 
         notify("{} is waiting patiently for everyone else to reveal their lowball hand...".format(me))
   else:
   # Checking for events before passing on to the reveal function
      me.setGlobalVariable('RevealReady','False')
      if not len(group): return # IF we have an empty hand just exit silently)
      evCount = 0
      foundEvents = ['','','','',''] # We need to declare the list because it will not work if it doesn't exist.
      for card in group:
         if card.Type == 'Event': # Check if the card is an event and save it's name.
            foundEvents[evCount] = card
            evCount += 1 # Count how many events we have in the hand
      if evCount > 1: # If we have more than one, select one at random
         eventPointer = rnd(0,evCount-1)
         revealHand(group, 'lowball',foundEvents[eventPointer]) # Then pass its name to the next function so that it can be highlighted and announced.
      elif evCount == 1: # If there's only one event, then just pass it's name on the revealHand function so that it can be highlighted and announced.
         revealHand(group, 'lowball',foundEvents[0])      
      else: revealHand(group, 'lowball')
   debugNotify("<<< revealLowballHand()")

def revealHandAsk(group):
   if getGlobalVariable('Shootout') == 'True': revealShootoutHand(group)
   else: revealLowballHand(group)
   
def playLowball(group = me.Deck):
# This function does the following. 
# * It takes one Ghost Rock from the player and adds it to the shared Lowball pot.
# * It draws 5 cards from the deck with the drawHandMany() function
# * It reveals those 5 with the revealLowballHand() function
# * It receives the winner result of the lowball and announces it
# * If there isn't a tie, then uses it gives the winner all the GR from the shared lowball pot
# * It assigns a "Winner" counter to the winner's outfit and wipes the previous winner's marker.
   mute()
   if me.getGlobalVariable('RevealReady') == 'Lowball': notify("{} is waiting patiently for everyone else to reveal their lowball hand...".format(me))
   else:
      if getGlobalVariable('Phase') != '1':
         #if not confirm(":::WARNING::: It is not yet the Gamblin' phase. Do you want to jump to lowball now?"): return
         goToGamblin()
      drawhandMany(me.Deck, 5, True)
      betLowball()
      revealLowballHand()

def betLowball(group = table,x = 0,y = 0, silent = False): # Bets a 1 ghost rock to the lowball pot
   mute()
   me.GhostRock -= 1
   potCard = getPotCard()
   potCard.markers[mdict['Ghost Rock']] += 1
   if not silent: notify ("{} has put their ante in their Lowball pot.".format(me))

def winLowball(group = table, x = 0,y = 0, winner = me): # A function which sets the lowball winner and awards him the lowball money
   mute()
   #confirm('winner = {}'.format(winner.name)) # Debug
   debugNotify(">>> winLowball()")
   #potCard = getPotCard()
   if getGlobalVariable('Phase') != '1' and not confirm(":::WARNING::: You are not currently in the Gamblin' phase. Are you sure you want to win lowball now?"): return 
   #if not getPotCard(True) and not confirm("Lowball winner seems to have been declared already. Proceed to win the lowball pot again anyway?"): return
   for player in getActivePlayers(): 
      if player == me: me.setGlobalVariable('UpkeepDone','False')
      else: remoteCall(player,'setPlayerVariable',['UpkeepDone','False'])      
   setWinner(winner) # Set the winner's marker
   #winner.GhostRock += potCard.markers[mdict['Ghost Rock']] # Give them all the money from the lowball pot
   winner.GhostRock += len(getActivePlayers()) # We just give them one GR per player, to avoid OCTGN lag issues
   notify("{} is the lowball winner has received {} Ghost Rock from the pot".format(winner, len(getActivePlayers()))) # Notify all other players
   clearPotCard() # Remove the lowball card from the table
   for card in table: # once we have a winner, we clear all the draw hands from the table.
      if card.highlight == DrawHandColor: 
         discard(card)  
         card.highlight = None
   goToUpkeep()
   debugNotify("<<< winLowball()")
      
