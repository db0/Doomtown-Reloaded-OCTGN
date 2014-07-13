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
   # WiP Checking deck legality. 
   
def chooseSide(silent = False): # Called from many functions to check if the player has chosen a side for this game.
   mute()
   global playerside, playeraxis
   plCount = 0
   for player in sorted(getPlayers()):
      if len(player.Deck) == 0: continue # We ignore spectators
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

def checkMovedCard(player,card,fromGroup,toGroup,oldIndex,index,oldX,oldY,x,y,isScriptMove,highlight = None,markers = None):
   mute()
   debugNotify("isScriptMove = {}".format(isScriptMove))
   if isScriptMove: return # If the card move happened via a script, then all automations should have happened already.
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
      if card.Type == 'Dude' or card.Type == 'Deed': 
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
   
def reconnect(group = table, x=0, y=0):
   global OutfitCard
   chooseSide(True)
   for card in table:
      if card.owner == me and card.Type == 'Outfit': 
         OutfitCard = card
   fetchCardScripts()
   barNotifyAll('#990000','{} has reconnected to the game'.format(me.name))