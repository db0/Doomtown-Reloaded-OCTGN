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
   if card.name == "Plasma Drill":
      targetDeed = findTarget('Targeted-atDeed',card = card)
      if len(targetDeed) == 0: return 'ABORT'
      production = compileCardStat(targetDeed[0], stat = 'Production')
      if not production: notify(":> {} uses the plasma drill on, but it has no production, so that was fairly useless, wasn't it?".format(me))
      else: remoteCall(targetDeed[0].owner,'PlasmaDrill',[targetDeed[0]])      
   elif card.name == "Allie Hensman":    
      remoteCall(targetCards[0].controller,'AllieHensmanXP',[targetCards[0],card])
   ### F&F ###    
   
   elif card.name == "Desolation Row":
      leader = targetCards[0]
      if leader.group == table and (leader.highlight == AttackColor or leader.highlight == InitiateColor):
         count = compileCardStat(leader, stat = 'Bullets')
         if count > 4: count = 4
         me.GhostRock += count
         leader.markers[mdict['Bounty']] += 2
         notify("{} completes the {} job and gains {} ghost rock, while {}'s bounty increases by 2".format(me,card,count,leader))
      else: notify("{} completes the {} job abut gains nothing since {} is not in their posse anymore".format(me,card,leader))
   elif card.name == "Mirror, Mirror":
      #targetCards = findTarget('DemiAutoTargeted-atDude-isParticipating-choose1',card = card, choiceTitle = "Choose which dude to mirror.")
      #if not len(targetCards): return 'ABORT'
      huckster = fetchHost(card)
      target = targetCards[0]         
      hucksterBullets = compileCardStat(huckster, stat = 'Bullets')
      targetBullets = compileCardStat(target, stat = 'Bullets')
      if re.search(r'-isFirstCustom',Autoscript):
         if hucksterBullets < targetBullets: plusBulletShootout(huckster, count = targetBullets - hucksterBullets, silent = True)
         elif hucksterBullets > targetBullets: minusBulletShootout(huckster, count = hucksterBullets - targetBullets, silent = True)
         if fetchDrawType(target) == 'Draw' and fetchDrawType(huckster) == 'Stud': 
            TokensX('Remove999Shootout:Stud', '', huckster)
            if huckster.properties['Draw Type'] == 'Stud': TokensX('Put1Shootout:Draw', '', huckster)  
         elif fetchDrawType(target) == 'Stud' and fetchDrawType(huckster) == 'Draw': 
            TokensX('Remove999Shootout:Draw', '', huckster)  
            if huckster.properties['Draw Type'] == 'Draw': TokensX('Put1Shootout:Stud', '', huckster)
         notify("{} sets {}'s bullets to {} {}".format(me,huckster,targetBullets, fetchDrawType(target)))
      else:
         if targetBullets < hucksterBullets: plusBulletShootout(target, count = hucksterBullets - targetBullets, silent = True)
         elif targetBullets > hucksterBullets: minusBulletShootout(target, count = targetBullets - hucksterBullets, silent = True)
         if fetchDrawType(huckster) == 'Draw' and fetchDrawType(target) == 'Stud': 
            TokensX('Remove999Shootout:Stud', '', target)  
            if target.properties['Draw Type'] == 'Stud': TokensX('Put1Shootout:Draw', '', target)  
         elif fetchDrawType(huckster) == 'Stud' and fetchDrawType(target) == 'Draw': 
            TokensX('Remove999Shootout:Draw', '', target)  
            if target.properties['Draw Type'] == 'Draw': TokensX('Put1Shootout:Stud', '', target)  
         notify("{} sets {}'s bullets to {} {}".format(me,target,hucksterBullets, fetchDrawType(huckster)))
   elif card.name == 'Felix Amador':
      me.piles['Deck'].addViewer(me)
      whisper("The top card of your deck is {} ({} of {})".format(me.piles['Deck'].top(),fullrank(me.piles['Deck'].top().Rank),fullsuit(me.piles['Deck'].top().Suit)))
      me.piles['Deck'].removeViewer(me)
   ### Frontier Justice ###
   elif card.name == "Confession":
      if not len(targetCards): return 'ABORT' 
      targetDude = targetCards[0]
      dude = fetchHost(card)
      skillCheck = fetchSkills(dude)
      targetDude.markers[mdict['Bounty']] += skillCheck[0][1]
      notify('{} increased {} bounty by {} Blessed skill rating'.format(card.name, targetDude, dude))
   ### IOUF ###
   elif card.name == 'Marcia Ridge':
      notify(":> {} use {}".format(announceText,targetCards[0]))
      remoteCall(targetCards[0].controller,'MarciaRidgeStart',[card,targetCards[0]])
      #useAbility(targetCards[0])
   elif card.name == 'Eagle Wardens':
      bootingDude = targetCards[0]
      boot(bootingDude, silent = True)
      if compileCardStat(bootingDude, 'Influence') >= 2: cardDraw = 3
      else: cardDraw = 2
      drawMany(me.deck, cardDraw, silent = True)      
      if len(me.hand):
         choicehand = None
         while choicehand == None:
            choicehand = askCard([c for c in me.hand],'Choose which card to discard or ace from your hand',card.Name)
      destination = SingleChoice("Discard or Ace {}?".format(choicehand.Name), ['Discard','Ace'])
      if not destination: destination = 0
      if destination: 
         choicehand.moveTo(me.piles['Boot Hill'])
         verb = 'ace'
      else: 
         choicehand.moveTo(me.piles['Discard Pile'])
         verb = 'discard'
      notify("{} booted {} to draw {} cards and {} {} from their hand".format(me,bootingDude,cardDraw,verb,choicehand))
   elif card.name == 'Den of Thieves':
      drawHandCards = [c for c in table if c.highlight == DrawHandColor and c.controller == me]
      if len(drawHandCards) != 5:
         whisper(":::ERROR::: You can only use the den of thieves if you have a draw hand revealed on the table")
         return 'ABORT'
      else: cxp, cyp = drawHandCards[2].position
      if not len([c for c in table if c.model == 'cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1' and c.controller == me]):
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
      notify("{} make their hand illegal and increase its rank by 1".format(announceText))
   ### TLS ###
   elif card.name == 'Phantom Fingers' and re.search(r'(Gadget|Mystical)',targetCards[0].Keywords): DrawX('Draw1Card', announceText, card, notification = 'Quick')   
   ### SB7-9 ###
   elif card.name == "Morgan Stables":
      drawMany(me.deck, 1, silent = True)
      choicehand = None
      while choicehand == None:
         choicehand = askCard([c for c in me.hand],'Choose which card to discard from your hand',card.Name)
      choicehand.moveTo(me.piles['Discard Pile'])
      notify("{} boot {} to draw 1 card and discard {} from their hand".format(announceText,card,choicehand))
   elif card.name == "Xemo's Turban":
      if card.orientation == Rot90: return 'ABORT'
      if pull()[1] == 'Clubs':
         notify(":> {}'s {} has malfunctioned and provides no more insights into the future".format(fetchHost(card),card))
      elif payCost(1) == 'ABORT':
         notify(":> {} remembered he didn't have the money to pay for Xemo's Turban, so they just pulled a card for nothing.".format(me))
      else:      
         drawMany(me.deck, 1, silent = True)
         choicehand = None
         while choicehand == None:
            choicehand = askCard([c for c in me.hand],'Choose which card to discard from your hand',card.Name)
         choicehand.moveTo(me.piles['Discard Pile'])
         remoteCall(me,'boot',[card])
         notify("{} boot {} to draw 1 card and discard {} from their hand".format(announceText,card,choicehand))
   elif card.name == "Arnold Stewart":
      topCards = list(me.piles['Deck'].top(5))
      for c in topCards: c.moveTo(me.piles['Discard Pile'])
      notify(":> {} discards {}".format(card,[c.Name for c in topCards]))
      availDeeds = [c for c in topCards if re.search(r'Out of Town',c.Keywords)]
      if availDeeds and card.orientation == Rot0:
         choiceDeed = askCard(availDeeds,'These were the available Out of Town deeds that were at the top of your deck. You may boot Arnold to take one in your hand',card.Name)
         notify("{} boot {} to take {} to their hand".format(announceText,card,choiceDeed))
         if choiceDeed: 
            choiceDeed.moveTo(me.hand)
            boot(card,True)
      elif not availDeeds and card.orientation == Rot0:
         notify(":> {} didn't discover any good spots out of town.".format(card))
   elif card.name == "Fool's Gold":
      potCard = getPotCard(True)
      if potCard:
         if potCard.markers[mdict['Ghost Rock']]: 
            me.GhostRock += 1
            potCard.markers[mdict['Ghost Rock']] -= 1
      else: me.GhostRock += 1 # If the potcard is not there for some reason (bug) we just give the player 1 GR 
      notify("{} take one Ghost Rock from the pot".format(announceText))
   ### Ghost Town ###
   elif card.name == "Sight Beyond Sight":
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else:
         choice = SingleChoice("Choose which player to hex", [pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]         
      remoteCall(player,'SightBeyondSightStart',[card])
   elif card.name == "Technological Exhibition":
      jobResults = eval(getGlobalVariable('Job Active'))
      leader = Card(num(jobResults[3]))
      if leader.group != table:
         whisper("Your leader is gone and cannot invent anything anymore!")
         return
      handG = []
      discG = []
      for c in me.hand: 
         if re.search(r'Gadget',c.Keywords):
            handG.append(c)
      for c in me.piles['Discard Pile']: 
         if re.search(r'Gadget',c.Keywords):
            discG.append(c)
      if len(handG) and len(discG):
         choice = SingleChoice("Choose Gadget Seek Option",['Hand ({} Gadgets Available)'.format(len(handG)),'Discard Pile ({} Gadgets Available)'.format(len(discG))])
         if choice == None: return 'ABORT'
      elif len(handG): choice = 0
      elif len(discG): choice = 1
      else: 
         notify("{} didn't have any gadgets in their hand or discard pile to exhibit!".format(me))
         return
      if choice == 0:
         if len(handG) == 1: gadget = handG[0]
         else: gadget = askCard([c for c in handG],"Which of your Gadgets in your hand will you exhibit?",card.Name)
      else:
         if len(discG) == 1: gadget = discG[0]
         else: gadget = askCard([c for c in discG],"Which of your Gadgets in your discard pile will you exhibit?",card.Name)
      if not gadget: return 'ABORT'
      playcard(gadget,costReduction = 5, preHost = leader) # We make sure it's the leader who tries to make the gadget.
      mark = Card(eval(getGlobalVariable('Mark')))
      if mark.Name == 'Town Square': 
         gadget.markers[mdict['ControlPlus']] += 1
         notify("{}'s {} succeeds at a technological exhibition in the Town Square. They invented a {} which gained a permanent Control Point!".format(me,leader,gadget))
      else:
         notify("{}'s {} succeeds at a technological exhibition. They invented a {}.".format(me,leader,gadget))      
   elif card.model == '28b4125d-61a9-4714-870c-2f27e4872e9f': # Turtle's Guard     
      if len([c for c in table if c.model == 'cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1' and c.controller != me]): # If the opponent is cheatin' we want to create a harrowed spirit token.
         token = spawnNature()
         participateDude(token)
         token.markers[mdict['Harrowed']] += 1
         notify("{} marks all their dudes as harrowed for this round and spawns a harrowed nature spirit".format(me))
      else:
         notify("{} marks all their dudes as harrowed for this round".format(me))
   elif card.name == 'Dr. Dayl Burnett':  
      gadgets = findTarget('DemiAutoTargeted-atGadget-fromHand-choose1',card = card, choiceTitle = "Choose which gadget to invent.")
      if len(gadgets):
         gadget = gadgets[0]
#         playcard(gadget,preHost = card)
         if payCost(num(gadget.Cost), loud) == 'ABORT' : return # Check if the player can pay the cost. If not, abort.
         gadgetPull = pull(silent = True) # pull returns a tuple with the results of the pull
         notify("{} attempted to manufacture a {} and pulled a {} {}".format(card,gadget,fullrank(gadgetPull[0]), fullsuit(gadgetPull[1])))
         attachCard(gadget,card)
   elif card.name == 'Sun-Touched Raven':
      me.deck.setVisibility('me')
      topCards = list(me.deck.top(5))
      for iter in range(3):
         notify(":> {}'s {} is helping them choose a card to discard ({}/3)".format(me,card,iter))
         choiceCard = askCard(topCards,"Double click on any card to discard it, or close this window to finish ({}/3)".format(iter))
         if not choiceCard: break
         else:
            topCards.remove(choiceCard)
            choiceCard.moveTo(me.piles['Discard Pile'])
      me.deck.setVisibility('None')
      shamanHost = fetchHost(card)
      if shamanHost.orientation == Rot0 and confirm("Do you want to boot this shaman to draw a card?"):
         shamanHost.orientation = Rot90
         drawMany(me.deck,count = 1, silent = True)
         notify(":> {} booted {} to draw 1 card".format(me,shamanHost))
   elif card.name == 'Inner Struggle':
      remoteCall(card.controller,'randomDiscard',[card.controller.hand])
  
   #There comes a reconing
   elif card.name == "Intercession":        
        if re.search(r'-isFirstCustom',Autoscript):
            if getGlobalVariable('Shootout') == 'True':
                dudes = findTarget('DemiAutoTargeted-atDude-targetMine-isParticipating-choose1')
                TokensX('Put1Shootout:Stud', '', dudes[0]) 
            else:
                dudes = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
                TokensX('Put1Noon:Stud', '', dudes[0])
        else:
            mDude = findTarget("DemiAutoTargeted-atDude-targetMine-isParticipating-choose1")
            oDude = findTarget("DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1")
            TokensX('Put2BulletNoonPlus', '', mDude[0])
            boot(mDude[0], forced = 'unboot')
            remoteCall(oDude[0].controller, 'Intercession', oDude)
   elif card.name == "Raven's Ruin":
        dudes = findTarget('DemiAutoTargeted-atDude-targetMine-choose1', card = card, choiceTitle = "Choose which dude to move")
        ModifyStatus('MoveTarget-moveToHere', '', card, dudes)
        deed = fetchHost(card)
        if deed.owner != me and deed.orientation == Rot0 and compileCardStat(deed, 'Control') > 0:
            if confirm("Do you want to boot this deed to get 1 GR?"):
                me.GhostRock += 1
                notify("{} gains 1 GR".format(me))
                boot(deed, forced = 'boot')
   elif card.name == "Censure":
        out = findTarget('DemiAutoTargeted-atOutfit-choose1', card = card, choiceTitle = "Choose outfit of the player whose hand rank will be increased")
        notify("{} hand rank is increased by 2".format(out[0].controller))
        if getGlobalVariable('Shootout') == 'True':
            notify("{} casualties are reduced by 3".format( me))
            if confirm("Do you want to send one of opposing dudes home"):
                dudes = findTarget("DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1")
                remoteCall(dudes[0].controller, "Censure", [card, dudes])
   elif card.name == "Sentinel":
        host = fetchHost(card)
        TokensX('Put1High Noon:Stud', '',host)
        TokensX('Put1BulletNoonPlus', '',host)
        TokensX('Put1Sentinel', '', host)
        TokensX('Put1High Noon:Skill Bonus:1', '', host)
        notify("You might move {} to adjecent location or Town Square".format(host))
   elif card.name == "Ezekiah Grimme":
        if re.search(r'-isFirstCustom',Autoscript):
            spell = me.piles['Discard Pile'].top()
            if not (re.search(r'Hex',spell.Keywords) or re.search(r'Miracle',spell.Keywords) or re.search(r'Spirit',spell.Keywords)):
                notify(" You need a spell to use this ability")
                return
            playcard(spell)
            boot(spell, forced = 'boot')
        else:
            dude = findTarget("DemiAutoTargeted-atHuckster_or_Shaman_or_Blessed-targetMine-isUnbooted-choose1")
            if  not len(dude):
                notify("Your dude has to be unbooted to use this ability")
                return
            boot(dude[0], forced = 'boot')
            topCards = list(me.piles['Deck'].top(5))
            for c in topCards: c.moveTo(me.piles['Discard Pile'])
            notify(":> {} discards {}".format(card,[c.Name for c in topCards]))
            availSpells = [c for c in topCards if re.search(r'Spell',c.Type)]
            playSpells = []
            for c in table:
                if c.type == "Spell" and c.controller == me:
                    playSpells.append(c)
            for spell in availSpells:
                a = 0
                for playS in playSpells:
                    if spell.name == playS.name:
                        a += 1
                        if a > 1:
                            availSpells.remove(spell)
            if availSpells:
                choiceSpell = askCard(availSpells,'These were the available Spells that were at the top of your deck. Do you want to play one on your dude',card.Name)
                notify("{} decided to play {} on {} ".format(me,choiceSpell, dude[0]))
                playcard(choiceSpell, preHost=dude[0])
      
            else:
                notify(":> {} didn't discover any spells available to play.".format(card))
   #2t2d
   elif card.name == "Property Is Theft":
      if getGlobalVariable('Shootout') == 'True':
         drawMany(me.Deck, 1, silent =True)
         if confirm("do you want to discard card(s)?"):
            disloop = 2;
            while disloop:
               chosenCard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
               chosenCard.moveTo(me.piles['Discard Pile'])
               disloop -= 1        
      else:
         if confirm("do you want to discard card(s)?"):
               chosenCard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
               chosenCard.moveTo(me.piles['Discard Pile'])
   elif card.model == "ae22bba2-cf1e-4038-b7bb-1d3429c10004": #Ying-Ssi Chieh T'ang
      drawhandMany(me.Deck, 1, True)
      discardCards = findTarget('DemiAutoTargeted-isDrawHand-targetMine-choose1', choiceTitle = "Choose a card to discard from your hand")
      discardCards[0].moveTo(discardCards[0].owner.piles['Discard Pile'])
      for c in table:
         if c.highlight == DrawHandColor and c.controller == me: c.moveTo(me.piles['Draw Hand'])
      revealHand(me.piles['Draw Hand'], type = 'shootout') # We move the cards back ot the draw hand and reveal again, letting the game announce the new rank.
   elif card.name == 'Murdered in Tombstone':
      disCR = [c for c in me.piles['Discard Pile'] if ("Action" in c.Type and re.search(r'Cheatin',c.Text))]
      deckCR = [c for c in me.piles['Deck'] if ("Action" in c.Type and re.search(r'Cheatin',c.Text))]
      string = len(disCR)
      cards = disCR + deckCR
      if len(cards) == 0:
         notify("You have no cards you can fetch with this ability")
         return
      card = askCard(cards, "Choose a CR to fetch if you do you will have to discard a card from your hand.First {} are in your discard".format(string))
      card.moveTo(me.hand)
      if card:
         choicehand = askCard([c for c in me.hand],'Choose which card to discard from your hand',card.Name)
         choicehand.moveTo(me.piles['Discard Pile'])

      notify("{} fetched {} using Murdered in Tombstone ability and discarded".format(me, card.name, choicehand)) 
      opponents = [pl for pl in getActivePlayers() if (pl != me or len(getActivePlayers()) == 1)]
      for opponent in opponents:
         remoteCall(opponent,'Murdered',card)
      return
   elif card.name == "Burn 'Em Out":
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else:
         choice = SingleChoice("Choose player ", [pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]         
      remoteCall(player,'BurnOut',card)
   elif card.name == 'Heist':
      mark = Card(eval(getGlobalVariable('Mark')))
      production = compileCardStat(mark, stat = 'Production')
      me.GhostRock += production
      if mark.controller != me:
         jobResults = eval(getGlobalVariable('Job Active'))
         leader = Card(num(jobResults[3]))
         if leader:
            dude.markers[mdict['Bounty']] += 1
            boot(leader , forced = 'unboot')
         notify("{} gained {} GR because of successful {}, {} unboots as heist happened at opponents location.".format(me, production, card.name, leader.name))
      notify("{} gained {} GR because of successful {}.".format(me, production, card.name))
   elif card.name == 'Ricochet':
      for card in table:
         if card.controller == me:
            if card.model == 'cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1': # The cheatin' icon
               return
      drawMany(me.deck, 1, silent = True)
      notify('{} does not take damage this turn and drew a card.'.format(me))
   elif card.name == 'Kevin Wainwright (Exp.1)':
      if confirm('Is there opponents dude with grit 11 or higher at your location?'):
         drawMany(me.deck, 2, silent = True)
         notify('{} drew to card after {} moved to location with high grit dude.'.format(me, card.name))
   elif card.name == 'Guiding Wind':
      dudes = findTarget('DemiAutoTargeted-atDude-isParticipating-choose1')
      dude = dudes[0]
      influence = compilecardstat(card, stat = 'Influence')
      if influence > 3:
         modifier = 3
      else: modifier = influence
      bullets = compilecardstat(card, stat = 'Bullets')
      if bullets < modifier:
         while bullets != modifier:
            TokensX('Put1BulletShootoutPlus', '', dude)
            bullets = compilecardstat(card, stat = 'Bullets')
      else:
         while bullets != modifier:
            TokensX('Put1BulletShootoutMinus', '', dude)
            bullets = compilecardstat(card, stat = 'Bullets')
   elif card.name =='High Stakes Haven':
      randomC = me.hand.random()
      if me.GhostRock <= 0:
         if randomC == None:
            notify('{} is broke and without cards to pay for {}.'.format(me, card))
         else: 
            randomC.moveTo(me.piles['Discard Pile'])
            notify('{} is broke, thus discarding random card for {}.'.format(me, card))
      elif randomC == None:
         me.GhostRock -= 1
         notify('{} is without cards, thus paying 1 Ghost Rock for {}.'.format(me, card))
      elif confirm('High Stakes Haven trait: Do you want to pay 1 Ghost Rock?\nIf No is selected, random card will be discarded instead.'):
         me.GhostRock -= 1
         notify('{} chose to pay 1 Ghost Rock for {}.'.format(me, card))
      else: 
         randomC.moveTo(me.piles['Discard Pile'])
         notify('{} chose to discard random card for {}.'.format(me, card))



#ausc

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
         whisper(":::ERROR::: No valid player found to bottom deal. Aborting!")
         return 'ABORT'
      else: 
         choice = SingleChoice("Please choose which of your opponents you're bottom dealin'.", [pl.name for pl in drawHandPlayers])
         if choice == None: return 'ABORT'
         targetPL = drawHandPlayers[choice]
      passPileControl(deck,targetPL)   
      passPileControl(discardPile,targetPL)   
      remoteCall(targetPL,'BottomDealing',[me,card])
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
   elif card.model == "8e50a03b-b42c-4207-9d0d-7a144ad31e3b" and action == 'USE': # Elander Boldman nonxp
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
      targetDude = findTarget('DemiAutoTargeted-atDude-isUnbooted-choose1-targetMine')
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
      #boot(targetDude[0],silent = True) # It doesn't actually boot the dude. Huh.
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
   elif card.name =="Cheatin' Varmint" and action == 'PLAY':
      if me.GhostRock - 5 < 0:
          if not confirm("You do not have enough Ghost Rock to use this ability. Proceed?"):
              notify("{} didn't have enough Ghost Rock, {} Should return Cheatin' Varmint to their hand".format(me,me))
              return 0
      me.GhostRock -= 5
      notify("{} pays 5 Ghost Rock to reduce a player's draw rank by 2 hand ranks".format(me))
### SB 1-3 ###
   if card.name == "Make 'em Sweat" and action == 'PLAY': 
      myDude = findTarget('DemiAutoTargeted-atDude-targetMine-isUnbooted-isParticipating-choose1', choiceTitle = "Choose which of your dudes to boot for {}".format(card.name))
      opDude = findTarget('DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1', choiceTitle = "Choose which dude to affect with {}".format(card.name))
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
### F&F ###       
   elif card.name == "This'll Hurt in the Mornin" and action == 'PLAY':
      targetCards = findTarget('DemiAutoTargeted-isDrawHand-targetOpponents-choose2',card = card, choiceTitle = "Choose which of your opponent's cards to discard")
      if not len(targetCards): return 'ABORT'
      if confirm("If your own draw hand illegal?"): remoteCall(targetCards[0].controller,'TWHITM',[targetCards,True])
      else: remoteCall(targetCards[0].controller,'TWHITM',[targetCards,False])
   elif card.name == "California Tax Office" and action == 'USE':
      targetCards = findTarget('Targeted-atDude',card = card, choiceTitle = "Choose which of your opponent's dudes has to pay their taxes")
      if not len(targetCards): return 'ABORT'
      else: remoteCall(targetCards[0].controller,'TaxOffice',[targetCards[0]])
   elif card.name == "The Fixer" and action == 'USE':
      for c in me.Deck.top(5): c.moveTo(me.piles['Discard Pile'])
      update()
      discardCards = [c for c in me.piles['Discard Pile']]
      choice = SingleChoice('Choose one of your discarded cards to take to your hand', makeChoiceListfromCardList(discardCards))
      notify("{} uses {} to take {} into their hand".format(me,card,discardCards[choice]))
      rnd(1,10)
      discardCards[choice].moveTo(me.hand)
      update()
      if re.search(r'Noon Job',discardCards[choice].Text) and discardCards[choice].Type == 'Action': remoteCall(me,'boot',[card]) # Doing remote call, so as to have a chance to finish the animation
### SB 4-6 ###
   elif card.name == "Howard Aswell" and action == 'USE':
      handCards = [c for c in me.hand]
      revealCards(handCards)
      while not confirm("You are now revealing your hand to all players. Press Yes to continue, Press No to ping the other players to see if they had enough time to see the cards"):
         notify("{} wants to know if it's OK to hide their hand once more".format(me))
      for c in handCards: c.moveTo(me.hand)
      notify("{} hides their play hand once more".format(me))   
      for c in me.Deck.top(10): c.moveTo(me.piles['Discard Pile'])
      update()
      discardCards = [c for c in me.piles['Discard Pile'] if re.search(r'(Ranch|Improvement)',c.Keywords)]
      if not len(discardCards):
         notify("{} tried to design some Ranches or Improvements but was unsuccesful.".format(card))
      else:
         choice = askCard(discardCards,"Choose card to retrieve")
         if choice == None:
            notify("{} chooses not to take a Ranch of Improvement into their hand".format(me))
         else:
            choicehand = askCard([c for c in me.hand],"Choose card to discard from hand.")
            choicehand.moveTo(me.piles['Discard Pile'])
            notify("{} uses {} and discards {} to take {} into their hand".format(me,card,choicehand,choice))
            choice.moveTo(me.hand)
            update()
   elif card.name == "Funtime Freddy" and action == 'USE':
      notify(":> {} is choosing the two hexes to retrieve with {}".format(me,card))
      whisper(":::CHOICE::: Choose first hex to retrieve")
      spell1 = askCard([c for c in deck if c.Type == 'Spell' and re.search(r'Hex',c.Keywords)],"Choose first spell to retrieve")
      if not spell1: 
         deck.shuffle()
         return 'ABORT'
      spell1.moveToTable(cwidth(),0)
      spell1.highlight = DrawHandColor
      spell2 = askCard([c for c in deck if c.Type == 'Spell' and re.search(r'Hex',c.Keywords)],"Choose second spell to retrieve")
      whisper(":::CHOICE::: Choose second hex to retrieve")
      while not spell2 or spell2.model == spell1.model:
         if confirm(":::ERROR::: You need to choose two different Hexes. Abort?"): 
            deck.shuffle()
            return 'ABORT'
         else: spell2 = askCard([c for c in deck if c.Type == 'Spell' and re.search(r'Hex',c.Keywords)],"Choose second spell to retrieve")      
      spell2.moveToTable(-1 * cwidth(),0)
      spell2.highlight = DrawHandColor
      opponents = [pl for pl in getPlayers() if pl != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else: 
         choice = SingleChoice("Choose the player who is going to select which spell you get to keep",[pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]
      remoteCall(player,'FuntimeFreddyChoose',[card,spell1,spell2])
      deck.shuffle()
   elif card.model == "294a7ce9-af00-46e1-b33c-aab21ebf3b09" and action == 'USE': # Elander Boldman Xp
      if getGlobalVariable('Shootout') != 'True': 
         whisper(":::ERROR::: {} can only use his shootout ability during shootouts".format(card))
         return 'ABORT'
      foundGadget = False
      hostCards = eval(getGlobalVariable('Host Cards'))
      for c in table:
         if c.targetedBy and c.targetedBy == me and c.Type == 'Goods' and (Card(hostCards[c._id]).highlight == AttackColor or Card(hostCards[c._id]).highlight == DefendColor): # If we've targeted a gadget with a participating dude...
            foundGadget = c   
            break
      if not foundGadget: 
         whisper(":::ERROR::: No Gadget on a participating dude targeted. Aborting!")
         return 'ABORT'
      else:
         foundGadget.orientation = Rot0         
         if re.search(r'Experimental',foundGadget.Keywords): 
            elUnboot = ", then finally unboots {}".format(card)
            update()
            rnd(1,10)
            remoteCall(me,'boot',[card,0,0,True]) # Doing remote call, so as to have a chance to finish the animation
         else: elUnboot = "".format(card)
         if re.search(r'Weapon',foundGadget.Keywords):          
            weaponBonus = ", make it provide +1 bullet and make {} a stud".format(Card(hostCards[foundGadget._id]))
            foundGadget.markers[mdict['BulletShootoutPlus']] += 1
            TokensX('Remove999Shootout:Draw', '', Card(hostCards[foundGadget._id]))
            TokensX('Put1Shootout:Stud', '', Card(hostCards[foundGadget._id]))
         else: weaponBonus = ""
         notify("{} uses {} to unboot {}{}{}".format(me,card,foundGadget,weaponBonus,elUnboot))
   elif card.name == "Cookin' Up Trouble" and action == 'PLAY':
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else:
         choice = SingleChoice("Choose which player to sabotage", [pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]         
      remoteCall(player,'CookinTroubleStart',[card])
   elif card.name == "Nathan Shane" and action == 'USE':
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else:
         choice = SingleChoice("Choose which player to snipe", [pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]         
      remoteCall(player,'NathanShaneStart',[card])
   ### IOUF ###
   elif card.name == "Butch Deuces" and action == 'USE':
      topC = list(deck.top(5))
      chosenC = askCard(topC,'Choose one Spirit or Attire to reveal or close this window to leave these cards where they are',card.Name)
      if not chosenC: notify("{} boots {} to look at the top 5 cards of their deck but opts to keep their current hand".format(me,card))
      else:
         for c in me.hand: c.moveToBottom(deck)
         for c in deck.top(5): c.moveTo(me.hand)
         notify("{} boots {} to reveal {} from the top 5 cards of their deck,  take those cards to their hand and shuffle their previous hand to their deck".format(me,card,chosenC.Name))
         deck.shuffle()         
   elif card.name == "Laughing Crow" and action == 'USE':
      topC = list(deck.top(2))
      spirits = []
      for c in topC: 
         c.moveTo(discardPile)
         if re.search(r'Spirit',c.Keywords): spirits.append(c)
      playedSpirit = 'select'
      while len(spirits) and playedSpirit != None:
         playedSpirit = askCard(spirits,'Select a spirit to play (paying all costs)',card.Name)
         if playedSpirit:
            playcard(playedSpirit)
            spirits.remove(playedSpirit)
            topC.remove(playedSpirit)
      if len(topC): notify("{} discarded {} from the top of their deck".format(card,[c.Name for c in topC]))
   elif card.name == "Benjamin Washington" and action == 'USE':
      handCards = list(me.hand)
      discardedC = askCard(handCards,'Select one card to discard or close this window to finish',card.Name)
      if not discardedC: return
      while discardedC != None and len(me.hand):
         discardedC.moveTo(discardPile)
         notify(":> {} uses {} to discard {}".format(me,card,discardedC))
         handCards.remove(discardedC)
         discardedC = askCard(handCards,'Select another card to discard or close this window to finish',card.Name)
      discardedNR = 5 - len(handCards)
      for iter in range(discardedNR):
         upkeepDudes = [c for c in table if compileCardStat(c, 'Upkeep') >= 1 and c.controller == me]
         upkeepFixed = askCard(upkeepDudes,'Select one of your dudes to reduce their upkeep by 2 ({}/{})'.format(iter + 1,discardedNR),card.Name)
         if not upkeepFixed: break
         if compileCardStat(upkeepFixed, 'Upkeep') >= 2: 
            upkeepFixed.markers[mdict['ProdPlus']] += 2
            TokensX('Put2UpkeepPrePaid', '', upkeepFixed)
         else: 
            upkeepFixed.markers[mdict['ProdPlus']] += 1 # We cannot exceed their production, as they would get prod instead then.
            TokensX('Put1UpkeepPrePaid', '', upkeepFixed)
         notify(":> {} reduces the upkeep of {} to {} until High Noon".format(card,upkeepFixed,compileCardStat(upkeepFixed, 'Upkeep')))
      draw()
   elif card.name == "Smiling Frog" and action == 'USE':
      discardC = findTarget('DemiAutoTargeted-choose1-fromHand')
      if not len(discardC): return 'ABORT'
      else:
         if re.search(r'Spirit',discardC[0].Keywords): 
            TokensX('Put2BulletNoonPlus', '', card)
            notify("{} discards {} to empower himself with 2 extra bullets".format(card,discardC[0]))
         else: 
            TokensX('Put1BulletNoonPlus', '', card)
            notify("{} discards {} and gains 1 extra bullet".format(card,discardC[0]))
         discardTarget(targetCards = discardC, silent = True)         
   ### TLS ###
   elif card.name == "The Extra Bet" and action == 'USE':
      if getGlobalVariable('Phase') != '1':
         #if not confirm(":::WARNING::: It is not yet the Gamblin' phase. Do you want to jump to lowball now?"): return
         goToGamblin()
      drawhandMany(me.Deck, 5, True)
      betLowball()
      if me.GhostRock < 1 and confirm("You do not seem to have enough ghost rock in your stash to use {}. Proceed to reveal your lowball hand as normal instead?".format(card.Name)):
         revealLowballHand()
         notify("{} did not have enough ghost rock in their stash to use {}".format(me,card))
      else: 
         betLowball()
         me.piles['Draw Hand'].lookAt(-1)
         notify("{} uses {} to ante an extra ghost rock and is looking at their draw hand for a card to redraw".format(me,card))
   ### SB7-9 ###
   elif card.name == "Rico Rodegain" and action == 'USE':
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else:
         choice = SingleChoice("Choose which player to investigate", [pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]         
      remoteCall(player,'RicoStart',[card])
   elif card.name == "Jael's Guile" and action == 'USE':
      for c in table:
         if c.model == "cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1" and c.controller == me:
            dude = fetchHost(card)
            if dude.orientation == Rot90 and not confirm("You need to boot your dude to use {} when your hand is illegal. Bypass?".format(card.Name)): return 'ABORT'
            boot(dude)
            break
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else:
         choice = SingleChoice("Which player are you shooting it out with?", [pl.name for pl in opponents])
         if choice == None: return 'ABORT'
         else: player = opponents[choice]         
      remoteCall(player,'JaelGuile',[card])
   elif card.name == "Rick Henderson" and action == 'USE':
      targetCards = findTarget('Targeted-atDude',card = card, choiceTitle = "Choose the dude you're robbing")
      if not len(targetCards): return 'ABORT'
      else: remoteCall(targetCards[0].controller,'RickHenderson',[targetCards[0],card])
   ### Ghost Town ###
   elif card.name == "Silent Sigil":
       if getGlobalVariable('Phase') == '4':
           drawMany(me.deck,count = 1, silent = True)
           notify("{} used {} ability.".format(me, card.name))
       else:
           notify("{} can be used only during Sundown.".format(card.name)) 
           
      
       
   elif card.name == "Ol' Howard" and action == 'USE':
      retrieveTuple = RetrieveX('Retrieve1Card-grabDeed-toTable-payCost', '', card)
      if retrieveTuple == 'ABORT':return 'ABORT'
      elif len(retrieveTuple[1]):
         deed = retrieveTuple[1][0]
         deed.markers[mdict['ProdMinus']] += num(deed.Production)
         deed.markers[mdict['PermControlMinus']] += num(deed.Control)
         attachCard(card,deed)
         notify("{} startings haunting {}".format(card,deed))
   elif card.name == "Notary Public" and action == 'USE':
      deeds = findTarget('Targeted-atDeed_and_Government_or_Deed_and_Public-isUnbooted')
      if not len(deeds): return 'ABORT'
      else:
         pub = False
         gov = False
         deed = deeds[0]
         boot(deed,silent = True)
         if re.search(r'Government',getKeywords(deed)): 
            dudesGov = findTarget('DemiAutoTargeted-atDude-choose1-choiceTitle{Choose which dude should receive a bounty}')
            if len(dudesGov):
               dudesGov[0].markers[mdict['Bounty']] += 1
               gov = True           
         if re.search(r'Public',getKeywords(deed)):
            dudesPub = findTarget('DemiAutoTargeted-atDude-targetMine-choose1-choiceTitle{Choose which dude should be moved}')
            if len(dudesPub):
               ModifyStatus('MoveTarget-moveToDeed_or_Town Square_or_Outfit', '', card, dudesPub)
               pub = True
      if gov and pub: notify("{} boots {} to increase the bounty of {} and move {} to another location".format(me,card,dudesGov[0], dudesPub[0]))
      elif gov: notify("{} boots {} to increase the bounty of {}".format(me,card,dudesGov[0]))
      elif pub: notify("{} boots {} move {} to another location".format(me,card,dudesPub[0]))
   elif card.name == "Framed" and action == 'PLAY':
      dudes = findTarget('DemiAutoTargeted-atDude-targetOpponents-choose1')
      if len(dudes):
         dude = dudes[0]
         if dude.markers[mdict['Bounty']]:
            dude.markers[mdict['Bounty']] += 3
            notify("{} easily frames the already wanted {}, increasing their bounty by 3.".format(me,dude))
         else:
            if payCost(compileCardStat(dude,'Influence'), MSG = "You do not have enough ghost rock to frame {}! Bypass?".format(dude)) == 'ABORT': return 'ABORT'
            remoteCall(dude.controller,'Framed',[card,dude])
   elif card.name == "Plague of Grasshoppers" and action == 'PLAY':
      dudes = findTarget('Targeted-atDude_and_Kung Fu-isUnbooted')
      location = findTarget('DemiAutoTargeted-atDeed_or_Town Square_or_Outfit-choose1')
      successDudes = []
      for dude in dudes:
         rank,suit = pull(silent = True)
         dudeKF = compileCardStat(dude,'Value')
         if num(rank) < dudeKF: 
            notify(":> {} pulled {} for {}, succeeding their Kung Fu pull by {}".format(me,rank,dude,dudeKF - num(rank) - 1))
            successDudes.append(dude)
         else:
            notify(":> {} failed their Kung Fu pull by {} by pulling a {}".format(dude,num(rank) - dudeKF + 1,rank))
      iter = 0
      for dude in successDudes:
         iter += 1
         x,y = location[0].position
         dude.moveToTable(x + cardDistance() * iter, y)
         orgAttachments(dude)
      if len(successDudes):
         notify("{} moves {} dudes to {} ({})".format(me,len(successDudes),location[0],[c.Name for c in successDudes]))
      else: 
         notify ("{} tried to move {} dudes to {} but failed miserably to move even a single one".format(me,len(dudes),location[0]))
   elif card.name == "Walters Creek Distillery" and action == 'USE':
      deeds = findTarget('Targeted-atDeed_and_Saloon_or_Deed_and_Casino-isUnbooted')
      if not len(deeds): return 'ABORT'
      else:
         saloon = False
         casino = False
         deed = deeds[0]
         boot(deed,silent = True)
         if re.search(r'Saloon',getKeywords(deed)): 
               handC = findTarget('DemiAutoTargeted-fromHand-choose1')
               if len(handC): 
                  discardTarget(targetCards = handC, silent = True)   
                  drawMany(deck, 1, silent = True)
                  saloon = True           
         if re.search(r'Casino',getKeywords(deed)):
            me.GhostRock += 2
            casino = True
      if saloon and casino: notify("{} boots {} to gain 2 ghost rock and discard a card to draw a card".format(me,card))
      elif saloon: notify("{} boots {} to discard a card to draw a card".format(me,card))
      elif casino: notify("{} boots {} to gain 2 ghost rock".format(me,card))
   elif card.name == "A Piece Of The Action" and action == 'PLAY':
      handDudes = findTarget('DemiAutoTargeted-atDude-fromHand-choose1')
      if not len(handDudes): return 'ABORT'
      dude = handDudes[0]
      cost = num(dude.Cost)
      if cost >= 4: 
         reducedCost = cost - 4
         if reducedCost < 4: reducedCost = 4
         reduction = cost - reducedCost
      else: 
         reducedCost = cost
         reduction = 0
      if chkGadgetCraft(dude):
         if payCost(reducedCost) == 'ABORT' : return 'ABORT' 
         placeCard(dude,'HireDude')
         notify(":> {} is giving {} a piece of the action".format(me,dude))
      availGoods = [c for c in discardPile if c.Type == 'Goods' and not re.search(r'Gadget',c.Keywords)]
      if len(availGoods):
         goods = askCard(availGoods,'You can equip a goods from your discard pile to {} with a {} Ghost Rock reduction to its cost. \nChoose one or close this window to equip nothing'.format(dude.Name,reduction),card.Name)
         if goods: playcard(goods,costReduction = reduction, preHost = dude)
   elif card.name == "Foreboding Glance" and action == 'PLAY':
      myDudes = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
      opDudes = findTarget('DemiAutoTargeted-atDude-targetOpponents-choose1')
      if not len(myDudes) or not len(opDudes):
         whisper("You need to target one of your dudes and one opposing dude to use this action")
         return 'ABORT'
      myDude = myDudes[0]
      opDude = opDudes[0]
      if compileCardStat(myDude, 'Control') > compileCardStat(opDude, 'Control'):
         hostCards = eval(getGlobalVariable('Host Cards'))
         attachmentsList = [Card(cID) for cID in hostCards if hostCards[cID] == opDude._id]
         for attachment in attachmentsList: boot(attachment, silent = 'True')
         notify(":> {}'s attachements are booted".format(opDude))
      if compileCardStat(myDude, 'Influence') > compileCardStat(opDude, 'Influence'):
         boot(opDude, silent = 'True')
         notify(":> {} is booted".format(opDude))
      if myDude.markers[mdict['Bounty']] > opDude.markers[mdict['Bounty']]:
         callout(myDude, silent = 'True', targetDudes = opDudes)
         notify(":> {} is calling out {}".format(myDude,opDude))
   elif card.name == "Ambrose Douglas" and action == 'USE':
      discardC = findTarget('DemiAutoTargeted-choose1-fromHand')
      if not len(discardC): return 'ABORT'
      else:
         TokensX('Put1InfluencePlus', '', card)
         if discardC[0].type == 'Spell' or (discardC[0].type == 'Goods' and re.search(r'Mystical',discardC[0].Keywords)): 
            OutfitCard.orientation = Rot0
            OutfitCard.markers[mdict['UsedAbility']] = 0
            notify("{} discards {} to gain 1 influence and are able to re-use their outfit card ability".format(card,discardC[0]))
         else: 
            notify("{} discards {} to gain 1 influence ".format(card,discardC[0]))
         discardTarget(targetCards = discardC, silent = True)         
   elif card.name == "Fool Me Once..." and action == 'USE':
      for player in getActivePlayers():
         if player != me: remoteCall(player,'drawMany',[player.Deck, 1, None, True])
      notify("{} revealed an illegal draw hand and everyone else gets to draw a card".format(me))
   elif card.name == "Theo Whateley-Boyer" and action == 'USE':
      if getGlobalVariable('Phase') == '1':
         if payCost(1, silent) == 'ABORT': return 'ABORT'
         jokers = findTarget('DemiAutoTargeted-atJoker-isDrawHand-choose1-targetMine')
         if not len(jokers):
            whisper(":::ERROR::: You need to have revealed a joker to use this ability")
            return 'ABORT'
         attachCard(jokers[0],card)
         jokers[0].highlight = None
         notify("{} paid 1 Ghost Rock to attach {} to {}".format(me,jokers[0],card))
      elif getGlobalVariable('Shootout') == 'True':
         if not card.markers[mdict['UsedAbility']] or (card.markers[mdict['UsedAbility']] and confirm("You've already used {}'s Ability Bypass Restriction?".format(card.name))): 
            if not card.markers[mdict['UsedAbility']]: card.markers[mdict['UsedAbility']] += 1 
            else: notify(":::WARN::: {} bypassed once-per turn restriction on {}'s ability".format(me,card))
            jokers = []
            hostCards = eval(getGlobalVariable('Host Cards'))
            attachmentsList = [Card(cID) for cID in hostCards if hostCards[cID] == card._id]
            for attachment in attachmentsList:
               if attachment.Type == 'Joker': jokers.append(attachment)
            if not len(jokers):
               whisper(":::ERROR::: You need to have an attached joker to use this ability")
               return 'ABORT'
            elif len(jokers) == 1: joker = jokers[0]
            else:
               joker = jokers[SingleChoice('Choose one of your attached jokers to put in your draw hand',[c.Name for c in jokers])]
            hex = findTarget('DemiAutoTargeted-atHex-onAttachment-isUnbooted-choose1', card = card, choiceTitle = "Choose which hex to boot to use this ability")
            if not len(hex): return 'ABORT'
            boot(hex[0], silent = True)
            discardCards = findTarget('DemiAutoTargeted-isDrawHand-targetMine-choose1')
            if not len(discardCards): return 'ABORT'
            discardCards[0].moveTo(discardCards[0].owner.piles['Discard Pile'])
            for c in table:
               if c.highlight == DrawHandColor and c.controller == me: c.moveTo(me.piles['Draw Hand'])
            joker.moveTo(me.piles['Draw Hand'])
            clearAttachLinks(joker)
            notify("{} boots their {} to replace {} with {}".format(card,hex[0],discardCards[0],joker))
            revealHand(me.piles['Draw Hand'], type = 'shootout') # We move the cards back ot the draw hand and reveal again, letting the game announce the new rank.
      else:
         whisper(":::ERROR::: You can only use Theo's ability during lowball or shootouts")
   elif card.name == "Antoine Peterson" and action == 'PLAY':
      discardedJobs = [c for c in me.piles['Discard Pile'] if re.search(r'Noon Job',c.Text) and c.Type == 'Action']
      choice = SingleChoice('Choose one of your jobs to take to your hand', makeChoiceListfromCardList(discardedJobs))
      if not choice: return
      discardedJobs[choice].moveTo(me.hand)
      handDiscard = None
      while not handDiscard:
         handDiscard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
      handDiscard.moveTo(me.piles['Discard Pile'])
      notify("{} uses {} to take {} into their hand and discard {}".format(me,card,discardedJobs[choice],handDiscard))      
      Sloanies = findTarget("Targeted-atDude_and_The Sloane Gang-targetMine-isBooted-noTargetingError")
      if len(Sloanies):
         boot(Sloanies[0], forced = 'unboot')
         Sloanies[0].markers[mdict['Bounty']] += 2
         notify("{} unboots {} and gives them 2 bounty".format(me,Sloanies[0]))
   elif card.name == "Denise Brancini" and action == 'DISCARD':
      if getGlobalVariable('Phase') == '2':
         notify(":> {} couldn't pay the upkeep of {} and so all other players refill their aced jokers".format(me,card))
         for player in getActivePlayers(): remoteCall(player,'DeniseBrancini',[card])
   elif card.name == "Serendipitous Arrival" and action == 'PLAY':
      handDudes = findTarget('DemiAutoTargeted-atDude-fromHand-choose1')
      if not len(handDudes): return 'ABORT'
      dude = handDudes[0]
      cost = num(dude.Cost)
      if cost - 5 > 0: 
         cost -= 5
         extraTXT = " was paid {} ghost rock and".format(cost)
      else: 
         cost = 0
         extraTXT = ''
      if payCost(cost) == 'ABORT' : return 'ABORT'
      
      placeCard(dude,'HireDude')
      notify(":> {}{} has serendipitously arrived in battle!".format(dude,extraTXT))
      participateDude(dude)
      TokensX('Put1Serendipitous', '', dude)
   ### There comes a reconing ###   
   elif card.name == "Agent Provocateur" and action == 'USE':
      if getGlobalVariable('Phase') != '4':
          notify(":> {} ability can be used only during Sundown".format(card.name))
          return
      handDudes = findTarget('DemiAutoTargeted-atDude-fromHand-choose1')
      if not len(handDudes): return 'ABORT'
      dude = handDudes[0]
      cost = num(dude.Cost)
      if cost > 4: 
         reducedCost = cost - 4
      else: 
         reducedCost = 0     
      if payCost(reducedCost) == 'ABORT' : return 'ABORT' 
      placeCard(dude,'HireDude')
      notify(":> {} is bringing {} into play".format(card.name,dude))
      ace(card)
   elif card.name == "Stewart Davidson" and action == 'USE':
      handDiscard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
      if not handDiscard: return
      handDiscard.moveTo(me.piles['Discard Pile'])
      dudes = findTarget('DemiAutoTargeted-atDude-targetOpponents-choose1')
      if len(dudes):
        dude = dudes[0]
      if payCost(compileCardStat(dude,'Influence'), MSG = "You do not have enough ghost rock to frame {}! Bypass?".format(dude)) == 'ABORT': return 'ABORT'
      notify(":> {} succesfully framed {} for 1 bounty".format(card.controller,dude))
      dude.markers[mdict['Bounty']] += 1
   elif card.name == "The Winning Agenda":       
        dudes = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
        toDiscard = compileCardStat(dudes[0],'Influence')      
        if toDiscard > 3: toDiscard = 3
        if toDiscard > len([c for c in me.hand]):
            notify("You don't have enough cards in your hand to use this ability")
            return
        disloop = toDiscard
        while disloop:
            chosenCard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
            chosenCard.moveTo(me.piles['Discard Pile'])
            disloop -= 1        
        drawMany(me.Deck, toDiscard, silent =True)
        notify(":> {} used {} to discard and draw {} cards".format(me,card.name, toDiscard))
   elif card.name == "Rosenbaum's Golem" and action == 'USE':
        if card.orientation == Rot90:
            notify(":> {} has to be unbooted to use his ability".format(card))
            return 
        else:
            boot(card, forced = 'boot')
            
        dudes = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-isUnbooted-choose1')
        boot(dudes[0], forced = 'boot')
        
        inf = compileCardStat(dudes[0],'Influence')
        val = compileCardStat(dudes[0], 'Value')
        bul = compileCardStat(dudes[0], 'Bullets')
        grit = inf + val + bul
        choice = confirm("Do you want give that dude 5 shootout value? {} has currently {} grit.".format(dudes[0].name, grit))
        if choice:
           dudes[0].markers[mdict['ValueShootoutPlus']] += 5
           grit +=5
        if grit >= 11:
           dudes = findTarget("AutoTargeted-atDude-isParticipating-isBooted-targetMine")
           
           
           dudes.remove(card)
           if not len(dudes): return
           if len(dudes) == 1:
                chosenCard = dudes[0]
           else:
                chosenCard = askCard(dudes,"Choose which dude to unboot")
           boot(chosenCard, forced = 'unboot')
   elif card.name == 'Zeb Whateley-Dupont':
        if OutfitCard.Outfit == 'The Fourth Ring':
            TokensX('Put1High Noon:Stud', '', card)
   elif card.name == "Rabid Rance Hitchcock":
        if card.markers[mdict['Bounty']] == 0:
            notify(":> {} has to be WANTED DUDE to use his ability".format(card.name))
            return 
        deed = findTarget("Targeted-atDeed-choose1")
        notify("{} uses {}'s ability".format(me,card))
        if not len(deed):
            TokensX('Remove999Noon:ControlBullets', '', card)
            return
        if deed[0].controller != me:
            notify(":> You have to control {} to use this ability".format(deed[0].name))   
            return
        TokensX('Remove999Noon:ControlBullets', '', card)
        prodBullets = int(compileCardStat(deed[0], stat = 'Production'))
        if prodBullets > 3: prodBullets = 3       
        TokensX('Put{}Noon:ControlBullets'.format(prodBullets), '', card)
   elif card.name == "Sheriff Eli Waters":
        wanted = findTarget("AutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-isParticipating")
        maxBounty = 0
        for dude in wanted:
            bounty = dude.markers[mdict['Bounty']]
            if bounty > maxBounty: maxBounty = bounty
        if maxBounty > 4: maxBounty = 4
        TokensX('Remove999Shootout:BountyBullets'.format(maxBounty), '', card)
        TokensX('Put{}Shootout:BountyBullets'.format(maxBounty), '', card)
   elif card.name == "Epitaph Branch Office":
        dudes = findTarget("DemiAutoTargeted-atDude-targetMine-choose1")
        if compileCardStat(dudes[0],'Influence') < 1:
            notify(":> {} has no influence!".format(dudes[0]))
            return
        if dudes[0].markers[mdict['PermControlPlus']] != 0:
            notify(":> {} has already a control point!".format(dudes[0]))
            return
        dudes[0].markers[mdict['PermControlPlus']] += 1
        notify(":> {} gains one control point!".format(dudes[0]))
   elif card.name == "Buffalo Emporium":
        dudes = findTarget("DemiAutoTargeted-atDude-targetMine-choose1")
        TokensX('Put1High Noon:Cannot be Moved or Booted', '', dudes[0])
        if re.search(r'Abomination',dudes[0].Keywords):
           boot(dudes[0], forced = 'unboot')
           TokensX('Put1High Noon:1 Stud posse bonus', '', dudes[0])
   elif card.name == "Explorer's Lodge":
        dudes = findTarget("DemiAutoTargeted-atDude-choose1")
        ModifyStatus('MoveTarget-moveToTown Squa', '', card, dudes)
        boot(dudes[0], forced = 'boot')
        if dudes[0].controller == me and me.GhostRock > 1:
            choice = confirm("Do you want to pay 2GR to unboot {}?.".format(dudes[0].name))
            if choice:
                boot(dudes[0], forced = 'unboot')
                me.GhostRock -= 2
                notify(":> {} pays 2GR to unboot{}".format(me, dudes[0]))
        else: 
            remoteCall(dudes[0].controller,'ExpLodge', dudes[0])
   elif card.name == "The Oriental":
        dudes = findTarget("DemiAutoTargeted-atDude-targetMine-choose1")
        if not dudes[0].orientation == Rot90:
            notify(":> You can only use this ability on unbooted dude!!!!")
            return
        boot(dudes[0], forced = 'unboot')
        dudes[0].markers[mdict['Bounty']] += 2
        notify(":> {} unbooted {} and raised their bounty bu two using connections at {}!".format(me, dudes[0], card))
   elif card.name == "Disarm":
        if getGlobalVariable('Shootout') == 'True':
            dudes = findTarget("DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1")
            dudeGoods = findTarget('DemiAutoTargeted-atGoods_or_Spell-onAttachment-isUnbooted-choose1', card = dudes[0])
            if len(dudeGoods) and re.search(r'Unique',dudeGoods[0].Keywords):
                dudeGoods[0].moveTo(dudeGoods[0].controller.piles['Discard Pile'])
                notify(":> {} disarmed {} and discarded {} !".format(me, dudes[0], dudeGoods[0]))
            elif len(dudeGoods):
                dudeGoods[0].moveTo(dudeGoods[0].controller.piles['Boot Hill'])
                notify(":> {} disarmed {} and aced {} !".format(me, dudes[0], dudeGoods[0]))
            if confirm("Is your revealed hand legal?"):
                dudes = findTarget("DemiAutoTargeted-atDude-targetMine-isParticipating-choose1")
                TokensX('Put1High Noon:Stud', '', dudes[0])
                TokensX('Put2BulletNoonPlus', '', dudes[0])
            notify("{} gets 2 noon bullets and becomes a stud till Sundown".format(dudes[0]))
            notify(":> {} ignores all casualties this round of shootout !".format(me))
            return
        else:
            dudes = findTarget("DemiAutoTargeted-atDude-targetOpponents-choose1")
            dudeGoods = findTarget('DemiAutoTargeted-atGoods_or_Spell-onAttachment-isUnbooted-choose1', card = dudes[0])
            if len(dudeGoods):
                boot(dudeGoods[0], forced = 'boot')
                notify(":> {} disarmed {} by booting {} !".format(me, dudes[0], dudeGoods[0]))
        if confirm("Is your revealed hand legal?"):
            dudes = findTarget("DemiAutoTargeted-atDude-targetMine-choose1")
            TokensX('Put1High Noon:Stud', '', dudes[0])
            TokensX('Put2BulletNoonPlus', '', dudes[0])
            notify("{} gets 2 noon bullets and becomes a stud till Sundown".format(dudes[0]))
         
   elif card.name == "Friends in High Places":
        if confirm("Are you sure your dude has higher influence?"):
            clearShootout()      
            notify("{} uses his dude's influence to avoid shootout".format(me))
   elif card.name == "You Had ONE Job!":
        dudes = findTarget('DemiAutoTargeted-atDude-hasMarker{Bounty}-isParticipating-choose1')
        if not len(dudes):
            notify("There are no valid targets for this ability")
            return
        if dudes[0].markers[mdict['Bounty']] < 3:
            notify("You need at least 3 bounty on a dude to use this ability")
            return
        if fetchDrawType(dudes[0]) == 'Draw': 
            TokensX('Remove999Shootout:Draw', '', dudes[0])
            TokensX('Put1Shootout:Stud', '', dudes[0])
        else:
            TokensX('Remove999Shootout:Stud', '', dudes[0])
            TokensX('Put1Shootout:Draw', '', dudes[0]) 
  
   elif card.name == "Grim Servant O' Death":
        dudes = findTarget("DemiAutoTargeted-atDude-isNotParticipating-choose1")
        if dudes[0].controller == me:
            choice = confirm("Do you want {} to participate in the shootout".format(dudes[0].name))
            if choice:
                participateDude(dudes[0])
                return
            else:
                remoteCall(dudes[0].controller,"GSOD2",[card])
        else: 
            if remoteCall(dudes[0].controller,"GSOD",[card, dudes[0]]) == "True":
                return          
        return             
   elif card.name == "Decimator Array" and action == 'PLAY':
        if confirm("Do you want to unboot one of your mad scientists?"):
            dude = findTarget("DemiAutoTargeted-atMad Scientist-targetMine-isBooted-choose1")
            update()
            boot(dude[0], forced = 'unboot')
   elif card.name == "Devil's Six Gun":        
        j1 = [j for j in me.piles['Boot Hill'] if j.type == 'Joker']
        j2 = [j for j in me.piles['Discard Pile'] if j.type == 'Joker']
        j3 = [j for j in me.piles['Deck'] if j.type == 'Joker']
        jokers = j1 + j2 + j3
        if not len(jokers):
            notify("You have no jokers that are available to retrieve")
            return           
        if len(j1) == 2:
            string = "Both jokers are in your Boot Hill."
        elif len(j2) == 2:
            string = "Both jokers are in your Discard Pile."
        elif len(j3) == 2:
            string = "Both jokers are in your Deck."
        elif j1 and j2:
            string = "Left joker is in your Boot Hill, right joker is in your Discard Pile."
        elif j1 and j3:
            string = "Left joker is in your Boot Hill, right joker is in your Deck."
        elif j2 and j3:
            string = "Left joker is in your Discard Pile, right joker is in your deck."
        elif j1:
            string = "Joker is in your Boot Hill"
        elif j2:
            string = "Joker is in your Discard Pile"
        else:
            string = "Joker is in your Deck"         
        joker = askCard(jokers, "Choose Joker to use.{}".format(string))
        discardCards = findTarget('DemiAutoTargeted-isDrawHand-targetMine-choose1')
        if not len(discardCards): return 'ABORT'
        discardCards[0].moveTo(discardCards[0].owner.piles['Discard Pile'])
        for c in table:
            if c.highlight == DrawHandColor and c.controller == me: c.moveTo(me.piles['Draw Hand'])
        joker.moveTo(me.piles['Draw Hand'])
        notify("{} uses their {} to replace {} with {}".format(me,card,discardCards[0],joker))
        if getGlobalVariable("Shootout") == "True":
            revealHand(me.piles['Draw Hand'], type = 'shootout')
        else:
            revealHand(me.piles['Draw Hand'], type = 'lowball')
        TokensX('Put1DoNotAce', '', joker) 
   elif card.name == "Darius Hellstromme":
        weapon = findTarget("DemiAutoTargeted-atWeapon_and_Gadget-isParticipating-isUnbooted-targetMine-choose1")
        if not len(weapon):
            notify("You need unbooted weapon-gadget to use this ability")
            return
        dude = fetchHost(weapon[0])
        boot(weapon[0], forced = 'boot')
        dude.markers[mdict['PermControlPlus']] += 1
   elif card.name == "Father Tolarios":
        if len(me.hand):
            cardChoice = askCard([c for c in me.hand], "Choose a card you want to discard")
        else:
            notify("You need to discard a card to use this ability")
            return
        cardChoice.moveTo(me.piles['Discard Pile'])   
        wanted = findTarget("DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-choose1")
        if not len(wanted):
            notify("You need a wanted dude to fetch a card")
            return
        wanted[0].markers[mdict['Bounty']] -= 1
        mirOrMysDiscard = [c for c in me.piles['Discard Pile'] if ("Miracle" in c.keywords and "Unique" not in c.keywords )] + [c for c in me.piles['Discard Pile'] if ("Mystic" in c.keywords and "Unique" not in c.keywords) ]
        mirOrMysDeck = [c for c in me.piles['Deck'] if ("Miracle" in c.keywords and "Unique" not in c.keywords )] + [c for c in me.piles['Deck'] if ("Mystic" in c.keywords and "Unique" not in c.keywords) ]
        string = len(mirOrMysDiscard)
        cards = mirOrMysDiscard + mirOrMysDeck
        if len(cards) == 0:
            notify("You have no cards you can fetch with this ability")
            return
        card = askCard(cards, "Choose a card to fetch.First {} are in your discard".format(string))
        card.moveTo(me.hand)
        notify("{} fetched {} using Father Tolarios ability".format(me, card.name)) 
        #2t2d
   elif card.name ==  "The Spiritualy Society":
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      else: return
      if me.Influence > player.Influence:
         if confirm('Do you have more influence than {} in Town Square? '.format(player.Name)):
            drawMany(me.deck, 1, silent = True) 
      else: return
      notify("{} drew one card because they control Town Square ".format(me)) 
   elif card.name == "Buskers":
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      targetDude = findTarget("DemiAutoTargeted-atDude-targetOpponents-choose1")
      if player.GhostRock >= 2: remoteCall(player,'Buskers',targetDude)
      boot(targetDude[0], silent = True)
      notify("{} booted {} using {} ability.".format(me, targetDude[0].name,card.name))
   elif card.name == "Taiyari":
      targetDude = findTarget('DemiAutoTargeted-atDude-targetMine-isParticipating-choose1')
      bullets = compileCardStat(targetDude[0], stat = 'Bullets')
      if bullets == 0: bullets = 1
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      me.GhostRock -= bullets
      player.GhostRock += bullets
      TokensX('Put1Shootout:Stud', '', targetDude[0])
      notify("{} paid {} GR to make {} a stud, {} has maximum 4 bullets till teh end of the shootout".format(me,bullets,targetDude[0], targetDude[0]))
   elif card.name == "Feichi Suitcase Lee":
      targetDude = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1')
      boot(targetDude[0], silent = True)
      dudeInfluence = compileCardStat(targetDude[0], stat = 'Influence')
      sInfluence = compileCardStat(card, stat = 'Influence')
      if dudeInfluence < sInfluence:
         dude = findTarget('DemiAutoTargeted-atDude-isNotParticipating-isMine-choose1')
         participateDude(dude[0])
         notify("{} booted {} and brought {} into shootout".format(card.name, targetDude[0], dude[0]))
         return
      notify("{} booted {}".format(card.name, targetDude[0]))
   elif card.name == "Vida Azul":
      discardCards = findTarget('DemiAutoTargeted-isDrawHand-targetMine-choose1', choiceTitle = "Choose a card to discard from your hand")
      discardCards[0].moveTo(discardCards[0].owner.piles['Discard Pile'])
      targetDude = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
      dudeHorse = findTarget('DemiAutoTargeted-atHorse-onAttachment-isBooted-choose1', card = targetDude[0])
      
      TokensX("Remove1AbilityUsed",'', dudeHorse[0])
      boot(dudeHorse[0], forced = 'unboot')
      if(discardCards[0].Type == "Goods"):
         boot(targetDude[0], forced = 'unboot')
         notify("{} discarded {} to unboot {} and {}".format(me, discardCards[0], dudeHorse[0],targetDude[0]))
         return
      notify("{} discarded {} to unboot {}".format(me, discardCards[0], dudeHorse[0]))
   elif card.model == 'ae22bba2-cf1e-4038-b7bb-1d3429c10026': # Silas Aims (Exp.1)
      if not confirm("Is {} a mark?".format(card.name)):
         boot(card, forced = 'boot')
      targetDude = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1')
      if card.markers[mdict['Bounty']] > targetDude[0].markers[mdict['Bounty']]:
         remoteCall(dudes[0].controller, "Censure", [card, targetDude])
         notify('{} send {} home booted'.format(card,targetDude[0]))
      else:
         notify('Your dude doesnt have enough bounty')
         return 'Abort'
   elif card.name == 'Electrostatic Pump Gun':
      topd = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1')
      topDude = topd[0]
      TokensX('Put1BulletShootoutMinus', '', topDude)
      if not pull()[1] == 'Clubs':
            bullets = compilecardstat(topDude, stat = 'Bullets')
            if bullets == 0:
               if fetchDrawType(topDude) == 'Stud':
                  TokensX('Put1Shootout:Draw', '', topDude)
               notify("{} is a draw till the end of the shootout".format(topDude.name))
      else: 
            if confirm("Do you want to play react ability to change this pull to different suite?"):
               bullets = compilecardstat(topDude, stat = 'Bullets')
               if bullets == 0:
                  if fetchDrawType(topDude) == 'Stud':
                     TokenX('Put1Shootout:Draw', '', topDude)
                  notify("{} is a draw till the end of the shootout".format(topDude.name))
                  notify("Reminder: {} has to use react ability to change pull's suite.".format(card.controller))
            else: notify("EPG malfunctioned as {} used water insted of ghost rock to fuel it.".format(card.controller))
   elif card.name == 'Analytical Cognisizer':
      if confirm('Have you succesfully invented this gadget, if you answer yes your MS unboots and you will draw a card?'):
         ModifyStatus('UnbootHost')
         card = deck.top(1)
         card[0].moveTo(me.hand)
         notify('{} successfully invented {} so he unbooted his MS and drew a card'.format(me, card.name))
   elif card.name == 'Exultant Translocation':
      dude = fetchHost(card)
      tmd = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
      tmDude = tmd[0]
      x,y = dude.position
      Jx,Jy = tmDude.position
      dude.moveToTable(Jx,Jy)
      tmDude.moveToTable(x,y)
      orgAttachments(dude)
      orgAttachments(tmDude)
      if confirm('Did pull succeed by 6 or more?'):
         aCard = askCard([dude, tmDude], 'Chose a dude to unboot.')
         boot(aCard, forced = 'unboot')
         notify("{} and {} swapped places thanks to {}.".format(dude, tmDude, card.name))
         notify("{} got unbooted as pull was successful by 6 or more.".format(aCard))
      notify("{} and {} swapped places thanks to {}.".format(dude, tmDude, card.name))
   elif card.name =='Hostile Takeover':
         tmd = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
         tmDude = tmd[0]
         if fetchDrawType(tmDude) == 'Draw':
            notify("You need a stud to use this ability.")
            return 'Abort'
         tdeed = findTarget('DemiAutoTargeted-atDeed-targetOpponents-choose1')
         deed = tdeed[0]
         if tmDude.orientation != Rot90 and tdeed.orientation != Rot90:
            boot(tmDude, forced = 'boot')
            boot(deed, forced = 'boot')
            production = compileCardStat(deed, stat = 'Production')
            me.GhostRock += production
            notify('{} gained {} Ghost Rock by plundering {}.'.format(me, production, deed.name ))
            if confirm("Do you want to ace {} to give {} 1 control point and {} 1 influence?".format(card.name, deed.name, tmDude)):
               ace(card)
               deed.markers[mdict['PermControlPlus']] += 1
               tmDude.markers[mdict['PermInfluencePlus']] += 1
               notify('{} aced {} to give {} permanent influence point and {} permanent control point.'.format(me, card.name, tmDude.name, deed.name))

         else: 
            notify('You need to boot a dude and a deed to use this ability.')
   elif card.name == "I'm Your Huckleberry":
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      for card in table:
         if card.controller == me:
            if card.model == 'cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1': # The cheatin' icon
               remoteCall(player,'Huckleberry',card)
            
      targetDude= findTarget('DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1', choiceTitle = "Choose a dude that will be controlled by your opponent till the end of the shootout.")
      if targetDude[0].highlight == AttackColor:
         targetDude[0].highlight = DefendColor   
      else: targetDude[0].highlight = AttackColor
      TokensX('Put1Shootout:Huckleberry', '', targetDude[0])

      notify('{} takes control over {} till the end of the shootout'.format(card.controller, targetDude[0].name))
      return 
   elif card.name == 'House of Many Faiths':
      tmd = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
      tmDude = tmd[0]
      hostCards = eval(getGlobalVariable('Host Cards'))
      if not len([Card(att_id) for att_id in hostCards if hostCards[att_id] == tmDude._id and re.search(r'Miracle',Card(att_id).Keywords)]):
         notify("You have to chose a dude with Miracle to use this ability")
         return 'Abort'
      if len(me.hand) and len(me.piles['Discard Pile']):
         handDiscard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
         handDiscard.moveTo(me.piles['Deck'])
         cardFromDiscard = askCard([ c for c in me.piles['Discard Pile']])
         cardFromDiscard.moveTo(me.piles['Deck'])
         me.Deck.shuffle()
         notify('{} put {} and {} that was fetched from discard into their deck.'.format(me, handDiscard, cardFromDiscard))
      else:
         notify ("You have to have a cards in hand and in discard pile to use this ability!")
         return 'Abort'
      ModifyStatus('MoveTarget-moveToTown Square', '', card, tmDude)
      boot(tmDude, forced = 'unboot')
      tmDude.markers[mdict['PermInfluencePlus']] += 1
      notify("{} moves {} to Town Squere unboots them and gives them noon influence.")
   elif card.name == "Jonah's Alliance":
      tmd = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
      tmDude = tmd[0]
      boot(tmDude, forced = 'boot')
      TokensX('Remove1High Noon:Draw', '',tmDude)
      TokensX('Put1High Noon:Stud', '',tmDude)
      for iter in range(2):
         if tmDude.markers[mdict['Bounty']] < 4:
            tmDude.markers[mdict['Bounty']] += 1
      TokensX('Jonah Control', '',tmDude)
      if confirm('Do you want to boot a hex at a location to remove all traits, abilities and bonuses at that location?'):
         spell = findTarget('DemiAutoTargeted-atSpell-isMine-isUnbooted-choose1',choiceTitle='Chose spell to boot')
         boot(spell[0], forced = 'boot')
         target = findTarget('DemiAutoTargeted-atSpell_or_Goods-targetOpponents-choose1', choiceTitle='Choose opponents attachment to blank it till the end of a day.')
         TokensX('Put1High Noon:Blank', '',target[0])
   elif card.name == 'Ke Wang':
      topd = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1')
      topDude = topd[0]
      upkeep = compileCardStat(topDude, stat = 'Upkeep')
      if me.GhostRock >= upkeep:
         me.GhostRock -= upkeep
         topDude.controller.GhostRock += upkeep
         boot(topDude, forced = 'boot')
         TokensX('Put1BulletShootoutMinus', '', topDude)
         norify('{} booted {} and gave them -1 bullets using {} ability'.format(me, topDude.name, card.name))
      else:
         notify('You do not have enough ghost rock to use this ability.')
         return
   elif card.name =='Doc Holliday':
      tpd = findTarget('DemiAutoTargeted-atDude-isParticipating-choose1', choiceTitle = 'Choose a skilled dude that ranking will be used for bullet bonus.')
      tpDude = topd[0]
      skillCheck = fetchSkills(tpDude)
      tmpd = findTarget('DemiAutoTargeted-atDude-targetMine-isParticipating-choose1', choiceTitle = 'Choose a dude that receives a bonus')
      tmpDude = tmpd[0]
      bullets = compileCardStat(card, stat = 'Bullets')
      if bullets < 0:
         bullets = 0
      if (bullets + skillCheck[0][1] <= 4):
         for iter in range(skillCheck[0][1]):
            TokensX('Put1BulletNoonPlus', '',tmpDude)
            notify('{} increased {} bullets by {} skill rating'.format(me, tmpDude.name, tpDude))
            return
      else:
         bRange = 4 - bullets
         if bRange > 0:
            for iter in range(bRange):
               TokensX('Put1BulletNoonPlus', '',tmpDude)
            notify('{} increased {} bullets by {} skill rating'.format(me, tmpDude.name, tpDude))
            return












#qwe



   else: notify("{} uses {}'s ability".format(me,card)) # Just a catch-all.
   return 'OK'

def fetchCustomUpkeep(card):
   extraUpkeep = 0
   if card.name == "Denise Brancini":
      for player in getActivePlayers():
         extraUpkeep += len([c for c in player.piles['Boot Hill'] if (c.type == 'Joker')])
   return extraUpkeep
               

def fetchCustomProduction(card):
   extraProduction = 0
   if card.name == "Long Strides Ranch":
      if len([c for c in table if re.search(r'Horse',c.Keywords)]) >= 2: extraProduction = 2
   return extraProduction
               

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
         if Time == 'Sundown' and re.search(r'Sentinel',marker[0]) and card.controller == me and card.owner == me:
            dudeSpells = findTarget('AutoTargeted-atSpell-onAttachment-isBooted', card = card)
            if not confirm("Is {} in the Town Square?".format(card.name)):
                continue
            for Spell in dudeSpells:                  
                if Spell.name == "Sentinel":
                    if confirm("Do you want to discard {} to give {} 1 Control Point?".format(Spell.name, card.name)):
                        TokensX("Remove1Sentinel",'', card)
                        card.markers[mdict['PermControlPlus']] += 1
                        Spell.moveTo(me.piles['Discard Pile'])                       
                    else:
                        TokensX("Remove1Sentinel",'', card)
         
         if Time == 'Sundown' and re.search(r'HandsomeCP',marker[0]) and card.owner == me and me.GhostRock >=4: 
 
               if confirm("Do you want to make pay 4 GR to make control point on {} permanent?".format(card.name)):
                  me.GhostRock -= 4
                  card.markers[mdict['PermControlPlus']] += 1
                  notify("{} decided to pay 4 GR to gain additional CP at {}".format(me, card.name))
               TokensX("Remove1HandsomeCP",'', card)
               TokensX("Remove1ControlPlus",'', card)
               
         if Time == 'Sundown' and re.search(r'Blank',marker[0]) and card.owner == me : 
            TokensX("Remove1High Noon:Blank",'', card)

         if Time == 'Sundown' and re.search(r'Jonah Control',marker[0]) and card.owner == me : 
            TokensX("Remove1High Noon:Jonah Control",'', card)
         if (Time == 'ShootoutEnd'
               and (re.search(r'Sun In Yer Eyes',marker[0])
                 or re.search(r'Unprepared',marker[0])
                 or re.search(r'Shootout:',marker[0]))):
            TokensX('Remove999'+marker[0], marker[0] + ':', card)
            notify("--> {} removes the {} resident effect from {}".format(me,marker[0],card))
         if (Time == 'ShootoutEnd'
               and (re.search(r'Huckleberry',marker[0]))):
                  TokensX('Remove999'+marker[0], marker[0] + ':', card)
                  ModifyStatus('SendHomeBootedTarget-DemiAutoTargeted-atDude', '',card, card)

         if Time == 'High Noon' and re.search(r'UpkeepPrePaid',marker[0]) and card.controller == me: # Tax Office reduction effects removal
            modProd(card, -card.markers[marker], True)
            card.markers[marker] = 0
         if Time == 'High Noon' and re.search(r'Rowdy Ike',marker[0]) and card.controller == me: 
            TokensX("Remove1Rowdy Ike",'', card)

         if Time == 'High Noon' and re.search(r'Ike Place',marker[0]) and card.controller == me: 
            TokensX("Remove1Ike Place",'', card)
            card.markers[mdict['ProdMinus']] = 0

         if (Time == 'ShootoutEnd' and re.search(r'Serendipitous',marker[0])):
            if confirm("Do you want to pay 3 Ghost Rock to keep this dude in play?") and payCost(3) != 'ABORT':
               TokensX('Remove999'+marker[0], marker[0] + ':', card)
               notify("--> {} paid 3 ghost rock to retain {} in play.".format(me,card))
            else:
               discard(card,silent = True)
               notify("--> {} wasn't paid properly so they left play.".format(card))
   
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
            targetDude.markers[mdict['PermControlPlus']] += 1
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
   if originator != me: me.hand.addViewer(originator)
   update()
   #remoteCall(originator,'WhisperCards',[me,[c for c in me.hand]])
   while not confirm("You are now revealing your hand to {}. Press Yes to continue, Press No to ping the other player to see if they had enough time to see the cards".format(originator.name)):
      notify("{} wants to know if it's OK to hide their hand once more".format(me))
   if originator != me: me.hand.removeViewer(originator)
   notify("{} hides their play hand once more".format(me))
   
def WhisperCards(player,cardList):
   mute()
   initText = "{} is revealing:\n".format(player)
   for c in cardList:
      initText += "- {}\n".format(c)   
   whisper(initText)

def BottomDealing(originPlayer,card):
   drawhandMany(originPlayer.Deck, 5, True,scripted = True)
   if getGlobalVariable('Shootout') == 'True': Drawtype = 'lowball'
   else: Drawtype = 'shootout' # These two are reversed so that the jokers are always used for their worst value comparatively.
   rnd(1,10)
   resultTXT = revealHand(me.piles['Draw Hand'], type = Drawtype, event = None, silent = True)
   notify("{}'s new hand rank is {}".format(me,resultTXT))
   passPileControl(originPlayer.Deck,originPlayer)   
   passPileControl(originPlayer.piles['Discard Pile'],originPlayer)   

def AllieHensmanXP(mark,allie):
   mute()
   markInfluence = compileCardStat(mark, stat = 'Influence')
   if confirm("Do you want to pay {} to {} to avoid discarding {}?".format(markInfluence,allie.controller.name,mark.Name)):
      if me.GhostRock >= markInfluence or not confirm("You do not seem to have enough Ghost Rock left. Bypass?"):
         me.GhostRock -= markInfluence
         allie.controller.GhostRock += markInfluence
         notify("{} corners {} and extracts {} Ghost Rock from {} for their safety".format(allie,mark,markInfluence,mark.controller))
      else: 
         discard(mark,silent = True)
         notify("{} couldn't afford {}'s tax and has to discard {}".format(mark.controller,allie,mark))
   else: 
      discard(mark,silent = True)
      notify("{} couldn't afford {}'s tax and has to discard {}".format(mark.controller,allie,mark))
   
def TWHITM(targetCards, discardCard = True): # This Will Hurt in the Morning
   mute()
   for card in targetCards:
      if discardCard: discard(card)
      else:
         if me.GhostRock >= 1 and confirm("Pay 1 Ghost Rock to prevent {} from being aced?".format(card.name)):
            me.GhostRock -= 1
            discard(card)
            notify("{} pays 1 ghost rock to avoid acing {}".format(me,card)) 
         else: 
            ace(card)
   for c in table:
      if c.highlight == DrawHandColor: c.moveTo(me.piles['Draw Hand']) # We move the remaining card back to the draw hand to be able to calculate value again
   drawhandMany(me.Deck, 2, True,scripted = True)
   if getGlobalVariable('Shootout') == 'True': Drawtype = 'shootout'
   else: Drawtype = 'lowball'
   resultTXT = revealHand(me.piles['Draw Hand'], type = Drawtype, event = None, silent = True)
   notify("{}'s new hand rank is {}".format(me,resultTXT))
         
def TaxOffice(dude):
   mute()
   upkeep = compileCardStat(dude, stat = 'Upkeep')
   if upkeep:
      if not confirm("Pay {} Ghost Rock to retain this dude this turn?".format(upkeep)):
         discard(dude)
      else:
         msg = payCost(upkeep, MSG = "You do you not seem to have enough ghost rock to pay your taxes varmint! Bypass?")
         if msg == 'ABORT': discard(dude)
         else:
            modProd(dude, upkeep, True)
            TokensX('Put{}UpkeepPrePaid'.format(upkeep), '', dude)
            notify("{} pays the tax required to retain {}".format(me,dude))
   else: notify(":> {} has 0 upkeep, so their accounts were already in order.".format(dude))

def FuntimeFreddyChoose(card,spell1,spell2):
   mute()
   notify("{} is choosing which hex to ace from {}'s ability".format(me,card))
   acedSpell = None
   whisper(":::CHOICE::: Choose which hex to ace")
   while not acedSpell: acedSpell = askCard([spell1,spell2],'Choose which spell to ace')
   if acedSpell == spell1: savedSpell = spell2
   else: savedSpell = spell1
   remoteCall(card.controller,'FuntimeFreddyFinish',[card,acedSpell,savedSpell,me])

def FuntimeFreddyFinish(card,acedSpell,savedSpell,acingPlayer):
   mute()
   ace(acedSpell, silent = True)
   ace(card, silent = True)
   hostCard = findHost(savedSpell)
   if hostCard: 
      attachCard(savedSpell,hostCard)
      payCost(savedSpell.Cost)
      savedSpell.highlight = None
   handDiscard = None
   while not handDiscard:
      handDiscard = askCard([c for c in me.hand],"Choose which card to discard from your hand")
   handDiscard.moveTo(me.piles['Discard Pile'])
   notify("{} discarded {} and aced {} to fetch and play {} (paying {}) on {} and {} chose to ace {}".format(me,handDiscard,card,savedSpell,savedSpell.Cost,hostCard,acingPlayer,acedSpell))

def CookinTroubleStart(card):
   mute()
   if not len(me.hand): notify(":::INFO::: {}'s play hand is empty. You have nothing to cook".format(me))
   else:
      me.hand.addViewer(card.controller)
      notify(":> {} Reveals their hand to {}".format(me,card.controller))
      remoteCall(card.controller,'CookinTroubleChoose',[card,[c for c in me.hand]])
      
def CookinTroubleChoose(card,handList):
   mute()
   update()
   whisper(":::CHOICE::: If your opponent cheated this turn, choose an action, goods, or spell to discard.")
   cardChoice = askCard([c for c in handList],'Choose an action,goods or spell card to discard.')
   if cardChoice == None:
      notify("{} does not sabotage any card in {}'s hand".format(me,handList[0].controller))
   while cardChoice.Type != 'Action' and cardChoice.Type != 'Goods' and cardChoice.Type != 'Spell': # If they chose a non-action, we force them to choose an action.
      if confirm("You cannot select cards which are not action, goods or spell  to discard with Cookin' Up Trouble. Do you want to choose nothing?"): 
         notify("{} does not sabotage any card in {}'s hand".format(me,handList[0].controller))
         cardChoice = None
         break
      else: 
         actionsList = [c for c in handList if (c.Type == 'Action' or c.Type == 'Goods' or c.Type == 'Spell')]
         if not actionsList: 
            notify("{} does not find any appropriate cards in {}'s hand to sabotage".format(me,handList[0].controller))
            cardChoice = None
            break
         else:
            cardChoice = askCard(actionsList,'Choose an action,goods or spell card to discard.')
            if cardChoice == None: 
               notify("{} does not sabotage any card in {}'s hand".format(me,handList[0].controller))
               break
   remoteCall(handList[0].controller,'CookinTroubleEnd',[card,cardChoice])

def CookinTroubleEnd(card,cardChoice):
   mute()
   if cardChoice:
      cardChoice.moveTo(me.piles['Discard Pile'])
      notify("{}'s {} sabotages {} out of {}'s play hand".format(card.controller,card,cardChoice,me))
   me.hand.removeViewer(card.controller)

def NathanShaneStart(card):
   mute()
   bullets = compileCardStat(card, stat = 'Bullets')
   if bullets > len(me.hand):
        bullets = len(me.hand)
   if not len(me.hand): notify(":::INFO::: {}'s play hand is empty. Nathan has nothing to snipe".format(me))
   elif not bullets: notify(":::INFO::: {} has currently 0 bullets and no capacity to snipe anything".format(card))
   else:
      randomCards = []
      for iter in range(bullets):
         randomC = me.hand.random()
         randomCards.append(randomC)
         randomC.moveTo(me.ScriptingPile)         
      notify(":> {} Reveals {} random cards to {}".format(me,bullets,card.controller))      
      remoteCall(card.controller,'NathanShaneChoose',[card,[c for c in me.ScriptingPile]])

def NathanShaneChoose(card,handList):
   mute()
   update()
   cardChoice = askCard([c for c in handList],"Choose action card to discard.")
   if cardChoice == None:
      notify("{} does not snipe any card in {}'s hand".format(me,handList[0].controller))
   else:
      while cardChoice.Type != 'Action': # If they chose a non-action, we force them to choose an action.
         if confirm("You cannot select non-action cards to discard with Nathan's ability. Do you want to choose nothing?"): 
            notify("{} does not snipe any card in {}'s hand".format(me,handList[0].controller))
            cardChoice = None
            break
         else: 
            actionsList = [c for c in handList if c.Type == 'Action']
            if not actionsList: 
               notify("{} does not find any action in {}'s hand to snipe".format(me,handList[0].controller))
               cardChoice = None
               break
            else:
               cardChoice = askCard(actionsList,"Choose action card to discard.")
               if cardChoice == None: 
                  notify("{} does not snipe any card in {}'s hand".format(me,handList[0].controller))
                  break
   remoteCall(handList[0].controller,'NathanShaneEnd',[card,cardChoice])

def NathanShaneEnd(card,cardChoice):
   mute()
   if cardChoice:
      cardChoice.moveTo(me.piles['Discard Pile'])
      notify("{}'s {} snipes {} out of {}'s play hand".format(card.controller,card,cardChoice,me))
   for c in me.ScriptingPile: c.moveTo(me.hand)
   
def MarciaRidgeStart(marcia,usedDeed):
   usedDeed.setController(marcia.controller)
   remoteCall(marcia.controller,'MarciaRidgeDeedUse',[marcia,usedDeed,me])

def MarciaRidgeDeedUse(marcia,usedDeed,origController):
   useAbility(usedDeed)
   usedDeed.setController(origController)

def RicoStart(card):
   mute()
   if not len(me.hand): notify(":::INFO::: {}'s play hand is empty for some reason!".format(me))
   else:
      me.hand.addViewer(card.controller)
      notify(":> {} Reveals their hand to {}".format(me,card.controller))
      remoteCall(card.controller,'RicoView',[card,[c for c in me.hand]])
      
def RicoView(card,handList):
   mute()
   update()
   askCard([c for c in handList],"This is your opponent's current hand. Double click a card or close this window to continue")
   whisper("Reminder: The opponent's hand contained: {}".format([c.Name for c in handList]))
   remoteCall(handList[0].controller,'RicoStopView',[card])
   if confirm("Do you want to retain your current starting gang? (In order to save time)"): 
      notify(":> {} opts to retain their current starting gang without change")
   else:
      startingDudesNR = 0
      for c in table:
         if c.Type == 'Dude' and c.controller == me and not re.search(r'Grifter',c.Keywords):
            clearAttachLinks(c)
            me.GhostRock += num(c.Cost)
            c.moveTo(me.Deck)
            startingDudesNR += 1
      selectedDudesNR = 0
      if startingDudesNR:
         me.Deck.addViewer(me)
         while selectedDudesNR < startingDudesNR:
            choiceDude = askCard([c for c in me.Deck if c.Type == 'Dude' and not re.search(r'Grifter',c.Keywords) and not re.search(r'Gadget',c.Keywords)],"Select dude to add to your starting posse ({}/{})\n Close the window to finish".format(selectedDudesNR + 1,startingDudesNR))
            if not choiceDude: break
            placeCard(choiceDude,'SetupDude',selectedDudesNR)
            payCost(choiceDude.Cost)
            selectedDudesNR += 1
         me.Deck.removeViewer(me)
         me.Deck.shuffle()
      announceText = "{}'s new starting gang is ".format(me)
      for dude in [c for c in table if c.controller == me and c.Type != 'Outfit' and c.Type != "Token"]:
         announceText += "{}, ".format(dude)
      notify(announceText)      

def RicoStopView(card):
   mute()
   if card.controller != me: me.hand.removeViewer(card.controller) # If clause, for debug purposes
   
def JaelGuile(card):
   mute()
   for iter in range(2):
      choiceDudes = findTarget('AutoTargeted-atDude-hasMarker{Bounty}-targetMine-isParticipating')
      if not len(choiceDudes): choiceDudes = findTarget('AutoTargeted-atDude-targetMine-isParticipating')
      if len(choiceDudes):
         choiceDude = askCard(choiceDudes,"Select a dude to be hit by {} ({}/2). \nAn unbooted dude will boot. A Booted dude will be discarded".format(card.Name,iter + 1))
         if choiceDude.orientation == Rot0: boot(choiceDude)
         else: discard(choiceDude)
   
def RickHenderson(dude,rick):
   mute()
   if not confirm("Pay 1 Ghost Rock to {} to retain {}?".format(rick.Name,dude.Name)): discard(dude)
   else:
      msg = payCost(1, MSG = "You do you not seem to have enough ghost rock to pay off {}! Bypass?".format(rick.Name))
      if msg == 'ABORT': discard(dude)
      else:
         rick.controller.GhostRock += 1
         notify("{} pays off {} to retain {}".format(me,rick,dude))
   
   
def Framed(card,dude):
   if dude.orientation != Rot90 and me.GhostRock > 0 and confirm('Do you want to boot {} and pay 1 Ghost Rock to {} to avoid giving them a bounty?'.format(dude.Name,card.controller)):
      dude.orientation = Rot90
      me.GhostRock -= 1
      card.controller.GhostRock += 1
      notify(":> {} boots {} and pays 1 Ghost Rock to {} to avoid becoming wanted".format(me,dude,card.controller))
      return
   dude.markers[mdict['Bounty']] += 1
   notify(":> {} succesfull framed {} for 1 bounty".format(card.controller,dude))
   
def SightBeyondSightStart(card):
   mute()
   if not len(me.hand): 
      notify(":::INFO::: {}'s play hand is empty. Sight Beyond Sight has nothing to discard".format(me))
      return 'ABORT'
   else:
      randomCards = []
      if len(me.hand) >= 2:
         for iter in range(2):
            randomC = me.hand.random()
            randomCards.append(randomC)
            randomC.moveTo(me.ScriptingPile)         
         notify(":> {} Reveals 2 random cards to {}".format(me,card.controller))      
         remoteCall(card.controller,'SightBeyondSightChoose',[card,[c for c in me.ScriptingPile]])
      else:
         randomC = me.hand.random()
         randomCards.append(randomC)
         randomC.moveTo(me.ScriptingPile)         
         notify(":> {} Reveals 1 random cards to {}".format(me,card.controller))      
         remoteCall(card.controller,'SightBeyondSightChoose',[card,[c for c in me.ScriptingPile]])
def SightBeyondSightChoose(card,handList):
   mute()
   update()
   cardChoice = askCard([c for c in handList],"Choose one non-Unique card to ace or close this window to ace none.")
   if cardChoice == None:
      notify("{} does not hex any card in {}'s hand".format(me,handList[0].controller))
   else:
      while ((cardChoice.Type == 'Dude' or cardChoice.Type == 'Deed') and not re.search(r'Non-Unique',cardChoice.Keywords)) or ((cardChoice.Type == 'Goods' or cardChoice.Type == 'Action') and re.search(r'Unique',cardChoice.Keywords)): # If they chose a unique card, we force them to choose an non-unique.
         if confirm("You cannot select unique cards to ace with Sight Beyond Sight's ability. Do you want to choose nothing?"): 
            notify("{} does not hex any card in {}'s hand".format(me,handList[0].controller))
            cardChoice = None
            break
         else: 
            cardList = [c for c in handList if ((c.Type == 'Dude' or c.Type == 'Deed') and re.search(r'Non-Unique',c.Keywords)) or ((c.Type == 'Goods' or c.Type == 'Action') and not re.search(r'Unique',c.Keywords))]
            if not cardList: 
               notify("{} does not find any non-unique in {}'s hand to hex".format(me,handList[0].controller))
               cardChoice = None
               break
            else:
               cardChoice = askCard(cardList,"Choose non-unique card to discard.")
               if cardChoice == None: 
                  notify("{} does not hex any card in {}'s hand".format(me,handList[0].controller))
                  break
   remoteCall(handList[0].controller,'SightBeyondSightEnd',[card,cardChoice])

def SightBeyondSightEnd(card,cardChoice):
   mute()
   if cardChoice:
      cardChoice.moveTo(me.piles['Boot Hill'])
      notify("{}'s {} hexes {} out of {}'s play hand".format(card.controller,card,cardChoice,me))
   for c in me.ScriptingPile: c.moveTo(me.hand)
   
def BurnOut(card):
   mute()
   if not len(me.hand): 
      notify(":::INFO::: {}'s play hand is empty. There is no card to ace.".format(me))
      return 'ABORT'
   else:
      cards = me.hand
      remoteCall(card.controller,'BurnOutChoice',[card, cards])

def BurnOutChoice(card, cards):
   update()
   cardChoice = askCard([c for c in cards],"Choose one card to ace")
   remoteCall(cardChoice.controller, 'BurnOutEnd', cardChoice)
def BurnOutChoice(cardChoice):
      cardChoice.moveTo(me.piles['Boot Hill'])
      notify("{}'s aces {} out of {}'s play hand".format(card.controller,cardChoice,me))

def chkHenryMoran(type):
   if type == 'lowball':
      for card in table:
         if card.Name == 'Henry Moran' and card.controller == me and card.orientation == Rot0:
            notify(":> {} is about to reveal a cheating hand in lowball, so {} is booting and forcing them to reveal the top 5 cards of their deck instead".format(me,card))
            boot(card, silent = True)
            for c in table:
               if c.highlight == DrawHandColor and c.controller == me: c.moveTo(c.owner.piles['Discard Pile']) # Henry always discards, and won't ace Jokers.
            drawhandMany(count = 5, silent = True, scripted = True)
            revealHand(me.piles['Draw Hand'], 'lowball')
            return True
   return False   
   
def DeniseBrancini():
   for c in me.piles['Boot Hill']:
      if c.type == 'Joker': c.moveTo(me.Deck)
   shuffle(me.Deck)
   
def ExpLodge(dude):
    if me.GhostRock > 1:
        choice = confirm("Do you want to pay 2GR to unboot {}?.".format(dude.name))
        if choice:
            boot(dude, forced = 'unboot')
            me.GhostRock -= 2
            notify(":> {} pays 2GR to unboot{}".format(dude.controller, dude))
            
def GSOD(card,dude):
    choice = confirm("Do you want {} to participate in the shootout".format(dude))
    if choice:
        participateDude(dude)
        return choice
    else:
        remoteCall(card.controller,"GSOD2", card)
def GSOD2(card):
    dude = findTarget("DemiAutoTargeted-atDude-targetMine-isParticipating-choose1")
    TokensX('Put1Shootout:Stud', '', dude[0])
    TokensX('Put2BulletShootoutPlus', '', dude[0]) 
    notify("Your opponent take two casualties if he reveals cheating hand this round of shootout!!!!!")

    
def Censure(card,dudes):
    ModifyStatus('SendHomeBootedTarget-DemiAutoTargeted-atDude', '',card, dudes)
    
def Intercession(oDude):
     TokensX('Put2BulletShootoutPlus', '', oDude)
     boot(oDude, forced = 'unboot')

def chkPropertyIsTheft(type):
   if type == 'shootout':
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]

      for card in table:
         if card.Name == 'Property Is Theft' and card.controller ==  player:
            if me.GhostRock > 0:
               payCost(1)
            else: return
            if not len([c for c in table if c.model == 'cd31eabe-e2d8-49f7-b4de-16ee4fedf3c1' and c.controller == player]):
               player.GhostRock += 1
               notify("{} got caught cheatin' during shootout and paid {} 1 Ghost Rock for it".format(me, player))
            else: 
               notify("{} got caught cheatin' during shootout and paid bank 1 Ghost Rock for it.".format(me))
            return True
   return False   
def Buskers(targetDude):
   
   if confirm("Do you want pay {} 2GR to avoid booting {}?".format(opponent, targetDude[0])):
      me.GhostRock -= 2
      opponents = [player for player in getPlayers() if player != me or len(getPlayers()) == 1]
      if len(opponents) == 1: player = opponents[0]
      player.GhostRock +=2
      notify("{} decided to pay 2 GR to avoid booting {}".format(me,targetDude[0]))
      return

   else:
      boot(targetDude[0], silent = True)
      return
def Murdered(card):
      disCR = [c for c in me.piles['Discard Pile'] if ("Action" in c.Type and re.search(r'Cheatin',c.Text))]
      deckCR = [c for c in me.piles['Deck'] if ("Action" in c.Type and re.search(r'Cheatin',c.Text))]
      string = len(disCR)
      cards = disCR + deckCR
      if len(cards) == 0:
         notify("You have no cards you can fetch with this ability")
         return
      card = askCard(cards, "Choose a CR to fetch if you do you will have to discard a card from your hand.First {} are in your discard".format(string))
      card.moveTo(me.hand)
      if card:
         choicehand = askCard([c for c in me.hand],'Choose which card to discard from your hand',card.Name)
         choicehand.moveTo(me.piles['Discard Pile'])
      else: return
      notify("{} fetched {} using Murdered in Tombstone ability and discarded {}".format(me, card.name, choicehand)) 
      return
def Huckleberry(card):
   targetDude= findTarget('DemiAutoTargeted-atDude-targetMine-isParticipating-choose1', choiceTitle = "Choose a dude that will be controlled by your opponent till the end of the shootout.")
   if targetDude[0].highlight == AttackColor:
      targetDude[0].highlight = DefendColor   
   else:
      targetDude[0].highlight = AttackColor
   TokensX('Put1Shootout:Huckleberry', '', targetDude[0])

   notify('{} takes control over {} till the end of the shootout'.format(card.controller, targetDude[0].name))
   return 
'''
#target opponents participating dude
   topd = findTarget('DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1')
   topDude = topd[0]

#target my participating dude
tmpd = findTarget('DemiAutoTargeted-atDude-targetMine-isParticipating-choose1')
tmpDude = tmpd[0]


#target opponents dude
   tod = findTarget('DemiAutoTargeted-atDude-targetOpponents-choose1')
   toDude = tod[0]

#target my dude
   tmd = findTarget('DemiAutoTargeted-atDude-targetMine-choose1')
   tmDude = tmd[0]

#target dudes attachement
dudeGoods = findTarget('DemiAutoTargeted-atGoods_or_Spell-onAttachment-isUnbooted-choose1', card =DUDECARD)

#discarding card from hand
choicehand = askCard([c for c in me.hand],'Choose which card to discard from your hand',card.Name)
choicehand.moveTo(me.piles['Discard Pile'])

#booting and unbooting cards
boot(CARD , forced = 'unboot')
boot(CARD, forced = 'boot')


#example of searching cards
if re.search(r'(Ranch|Improvement)',c.Keywords)

#discard pile, deck, boot hill and moving cards to pile
discardPile = me.piles['Discard Pile']
deck = me.piles['Deck']
bootHill = me.piles['Boot Hill']
CARD.moveTo(me.piles['Discard Pile'])

#examples of modifying statuses
ModifyStatus('SendHomeBootedTarget-DemiAutoTargeted-atDude', '',card, dudes)
ModifyStatus('MoveTarget-moveToDeed_or_Town Square_or_Outfit', '', card, dudesPub)

#MARKERS AND SIMILAR
dude.markers[mdict['Bounty']] += 1

   '''


