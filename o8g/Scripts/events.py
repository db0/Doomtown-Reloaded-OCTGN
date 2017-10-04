import re
import collections
import time

def chkTwoSided():
   mute()
   #confirm('test1')
   if table.isTwoSided(): information(":::WARNING::: This game is NOT designed to be played on a two-sided table. Things will not look right!! Please start a new game and unckeck the appropriate button.")
   fetchCardScripts()

def checkDeck(player,groups):
   mute()
   foundOutfit = False
   if player == me:
      #confirm(str([group.name for group in groups]))
      for group in groups:
         if group == me.hand:
            for card in group:
               if card.Type == 'Outfit': 
                  notify("{} is playing {}".format(player,card.name))
                  foundOutfit = True
            if not foundOutfit: information(":::ERROR::: No outfit card found! Please put an outfit card in your deck before you try to use it in a game!")
         else:
            group.setVisibility('me')
            counts = collections.defaultdict(int)
            ok = True
            for card in group:
               if card.Type == 'Joker': 
                  counts['Jokers'] += 1
                  if counts['Jokers'] > 2:
                     ok = False
                     notify(":::ERROR::: More than 2 Jokers found in{}'s deck!".format(player))
               if card.name == 'Gunslinger' or card.name == 'Nature Spirit' or card.name == 'Ancestor Spirit':
                  ok = False
                  notify(":::ERROR::: Token card found in {}'s deck!".format(player))
               counts[card.name] += 1
               if counts[card.name] > 4: 
                  ok = False
                  notify(":::ERROR::: More than 4 cards of the same name ({}) found in {}'s deck!".format(card.name,player))
               counts[card.Rank + card.Suit] += 1
               if counts[card.Rank + card.Suit] > 4: 
                  ok = False
                  notify(":::ERROR::: More than 4 cards of the same suit and rank ({} of {}) found in {}'s deck!".format(card.Rank,card.Suit,player))
            deckLen = len(group) + len([c for c in me.hand if (c.Type != 'Outfit' and c.Type != 'Legend')]) - counts['Jokers']
            if deckLen != 52:
               ok = False
               notify(":::ERROR::: {}'s deck is not exactly 52 play cards ({})!".format(player,deckLen))
            group.setVisibility('None')
            if ok: notify("-> Deck of {} is OK!".format(player))
            else: 
               notify("-> Deck of {} is _NOT_ OK!".format(player))
               information("We have found illegal cards in your deck. Please load a legal deck!")
   # WiP Checking deck legality. 
   
def chooseSide(silent = False): # Called from many functions to check if the player has chosen a side for this game.
   mute()
   global playerside, playeraxis
   plCount = 0
   for player in sorted(getPlayers()):
      if len(player.Deck) == 0 and len(player.piles['Discard Pile']) == 0: continue # We ignore spectators
      plCount += 1
      if player != me: continue # We only set our own side
      if plCount == 1: # First player is on the right
         playeraxis = Xaxis
         playerside = 1
         if not silent: notify(":> {}'s gang arrives on the west side of town.".format(me))
      elif plCount == 2: # First player is on the left
         playeraxis = Xaxis
         playerside = -1
         if not silent: notify(":> {}' dudes scout warily from the east.".format(me))
      elif plCount == 3: # Third player is on the bottom
         playeraxis = Yaxis
         playerside = 1
         if not silent: notify(":> {}' outfit sets up on the south entrance.".format(me))
      elif plCount == 4: # Fourth player is on the top
         playeraxis = Yaxis
         playerside = -1
         if not silent: notify(":> {}'s posse claims the north entrance.".format(me))
      else:
         playeraxis = None  # Fifth and upward players are unaligned
         playerside = 0
         if not silent: notify(":> {}' arrive late to the party.".format(me))

def checkMovedCards(player,cards,fromGroups,toGroups,oldIndexs,indexs,oldXs,oldYs,xs,ys,faceups,highlights,markers):
   mute()
   for iter in range(len(cards)):
      card = cards[iter]
      fromGroup = fromGroups[iter]
      toGroup = toGroups[iter]
      oldIndex = oldIndexs[iter]
      index = indexs[iter]
      oldX = oldXs[iter]
      oldY = oldYs[iter]
      x = xs[iter]
      y = ys[iter]
      faceup = faceups[iter]
      highlight = highlights[iter]
      marker = markers[iter]
      #if isScriptMove: return # If the card move happened via a script, then all automations should have happened already.
      if fromGroup == me.hand and toGroup == table: 
         if card.Type == 'Outfit': 
            card.moveTo(me.hand)
            update()
            setup(group = table)
         
         else: playcard(card, retainPos = True)
         
      elif fromGroup == me.Deck and toGroup == table and card.owner == me: # If the player moves a card into the table from their Deck we assume they are revealing it as a pull or draw hand replacement.
         card.highlight = DrawHandColor
         notify("{} reveals a {} of {}".format(me,fullrank(card.Rank), fullsuit(card.Suit)))
      elif fromGroup != table and toGroup == table and card.owner == me: # If the player moves a card into the table from Hand, or Trash, we assume they are installing it for free.
         reCalculate(notification = 'silent')
         if card.Type == 'Goods' or card.Type == 'Spell':
            hostCard = findHost(card)
            if hostCard: 
               attachCard(card,hostCard)
               notify(":> {} was attached to {}".format(card,hostCard))
      elif fromGroup == table and toGroup != table and card.owner == me: # If the player dragged a card manually from the table to their discard pile...
         clearAttachLinks(card) # If the card was manually removed from play then we simply take care of any attachments
         reCalculate(notification = 'silent')
      elif fromGroup == table and toGroup == table and card.controller == me: # If the player dragged a card manually to a different location on the table, we want to re-arrange the attachments
         if card.Type == 'Dude' or card.Type == 'Deed' or card.Type == 'Outfit': 
            update()
            orgAttachments(card) 

def chkMarkerChanges(card,markerName,oldValue,newValue,isScriptChange):
   mute()
   #notify(markerName) #debug
   #return # Not in use yet
   if isScriptChange: return # If the marker change happened via a script, then all automations should have happened already.
   reCalculate(notification = 'silent')
   #if markerName == "+1 Influence": modInfluence(-1)
   #if markerName == "-1 Influence" and num(card.Influence) > card.markers[mdict['InfluenceMinus']]: modInfluence()
   #if markerName == "+1 Control": modControl(-1)
   #if markerName == "-1 Control" and num(card.Influence) > card.markers[mdict['ControlMinus']]: modControl()   
     
def checkPlayerGlobalVars(player,name,oldValue,value):
   mute()
   if name == 'RevealReady' and me._id == 1 and value != 'False': checkHandReveal(player) # Only the hosting player reveals hands
   if name == 'Hand Rank' and me._id == 1 and value != 'N/A': compareHandRanks() # Only the hosting player reveals hands

def checkHandReveal(playerVar):           
   playersReady = []
   if getGlobalVariable('Shootout') == 'True': # If it's a shootout, we only care to see if that player's opponent is ready.
      for player in getActivePlayers():
         if player.getGlobalVariable('RevealReady') == 'Shootout': playersReady.append(player)
         if len(playersReady) == 2: break
      if len(playersReady) < 2 and len(getPlayers()) != 1:
         notify("{} is ready to reveal their shootout hand. Waiting for their opponent...".format(playerVar))
      else:
         for player in playersReady:
            remoteCall(player,'revealShootoutHand',[player.piles['Draw Hand'],True,False])
   else:
      for player in getActivePlayers():
         if player.getGlobalVariable('RevealReady') != 'False': playersReady.append(player)
      if len(playersReady) < len(getActivePlayers()):
         notify("{} is ready to reveal their lowball hand. Waiting for everyone else...".format(playerVar))
      else:
         for player in playersReady:
            remoteCall(player,'revealLowballHand',[player.piles['Draw Hand'],True,False])
   
def compareHandRanks():
   if getGlobalVariable('Shootout') == 'True': 
      competingPlayers = []
      for player in getActivePlayers():
         if player.getGlobalVariable('Hand Rank') != 'N/A': competingPlayers.append(player)
         if len(competingPlayers) == 2: break
      if len(competingPlayers) == 2: 
         if num(competingPlayers[0].getGlobalVariable('Hand Rank')) < num(competingPlayers[1].getGlobalVariable('Hand Rank')): 
            notify("\n-- The winner is {} by {} ranks and {} must absorb as many casualties in this round.".format(competingPlayers[1], (num(competingPlayers[1].getGlobalVariable('Hand Rank')) - num(competingPlayers[0].getGlobalVariable('Hand Rank'))), competingPlayers[0]))
         elif num(competingPlayers[0].getGlobalVariable('Hand Rank')) > num(competingPlayers[1].getGlobalVariable('Hand Rank')): 
            notify("\n-- The winner is {} by {} ranks and {} must absorb as many casualties in this round.".format(competingPlayers[0], (num(competingPlayers[0].getGlobalVariable('Hand Rank')) - num(competingPlayers[1].getGlobalVariable('Hand Rank'))), competingPlayers[1]))
         else: 
            notify ("\n-- The Shootout is a tie. Both player suffer one casualty")
         clearHandRanks()
   else:
      winner = findLowballWinner()
      if winner == 'tie': notify ("\n-- It's a tie! Y'all need to compare high cards to determine the lucky bastard. (Winner needs to press Ctrl+W)")
      else: # Otherwise the evuation will fail which means that the winner variable holds is a player class.
         notify ("\n-- The winner is {}. (They need to press Ctrl+W once the resolution phase has ended.)".format(winner)) # Thus we can just announce them.
   
def reconnect(group = table, x=0, y=0):
   global OutfitCard
   chooseSide(True)
   for card in table:
      if card.owner == me and card.Type == 'Outfit': 
         OutfitCard = card
   fetchCardScripts()
   barNotifyAll('#990000','{} has reconnected to the game'.format(me.name))