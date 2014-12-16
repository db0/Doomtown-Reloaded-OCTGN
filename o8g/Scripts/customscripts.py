    # Python Scripts for the Star Wards LCG definition for OCTGN
    # Copyright (C) 2013  Konstantine Thoukydides

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

###==================================================File Contents==================================================###
# This file contains the autoscripting for cards with specialized effects. So called 'CustomScripts'
# * UseCustomAbility() is used among other scripts, and it just one custom ability among other normal core commands
# * CustomScipt() is a completely specialized effect, that is usually so unique, that it's not worth updating my core commands to facilitate it for just one card.
# Remote Functions are custom functions coming from specific cards which usually affect other players and are called via remoteCall()
###=================================================================================================================###

def UseCustomAbility(Autoscript, announceText, card, targetCards = None, notification = None, n = 0):
   mute()
   announceString = ''
   debugNotify(">>> UseCustomAbility() with Autoscript: {}".format(Autoscript)) #Debug
   debugNotify("<<< UseCustomAbility() with announceString: {}".format(announceString)) #Debug
   return announceString

def CustomScript(card, action = 'PLAY'): # Scripts that are complex and fairly unique to specific cards, not worth making a whole generic function for them.
   debugNotify(">>> CustomScript() with action: {}".format(action)) #Debug
   mute()
   discardPile = me.piles['Discard Pile']
   deck = me.piles['Deck']
   bootHill = me.piles['Boot Hill']
   if card.name == "Bottom Dealin'" and action == 'PLAY':
      debugNotify("Bottom Dealin' Script")
      drawHandPlayers = []
      for c in table:
         if c.controller != me and c.controller not in drawHandPlayers and c.highlight == DrawHandColor: drawHandPlayers.append(c.controller)
      if len(drawHandPlayers) == 1: targetPL = drawHandPlayers[0]
      elif len(drawHandPlayers) == 0:
         whisper(":::ERRROR::: No valid player found to bottom deal. Aborting!")
         return 'ABORT'
      else: 
         choice = SingleChoice("Please choose which of your opponents you're bottom dealin'.", [pl.name for pl in drawHandPlayers])
         if choice == None: return 'ABORT'
         targetPL = drawHandPlayers[choice]
      remoteCall(targetPL,'clearDrawHandonTable',[])
      drawhandMany(me.Deck, 5, True,scripted = True)
      if getGlobalVariable('Shootout') == 'True': Drawtype = 'shootout'
      else: Drawtype = 'lowball'
      resultTXT = revealHand(me.piles['Draw Hand'], type = Drawtype, event = None, silent = True)
      notify("{}'s new hand rank is {}".format(targetPL,resultTXT))
   elif card.name == "Coachwhip!" and action == 'PLAY':
      debugNotify("Coachwhip Script")
      targetDude = [c for c in table if c.targetedBy and c.targetedBy == me and c.controller != me and c.Type == 'Dude']
      if not len(targetDude): notify(":> No target selected. Cheating player has to select one of their dudes to boot or ace")
      else:
         if getGlobalVariable('Shootout') == 'True': 
            aceTarget(targetCards = targetDude[1:], silent = True)
            notify(":> {} is caught cheating in a shootout while {} has a legal hand and the Coachwhip forces them to ace {}".format(targetDude[0].controller,me,targetDude[0]))
         else: 
            remoteCall(targetDude[0].controller,'boot',[targetDude[0]])
            notify(":> {} is caught cheating in lowball while {} has a legal hand and the Coachwhip forces them to boot {}".format(targetDude[0].controller,me,targetDude[0]))
   elif card.name == "Elander Boldman" and action == 'USE':
      if getGlobalVariable('Shootout') != 'True': 
         whisper(":::ERROR::: {} can only use his shootout ability during shootouts".format(card))
         return 'ABORT'
      foundDude = False
      hostCards = eval(getGlobalVariable('Host Cards'))
      for c in table:
         attachedWG = [Card(att_id) for att_id in hostCards if hostCards[att_id] == c._id and re.search(r'Weapon',Card(att_id).Keywords) and re.search(r'Gadget',Card(att_id).Keywords)]
         if c.targetedBy and c.targetedBy == me and c.Type == 'Dude' and c.controller == me and len(attachedWG): # If we've targeted a dude with a weapon gadget...
            rank,suit = pull(silent = True)
            notify("{} attempts to optimize {} and pulls a {} {}.".format(card,attachedWG[0],rank, suit))
            if suit == 'Clubs':
               notify(":> Oops! The {} explodes. {} is discarded".format(attachedWG[0],c))
               if confirm("You pulled a club! Go ahead and discard {}?".format(c.name)): discard(c,silent = True)
            else:
               attachedWG[0].markers[mdict['BulletShootoutPlus']] += 3
               notify(":> The tweaks done on {} give it +3 bullet bonus for this shootout".format(attachedWG[0],c))
            foundDude = True
            break
      if not foundDude: 
         whisper(":::ERROR::: No dude targeted. Aborting!")
         return 'ABORT'
   elif card.name == "Jarrett Blake" and action == 'USE':
      if getGlobalVariable('Shootout') != 'True': 
         whisper(":::ERROR::: {} can only use his shootout ability during shootouts".format(card))
         return 'ABORT'
      hostCards = eval(getGlobalVariable('Host Cards'))
      if not len([Card(att_id) for att_id in hostCards if hostCards[att_id] == card._id and re.search(r'Horse',Card(att_id).Keywords)]):
         whisper(":::ERROR::: {} can only use his shootout ability while they have a horse attached".format(card))
         return 'ABORT'
      foundDude = False
      for c in table:
         if c.targetedBy and c.targetedBy == me and c.Type == 'Dude' and c.controller == me and (c.highlight == AttackColor or c.highlight == DefendColor): # If we've targeted a dude in a shootout
            x,y = c.position
            Jx,Jy = card.position
            c.moveToTable(Jx,Jy)
            card.moveToTable(x,y)
            orgAttachments(card)
            orgAttachments(c)
            participateDude(card)
            leavePosse(c)
            foundDude = True
            notify("{} switches places with {}".format(card,c))
            break
      if not foundDude: 
         whisper(":::ERROR::: No dude targeted. Aborting!")
         return 'ABORT'         
   elif card.name == "Morgan Cattle Co." and action == 'USE':
      targetDeed = findTarget('DemiAutoTargeted-atDeed-fromHand-choose1')
      if not len(targetDeed):
         whisper(":::ERROR::: You have no deeds in your hand to attempt to build")
         return 'ABORT'
      targetDude = findTarget('DemiAutoTargeted-atDude-isUnbooted-hasProperty{Influence}gt0-choose1')
      if not len(targetDude):
         whisper(":::ERROR::: You have no available dudes in play to build that deed")
         return 'ABORT'
      reduction = compileCardStat(targetDude[0], 'Influence')
      playcard(targetDeed[0],costReduction = reduction)
      x,y = targetDeed[0].position
      boot(targetDude[0],forced = 'boot')
      targetDude[0].moveToTable(x + cardDistance(), y)
      orgAttachments(targetDude[0])
      notify("{} uses {} and boots {} to build {}, reducing its cost by {}.".format(me,card,targetDude[0],targetDeed[0],reduction))      
   elif card.name == "The Union Casino" and action == 'USE':
      targetDude = findTarget('Targeted-atDude')
      if not len(targetDude):
         whisper(":::ERROR::: You need to target an unbooted dudes at this deed to use this ability")
         return 'ABORT'
      boot(targetDude[0],silent = True)
      myBet = askInteger("How much ghost rock do you want to bet on the Union Casino?",4)
      if payCost(myBet, loud) == 'ABORT': return 'ABORT'
      if myBet <= 3: notify(":> {} felt the need to burn some money by wasting {} Ghost Rock on Union Casino. Nothing else happens".format(me,myBet))
      else:
         notify(":> {} boots {} and uses {}'s ability to bet {}".format(me,targetDude[0],card,myBet))
         for player in getActivePlayers():
            if player != me or len(getActivePlayers()) == 1: remoteCall(player,'UnionCasino',[card,myBet,targetDude[0],'others bet']) 
   elif card.name == "This is a Holdup!" and action == 'PLAY':
      targetDeed = findTarget('Targeted-atDeed')
      if not len(targetDeed):
         whisper(":::ERROR::: You need to target a deed with production to steal from first. Aborting.")
         return 'ABORT'
      deed = targetDeed[0]
      if deed.owner.GhostRock == 0:
         whisper(":::ERROR::: {} has no money in their bank to steal. Aborting")
         return 'ABORT'
      deedProd = compileCardStat(deed, stat = 'Production')
      if deedProd == 0:
         whisper(":::ERROR::: {} has no production to steal. Aborting")
         return 'ABORT'
      targetDude = findTarget('Targeted-atDude-isUnbooted')
      if not len(targetDude):
         whisper(":::ERROR::: You need to target an unbooted dudes at this deed to use this ability. Aborting.")
         return 'ABORT'      
      boot(targetDude[0],silent = True, forced = 'boot')
      if deedProd > deed.owner.GhostRock: 
         notify(":> {} doesn't have the full {} ghost rock to steal, so {} is taking the {} possible.".format(deed.owner,deedProd,card,deed.controller.GhostRock))
         me.GhostRock += deed.owner.GhostRock # We cannot steal more money than the target player has.
         targetDude[0].markers[mdict['Bounty']] += deed.owner.GhostRock
         deed.owner.GhostRock = 0
      else:
         notify(":> {} is holding up {} and taking {} ghost rock from {}.".format(targetDude[0],deed,deedProd,deed.owner))
         me.GhostRock += deedProd # We cannot steal more money than the target player has.
         deed.owner.GhostRock -= deedProd      
         targetDude[0].markers[mdict['Bounty']] += deedProd
   elif card.name == "Unprepared" and action == 'PLAY':
      targetDude = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1')
      if not len(targetDude):
         whisper(":::ERROR::: You need to target an dude in this shootout. Aborting.")
         return 'ABORT'
      boot(targetDude[0],silent = True, forced = 'boot')
      TokensX('Put1Unprepared', '', targetDude[0])
      dudeGoods = findTarget('AutoTargeted-atGoods_or_Spell-onAttachment', card = targetDude[0])
      for attachment in dudeGoods: 
         boot(attachment,silent = True, forced = 'boot')
         TokensX('Put1Unprepared', '', attachment)         
      targetDude[0].markers[mdict['BulletShootoutMinus']] += 1
      notify("{} has been caught with their pants down.".format(targetDude[0]))
### SB 1-3 ###
   elif card.name == "Make 'em Sweat" and action == 'PLAY':
      myDude = findTarget('DemiAutoTargeted-atDude-targetMine-isUnbooted-isParticipating-choose1',card = card, choiceTitle = "Choose which of your dudes to boot for {}".format(card.name))
      opDude = findTarget('DemiAutoTargeted-atDude-targetMine-isParticipating-choose1',card = card, choiceTitle = "Choose which dude to affect with {}".format(card.name))
      if len(myDude) == 0 or len(opDude) == 0: return 'ABORT'
      boot(myDude[0], silent = True)
      bulletReduction = compileCardStat(myDude[0], stat = 'Bullets')
      if bulletReduction: minusBulletShootout(opDude[0],count = bulletReduction)
      if compileCardStat(opDude[0], stat = 'Bullets') == 0 and opDude[0].orientation == Rot0: 
         boot(opDude[0], silent = True)
         sweatedTXT = ' {} is booted.'.format(opDude[0])
      else: sweatedTXT = ''
      notify(":> {} boots to reduce {}'s bullets by {}.{}".format(myDude[0],opDude[0],bulletReduction,sweatedTXT))
   elif card.name == "The R&D Ranch" and action == 'USE':
      rank,suit = pull(silent = True)
      me.GhostRock += 2 # You always get the GR first anyway.
      if suit == 'Clubs':
         notify(":> {} tries to use {} and pulled a {} of {}. It all goes horribly wrong! They have to discard the deed and all cards at that location".format(me,card,rank,suit))
         if confirm("You pulled a club! Proceed to discard {}?".format(card.name)): discard(card)
         else: notify(":::INFO::: {} did not discard {} even though they pulled a {}".format(me,card,suit))
      else:
         notify(":> {} succesfully used {} by pulling a {} of {} and produced some very tasty meat indeed. They gain 2 ghost rock.".format(me,card,rank,suit))      
   elif card.name == "Gang Yi" and action == 'USE':
      if getGlobalVariable('Shootout') != 'True': 
         whisper(":::ERROR::: {} can only use his shootout ability during shootouts".format(card))
         return 'ABORT'
      foundDude = False
      for c in table:
         if c.targetedBy and c.targetedBy == me and c.Type == 'Dude' and c.controller == me and (c.highlight == AttackColor or c.highlight == DefendColor): # If we've targeted a dude in a shootout
            x,y = c.position
            Jx,Jy = card.position
            c.moveToTable(Jx,Jy)
            card.moveToTable(x,y)
            orgAttachments(card)
            orgAttachments(c)
            participateDude(card)
            leavePosse(c)
            foundDude = True
            notify("{} switches places with {}".format(card,c))
            break
      if not foundDude: 
         whisper(":::ERROR::: No dude targeted. Aborting!")
         return 'ABORT'         
   elif card.name == "Telepathy Helmet" and action == 'USE':
      opponents = [pl for pl in getActivePlayers() if (pl != me or len(getActivePlayers()) == 1)]
      if len(opponents) == 1: choice = 0
      else: choice = SingleChoice("Choose which player's hand to look at",[pl.name for pl in opponents])
      if choice == None: return
      remoteCall(opponents[choice],'TelepathyHelmet',[me,card]) 
   else: notify("{} uses {}'s ability".format(me,card)) # Just a catch-all.
   return 'OK'


def markerEffects(Time = 'Start'):
   debugNotify(">>> markerEffects() at time: {}".format(Time)) #Debug
   cardList = [c for c in table if c.markers]
   for card in cardList:
      for marker in card.markers:
         if (Time == 'Sundown'
               and (re.search(r'Bad Company',marker[0])
                 or re.search(r'High Noon:',marker[0])
                 or re.search(r'Hiding in the Shadows',marker[0])
                 or re.search(r'Rumors',marker[0]))):
            TokensX('Remove999'+marker[0], marker[0] + ':', card)
            notify("--> {} removes the {} resident effect from {}".format(me,marker[0],card))
         if Time == 'Sundown' and re.search(r'Come Git Some',marker[0]) and card.controller == me and card.owner == me: # This is the Sloane outfit ability
            if card.markers[mdict['PermControlPlus']]: 
               choice = SingleChoice("Do you want to take one Ghost Rock per player?", ['No, {} is not in the Town Square anymore.'.format(card.name),'Yes! Take 1 GR per player.'])
            else: choice = SingleChoice("Do you want to take one Ghost Rock per player, or put a permanent control point on this dude?'.", ['None of the above. {} is not in the Town Square anymore.'.format(card.name),'Take 1 GR per player.','Put 1 permanent CP on {}.'.format(card.name)])
            if not choice: # If the choice is 0 or None (i.e. closed the selection window) the dude is assumed to be out of the Town Square
               notify("{}'s {} didn't manage to hold the Town Square. They gain nothing this turn".format(me,card,len(getActivePlayers()) - 1))
            elif choice == 1: # If the choice is 0 or None (i.e. closed the selection window, we give them money)
               me.GhostRock += len(getActivePlayers()) - 1
               notify("{}'s {} and shakes down the citizens of Gomorra for {} Ghost Rock".format(me,card,len(getActivePlayers()) - 1))
            else: 
               notify("{}'s {} puts the fear of the gun to the town, giving them one permanent control point".format(me,card))
               card.markers[mdict['PermControlPlus']] += 1
            card.markers[marker] = 0
         if (Time == 'ShootoutEnd'
               and (re.search(r'Sun In Yer Eyes',marker[0])
                 or re.search(r'Unprepared',marker[0])
                 or re.search(r'Shootout:',marker[0]))):
            TokensX('Remove999'+marker[0], marker[0] + ':', card)
            notify("--> {} removes the {} resident effect from {}".format(me,marker[0],card))
   
#------------------------------------------------------------------------------
# Remote Functions
#------------------------------------------------------------------------------
      
def UnionCasino(card,mainBet,targetDude, function = 'others bet'):
   mute()
   if function == 'others bet' and len(getActivePlayers()) > 1:
      minBet = mainBet - 3
      if minBet < 0: minBet = 0
      myBet = askInteger("{} has started the Union Casino pool with {}. You need {} to check. Bet how much?".format(card.controller,mainBet,minBet),0)
      if payCost(myBet, loud) == 'ABORT': myBet = 0
      if myBet == 0: TokensX('Put1Union Casino Zero Bet:{}'.format(me.name), '', card)
      else: TokensX('Put{}Union Casino Bet:{}'.format(myBet,me.name), '', card)
      remoteCall(card.controller,'UnionCasino',[card,mainBet,targetDude,'resolve'])
   else:
      #confirm('b')   
      betPlayers = 1
      for player in getActivePlayers():
         if player != me and findMarker(card, ':{}'.format(player.name)): betPlayers += 1
      if betPlayers == len(getActivePlayers()): # We compare to see if the controller won only after all players have finished betting.
         highBet = 0
         highBetter = None
         #confirm('a')
         for player in getActivePlayers():
            if player != me:
               zeroMarker = findMarker(card, 'Union Casino Zero Bet:{}'.format(player.name))
               if zeroMarker:
                  card.markers[zeroMarker] = 0
                  continue
               else: 
                  currBet = findMarker(card, ':{}'.format(player.name))
                  if highBet < card.markers[currBet]:
                     highBet = card.markers[currBet]
                     card.markers[currBet] = 0
                     highBetter = player
         if mainBet >= (highBet + 4) or not highBetter: 
            targetDude.markers[mdict['PermControl']] += 1
            notify(":> {} outbid all other players by {} and thus {} gains a permanent control point".format(me,mainBet - highBet,targetDude))
         else: notify(":> {} checked the bet by raising {} to {}'s {}".format(me,highBet,card.controller,mainBet))

def PlasmaDrill(card):
   mute()
   production = compileCardStat(card, stat = 'Production')
   if production > me.GhostRock: extraTXT = "\n\nAttention! You do not seem to have enough Ghost Rock to save this deed from the Plasma Drill. Pay anyway?\
                                          \n(Saying yes will bring your ghost rock bank to the negative)"                                          
   else: extraTXT = ''
   if confirm("Do you want to pay {} to save {} from the Plasma Drill?{}".format(production,card.name,extraTXT)) and payCost(production) != 'ABORT': 
      notify(":> {} pays {} to repair {} from the damage inflicted by the Plasma Drill".format(me,production,card))
   else:
      discard(card,silent = True)
      notify(":> {} is damaged beyond repair by the plasma drill and is discarded".format(card))
                               
def TelepathyHelmet(originator,card):
   mute()
   notify("{}'s {} is revealing {} hand...".format(originator,card,me))
   me.hand.addViewer(originator)
   update()
   remoteCall(originator,'WhisperCards',[me,[c for c in me.hand]])
   while not confirm("You are now revealing your hand to {}. Press Yes to continue, Press No to ping the other player to see if they had enough time to see the cards"):
      notify("{} wants to know if it's OK to hide their hand once more".format(me))
   me.hand.removeViewer(originator)
   notify("{} hides their play hand once more".format(me))
   
def WhisperCards(player,cardList):
   mute()
   initText = "{} is revealing: ".format(player)
   for c in cardList:
      initText += "- {}\n".format(c)   
   whisper(cardList)