    # Python Scripts for the Star Wards LCG definition for OCTGN
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

import re

failedRequirement = True #A Global boolean that we set in case an Autoscript cost cannot be paid, so that we know to abort the rest of the script.
#selectedAbility = {} # Used to track which ability of multiple the player is trying to pay.
TitleDone = 'Unset'
#------------------------------------------------------------------------------
# Play/Score/Rez/Trash trigger
#------------------------------------------------------------------------------

def executePlayScripts(card, action):
   #action = action.upper() # Just in case we passed the wrong case
   debugNotify(">>> executePlayScripts() with action: {}".format(action)) #Debug
   global failedRequirement
   scriptEffect = 'INCOMPLETE'
   if not Automations['Play']: 
      #whisper(":::WARNING::: Your play automations have been deactivated.")
      return
   if not card.isFaceUp: return
   if CardsAS.get(card.model,'') != '': # Commented in order to allow scripts in attacked cards to trigger
      debugNotify("We have autoScripts!") # Debug
      failedRequirement = False
      X = 0
      Autoscripts = CardsAS.get(card.model,'').split('||') # When playing cards, the || is used as an "and" separator, rather than "or". i.e. we don't do choices (yet)
      autoScriptsSnapshot = list(Autoscripts) # Need to work on a snapshot, because we'll be modifying the list.
      debugNotify("List of autoscripts before scrubbing: {}".format(Autoscripts)) # Debug
      for autoS in autoScriptsSnapshot: # Checking and removing any "AtTurnStart" clicks.
         if (re.search(r'atPhase', autoS) or 
             re.search(r'whileInPlay', autoS) or
             re.search(r'constantAbility', autoS) or
             re.search(r'after([A-za-z]+)', autoS) or 
             re.search(r'onPay', autoS) or # onPay effects are only useful before we go to the autoscripts, for the cost reduction.
             re.search(r'-isTrigger', autoS) or
             re.search(r'Empty', autoS)): Autoscripts.remove(autoS) # Empty means the card has no autoscript, but we still want an empty list.
         elif not chkDummy(autoS, card): Autoscripts.remove(autoS)
      debugNotify('Looking for multiple choice options') # Debug
      if action == 'PLAY': trigger = 'onPlay' # We figure out what can be the possible multiple choice trigger
      else: trigger = 'N/A'
      debugNotify('trigger = {}'.format(trigger)) # Debug
      if trigger != 'N/A': # If there's a possibility of a multiple choice trigger, we do the check
         TriggersFound = [] # A List which will hold any valid abilities for this trigger
         for AutoS in Autoscripts:
            if re.search(r'{}:'.format(trigger),AutoS): # If the script has the appropriate trigger, we put it into the list.
               TriggersFound.append(AutoS)
         debugNotify('TriggersFound = {}'.format(TriggersFound)) # Debug
         if len(TriggersFound) > 1: # If we have more than one option for this trigger, we need to ask the player for which to use.
            if Automations['WinForms']: ChoiceTXT = "This card has multiple abilities that can trigger at this point.\nSelect the ones you would like to use."
            else: ChoiceTXT = "This card has multiple abilities that can trigger at this point.\nType the number of the one you would like to use."
            debugNotify("trigger = {}. Instructions = {}".format(trigger,card.Instructions), 4)
            triggerInstructions = re.search(r'{}\[(.*?)\]'.format(trigger),card.Instructions) # If the card has multiple options, it should also have some card instructions to have nice menu options.
            if not triggerInstructions and debugVerbosity >= 1: notify("## Oops! No multiple choice instructions found and I expected some. Will crash prolly.") # Debug
            cardInstructions = triggerInstructions.group(1).split('|-|') # We instructions for trigger have a slightly different split, so as not to conflict with the instructions from AutoActions.
            choices = cardInstructions
            abilChoice = SingleChoice(ChoiceTXT, choices, type = 'button')
            if abilChoice == 'ABORT' or abilChoice == None: return # If the player closed the window, or pressed Cancel, abort.
            TriggersFound.pop(abilChoice) # What we do now, is we remove the choice we made, from the list of possible choices. We remove it because then we will remove all the other options from the main list "Autoscripts"
            for unchosenOption in TriggersFound:
               debugNotify(' Removing unused option: {}'.format(unchosenOption)) # Debug
               Autoscripts.remove(unchosenOption)
            debugNotify('Final Autoscripts after choices: {}'.format(Autoscripts)) # Debug
      debugNotify("List of autoscripts after scrubbing: {}".format(Autoscripts)) # Debug
      if len(Autoscripts) == 0 and debugVerbosity >= 2: notify("### No autoscripts remaining.") # Debug
      for autoS in Autoscripts:
         debugNotify("First Processing: {}".format(autoS)) # Debug
         effectType = re.search(r'(on[A-Za-z]+|while[A-Za-z]+):', autoS)
         if not effectType: 
            whisper(":::ERROR::: Script on {} is malformed. Please contact Db0!".format(card))
            return
         scriptHostCHK = re.search(r'(?<!-)onHost([A-Za-z]+)',effectType.group(1))
         actionHostCHK = re.search(r'HOST-([A-Z-]+)',action)
         currObjID = getGlobalVariable('Engaged Objective')
         #if debugVerbosity >= 2 and scriptHostCHK: notify ('### scriptHostCHK: {}'.format(scriptHostCHK.group(1))) # Debug
         #if debugVerbosity >= 2 and actionHostCHK: notify ('### actionHostCHK: {}'.format(actionHostCHK.group(1))) # Debug
         if (scriptHostCHK or actionHostCHK) and not ((scriptHostCHK and actionHostCHK) and (re.search(r'{}'.format(scriptHostCHK.group(1).upper()),actionHostCHK.group(1)))): continue # If this is a host card
         if ((effectType.group(1) == 'onPlay' and action != 'PLAY') or 
             (effectType.group(1) == 'onParticipation' and action != 'PARTICIPATION') or
             (effectType.group(1) == 'onUnparticipation' and action != 'UNPARTICIPATE') or
             (effectType.group(1) == 'onThwart' and action != 'THWART')):
            debugNotify("Skipping autoS. Not triggered.\n#### EffectType: {}\n#### action = {}".format(effectType.group(1),action)) 
            continue 
         markerModRegex = re.search(r'onMarker(Add|Sub)([A-Za-z]+)', effectType.group(1))
         if markerModRegex:
            debugNotify("got markerModRegex: {}".format(markerModRegex.groups()))
            operation = markerModRegex.group(1)
            markerType = markerModRegex.group(2)
            if 'MARKER' + operation.upper + markerType.upper() != action: 
               debugNotify("{} != {}".format('MARKER' + operation.upper + markerType.upper(), action))
               continue
         if not checkOriginatorRestrictions(autoS,card): continue
         if re.search(r'-isOptional', autoS):
            if not confirm("This card has an optional ability you can activate at this point. Do you want to do so?"): 
               notify("{} opts not to activate {}'s optional ability".format(me,card))
               continue
            else: notify("{} activates {}'s optional ability".format(me,card))
         executeAutoscripts(card,autoS,action = action)
         scriptEffect = 'COMPLETE'
         if re.search(r'-isResolution',autoS): autoscriptOtherPlayers('Resolution',card) # This is used for cards which specifically trigger from Resolution effects.
   debugNotify("About to go check if I'm to go into executeAttachmentScripts()",2) # Debug
   if not re.search(r'HOST-',action): executeAttachmentScripts(card, action) # if the automation we're doing now is not for an attachment, then we check the current card's attachments for more scripts
   debugNotify("<<< executePlayScripts() with scriptEffect = {}".format(scriptEffect))
   reCalculate(notification = 'silent')
   return scriptEffect

#------------------------------------------------------------------------------
# Attached cards triggers
#------------------------------------------------------------------------------

def executeAttachmentScripts(card, action):
   debugNotify(">>> executeEnhancementScripts() with action: {}".format(action)) #Debug
   hostCards = eval(getGlobalVariable('Host Cards'))
   for attachment in hostCards:
      if hostCards[attachment] == card._id:
         executePlayScripts(Card(attachment), 'HOST-' + action)
   debugNotify("<<< executeEnhancementScripts()") # Debug

#------------------------------------------------------------------------------
# Card Use trigger
#------------------------------------------------------------------------------

def useAbility(card, x = 0, y = 0, manual = True): # The start of autoscript activation.
   debugNotify(">>> useAbility(){}".format(extraASDebug())) #Debug
   mute()
   global failedRequirement
   AutoscriptsList = [] # An empty list which we'll put the AutoActions to execute.
   failedRequirement = False # We set it to false when we start a new autoscript.
   if not Automations['Play']:
      whisper(":::WARNING::: Play automations have been deactivated. Aborting!",4)
      return
   Autoscripts = CardsAA.get(card.model,'').split('||')
   AutoScriptSnapshot = list(Autoscripts)
   for autoS in AutoScriptSnapshot: # Checking and removing any clickscripts which were put here in error.
      if not chkDummy(autoS, card): Autoscripts.remove(autoS)
      if re.search(r'-onlyInShootouts',autoS) and getGlobalVariable('Shootout') != 'True': Autoscripts.remove(autoS)
      if re.search(r'-onlyInNoon',autoS) and getGlobalVariable('Shootout') == 'True': Autoscripts.remove(autoS)      
   debugNotify("Removed bad options")
   if len(Autoscripts) == 0:
      whisper("This card has no automated abilities for this phase. Aborting")
      return 
   debugNotify("+++ All checks done!. Starting Choice Parse...",4)
   ### Checking if card has multiple autoscript options and providing choice to player.
   if len(Autoscripts) > 1: 
      #abilConcat = "This card has multiple abilities.\nWhich one would you like to use?\
                #\n\n(Tip: You can put multiple abilities one after the the other (e.g. '110'). Max 9 at once)\n\n" # We start a concat which we use in our confirm window.
      ChoiceTXT = "This card has multiple abilities.\nSelect the one you would like to use and press the [Finish Selection] button"
      choices = card.Instructions.split('||') # A card with multiple abilities on use MUST use the Instructions properties
      choice = SingleChoice(ChoiceTXT, choices, type = 'button', default = 0)
      if choice == None: return
      selectedAutoscript = Autoscripts[choice]
      debugNotify("AutoscriptsList: {}".format(AutoscriptsList)) # Debug
   else: selectedAutoscript = Autoscripts[0]
   debugNotify("selectedAutoscript = {}".format(selectedAutoscript),2)
   debugNotify("About to check for actionCostRegex",2)
   actionCostRegex = re.match(r"GR([0-9]+)B([0-1])R([0-1]):", selectedAutoscript) # Any cost will always be at the start
   # GR is Ghost Rock cost to use the ability
   # B is boot cost
   # R is repeat switch. 0 means no repeat (i.e. only once per turn), 1 means it's a repeat ability (or just a card trait which can be used as many times as its trigger hits)
   if actionCostRegex:
      if (actionCostRegex.group(2) == '1' and card.orientation == Rot0) or actionCostRegex.group(2) == '0' or (actionCostRegex.group(2) == '1' and card.orientation == Rot90 and confirm("Card requires to be booted to use its ability. Bypass?")): # First we check if the card is booted and it needs to boot.
         if actionCostRegex.group(3) == '1' or not card.markers[mdict['UsedAbility']] or (card.markers[mdict['UsedAbility']] and confirm("You've already used {}'s Ability Bypass Restriction?".format(card.name))):
            if payCost(actionCostRegex.group(1), silent) != 'ABORT': 
               if executeAutoscripts(card,selectedAutoscript,action = 'USE') != 'ABORT':
                  if card.group == table: # If the card is still on the table, then we take care of the other costs
                     if actionCostRegex.group(2) == '1':
                        if card.orientation == Rot0: boot(card, silent = True) # If the B cost is 1, card is supposed to boot.
                        else: notify(":::WARN::: {} bypassed requirement to boot {} to use its ability".format(me,card))
                     if actionCostRegex.group(3) == '0':
                        if not card.markers[mdict['UsedAbility']]: card.markers[mdict['UsedAbility']] += 1 # If a card is repeat, we don't put a marker
                        else: notify(":::WARN::: {} bypassed once-per turn restriction on {}'s ability".format(me,card))
                     if re.search(r'-isResolution',selectedAutoscript): autoscriptOtherPlayers('Resolution',card) # This is used for cards which specifically trigger from Resolution effects.
               else:
                  if num(actionCostRegex.group(1)): 
                     #whisper(":::INFO::: Ability aborted. Returning ghost rock cost")
                     me.GhostRock += num(actionCostRegex.group(1))
   else: whisper(":::INFO::: {} has no scripted ability".format(card))
   reCalculate(notification = 'silent')
      
#------------------------------------------------------------------------------
# Other Player trigger
#------------------------------------------------------------------------------
   
def autoscriptOtherPlayers(lookup, origin_card = OutfitCard, count = 1, origin_player = me): # Function that triggers effects based on the opponent's cards.
# This function is called from other functions in order to go through the table and see if other players have any cards which would be activated by it.
# For example a card that would produce credits whenever a trace was attempted. 
   if not Automations['Triggers']: return # If automations have been disabled, do nothing.
   debugNotify(">>> autoscriptOtherPlayers() with lookup: {} and origin_card: {}".format(lookup,origin_card)) #Debug
   for card in table:
      debugNotify(' Checking {}'.format(card)) # Debug
      costText = '{} activates {} to'.format(card.controller, card) 
      Autoscripts = CardsAS.get(card.model,'').split('||')
      debugNotify("{}'s AS: {}".format(card,Autoscripts),4) # Debug
      autoScriptSnapshot = list(Autoscripts)
      for autoS in autoScriptSnapshot: # Checking and removing anything other than whileRezzed or whileScored.
         if not re.search(r'whileInPlay', autoS): Autoscripts.remove(autoS)
      if len(Autoscripts) == 0: continue
      for autoS in Autoscripts:
         debugNotify(' autoS: {}'.format(autoS)) # Debug
         cardTriggerRegex = re.search(r'-foreach([A-Za-z]+)', autoS) # This regex extracts the card's trigger keyword. So if a card says "put1Focus-perCardCaptured", it's trigger word is "CardCaptured".
         if not cardTriggerRegex: continue # If the card does not have a trigger word, it does not have an abilit that's autoscripted by other players.
         debugNotify("cardTriggerRegex Keyword {}".format(cardTriggerRegex.group(1)))
         if not re.search(r'{}'.format(cardTriggerRegex.group(1)), lookup): # Now we look for the trigger keyword, in what kind of trigger is being checked in this instance.
                                                                            # So if our instance's trigger is currently "UnitCardCapturedFromTable" then the trigger word "CardCaptured" is contained within and will match.
            debugNotify("Couldn't lookup the trigger: {} in autoscript. Ignoring".format(lookup),2)
            continue # Search if in the script of the card, the string that was sent to us exists. The sent string is decided by the function calling us, so for example the ProdX() function knows it only needs to send the 'GeneratedSpice' string.
         if re.search(r'-byOpposingOriginController', autoS) and chkPlayer('byOpponent', origin_card.controller,False, player = card.controller) == 0: continue
         # If we have the -byOpposingOriginController modulator, our scripts need to compare the controller of the card that triggered the script with the controller of the card that has the script.
         # See for example Renegade Squadron Mobilization, where we need to check that the controller of the card leaving play is the opponent of the player that controls Renegade Squadron Mobilization
         # If we had let it as it was, it would simply check if Renegade Squadron Mobilization is controlled by the opponent, thus triggering the script each time our opponent's action discarded a unit, even if the unit was ours.
         if re.search(r'-byFriendlyOriginController', autoS) and chkPlayer('byAlly', origin_card.controller,False, player = card.controller) == 0: continue
         if chkPlayer(autoS, card.controller,False, player = origin_player) == 0: continue # Check that the effect's origninator is valid.
         if re.search(r'-ifCapturingObjective', autoS) and capturingObjective != card: continue  # If the card required itself to be the capturing objective, we check it here via a global variable.             
         confirmText = re.search(r'ifConfirm{(A-Za-z0-9)+}', autoS) # If the card contains the modified "ifConfirm{some text}" then we present "some text" as a question before proceeding.
                                                                    # This is different from -isOptional in order to be able to trigger abilities we cannot automate otherwise.
         if confirmText and not confirm(confirmText.group(1)): continue
         edgeDiffRegex = re.search(r'ifEdgeDiff(ge|le|eq)([0-9])', autoS) # If the card is expecting a specific Edge Difference, it should have been passed via the count above.
         if edgeDiffRegex:
            if edgeDiffRegex.group(1) == 'ge' and count < num(edgeDiffRegex.group(2)): 
               debugNotify("!!! Failing because Edge Difference ({}) less than {}".format(count,edgeDiffRegex.group(2)),2)
               continue
            if edgeDiffRegex.group(1) == 'le' and count > num(edgeDiffRegex.group(2)): 
               debugNotify("!!! Failing because Edge Difference ({}) more than {}".format(count,edgeDiffRegex.group(2)),2)
               continue
            if edgeDiffRegex.group(1) == 'eq' and count != num(edgeDiffRegex.group(2)): 
               debugNotify("!!! Failing because Edge Difference ({}) not equal to {}".format(count,edgeDiffRegex.group(2)),2)
               continue
         if not chkDummy(autoS, card): continue
         if not checkCardRestrictions(gatherCardProperties(origin_card), prepareRestrictions(autoS,'type')): continue #If we have the '-type' modulator in the script, then need ot check what type of property it's looking for
         else: debugNotify("Not Looking for specific type or type specified found.")
         if not checkOriginatorRestrictions(autoS,card): continue
         debugNotify("Automatic Autoscripts: {}".format(autoS)) # Debug
         if re.search(r'onTriggerCard',autoS): 
            debugNotify("Target Card is the origin card",2)
            targetCardID = origin_card._id # if we have the "-onTriggerCard" modulator, then the target of the script will be the original card
         else: targetCardID = None
         if re.search(r'-isReact', autoS): #If the effect -isReact, then the opponent has a chance to interrupt so we need to give them a window.
            if card.highlight != ReadyEffectColor:
               ### Setting card's selectedAbility Global Variable.
               storeCardEffects(card,autoS,0,card.highlight,'Automatic',targetCardID,count) # We pass the special target's ID in our global variable to allow it to be retrieved by later scripts.
               if re.search(r'-isForced', autoS): readyEffect(card,True)
               else: readyEffect(card)
            continue
         ### Otherwise the automation is uninterruptible and we just go on with the scripting.
         if targetCardID: executeAutoscripts(card,autoS,count,action = 'Automatic',targetCards = [Card(targetCardID)])
         else: executeAutoscripts(card,autoS,count,action = 'Automatic')
   debugNotify("<<< autoscriptOtherPlayers()") # Debug

#------------------------------------------------------------------------------
# Start/End of Turn/Phase trigger
#------------------------------------------------------------------------------
   
def atTimedEffects(Time = 'Start'): # Function which triggers card effects at the start or end of the turn.
   mute()
   global TitleDone
   debugNotify(">>> atTimedEffects() at time: {}".format(Time)) #Debug
   if not Automations['Triggers']: 
      if Time == 'Start': delayed_whisper(":::WARNING::: Your trigger automations have been deactivated.")
      return
   TitleDone = False
   X = 0
   for card in table:
      debugNotify("Checking card: {}".format(card),4)
      if not card.isFaceUp: 
         debugNotify("Card is face down. Ignoring",3)
         continue
      Autoscripts = CardsAS.get(card.model,'').split('||')
      for autoS in Autoscripts:
         debugNotify("Processing {} Autoscript: {}".format(card, autoS))
         effect = re.search(r'atPhase(Gamblin|Upkeep|High Noon|Sundown|ShootoutStart|ShootoutEnd):(.*)', autoS) #Putting the phase in a group to compare with the Time variable later
         if not effect: continue
         debugNotify("Time Regex fits. Script triggers on: {}".format(effect.group(1)))
         if chkPlayer(effect.group(2), card.controller,False) == 0: continue # Check that the effect's origninator is valid. 
         if effect.group(1) != Time:
            debugNotify("Time didn't match!")
            continue 
         # If the effect trigger we're checking (e.g. gamblin) does not match the phase trigger we're in (e.g. upkeep)
         if debugVerbosity >= 2 and effect: notify("!!! effects: {}".format(effect.groups()))
         if not chkDummy(autoS, card): continue
         if not checkOriginatorRestrictions(autoS,card): continue
         if re.search(r'isOptional', effect.group(2)):
            debugNotify("Checking Optional Effect")
            extraCountersTXT = '' 
            for cmarker in card.markers: # If the card has any markers, we mention them do that the player can better decide which one they wanted to use (e.g. multiple bank jobs)
               extraCountersTXT += " {}x {}\n".format(card.markers[cmarker],cmarker[0])
            if extraCountersTXT != '': extraCountersTXT = "\n\nThis card has the following counters on it\n" + extraCountersTXT
            if not confirm("{} can have its optional ability take effect at this point. Do you want to activate it?{}".format(card.name),extraCountersTXT): continue 
         executeAutoscripts(card,autoS,action = Time)
   markerEffects(Time) 
   if TitleDone: notify(":::{:=^30}:::".format('='))
   TitleDone = 'Unset' # We set it to a special string so that it's never used unless we start this function anew.
   debugNotify("<<< atTimedEffects()") # Debug
               

   
   
#------------------------------------------------------------------------------
# Redirect to Core Commands
#------------------------------------------------------------------------------
def executeAutoscripts(card,Autoscript,count = 0,action = 'PLAY',targetCards = None):
   debugNotify(">>> executeAutoscripts(){}".format(extraASDebug(Autoscript))) #Debug
   #confirm("card = {}, count = {}, action = {}, targetCards = {}".format(card,count,action,targetCards))
   global failedRequirement
   failedRequirement = False
   X = count # The X Starts as the "count" passed variable which sometimes may need to be passed.
   selectedAutoscripts = Autoscript.split('$$')
   if debugVerbosity >= 2: notify ('selectedAutoscripts: {}'.format(selectedAutoscripts)) # Debug
   if re.search(r'CustomScript', Autoscript):  
      return CustomScript(card,action) # If it's a customscript, we don't need to try and split it and it has its own checks.
   else: 
      for passedScript in selectedAutoscripts: 
         if chkWarn(card, passedScript) == 'ABORT': return 'ABORT'
         if chkPlayer(passedScript, card.controller,False) == 0: continue
         if re.search(r'-ifHaveForce', passedScript) and not haveForce(): 
            debugNotify("Rejected -ifHaveForce script")
            continue
         if re.search(r'-ifHaventForce', passedScript) and haveForce(): 
            debugNotify("Rejected -ifHaventForce script")
            continue         
         X = redirect(passedScript, card, action, X,targetCards)
         if failedRequirement or X == 'ABORT': return 'ABORT' # If one of the Autoscripts was a cost that couldn't be paid, stop everything else.

def redirect(Autoscript, card, action, X = 0,targetC = None):
   debugNotify(">>> redirect(){}".format(Autoscript)) #Debug
   global TitleDone
   if re.search(r':Pass\b', Autoscript): return X # Pass is a simple command of doing nothing ^_^. We put it first to avoid checking for targets and so on
   if not targetC: targetC = findTarget(Autoscript,card = card)
   if not TitleDone and not (len(targetC) == 0 and re.search(r'AutoTargeted',Autoscript)): # We don't want to put a title if we have a card effect that activates only if we have some valid targets (e.g. Admiral Motti)
      Phase = re.search(r'after([A-za-z]+)',action)
      if Phase: title = "{}'s Post-{} Effects".format(me,Phase.group(1))
      else: title = "{}'s {}-of-Turn Effects".format(me,action)
      notify("{:=^36}".format(title))
      TitleDone = True
   debugNotify("card.owner = {}".format(card.owner),2)
   actionCostRegex = re.match(r"GR([0-9]+)B([0-1])R([0-1]):", Autoscript) # We check the costs to put out the correct announcements
   if actionCostRegex:
      if num(actionCostRegex.group(1)) and actionCostRegex.group(2) == '1': announceText = "{} pays {} and boots {} to".format(card.controller,actionCostRegex.group(1),card)
      elif num(actionCostRegex.group(1)) and actionCostRegex.group(2) == '0': announceText = "{} pays {} for {} to".format(card.controller,actionCostRegex.group(1),card)
      elif not num(actionCostRegex.group(1)) and actionCostRegex.group(2) == '1': announceText = "{} boots {} to".format(card.controller,card)
      else: announceText = "{} uses {}'s ability to".format(card.controller,card)
   elif action == 'Quick': announceText = "{} uses {}'s ability to".format(card.controller,card) 
   elif card.highlight == DummyColor: announceText = "{}'s lingering effects:".format(card)
   else: announceText = "{} uses {} to".format(card.controller,card)
   debugNotify("targetC: {}. Notification Type = {}".format([c.name for c in targetC],'Quick'), 3) # Debug   
   if regexHooks['GainX'].search(Autoscript):
      debugNotify("in GainX hook")
      gainTuple = GainX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X)
      if gainTuple == 'ABORT': return 'ABORT'
      X = gainTuple[1] 
   if regexHooks['CreateDummy'].search(Autoscript): 
      debugNotify("in CreateDummy hook")
      if CreateDummy(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['DrawX'].search(Autoscript): 
      debugNotify("in DrawX hook")
      if DrawX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['RetrieveX'].search(Autoscript): 
      debugNotify("in RetrieveX hook")
      if RetrieveX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['TokensX'].search(Autoscript): 
      debugNotify("in TokensX hook")
      if TokensX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['RollX'].search(Autoscript): 
      debugNotify("in RollX hook")
      rollTuple = RollX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X)
      if rollTuple == 'ABORT': return 'ABORT'
      X = rollTuple[1] 
   elif regexHooks['RequestInt'].search(Autoscript): 
      debugNotify("in RequestInt hook")
      numberTuple = RequestInt(Autoscript, announceText, card, targetC, notification = 'Quick', n = X)
      if numberTuple == 'ABORT': return 'ABORT'
      X = numberTuple[1] 
   elif regexHooks['DiscardX'].search(Autoscript): 
      debugNotify("in DiscardX hook")
      discardTuple = DiscardX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X)
      if discardTuple == 'ABORT': return 'ABORT'
      X = discardTuple[1] 
   elif regexHooks['ReshuffleX'].search(Autoscript): 
      debugNotify("in ReshuffleX hook")
      reshuffleTuple = ReshuffleX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X)
      if reshuffleTuple == 'ABORT': return 'ABORT'
      X = reshuffleTuple[1]
   elif regexHooks['ShuffleX'].search(Autoscript): 
      debugNotify("in ShuffleX hook")
      if ShuffleX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['ChooseKeyword'].search(Autoscript): 
      debugNotify("in ChooseKeyword hook")
      if ChooseKeyword(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['SpawnX'].search(Autoscript): 
      debugNotify("in SpawnX hook")
      if SpawnX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['ModifyStatus'].search(Autoscript): 
      debugNotify("in ModifyStatus hook")
      if ModifyStatus(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['GameX'].search(Autoscript): 
      debugNotify("in GameX hook")
      if GameX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['UseCustomAbility'].search(Autoscript): 
      debugNotify("in UseCustomAbility hook")
      if UseCustomAbility(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['SimplyAnnounce'].search(Autoscript): 
      debugNotify("in SimplyAnnounce hook")
      if SimplyAnnounce(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['StartJob'].search(Autoscript): 
      debugNotify("in StartJob hook")
      if StartJob(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   elif regexHooks['PullX'].search(Autoscript): 
      debugNotify("in PullX hook")
      if PullX(Autoscript, announceText, card, targetC, notification = 'Quick', n = X) == 'ABORT': return 'ABORT'
   else: debugNotify("No regexhook match! :(") # Debug
   debugNotify("Loop for scipt {} finished".format(Autoscript), 2)
   return X # If all went well,we return the X.

#------------------------------------------------------------------------------
# Core Commands
#------------------------------------------------------------------------------
   
def GainX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0, actionType = 'USE'): # Core Command for modifying counters or global variables
   debugNotify(">>> GainX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   gain = 0
   action = re.search(r'\b(Gain|Lose|SetTo)([0-9]+)([A-Z][A-Za-z &]+)-?', Autoscript)
   debugNotify("action groups: {}. Autoscript: {}".format(action.groups(0),Autoscript)) # Debug
   gain += num(action.group(2))
   targetPLs = ofwhom(Autoscript, card.controller)
   if len(targetPLs) > 1 or targetPLs[0] != me: otherTXT = ' force {} to'.format([targetPL.name for targetPL in targetPLs])
   else: otherTXT = ''
   for targetPL in targetPLs:
      multiplier = per(Autoscript, card, n, targetCards) # We check if the card provides a gain based on something else, such as favour bought, or number of dune fiefs controlled by rivals.
      if action.group(1) == 'Lose': gain *= -1 
      debugNotify("GainX() after per",3) # Debug
      if re.match(r'Ghost Rock', action.group(3)): 
         if action.group(1) == 'SetTo': targetPL.counters['GhostRock'].value = 0 # If we're setting to a specific value, we wipe what it's currently.
         targetPL.counters['GhostRock'].value += gain * multiplier
         if targetPL.counters['GhostRock'].value < 0 and not re.search(r'isCost', Autoscript): targetPL.counters['GhostRock'].value = 0 # If it's a cost, then we can fall below 0 to show they didn't have enough to pay
      else: 
         whisper("Gain what?! (Bad autoscript)")
         return 'ABORT'
   debugNotify("<<< Gainx() Finished counter manipulation")
   if action.group(1) == 'Gain': # Since the verb is in the middle of the sentence, we want it lowercase. 
      verb = 'gain'
   elif action.group(1) == 'Lose': 
      if re.search(r'isCost', Autoscript): verb = 'pay'
      else: verb = 'lose'
   else: verb = 'set to'
   debugNotify("<<< Gainx() Finished preparing verb ({}). Notification was: {}".format(verb,notification))
   if abs(gain) == abs(999): total = 'all' # If we have +/-999 as the count, then this mean "all" of the particular counter.
   else: total = abs(gain * multiplier) # Else it's just the absolute value which we announce they "gain" or "lose"
   closureTXT = "{} {}".format(total, action.group(3))
   debugNotify("<<< Gainx() about to announce")
   if notification == 'Quick': announceString = "{}{} {} {}".format(announceText, otherTXT, verb, closureTXT)
   else: announceString = "{}{} {} {}".format(announceText, otherTXT, verb, closureTXT)
   if notification and multiplier > 0: notify(':> {}.'.format(announceString))
   debugNotify("<<< Gain() total: {}".format(total))
   return (announceString,total)
   
def TokensX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for adding tokens to cards
   debugNotify(">>> TokensX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   if re.search(r'atHost', Autoscript):
      hostCards = eval(getGlobalVariable('Host Cards'))
      for attachment in hostCards: # We check out attachments dictionary to find out who this card's host is.
         if attachment == card._id: targetCards.append(Card(hostCards[attachment]))
   if len(targetCards) == 0:
      if re.search(r'AutoTargeted',Autoscript): 
         if re.search(r'isCost', Autoscript): return 'ABORT' # If removing a token is an actual cost, then we abort the rest of the script
         else: return announceText # Otherwise we continue with the rest of the script if we only need an automatic target but have no valid one
      else: #Otherwise we just put it on ourself and assume the player forgot to target first. They can move the marker manually if they need to.
         targetCards.append(card) # If there's been to target card given, assume the target is the card itself.
         targetCardlist = ' on it' 
   else:
      targetCardlist = ' on' # A text field holding which cards are going to get tokens.
      for targetCard in targetCards:
         targetCardlist += ' {},'.format(targetCard)
   foundKey = False # We use this to see if the marker used in the AutoAction is already defined.
   action = re.search(r'\b(Put|Remove|Refill|Use|Transfer)([0-9]+)([\w: ]+)-?', Autoscript)
   debugNotify("action Regex = {}".format(action.groups()),3)
   if action.group(3) in mdict: token = mdict[action.group(3)]
   else: # If the marker we're looking for it not defined, then either create a new one with a random color, or look for a token with the custom name we used above.
      if targetCards[0].markers:
         for key in targetCards[0].markers:
            if key[0] == action.group(3):
               foundKey = True
               token = key
      if not foundKey: # If no key is found with the name we seek, then create a new one with a random colour.
         #counterIcon = re.search(r'-counterIcon{([A-Za-z]+)}', Autoscript) # Not possible at the moment
         #if counterIcon and counterIcon.group(1) == 'plusOne':             # See https://github.com/kellyelton/OCTGN/issues/446
         #   token = ("{}".format(action.group(3)),"aa261722-e12a-41d4-a475-3cc1043166a7")         
         #else:
         rndGUID = rnd(1,8)
         token = ("{}".format(action.group(3)),"00000000-0000-0000-0000-00000000000{}".format(rndGUID)) #This GUID is one of the builtin ones
   count = num(action.group(2))
   multiplier = per(Autoscript, card, n, targetCards, notification)
   debugNotify("About to check type of module for {}".format(action.group(1)),3)
   if action.group(1) == 'Transfer':
      debugNotify("In transfer module",2)
      if len(targetCards) != 2:
         delayed_whisper(":::ERROR::: You must target exactly 2 valid cards to use this ability.")
         return 'ABORT'
      completedSeek = False
      while not completedSeek:
         if re.search(r'-sourceAny',Autoscript): 
            sourceRegex = re.search(r'-sourceAny-(.*?)-destination',Autoscript)
            sourceTargets = findTarget('Targeted-{}'.format(sourceRegex.group(1)))
         else:
            sourceRegex = re.search(r'-source(.*?)-destination',Autoscript)
            sourceTargets = findTarget('Targeted-at{}'.format(sourceRegex.group(1)))
         debugNotify("sourceRegex = {}".format(sourceRegex.groups()),2)
         if len(sourceTargets) == 0:
            delayed_whisper(":::ERROR::: No valid source card targeted.")
            return 'ABORT'
         elif len(sourceTargets) > 1:
            targetChoices = makeChoiceListfromCardList(sourceTargets)
            choiceC = SingleChoice("Choose from which card to remove the token", targetChoices, type = 'button', default = 0)
            if choiceC == 'ABORT': return 'ABORT'
            debugNotify("choiceC = {}".format(choiceC),4) # Debug
            sourceCard = sourceTargets.pop(choiceC)
         else: sourceCard = sourceTargets[0]
         debugNotify("sourceCard = {}".format(sourceCard)) # Debug
         if re.search(r'-destinationAny',Autoscript): 
            destRegex = re.search(r'-destinationAny-(.*)',Autoscript)
            destTargets = findTarget('Targeted-{}'.format(destRegex.group(1)))
         else:
            destRegex = re.search(r'-destination(.*)',Autoscript)
            destTargets = findTarget('Targeted-at{}'.format(destRegex.group(1)))
         debugNotify("destRegex = {}".format(destRegex.groups()),2)
         if sourceCard in destTargets: destTargets.remove(sourceCard) # If the source card is targeted and also a valid destination, we remove it from the choices list.
         if len(destTargets) == 0:
            if not confirm("Your choices have left you without a valid destination to transfer the token. Try again?"): return 'ABORT'
            else: continue
         completedSeek = True #If we have a valid source and destination card, then we can exit the loop
         targetCard = destTargets[0] # After we pop() the choice card, whatever remains is the target card.
         debugNotify("targetCard = {}".format(targetCard)) # Debug
      if count == 999: modtokens = sourceCard.markers[token] # 999 means move all tokens from one card to the other.
      else: modtokens = count * multiplier
      debugNotify("About to check if it's a basic token to remove")
      sourceCard.markers[token] -= modtokens
      targetCard.markers[token] += modtokens
      notify("{} has moved one focus token from {} to {}".format(card,sourceCard,targetCard))
   else:
      debugNotify("In normal tokens module")
      for targetCard in targetCards:
         if action.group(1) == 'Put':
            if re.search(r'isCost', Autoscript) and targetCard.markers[token] and targetCard.markers[token] > 0 and not confirm(":::ERROR::: This card already has a {} marker on it. Proceed anyway?".format(token[0])):
               return 'ABORT'
            else: modtokens = count * multiplier
         elif action.group(1) == 'Refill': modtokens = count - targetCard.markers[token]
         elif action.group(1) == 'USE':
            if not targetCard.markers[token] or count > targetCard.markers[token]: 
               whisper("There's not enough counters left on the card to use this ability!")
               return 'ABORT'
            else: modtokens = -count * multiplier
         else: #Last option is for removing tokens.
            debugNotify("About to remove tokens",3)
            if count == 999: # 999 effectively means "all markers on card"
               if targetCard.markers[token]: count = targetCard.markers[token]
               else: 
                  if not re.search(r'isSilent', Autoscript): whisper("There was nothing to remove.")
                  count = 0
            elif re.search(r'isCost', Autoscript) and (not targetCard.markers[token] or (targetCard.markers[token] and count > targetCard.markers[token])):
               if notification != 'Automatic': whisper ("No enough markers to remove. Aborting!") #Some end of turn effect put a special counter and then remove it so that they only run for one turn. This avoids us announcing that it doesn't have markers every turn.
               debugNotify("Not enough markers to remove as cost. Aborting",2)
               return 'ABORT'
            elif not targetCard.markers[token]:
               if not re.search(r'isSilent', Autoscript): whisper("There was nothing to remove.")
               debugNotify("Found no {} tokens to remove".format(token[0]),2)
               count = 0 # If we don't have any markers, we have obviously nothing to remove.
            modtokens = -count * multiplier
         debugNotify("About to check if it's a basic token to remove")
         if token == mdict['BulletShootoutPlus']: plusBulletShootout(targetCard,count = modtokens) # We use the existing functions, because they also remove conflicting markers
         elif token == mdict['BulletShootoutMinus']: minusBulletShootout(targetCard,silent = True, count = modtokens)
         elif token == mdict['BulletNoonPlus']: plusBulletNoon(targetCard,silent = True,count = modtokens)
         elif token == mdict['BulletNoonMinus']: minusBulletNoon(targetCard,silent = True,count = modtokens)
         elif token == mdict['PermBulletPlus']: plusPermBullet(targetCard,silent = True,count = modtokens)
         elif token == mdict['PermBulletMinus']: minusPermBullet(targetCard,silent = True,count = modtokens)
         elif token == mdict['InfluencePlus']: plusInfluence(targetCard,silent = True,count = modtokens)
         elif token == mdict['InfluenceMinus']: minusInfluence(targetCard,silent = True,count = modtokens)
         elif token == mdict['PermInfluencePlus']: plusPermInfluence(targetCard,silent = True,count = modtokens)
         elif token == mdict['PermInfluenceMinus']: minusPermInfluence(targetCard,silent = True,count = modtokens)
         elif token == mdict['ControlPlus']: plusControl(targetCard,silent = True,count = modtokens)
         elif token == mdict['ControlMinus']: minusControl(targetCard,silent = True,count = modtokens)
         elif token == mdict['PermControlPlus']: plusPermControl(targetCard,silent = True,count = modtokens)
         elif token == mdict['PermControlMinus']: minusPermControl(targetCard,silent = True,count = modtokens)
         elif token == mdict['ValueNoonPlus']: plusValue(targetCard,silent = True,valuemod = modtokens)
         elif token == mdict['ValueNoonMinus']: minusValue(targetCard,silent = True,valuemod = modtokens)
         elif token == mdict['ValuePermPlus']: plusPermValue(targetCard,silent = True,valuemod = modtokens)
         elif token == mdict['ValuePermMinus']: minusPermValue(targetCard,silent = True,valuemod = modtokens)
         elif token == mdict['ProdPlus']: modProd(targetCard,silent = True,count = modtokens)
         elif token == mdict['ProdMinus']: modProd(targetCard,silent = True,count = -modtokens)
         else: targetCard.markers[token] += modtokens # Finally we apply the marker modification
   if abs(num(action.group(2))) == abs(999): total = 'all'
   else: total = abs(modtokens)
   if re.search(r'isPriority', Autoscript): card.highlight = PriorityColor
   countersTXT = 'counters'
   debugNotify("About to set announceString",2)
   if action.group(1) == 'Transfer': announceString = "{} {} {} {} {} from {} to {}".format(announceText, action.group(1).lower(), total, token[0],countersTXT,sourceCard,targetCard)
   else: announceString = "{} {} {} {} {}{}".format(announceText, action.group(1).lower(), total, token[0],countersTXT,targetCardlist)
   debugNotify("About to Announce",2)
   if notification and modtokens != 0 and not re.search(r'isSilent', Autoscript): notify(':> {}.'.format(announceString))
   debugNotify("<<< TokensX() String: {}".format(announceString)) #Debug
   debugNotify("<<< TokensX()")
   if re.search(r'isSilent', Autoscript): return announceText # If it's a silent marker, we don't want to announce anything. Returning the original announceText will be processed by any receiving function as having done nothing.
   else: return announceString
 
def DrawX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for drawing X Cards from the house deck to your hand.
   debugNotify(">>> DrawX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   destiVerb = 'draw'
   action = re.search(r'\bDraw([0-9]+)Card', Autoscript)
   targetPLs = ofwhom(Autoscript, card.controller)
   if len(targetPLs) > 1 or targetPLs[0] != me: otherTXT = ' force {} to'.format([targetPL.name for targetPL in targetPLs])
   else: otherTXT = ''
   if len(targetPLs) > 1 or targetPLs[0] != me: destiVerb = 'move'
   for targetPL in targetPLs:
      debugNotify("Setting Source")
      if re.search(r'-fromDiscard', Autoscript):
         source = targetPL.piles['Discard Pile']
         sourcePath =  " from their Discard Pile"
      else: 
         source = targetPL.piles['Deck']
         sourcePath =  ""
      debugNotify("Setting Destination")
      if re.search(r'-toDeck', Autoscript): 
         destination = targetPL.piles['Deck']
         destiVerb = 'move'
      elif re.search(r'-toDiscard', Autoscript):
         destination = targetPL.piles['Discard Pile']
         destiVerb = 'discard'   
      else: destination = targetPL.hand
      preventDraw = False
      if source == targetPL.piles['Deck'] and destination == targetPL.hand: # We need to look if there's card on the table which prevent card draws.
         debugNotify("About to check for Draw Prevention",2)
         for c in table:
            if preventDraw: break #If we already found a card effect which prevents draws, don't check any more cards on the table.
            Autoscripts = CardsAS.get(c.model,'').split('||')
            for autoS in Autoscripts:
               debugNotify("Checking autoS {}".format(autoS),2)
               if re.search(r'\bPreventDraw', autoS) and chkPlayer(autoS,targetPL,False) and checkOriginatorRestrictions(autoS,c):
                  preventDraw = True
                  notify(":> {}'s {} draw effects were blocked by {}".format(card.controller,card,c))
      if not preventDraw:
         debugNotify("Card Draw not prevented")
         draw = num(action.group(1))
         if draw == 999:
            multiplier = 1
            if targetPL.Reserves >= len(targetPL.hand): # Otherwise drawMany() is going to try and draw "-1" cards which somehow draws our whole deck except one card.
               count = drawMany(source, targetPL.Reserves - len(targetPL.hand), destination, True) # 999 means we refresh our hand
            else: count = 0 
            #confirm("cards drawn: {}".format(count)) # Debug
         else: # Any other number just draws as many cards.
            multiplier = per(Autoscript, card, n, targetCards, notification)
            count = drawMany(source, draw * multiplier, destination, True)
         if destiVerb != 'discard': destPath = " to their {}".format(destination.name)
         else: destPath = ''
      else: count = 0
   debugNotify("About to announce.")
   #if count == 0: return announceText # If there are no cards, then we effectively did nothing, so we don't change the notification.
   if notification == 'Quick': announceString = "{} draw {} cards{}".format(announceText, action.group(1),sourcePath)
   elif source.name == 'Deck' and destination.name == 'Hand': announceString = "{}{} draw {} cards.".format(announceText, otherTXT, action.group(1))
   else: announceString = "{}{} {} cards from {}{}".format(announceText,otherTXT, destiVerb, action.group(1), source.name, destPath)
   if notification and multiplier > 0: notify(':> {}.'.format(announceString))
   debugNotify("<<< DrawX()")
   return announceString

def DiscardX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for drawing X Cards from the house deck to your hand.
   debugNotify(">>> DiscardX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   action = re.search(r'\bDiscard([0-9]+)Card', Autoscript)
   targetPLs = ofwhom(Autoscript, card.controller)
   if len(targetPLs) > 1 or targetPLs[0] != me: otherTXT = ' force {} to'.format([targetPL.name for targetPL in targetPLs])
   else: otherTXT = ''
   for targetPL in targetPLs:
      discardNR = num(action.group(1))
      if discardNR == 999:
         multiplier = 1
         discardNR = len(targetPL.hand) # 999 means we discard our whole hand
      if re.search(r'-isRandom',Autoscript): # the -isRandom modulator just discard as many cards at random.
         multiplier = per(Autoscript, card, n, targetCards, notification)
         count = handRandomDiscard(targetPL.hand, discardNR * multiplier, targetPL, silent = True)
         if re.search(r'isCost', Autoscript) and count < discardNR:
            whisper("You do not have enough cards in your hand to discard")
            return ('ABORT',0)
      else: # Otherwise we just discard the targeted cards from hand  
         multiplier = 1
         count = len(targetCards)
         if re.search(r'isCost', Autoscript) and count < discardNR:
            whisper("You do not have enough cards in your hand to discard")
            return ('ABORT',0)
         for targetC in targetCards: handDiscard(targetC)
         debugNotify("Finished discarding targeted cards from hand")
      if count == 0: 
         debugNotify("Exiting because count == 0")
         return (announceText,count) # If there are no cards, then we effectively did nothing, so we don't change the notification.
   if notification == 'Quick': announceString = "{}{} discard {} cards".format(announceText,otherTXT, count)
   else: announceString = "{}{} discard {} cards from their hand".format(announceText,otherTXT, count)
   if notification and multiplier > 0: notify(':> {}.'.format(announceString))
   debugNotify("<<< DiscardX()")
   return (announceString,count)
         
def ReshuffleX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # A Core Command for reshuffling a pile into the R&D/Stack
   debugNotify(">>> ReshuffleX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   mute()
   X = 0
   action = re.search(r'\bReshuffle([A-Za-z& ]+)', Autoscript)
   debugNotify("!!! regex: {}".format(action.groups())) # Debug
   targetPLs = ofwhom(Autoscript, card.controller)
   if len(targetPLs) > 1 or targetPLs[0] != me: otherTXT = ' force {} to'.format([targetPL.name for targetPL in targetPLs])
   else: otherTXT = ''
   for targetPL in targetPLs:
      if action.group(1) == 'Hand':
         namestuple = groupToDeck(targetPL.hand, targetPL , True) # We do a silent hand reshuffle into the deck, which returns a tuple
         X += namestuple[2] # The 3rd part of the tuple is how many cards were in our hand before it got shuffled.
      elif action.group(1) == 'Discard': 
         namestuple = groupToDeck(targetPL.piles['Discard Pile'], targetPL, True)    
         X += namestuple[2] 
      else: 
         whisper("Wat Group? [Error in autoscript!]")
         return 'ABORT'
      shuffle(targetPL.piles['Deck'])
   if notification == 'Quick': announceString = "{}{} shuffle their {} into their {}".format(announceText, otherTXT, namestuple[0], namestuple[1])
   else: announceString = "{}{} shuffle their {} into their {}".format(announceText,otherTXT, namestuple[0], namestuple[1])
   if notification: notify(':> {}.'.format(announceString))
   debugNotify("<<< ReshuffleX() return with X = {}".format(X))
   return (announceString, X)

def ShuffleX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # A Core Command for reshuffling a pile into the R&D/Stack
   debugNotify(">>> ShuffleX(){}".format(extraASDebug())) #Debug
   if targetCards is None: targetCards = []
   mute()
   action = re.search(r'\bShuffle([A-Za-z& ]+)', Autoscript)
   targetPLs = ofwhom(Autoscript, card.controller)
   if len(targetPLs) > 1 or targetPLs[0] != me: otherTXT = ' force {} to'.format([targetPL.name for targetPL in targetPLs])
   else: otherTXT = ''
   for targetPL in targetPLs: 
      if action.group(1) == 'Discard': pile = targetPL.piles['Discard Pile']
      elif action.group(1) == 'Deck': pile = targetPL.piles['Deck']
      random = rnd(10,100) # Small wait (bug workaround) to make sure all animations are done.
      shuffle(pile)
   announceString = "{}{} shuffle their {}".format(announceText,otherTXT, pile.name)
   if notification: notify(':> {}.'.format(announceString))
   debugNotify("<<< ShuffleX()")
   return announceString
   
def RollX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for drawing X Cards from the house deck to your hand.
   debugNotify(">>> RollX(){}".format(extraASDebug())) #Debug
   if targetCards is None: targetCards = []
   d6 = 0
   d6list = []
   result = 0
   action = re.search(r'\bRoll([0-9]+)Dice(-chk)?([1-6])?', Autoscript)
   multiplier = per(Autoscript, card, n, targetCards, notification)
   count = num(action.group(1)) * multiplier 
   for d in range(count):
      if d == 2: whisper("-- Please wait. Rolling {} dice...".format(count))
      if d == 8: whisper("-- A little while longer...")
      d6 = rolld6(silent = True)
      d6list.append(d6)
      if action.group(3): # If we have a chk modulator, it means we only increase our total if we hit a specific number.
         if num(action.group(3)) == d6: result += 1
      else: result += d6 # Otherwise we add all totals together.
      debugNotify("iter:{} with roll {} and total result: {}".format(d,d6,result))
   if notification == 'Quick': announceString = "{} rolls {} on {} dice".format(announceText, d6list, count)
   else: announceString = "{} roll {} dice with the following results: {}".format(announceText,count, d6list)
   if notification: notify(':> {}.'.format(announceString))
   debugNotify("<<< RollX() with result: {}".format(result))
   return (announceString, result)

def StartJob(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for starting a job
   debugNotify(">>> StartJob(){}".format(extraASDebug())) #Debug
   if targetCards is None: targetCards = []
   if not len(targetCards): return 'ABORT'
   action = re.search(r'\bStartJob', Autoscript)
   mark = None
   leader = None
   posse = []
   for c in targetCards:
      if c.Type != 'Dude': mark = c
   if not mark:
      for c in targetCards:
         if c.controller != me: mark = c
   if not mark:
      if len(targetCards) == 1: mark = targetCards[0]
      else:
         choice = SingleChoice('Choose one of your targeted dudes as the mark', makeChoiceListfromCardList(targetCards))
         if choice == None: return 'ABORT'
         mark = targetCards.pop(choice)
   if card.Type == 'Dude': 
      leader = card
      posse = [c for c in table
               if c.Type == 'Dude'
               and c.controller == me
               and c.orientation == Rot0
               and c.targetedBy and c.targetedBy == me
               and c != mark]
   else:
      targetedDudes = [c for c in table
                       if c.Type == 'Dude'
                       and c.controller == me
                       and c.orientation == Rot0
                       and c.targetedBy and c.targetedBy == me
                       and c != mark]
      if len(targetedDudes) == 1: leader = targetedDudes[0]
      elif len(targetedDudes) > 1:
         choice = SingleChoice('Choose one of your targeted dudes to lead this job\n\n(the rest will be marked as being in your posse)', makeChoiceListfromCardList(targetedDudes))  
         if choice == None: return 'ABORT'
         else: leader = targetedDudes.pop(choice)
         posse = targetedDudes
      else:
         availableDudes = [c for c in table
                          if c.Type == 'Dude'
                          and c.controller == me
                          and c.orientation == Rot0
                          and c != mark]
         if len(availableDudes) == 1: leader = availableDudes[0]
         elif len(availableDudes) > 1:
            choice = SingleChoice("Choose one of your available dudes to lead this job\n\n(You will need to double click any other dude you'd like to join manually)", makeChoiceListfromCardList(availableDudes))
            if choice == None: return 'ABORT'
            else: leader = availableDudes.pop(choice)
   leader.highlight = InitiateColor
   executePlayScripts(leader, 'PARTICIPATION')
   if re.search(r'bootLeader', Autoscript): leader.orientation = Rot90
   if re.search(r'bountyLeader', Autoscript) or re.search(r'bountyPosse', Autoscript): modBounty(leader)
   if len(posse):
      for c in posse: 
         c.highlight = InitiateColor
         if re.search(r'bountyPosse', Autoscript): modBounty(c)
         executePlayScripts(c, 'PARTICIPATION')
      posseTXT = " and {} are also in their posse".format([c.name for c in posse])
   else: posseTXT = ''
   setGlobalVariable('Mark',str(mark._id))
   jobEffects = re.search(r'-jobEffects<(.*?),(.*?)>', Autoscript)
   if jobEffects: setGlobalVariable('Job Active',str((card._id,jobEffects.group(1),jobEffects.group(2)))) # We store the success and fail clause of the job as a tuple. We then retrieve it later.
   else: setGlobalVariable('Job Active','True')
   if notification == 'Quick': announceString = "{} start a job marking {}. {} is leading{}.".format(announceText, mark, leader,posseTXT)
   else: announceString = "{} start a job marking {}. {} is leading{}.".format(announceText, mark, leader,posseTXT)
   if notification: notify(':> {}.'.format(announceString))
   debugNotify("<<< StartJob()")
   return announceString

def PullX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for drawing X Cards from the house deck to your hand.
   debugNotify(">>> DrawX(){}".format(extraASDebug(Autoscript))) #Debug
   rank = None
   suit = None
   if targetCards is None: targetCards = []
   action = re.search(r'\bPull([0-9]+)Card', Autoscript)
   targetPLs = ofwhom(Autoscript, card.controller)
   announceString = "{} pull".format(announceText)
   for targetPL in targetPLs:
      for iter in range(num(action.group(1))):
         if targetPL == me: 
            rank,suit = pull(silent = True)
            if iter == 0: announceString += " a {} {}".format(fullrank(rank), fullsuit(suit))
            elif iter == num(action.group(1)) - 1: announceString += " and a {} {}".format(fullrank(rank), fullsuit(suit))
            else: announceString += ", a {} {}".format(fullrank(rank), fullsuit(suit))
         else: remoteCall(targetPL,'pull',[])
   spellDifficulty = re.search(r'-test(Hex|Miracle|Spirit|Mad Science)([0-9]+|X)', Autoscript)      
   spellResolved = ''
   if spellDifficulty and rank and suit: # We only check for spell effects if we got a rank and suit result.
      if spellDifficulty.group(2) == 'X':
         if not len(targetCards): 
            whisper(":::ERROR::: No target to get variable difficulty found. Aborting!")
            return 'ABORT'
         difficultyTarget = re.search(r'difficulty(Grit|Value)',Autoscript)
         if difficultyTarget.group(1) == 'Grit':  # Git is the dude's current value + bullets + influence
            difficulty = compileCardStat(targetCards[0], 'Influence') + compileCardStat(targetCards[0], 'Bullets') + compileCardStat(targetCards[0], 'Value')
         else: difficulty = compileCardStat(targetCards[0], 'Value') # If it's not grit, the only other option (for now) is value
      else: difficulty = num(spellDifficulty.group(2))  # If it's not a variable difficulty, then we just set the numeric value for it
      if card.Type == 'Dude': skilledDude = card # if the card calling the script is a dude, we assume the ability is coming from them.
      else: skilledDude = fetchHost(card)
      skills = fetchSkills(skilledDude)
      neededSkill = None
      spellEffects = re.search(r'-spellEffects<(.*?),(.*?)>', Autoscript)
      for skill in skills:
         if (skill[0] == 'Huckster' and spellDifficulty.group(1) == 'Hex'
             or skill[0] == 'Blessed' and spellDifficulty.group(1) == 'Miracle'
             or skill[0] == 'Mad Science' and spellDifficulty.group(1) == 'Mad Scientist'
             or skill[0] == 'Shaman' and spellDifficulty.group(1) == 'Spirit'):
            neededSkill = skill
      if not neededSkill: # If we didn't find a relevant skill on the dude, then we assume they have the required skill at 0, or they wouldn't have been used.
         if spellDifficulty.group(1) == 'Hex': neededSkill = ('Huckster',0)
         elif spellDifficulty.group(1) == 'Miracle': neededSkill = ('Blessed',0)
         elif spellDifficulty.group(1) == 'Spirit': neededSkill = ('Shaman',0)
         else: neededSkill = ('Mad Scientist',0)
         notify(":::Warning::: Necessary skill not found on {}. Assuming they have {} 0 from card effects".format(skilledDude,neededSkill[0]))
      skillLevel = neededSkill[1]
      numericRank = numrank(rank, True) # Setting it in advance so that it does't ask the value of a joker twice
      #confirm('skill = {}, pull = {}, diff = {}'.format(skillLevel, numericRank, difficulty))
      if skillLevel + numericRank >= difficulty: spellResolved = '. {} succeeds the {} skill test by {}'.format(skilledDude,neededSkill[0],skillLevel + numericRank - difficulty) # If the spell is succesful, we want to mention it, before we mention its results
      elif spellEffects.group(2) != '': spellResolved = '. {} fails the {} skill test'.format(skilledDude,neededSkill[0])
      if not neededSkill: whisper(":::ERROR::: Oops, something went wrong. Can't find the required skill on this dude. Aborting!")
   debugNotify("About to announce.")
   if notification and announceString != "{} pull".format(announceText): notify(':> {}{}.'.format(announceString,spellResolved))
   if spellResolved: # We only check for spell effects if we got a rank and suit result.
      if re.search(r'succeeds',spellResolved): executeAutoscripts(card,spellEffects.group(1).replace('++','$$'),action = 'USE',targetCards = targetCards) # If the spell is succesful, execute it's effects
      else: executeAutoscripts(card,spellEffects.group(2).replace('++','$$'),action = 'USE',targetCards = targetCards) # If it isn't successful and it has a failing condition, activate it now.
   debugNotify("<<< DrawX()")
   return announceString

def RequestInt(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for drawing X Cards from the house deck to your hand.
   debugNotify(">>> RequestInt(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   action = re.search(r'\bRequestInt(-Min)?([0-9]*)(-div)?([0-9]*)(-Max)?([0-9]*)(-Msg)?\{?([A-Za-z0-9?$& ]*)\}?', Autoscript)
   if debugVerbosity >= 2:
      if action: notify('!!! regex: {}'.format(action.groups()))
      else: notify("!!! No regex match :(")
   debugNotify("Checking for Min")
   if action.group(2): 
      min = num(action.group(2))
      minTXT = ' (minimum {})'.format(min)
   else: 
      min = 0
      minTXT = ''
   debugNotify("Checking for Max")
   if action.group(6): 
      max = num(action.group(6))
      minTXT += ' (maximum {})'.format(max)
   else: 
      max = None
   debugNotify("Checking for div")
   if action.group(4): 
      div = num(action.group(4))
      minTXT += ' (must be a multiple of {})'.format(div)
   else: div = 1
   debugNotify("Checking for Msg")
   if action.group(8): 
      message = action.group(8)
   else: message = "{}:\nThis effect requires that you provide an 'X'. What should that number be?{}".format(card.name,minTXT)
   number = min - 1
   debugNotify("About to ask")
   while number < min or number % div or (max and number > max):
      number = askInteger(message,min)
      if number == None: 
         whisper("Aborting Function")
         return 'ABORT'
   debugNotify("<<< RequestInt()")
   return (announceText, number) # We do not modify the announcement with this function.
   
def SimplyAnnounce(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for drawing X Cards from the house deck to your hand.
   debugNotify(">>> SimplyAnnounce(){}".format(extraASDebug())) #Debug
   if targetCards is None: targetCards = []
   action = re.search(r'\bSimplyAnnounce{([A-Za-z0-9&,\.\' ]+)}', Autoscript)
   if debugVerbosity >= 2: #Debug
      if action: notify("!!! regex: {}".format(action.groups())) 
      else: notify("!!! regex failed :(") 
   if re.search(r'break',Autoscript) and re.search(r'subroutine',Autoscript): penaltyNoisy(card)
   if notification == 'Quick': announceString = "{} {}".format(announceText, action.group(1))
   else: announceString = "{} {}".format(announceText, action.group(1))
   if notification: notify(':> {}.'.format(announceString))
   debugNotify("<<< SimplyAnnounce()")
   return announceString

def CreateDummy(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for creating dummy cards.
   debugNotify(">>> CreateDummy(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   Dummywarn = getSetting('Dummywarn',True)
   dummyCard = None
   action = re.search(r'\bCreateDummy[A-Za-z0-9_ -]*(-with)(?!onOpponent|-doNotDiscard|-nonUnique)([A-Za-z0-9_ -]*)', Autoscript)
   # We only want this regex to be true if the dummycard is going to have tokens put on it automatically.
   if action and debugVerbosity >= 3: notify('### Regex: {}'.format(action.groups())) # debug
   elif debugVerbosity >= 3: notify('### No regex match! Aborting') # debug
   targetPLs = ofwhom(Autoscript, card.controller)
   for targetPL in targetPLs: 
      for c in table:
         if c.model == card.model and c.controller == targetPL and c.highlight == DummyColor: dummyCard = c # We check if already have a dummy of the same type on the table.
      debugNotify(' Checking to see what our dummy card is') # debug
      if not dummyCard or re.search(r'nonUnique',Autoscript): #Some create dummy effects allow for creating multiple copies of the same card model.
         debugNotify(' Dummywarn = {}'.format(Dummywarn)) # debug .
         debugNotify(' no dummyCard exists') # debug . Dummywarn = {}'.format(Dummywarn)
         if Dummywarn and re.search('onOpponent',Autoscript):
            if not confirm("This action creates an effect for your opponent and a way for them to remove it.\
                          \nFor this reason we've created a dummy card on the table and marked it with a special highlight so that you know that it's just a token.\
                        \n\nYou opponent can activate any abilities meant for them on the Dummy card. If this card has one, they can activate it by double clicking on the dummy. Very often, this will often remove the dummy since its effect will disappear.\
                        \n\nOnce the   dummy card is on the table, please right-click on it and select 'Pass control to {}'\
                        \n\nDo you want to see this warning again?".format(targetPL)): setSetting('Dummywarn',False)
         elif Dummywarn:
            information("This card is now supposed to go to your discard pile, but its lingering effects will only work automatically while a copy is in play.\
                          \nFor this reason we've created a dummy card on the table and marked it with a special highlight so that you know that it's just a token.\
                        \n\n(This message will not appear again.)")
            setSetting('Dummywarn',False)
         elif re.search(r'onOpponent', Autoscript): 
            debugNotify(' about to pop information') # debug
            information('The dummy card just created is meant for your opponent. Please right-click on it and select "Pass control to {}"'.format(targetPL))
         debugNotify(' Finished warnings. About to announce.') # debug
         dummyCard = table.create(card.model, playerside * 360, (20 * playerside * len([c for c in table if c.controller == targetPL and c.highlight == DummyColor])), 1) # This will create a fake card like the one we just created.
         dummyCard.highlight = DummyColor
   debugNotify(' About to move to discard pile if needed') # debug
   if not re.search(r'doNotDiscard',Autoscript): card.moveTo(card.owner.piles['Discard Pile'])
   if action: announceString = TokensX('Put{}'.format(action.group(2)), announceText,dummyCard, n = n) # If we have a -with in our autoscript, this is meant to put some tokens on the dummy card.
   else: announceString = announceText + 'create a lingering effect for {}'.format([targetPL.name for targetPL in targetPLs])
   debugNotify("<<< CreateDummy()")
   if re.search(r'isSilent', Autoscript): return announceText
   else: return announceString # Creating a dummy isn't usually announced.

def SpawnX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for token cards
   debugNotify(">>> CreateDummy(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   targetPLs = ofwhom(Autoscript, card.controller)
   action = re.search(r'\bSpawn([1-9]+)([A-Za-z ]+)', Autoscript)
   debugNotify(str(action.groups()),4)
   markers = re.search(r'\bSpawn[A-Za-z0-9_ -]*(-with)([A-Za-z0-9_ -]*)', Autoscript)
   modAction = re.search(r'-modAction:(.+)', Autoscript)
   if modAction: debugNotify(str(modAction.groups()),4)
   if action.group(2) == 'Gunslinger': spawnModel = '94fe7823-077c-4abd-9278-6e64bda6dc64' # for now we only have the gunslinger token, but in the future we might get more of them.
   else:
      whisper(":::ERROR::: Spawn Model for '{}' not understood. Aborting".format(action.group(2)))
      return 'ABORT'
   for iter in range(num(action.group(1))):
      tokenCard = table.create(spawnModel, cardDistance() + (20 * playerside * iter), (40 * playerside * iter), 1)
      if markers: tokensTXT = TokensX('Put{}'.format(markers.group(2)), announceText,tokenCard) # If we have a -with in our autoscript, this is meant to put some tokens on the dummy card.
      if modAction: ModifyStatus(modAction.group(1), announceText, tokenCard,targetCards,'Quick')
   if markers: ' and ' + tokensTXT
   else: extraTXT = ''
   announceString = announceText + 'spawn {} {} token{}.'.format(action.group(1),tokenCard,extraTXT)
   debugNotify("<<< CreateDummy()")
   if notification and not silent: notify(':> {}.'.format(announceString))
   elif silent: return announceText
   else: return announceString

def ChooseTrait(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for marking cards to be of a different trait than they are
   debugNotify(">>> ChooseTrait(){}".format(extraASDebug(Autoscript))) #Debug
   #confirm("Reached ChooseTrait") # Debug
   choiceTXT = ''
   targetCardlist = ''
   existingTrait = None
   if targetCards is None: targetCards = []
   if len(targetCards) == 0: targetCards.append(card) # If there's been to target card given, assume the target is the card itself.
   for targetCard in targetCards: targetCardlist += '{},'.format(targetCard)
   targetCardlist = targetCardlist.strip(',') # Re remove the trailing comma
   action = re.search(r'\bChooseTrait{([A-Za-z\| ]+)}', Autoscript)
   #confirm("search results: {}".format(action.groups())) # Debug
   traits = action.group(1).split('|')
   #confirm("List: {}".format(traits)) # Debug
   if len(traits) > 1:
      for i in range(len(traits)): choiceTXT += '{}: {}\n'.format(i, traits[i])
      choice = len(traits)
   else: choice = 0
   while choice > len(traits) - 1: 
      choice = askInteger("Choose one of the following traits to assign to this card:\n\n{}".format(choiceTXT),0)
      if choice == None: return 'ABORT'
   for targetCard in targetCards:
      if targetCard.markers:
         for key in targetCard.markers:
            if re.search('Trait:',key[0]):
               existingTrait = key
      if re.search(r'{}'.format(traits[choice]),targetCard.Traits): 
         if existingTrait: targetCard.markers[existingTrait] = 0
         else: pass # If the trait is anyway the same printed on the card, and it had no previous trait, there is nothing to do
      elif existingTrait:
         debugNotify("Searching for {} in {}".format(traits[choice],existingTrait[0])) # Debug               
         if re.search(r'{}'.format(traits[choice]),existingTrait[0]): pass # If the trait is the same as is already there, do nothing.
         else: 
            targetCard.markers[existingTrait] = 0 
            TokensX('Put1Trait:{}'.format(traits[choice]), '', targetCard)
      else: TokensX('Put1Trait:{}'.format(traits[choice]), '', targetCard)
   if notification == 'Quick': announceString = "{} marks {} as being {} now".format(announceText, targetCardlist, traits[choice])
   else: announceString = "{} mark {} as being {} now".format(announceText, targetCardlist, traits[choice])
   if notification: notify(':> {}.'.format(announceString))
   debugNotify("<<< ChooseTrait()")
   return announceString
            
def ModifyStatus(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for modifying the status of a card on the table.
   debugNotify(">>> ModifyStatus(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   targetCardlist = '' # A text field holding which cards are going to get tokens.
   extraTXT = ''
   action = re.search(r'\b(Boot|Unboot|SendHomeBooted|Discard|Ace|Return|Play|SendToBottom|SendToDraw|Takeover|Participate|Unparticipate|Callout|Move)(Target|Host|Multi|Myself)[-to]*([A-Z][A-Za-z&_ ]+)?', Autoscript)
   if action.group(2) == 'Myself': 
      del targetCards[:] # Empty the list, just in case.
      targetCards.append(card)
   if action.group(2) == 'Host': 
      del targetCards[:] # Empty the list, just in case.
      debugNotify("Finding Host")
      host = fetchHost(card)
      if host: targetCards = [host]
      else: 
         debugNotify("No Host Found? Aborting")
         return 'ABORT'      
   if action.group(3): dest = action.group(3)
   else: dest = 'hand'
   debugNotify("targetCards(){}".format([c.name for c in targetCards]),2) #Debug   
   for targetCard in targetCards: 
      if (action.group(1) == 'Play' or  action.group(1) == 'Return') and targetCard.group == table and targetCard.isFaceUp: 
         targetCardlist += '{},'.format(targetCard.name) 
      else: targetCardlist += '{},'.format(targetCard)
      if action.group(2) != 'Multi': break # If we're not doing a multi-targeting, we only mention the first target card's name.
   rnd(1,10) # Dela yto be able to grab the names
   debugNotify("Preparing targetCardlist",2)      
   targetCardlist = targetCardlist.strip(',') # Re remove the trailing comma
   if action.group(1) == 'SendToBottom': # For SendToBottom, we need a different mthod, as we need to shuffle the cards.
      if action.group(2) == 'Multi': 
         debugNotify("Sending Multiple card to the bottom",3)   
         sendToBottom(targetCards)
      else: 
         debugNotify("Sending Single card to the bottom",3)   
         try: sendToBottom([targetCards[0]])
         except: 
            delayed_whisper(":::ERROR::: You have not targeted a valid card")
            return 'ABORT'
   else:
      if re.search(r'-isCost',Autoscript) and not len(targetCards): return 'ABORT' # If the modification is a cost, but there was no valid target, we abort.
      for targetCard in targetCards:
         if action.group(1) == 'Boot':
            if boot(targetCard, silent = True, forced = 'boot') == 'FAIL' and re.search(r'-isCost',Autoscript):
               whisper(":::INFO::: Failed to pay the boot cost. ABORTING")
               return 'ABORT'
         elif action.group(1) == 'Unboot': boot(targetCard, silent = True, forced = 'unboot') 
         elif action.group(1) == 'Discard': discardTarget(targetCards = [targetCard], silent = True)        
         elif action.group(1) == 'Ace': aceTarget(targetCards = [targetCard], silent = True)
         elif action.group(1) == 'SendToDraw': sendToDrawHand(targetCard)
         elif action.group(1) == 'Participate':
            if not participateDude(targetCard): 
               whisper(":::ERROR::: {} is already in this shootout!".format(targetCard))
               return 'ABORT'
         elif action.group(1) == 'Unparticipate': leavePosse(targetCard)
         elif action.group(1) == 'Callout':
            leaderTarget = re.search(r"-leaderTarget\{(.+)\}", Autoscript)
            if leaderTarget:
               possibleTargets = findTarget("DemiAutoTargeted-at{}_and_not{}-targetMine-choose1".format(leaderTarget.group(1),targetCard.name),choiceTitle = "Choose which of your dudes performs the call out")
               if not len(possibleTargets): 
                  notify(":::ERROR::: No valid Target to move to found. Aborting!")
                  return 'ABORT'
               else: 
                  callout(possibleTargets[0], silent = True, targetDudes = [targetCard])
                  extraTXT = " with {}".format(possibleTargets[0])
            else: callout(card, silent = True, targetDudes = [targetCard])
         elif action.group(1) == 'Return': 
            returnToHand(targetCard, silent = True)
            extraTXT = " to their owner's hand"
         elif action.group(1) == 'Play': 
            if re.search(r'-payCost',Autoscript): # This modulator means the script is going to pay for the card normally
               preReducRegex = re.search(r'-reduc([0-9])',Autoscript) # this one means its going to reduce the cost a bit.
               if preReducRegex: preReduc = num(preReducRegex.group(1))
               else: preReduc = 0
               playcard(targetCard,costReduction = preReduc)
            else:
               placeCard(targetCard)
               executePlayScripts(targetCard, 'PLAY') # We execute the play scripts here only if the card is 0 cost.
               autoscriptOtherPlayers('CardPlayed',targetCard)            
         elif action.group(1) == 'Move':
            moveTarget = re.search(r"-moveTo(.+)", Autoscript)
            if not moveTarget: 
               notify(":::ERROR::: No valid moveTarget. Aborting!")
               return 'ABORT'
            if moveTarget.group(1) == 'Here': # If the moveTarget is "Here", then we try to figure out the current card's location and set it as the destination.
               if card.Type == 'Dude' or card.Type == 'Deed': possibleTargets = [card]
               elif card.Type == 'Action': 
                  notify(":::ERROR::: Bad Script. Actions should never 'moveToHere'. Aborting!")
                  return 'ABORT'
               else:
                  possibleTargets = [fetchHost(card)]
            else:
               possibleTargets = findTarget("DemiAutoTargeted-at{}-choose1".format(moveTarget.group(1)), card = targetCard,choiceTitle = "Choose which location you're moving to")
               if not len(possibleTargets): 
                  notify(":::ERROR::: No valid Target to move to found. Aborting!")
                  return 'ABORT'
            x,y = possibleTargets[0].position
            if targetCard.controller == me: targetCard.moveToTable(x + cardDistance(), y)
            else: remoteCall(targetCard.controller,'moveCard',[targetCard, x + cardDistance(), y])
            orgAttachments(targetCard)
            if possibleTargets[0].type == 'Deed': extraTXT = " to {}".format(possibleTargets[0])
            else: extraTXT = " to {}'s location".format(possibleTargets[0])
         elif action.group(1) == 'SendHomeBooted':
            for c in table: 
               if c.Type == 'Outfit' and c.controller == targetCard.controller: 
                  home = c
                  break
            x,y = home.position
            if targetCard.controller == me: targetCard.moveToTable(x + cardDistance(), y)
            else: 
               remoteCall(targetCard.controller,'moveCard',[targetCard,x + cardDistance(), y])
            if targetCard.highlight == AttackColor or targetCard.highlight == DefendColor: leavePosse(targetCard)
            if not re.search(r'-doNotBoot',Autoscript): boot(targetCard,silent = True, forced = 'boot')
            orgAttachments(targetCard)
         elif action.group(1) == 'Takeover':
            targetPLs = ofwhom(Autoscript, card.controller)
            claimCard(targetCard,targetPLs[0])
            remoteCall(targetPLs[0],'placeCard',[targetCard])
         else: return 'ABORT'
         if action.group(2) != 'Multi': break # If we're not doing a multi-targeting, abort after the first run.
   debugNotify("Finished Processing Modifications. About to announce",2)
   if notification == 'Quick': announceString = "{} {} {}{}".format(announceText, action.group(1), targetCardlist,extraTXT)
   else: announceString = "{} {} {}{}".format(announceText, action.group(1), targetCardlist, extraTXT)
   if notification and not re.search(r'isSilent', Autoscript): notify(':> {}.'.format(announceString))
   debugNotify("<<< ModifyStatus()")
   if re.search(r'isSilent', Autoscript): return announceText
   else: return announceString

def GameX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for alternative victory conditions
   debugNotify(">>> GameX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   action = re.search(r'\b(Lose|Win)Game', Autoscript)
   if debugVerbosity >= 2: #Debug
      if action: notify("!!! regex: {}".format(action.groups())) 
      else: notify("!!! regex failed :(") 
   if re.search(r'forController', Autoscript): player = card.controller
   elif re.search(r'forOwner', Autoscript): player = card.owner 
   elif re.search(r'forDark Side', Autoscript): 
      if Side == 'Dark': player = me
      else: player == findOpponent('Ask',"Please choose which opponent has won the game.")
   elif re.search(r'forLight Side', Autoscript): 
      if Side == 'Light': player = me
      else: player == findOpponent('Ask',"Please choose which opponent has won the game.")
   else: player == me
   if action.group(1) == 'Lose': 
      announceString = "=== {} loses the game! ===".format(player)
      reportGame('SpecialDefeat')
   else: 
      announceString = "=== {} wins the game! ===".format(player)
      reportGame('SpecialVictory')
   notify(announceString)
   debugNotify("<<< GameX()")
   return announceString

def RetrieveX(Autoscript, announceText, card, targetCards = None, notification = None, n = 0): # Core Command for finding a specific card from a pile and putting it in hand or discard pile
   debugNotify(">>> RetrieveX(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   action = re.search(r'\bRetrieve([0-9]+)Card', Autoscript)
   targetPLs = ofwhom(Autoscript, card.controller)
   for targetPL in targetPLs: # RetrieveX does not normally retrieve for anyone else but we loop anyway to be consistent. 
      debugNotify("Setting Source")
      if re.search(r'-fromDiscard', Autoscript):
         source = targetPL.piles['Discard Pile']
         sourcePath =  "from their Discard Pile"
      elif re.search(r'-fromBootHill', Autoscript):
         source = targetPL.piles['Boot Hill']
         sourcePath =  "from their Boot Hill"
      else: 
         source = targetPL.piles['Deck']
         sourcePath =  "from their Deck"
      debugNotify("Setting Destination")
      if re.search(r'-toTable', Autoscript):
         destination = table
         destiVerb = 'play'   
      elif re.search(r'-toDeck', Autoscript):
         destination = targetPL.piles['Deck']
         destiVerb = 'rework'
      elif re.search(r'-toDiscard', Autoscript):
         destination = targetPL.piles['Discard Pile']
         destiVerb = 'discard'
      elif re.search(r'-toBootHill', Autoscript):
         destination = targetPL.piles['Boot Hill']
         destiVerb = 'ace'
      else: 
         destination = targetPL.hand
         destiVerb = 'retrieve'
      debugNotify("Fething Script Variables")
      count = num(action.group(1))
      multiplier = per(Autoscript, card, n, targetCards, notification)
      if source == targetPL.piles['Deck']: # The discard pile is anyway visible.
         source.addViewer(me)
         rnd(1,10) # We give a delay to allow OCTGN to read the card properties before we proceed with checking them
      restrictions = prepareRestrictions(Autoscript, seek = 'retrieve')
      cardList = []
      countRestriction = re.search(r'-onTop([0-9]+)Cards', Autoscript)
      if countRestriction: topCount = num(countRestriction.group(1))
      else: topCount = len(source)
      if count == 999: count = topCount # Retrieve999Cards means the script will retrieve all cards that match the requirements, regardless of how many there are. As such, a '-onTop#Cards' modulator should always be included.
      for c in source.top(topCount):
         debugNotify("Checking card: {}".format(c),4)
         if re.search(r'-tellPlayer',Autoscript): delayed_whisper(":::INFO::: {} card is: {}".format(numOrder(c.getIndex),c)) # The -tellPlayer modulator, will tell the one retrieving what all cards were, even if they are not valid targets
         if checkCardRestrictions(gatherCardProperties(c), restrictions) and checkSpecialRestrictions(Autoscript,c):
            cardList.append(c)
            if re.search(r'-isTopmost', Autoscript) and len(cardList) == count: break # If we're selecting only the topmost cards, we select only the first matches we get. 
      debugNotify("cardList: {}".format(cardList),3)
      chosenCList = []
      abortedRetrieve = False
      if len(cardList) > count or re.search(r'upToAmount',Autoscript):
         cardChoices = []
         cardTexts = []
         for iter in range(count):
            debugNotify("iter: {}/{}".format(iter,count),4)
            del cardChoices[:]
            del cardTexts[:]
            for c in cardList:
               if c.Text not in cardTexts: # we don't want to provide the player with a the same card as a choice twice.
                  debugNotify("Appending card",4)
                  cardChoices.append(c)
                  cardTexts.append(c.Text) # We check the card text because there are cards with the same name in different sets (e.g. Darth Vader)            
            if re.search(r'upToAmount',Autoscript): cancelButtonName = 'Done'
            else: cancelButtonName = 'Cancel'
            choice = SingleChoice("Choose card to retrieve{}".format({1:''}.get(count,' {}/{}'.format(iter + 1,count))), makeChoiceListfromCardList(cardChoices), type = 'button', cancelName = cancelButtonName)
            if choice == None:
               if not re.search(r'upToAmount',Autoscript): abortedRetrieve = True # If we have the upToAmount, it means the retrieve can get less cards than the max amount, so cancel does not work as a cancel necessarily.            
               break
            else:
               chosenCList.append(cardChoices[choice])
               cardList.remove(cardChoices[choice])
      else: chosenCList = cardList
      debugNotify("chosenCList: {}".format(chosenCList))
      if not abortedRetrieve:   
         for c in chosenCList:
            if destination == table: 
               if re.search(r'-payCost',Autoscript): # This modulator means the script is going to pay for the card normally
                  preReducRegex = re.search(r'-reduc([0-9])',Autoscript) # this one means its going to reduce the cost a bit.
                  if preReducRegex: preReduc = num(preReducRegex.group(1))
                  else: preReduc = 0
                  playcard(c,costReduction = preReduc)
               else:
                  placeCard(c)
                  executePlayScripts(c, 'PLAY') # We execute the play scripts here only if the card is 0 cost.
                  autoscriptOtherPlayers('CardPlayed',c)            
            else: c.moveTo(destination)
      source.removeViewer(me)
      if abortedRetrieve: #If the player canceled a retrieve effect from R&D / Stack, we make sure to shuffle their pile as well.
         notify("{} has aborted the retrieval effect from {}".format(me,card))
         if source == targetPL.piles['Deck']: shuffle(targetPL.piles['Deck'])
         return 'ABORT'
   debugNotify("About to announce.")
   if re.search(r'doNotReveal',Autoscript): cardNames = "{} cards".format(len(chosenCList))
   else: cardNames = str([c.name for c in chosenCList])
   if len(chosenCList) == 0: announceString = "{} attempts to {} a card {}, but there were no valid targets.".format(announceText, destiVerb, sourcePath)
   else: announceString = "{} {} {} {}.".format(announceText, destiVerb, cardNames, sourcePath)
   if notification and multiplier > 0: notify(':> {}.'.format(announceString))
   debugNotify("<<< RetrieveX()")
   return announceString
   
#------------------------------------------------------------------------------
# Helper Functions
#------------------------------------------------------------------------------
       
def findTarget(Autoscript, fromHand = False, card = None, choiceTitle = None): # Function for finding the target of an autoscript
   debugNotify(">>> findTarget(){}".format(extraASDebug(Autoscript))) #Debug
   debugNotify("fromHand = {}. card = {}".format(fromHand,card)) #Debug
   if fromHand == True or re.search(r'-fromHand',Autoscript): group = me.hand
   elif re.search(r'-fromCommonReserves',Autoscript): group = grabFullReserves() # We can afford to use a list as a group, because we're not using any special class functions here, just stuff lists can also do
   elif re.search(r'-fromTopDeckMine',Autoscript): # Quick job because I cannot be bollocksed.
      debugNotify("Returing my top deck card",2)
      return [me.piles['Deck'].top()]
   elif re.search(r'-fromTopDeckOpponents',Autoscript): 
      debugNotify("Returing opponent top deck card",2)
      opponentPL = findOpponent('Ask')
      return [opponentPL.piles['Deck'].top()]
   else: group = table
   foundTargets = []
   if re.search(r'Targeted', Autoscript):
      requiredAllegiances = []
      targetGroups = prepareRestrictions(Autoscript)
      debugNotify("About to start checking all targeted cards.\n### targetGroups:{}".format(targetGroups)) #Debug
      for targetLookup in group: # Now that we have our list of restrictions, we go through each targeted card on the table to check if it matches.
         if (targetLookup.targetedBy and targetLookup.targetedBy == me) or re.search(r'AutoTargeted', Autoscript):
         # OK the above target check might need some decoding:
         # Look through all the cards on the group and start checking only IF...
         # * Card is targeted and targeted by the player OR target search has the -AutoTargeted modulator and it is NOT highlighted as a Fate, Edge or Captured.
         # * The player who controls this card is supposed to be me or the enemy.
            debugNotify("Checking {}".format(targetLookup))
            playerChk = me
            if card:
               if card.controller != me: # If we have provided the originator card to findTarget, and the card is not our, we assume that we need to treat the script as being run by our opponent
                  debugNotify("Reversing player check")
                  playerChk = card.controller
            if not checkSpecialRestrictions(Autoscript,targetLookup,playerChk): continue
            hostCards = eval(getGlobalVariable('Host Cards'))
            if re.search(r'-onHost',Autoscript):   
               debugNotify("Looking for Host")
               if not card: continue # If this targeting script targets only a host and we have not passed what the attachment is, we cannot find the host, so we abort.
               debugNotify("Attachment is: {}".format(card))
               isHost = False
               debugNotify("hostCards = {}".format([Card(attachID).name for attachID in hostCards]),4)
               for attachment in hostCards:
                  debugNotify("Comparing attachment {} (ID: {}) with card {} (ID: {}) and hostCard {} (ID: {}) with targetLookup {} (ID:{})".format(Card(attachment),attachment,card,card._id,Card(hostCards[attachment]),hostCards[attachment],targetLookup,targetLookup._id),4)
                  if attachment == card._id and hostCards[attachment] == targetLookup._id: 
                     debugNotify("Host found! {}".format(targetLookup))
                     isHost = True
               if not isHost: 
                  debugNotify("{} is not the host of {}. Skipping".format(targetLookup,card))
                  continue
            if re.search(r'-onAttachment',Autoscript):   
               debugNotify("Looking for Attachments")
               if not card: continue # If this targeting script targets only a host and we have not passed what the attachment is, we cannot find the host, so we abort.
               debugNotify("Host is: {}".format(card))
               isAttachment = False
               debugNotify("hostCards = {}".format([Card(attachID).name for attachID in hostCards]),4)
               for attachment in hostCards:
                  debugNotify("Comparing host {} (ID: {}) with attachment {} (ID: {}) and hostCard {} (ID: {}) with targetLookup {} (ID:{})".format(Card(attachment),attachment,card,card._id,Card(hostCards[attachment]),hostCards[attachment],targetLookup,targetLookup._id),4)
                  if hostCards[attachment] == card._id and attachment == targetLookup._id: 
                     debugNotify("Attachment found! {}".format(targetLookup))
                     isAttachment = True
               if not isAttachment: 
                  debugNotify("{} is not  attached to {}. Skipping".format(targetLookup,card))
                  continue
            if checkCardRestrictions(gatherCardProperties(targetLookup), targetGroups): 
               if not targetLookup in foundTargets: 
                  debugNotify("About to append {}".format(targetLookup)) #Debug
                  foundTargets.append(targetLookup) # I don't know why but the first match is always processed twice by the for loop.
            elif debugVerbosity >= 3: notify("### findTarget() Rejected {}".format(targetLookup))# Debug
      debugNotify("Finished seeking. foundTargets List = {}".format([c.name for c in foundTargets]))
      if re.search(r'DemiAutoTargeted', Autoscript):
         debugNotify("Checking DemiAutoTargeted switches")# Debug
         targetNRregex = re.search(r'-choose([1-9])',Autoscript)
         targetedCards = 0
         foundTargetsTargeted = []
         debugNotify("About to count targeted cards")# Debug
         for targetC in foundTargets:
            if targetC.targetedBy and targetC.targetedBy == me: foundTargetsTargeted.append(targetC)
         if targetNRregex:
            debugNotify("!!! targetNRregex exists")# Debug
            if len(foundTargetsTargeted): foundTargets = foundTargetsTargeted # If we have the same amount of cards targeted as the amount we need, then we just select the targeted cards
                                                                           # This will also work if the player has targeted more cards than they need. The later choice will be simply between those cards.
         else: # If we do not want to choose, then it's probably a bad script. In any case we make sure that the player has targeted something (as the alternative it giving them a random choice of the valid targets)
            del foundTargets[:]
      if len(foundTargets) == 0 and not re.search(r'(?<!Demi)AutoTargeted', Autoscript) and not re.search(r'noTargetingError', Autoscript): 
         targetsText = ''
         mergedList = []
         for posRestrictions in targetGroups: 
            debugNotify("About to notify on restrictions")# Debug
            if targetsText == '': targetsText = '\nYou need: '
            else: targetsText += ', or '
            del mergedList[:]
            mergedList += posRestrictions[0]
            if len(mergedList) > 0: targetsText += "{} and ".format(mergedList)  
            del mergedList[:]
            mergedList += posRestrictions[1]
            if len(mergedList) > 0: targetsText += "not {}".format(mergedList)
            if targetsText.endswith(' and '): targetsText = targetsText[:-len(' and ')]
         debugNotify("About to chkPlayer()")# Debug
         playerChk = me
         if card:
            if card.controller != me: # If we have provided the originator card to findTarget, and the card is not our, we assume that we need to treat the script as being run by our opponent
               debugNotify("Reversing player check")
               playerChk = card.controller
         if not chkPlayer(Autoscript, targetLookup.controller, False, True, player = playerChk): 
            allegiance = re.search(r'target(Opponents|Mine)', Autoscript)
            requiredAllegiances.append(allegiance.group(1))
         if len(requiredAllegiances) > 0: targetsText += "\nValid Target Allegiance: {}.".format(requiredAllegiances)
         delayed_whisper(":::ERROR::: You need to target a valid card before using this action{}.".format(targetsText))
      elif len(foundTargets) >= 1 and re.search(r'-choose',Autoscript):
         debugNotify("Going for a choice menu")# Debug
         choiceType = re.search(r'-choose([0-9]+)',Autoscript)
         if not choiceTitle:
            if not card: choiceTitle = "Choose one of the valid targets for this effect"
            else: choiceTitle = "Choose one of the valid targets for {}'s ability".format(card.name)
         debugNotify("Checking for SingleChoice")# Debug
         if choiceType.group(1) == '1':
            if len(foundTargets) == 1: choice = 0 # If we only have one valid target, autoselect it.
            #if len(foundTargets) == 1: foundTargets = foundTargets[0] # If we only have one valid target, autoselect it. # for askCard implementation
            else: choice = SingleChoice(choiceTitle, makeChoiceListfromCardList(foundTargets), type = 'button', default = 0)
            if choice == None: del foundTargets[:]
            else: foundTargets = [foundTargets.pop(choice)] # if we select the target we want, we make our list only hold that target
         else:
            choiceAmount = num(choiceType.group(1))
            if len(foundTargets) <= choiceAmount: pass # If the amount of cards we have to target are equal to the available targets, then we just select all of them.
            else: 			
               availTargets = list(foundTargets) # We make a new list because we're going to start repopulating the foundTargets list again
               del foundTargets[:]
               for iter in range(choiceAmount):
                  choice = SingleChoice(choiceTitle, makeChoiceListfromCardList(availTargets), type = 'button', default = 0)
                  if choice == None: break
                  else: foundTargets.append(availTargets.pop(choice))
   if debugVerbosity >= 3: # Debug
      tlist = [] 
      for foundTarget in foundTargets: tlist.append(foundTarget.name) # Debug
      notify("<<< findTarget() by returning: {}".format(tlist))
   return foundTargets

def gatherCardProperties(card):
   debugNotify(">>> gatherCardProperties()") #Debug
   cardProperties = []
   debugNotify("Appending name",4) # Debug                
   cardProperties.append(card.name) # We are going to check its name
   debugNotify("Appending Type",4) # Debug                
   cardProperties.append(card.Type) # We are going to check its Type
   debugNotify("Appending Outfit",4) # Debug                
   cardProperties.append(card.Outfit) # We are going to check its Outfit
   debugNotify("Appending Keywords",4) # Debug                
   cardSubtypes = card.keywords.split('-') # And each individual Keyword. Keywords are separated by " - "
   for cardSubtype in cardSubtypes:
      strippedCS = cardSubtype.strip() # Remove any leading/trailing spaces between traits. We need to use a new variable, because we can't modify the loop iterator.
      if strippedCS:
         cardProperties.append(strippedCS) # If there's anything left after the stip (i.e. it's not an empty string anymrore) add it to the list.
         skillRegex = re.search(r'(Huckster|Blessed|Shaman|Mad Scientist) [0-9]',strippedCS)
         if skillRegex: cardProperties.append(skillRegex.group(1)) # If we discover a skill, we also append only its name, so that it's seekable alone, without the level of the skill.
   debugNotify("Appending Suit",4) # Debug                
   cardProperties.append(card.Suit)
   debugNotify("<<< gatherCardProperties() with Card Properties: {}".format(cardProperties)) #Debug
   return cardProperties

def prepareRestrictions(Autoscript, seek = 'target'):
# This is a function that takes an autoscript and attempts to find restrictions on card traits/types/names etc. 
# It goes looks for a specific working and then gathers all restrictions into a list of tuples, where each tuple has a negative and a positive entry
# The positive entry (position [0] in the tuple) contains what card properties a card needs to have to be a valid selection
# The negative entry (position [1] in the tuple) contains what card properties a card needs to NOT have to be a vaid selection.
   debugNotify(">>> prepareRestrictions() {}. Seektype = {}".format(extraASDebug(Autoscript),seek)) #Debug
   validTargets = [] # a list that holds any type that a card must be, in order to be a valid target.
   targetGroups = []
   Autoscript = scrubTransferTargets(Autoscript)
   if seek == 'type': whatTarget = re.search(r'\b(type)([A-Za-z_{},&. ]+)[-]?', Autoscript) # seek of "type" is used by autoscripting other players, and it's separated so that the same card can have two different triggers (e.g. see Darth Vader)
   elif seek == 'retrieve': whatTarget = re.search(r'\b(grab)([A-Za-z_{},&. ]+)[-]?', Autoscript) # seek of "retrieve" is used when checking what types of cards to retrieve from one's deck or discard pile
   elif seek == 'reduce': whatTarget = re.search(r'\b(affects)([A-Za-z_{},&. ]+)[-]?', Autoscript) # seek of "reduce" is used when checking for what types of cards to recuce the cost.
   elif seek == 'hostType': whatTarget = re.search(r'\b(ifHost)([A-Za-z_{},&. ]+)[-]?', Autoscript) # seek of "reduce" is used when checking for what types of cards to recuce the cost.
   else: whatTarget = re.search(r'-(at)([A-Za-z_{},& ]+)[-]?', Autoscript) # We signify target restrictions keywords by starting a string with "or"
   if whatTarget: 
      debugNotify("Splitting on _or_") #Debug
      validTargets = whatTarget.group(2).split('_or_') # If we have a list of valid targets, split them into a list, separated by the string "_or_". Usually this results in a list of 1 item.
      ValidTargetsSnapshot = list(validTargets) # We have to work on a snapshot, because we're going to be modifying the actual list as we iterate.
      for iter in range(len(ValidTargetsSnapshot)): # Now we go through each list item and see if it has more than one condition (Eg, non-desert fief)
         debugNotify("Creating empty list tuple") #Debug            
         targetGroups.insert(iter,([],[])) # We create a tuple of two list. The first list is the valid properties, the second the invalid ones
         multiConditionTargets = ValidTargetsSnapshot[iter].split('_and_') # We put all the mutliple conditions in a new list, separating each element.
         debugNotify("Splitting on _and_ & _or_ ") #Debug
         debugNotify("multiConditionTargets is: {}".format(multiConditionTargets),4) # Debug
         for chkCondition in multiConditionTargets:
            debugNotify("Checking: {}".format(chkCondition),4) # Debug
            regexCondition = re.search(r'(no[nt]){?([A-Za-z,& ]+)}?', chkCondition) # Do a search to see if in the multicondition targets there's one with "non" in front
            if regexCondition and (regexCondition.group(1) == 'non' or regexCondition.group(1) == 'not'):
               debugNotify("Invalid Target",4) # Debug
               if regexCondition.group(2) not in targetGroups[iter][1]: targetGroups[iter][1].append(regexCondition.group(2)) # If there is, move it without the "non" into the invalidTargets list.
            else: 
               debugNotify("Valid Target",4) # Debug
               targetGroups[iter][0].append(chkCondition) # Else just move the individual condition to the end if validTargets list
   else: debugNotify("No restrictions regex") #Debug 
   debugNotify("<<< prepareRestrictions() by returning: {}.".format(targetGroups))
   return targetGroups

def checkCardRestrictions(cardPropertyList, restrictionsList):
   debugNotify(">>> checkCardRestrictions()") #Debug
   debugNotify("cardPropertyList = {}".format(cardPropertyList)) #Debug
   debugNotify("restrictionsList = {}".format(restrictionsList)) #Debug
   validCard = True
   for restrictionsGroup in restrictionsList: 
   # We check each card's properties against each restrictions group of valid + invalid properties.
   # Each Restrictions group is a tuple of two lists. First list (tuple[0]) is the valid properties, and the second list is the invalid properties
   # We check if all the properties from the valid list are in the card properties
   # And then we check if no properties from the invalid list are in the properties
   # If both of these are true, then the card is a valid choice for our action.
      validCard = True # We need to set it here as well for further loops
      debugNotify("restrictionsGroup checking: {}".format(restrictionsGroup),3)
      if len(restrictionsList) > 0 and len(restrictionsGroup[0]) > 0: 
         for validtargetCHK in restrictionsGroup[0]: # look if the card we're going through matches our valid target checks
            debugNotify("Checking for valid match on {}".format(validtargetCHK),4) # Debug
            if not validtargetCHK in cardPropertyList: 
               debugNotify("{} not found in {}".format(validtargetCHK,cardPropertyList),4) # Debug
               validCard = False
      elif debugVerbosity >= 4: notify("### No positive restrictions")
      if len(restrictionsList) > 0 and len(restrictionsGroup[1]) > 0: # If we have no target restrictions, any selected card will do as long as it's a valid target.
         for invalidtargetCHK in restrictionsGroup[1]:
            debugNotify("Checking for invalid match on {}".format(invalidtargetCHK),4) # Debug
            if invalidtargetCHK in cardPropertyList: validCard = False
      elif debugVerbosity >= 4: notify("### No negative restrictions")
      if validCard: break # If we already passed a restrictions check, we don't need to continue checking restrictions 
   debugNotify("<<< checkCardRestrictions() with return {}".format(validCard)) #Debug
   return validCard

def checkSpecialRestrictions(Autoscript,card, playerChk = me):
# Check the autoscript for special restrictions of a valid card
# If the card does not validate all the restrictions included in the autoscript, we reject it
   debugNotify(">>> checkSpecialRestrictions() {}".format(extraASDebug(Autoscript))) #Debug
   debugNotify("Card: {}".format(card)) #Debug
   validCard = True
   Autoscript = scrubTransferTargets(Autoscript)
   host = fetchHost(card)
   if re.search(r'isUnbooted',Autoscript) and card.orientation == Rot90: 
      debugNotify("!!! Failing because it's booted")
      validCard = False
   if re.search(r'isBooted',Autoscript) and card.orientation == Rot0: 
      debugNotify("!!! Failing because it's unbooted")
      validCard = False
   if re.search(r'isStudDude',Autoscript) and fetchDrawType(card) == 'Draw':
      debugNotify("!!! Failing because card is a Draw")
      validCard = False
   if re.search(r'isDrawDude',Autoscript) and fetchDrawType(card) == 'Stud':
      debugNotify("!!! Failing because card is a Stud")
      validCard = False
   if re.search(r'isParticipating',Autoscript):
      if host:
         if host.highlight != AttackColor and host.highlight != DefendColor and host.highlight != InitiateColor:
            debugNotify("!!! Failing because host is not participating")
            validCard = False
      else:
         if card.highlight != AttackColor and card.highlight != DefendColor and card.highlight != InitiateColor: 
            debugNotify("!!! Failing because dude is not participating")
            validCard = False
   if re.search(r'isNotParticipating',Autoscript):
      if host:
         if (host.highlight == AttackColor or host.highlight == DefendColor or host.highlight == InitiateColor): 
            debugNotify("!!! Failing because host is participating")
            validCard = False
      else:
         if (card.highlight == AttackColor or card.highlight == DefendColor or card.highlight == InitiateColor): 
            debugNotify("!!! Failing because dude is participating")
            validCard = False
   if re.search(r'isDrawHand',Autoscript) and card.highlight != DrawHandColor: 
      debugNotify("!!! Failing because card is not in the draw hand")
      validCard = False
   if re.search(r'isNotDrawHand',Autoscript) and card.highlight == DrawHandColor: 
      debugNotify("!!! Failing because card is in the draw hand")
      validCard = False
   if not chkPlayer(Autoscript, card.controller, False, True, playerChk): 
      debugNotify("!!! Failing because not the right controller")
      validCard = False
   markerName = re.search(r'-hasMarker{([\w +:]+)}',Autoscript) # Checking if we need specific markers on the card.
   if markerName: #If we're looking for markers, then we go through each targeted card and check if it has any relevant markers
      debugNotify("Checking marker restrictions")# Debug
      debugNotify("Marker Name: {}".format(markerName.group(1)))# Debug
      marker = findMarker(card, markerName.group(1))
      debugNotify("Marker match for {} == {}".format(card,str(marker)),4) # Debug
      if not marker: 
         debugNotify("!!! Failing because it's missing marker")
         validCard = False
   markerNeg = re.search(r'-hasntMarker{([\w +:]+)}',Autoscript) # Checking if we need to not have specific markers on the card.
   if markerNeg: #If we're looking for markers, then we go through each targeted card and check if it has any relevant markers
      debugNotify("Checking negative marker restrictions")# Debug
      debugNotify("Marker Name: {}".format(markerNeg.group(1)))# Debug
      marker = findMarker(card, markerNeg.group(1))
      if marker: 
         debugNotify("!!! Failing because it has marker")
         validCard = False
   elif debugVerbosity >= 4: notify("### No negative marker restrictions.")
   # Checking if the target needs to have a property at a certiain value. 
   propertyReq = re.search(r'-hasProperty{([\w ]+)}(eq|le|ge|gt|lt)([0-9])',Autoscript) 
   if propertyReq and validCard: 
      if propertyReq == 'Influence' or propertyReq == 'Control' or propertyReq == 'Bullets' or propertyReq == 'Value' or propertyReq == 'Production' or propertyReq == 'Upkeep': 
      # If it's one of the core card stats, we make sure to include markers and attachments in our calculations
         compareValue(propertyReq.group(2), compileCardStat(card, propertyReq), num(propertyReq.group(3))) 
      else: validCard = compareValue(propertyReq.group(2), num(card.properties[propertyReq.group(1)]), num(propertyReq.group(3))) 
   # Since we're placing the value straight into validCard, we don't want to check at all is validCard is already false
   # Checking if the target needs to have a markers at a particular value.
   MarkerReq = re.search(r'-ifMarkers{([\w ]+)}(eq|le|ge|gt|lt)([0-9])',Autoscript)
   if MarkerReq and validCard: 
      if debugVerbosity >= 4: notify("Found marker comparison req. regex groups: {}".format(MarkerReq.groups()))
      markerSeek = findMarker(card, MarkerReq.group(1))
      if markerSeek:
         validCard = compareValue(MarkerReq.group(2), card.markers[markerSeek], num(MarkerReq.group(3)))
   # Checking if the DS Dial needs to be at a specific value
   debugNotify("<<< checkSpecialRestrictions() for {} with return {}".format(card.name,validCard)) #Debug
   return validCard

def checkOriginatorRestrictions(Autoscript,card):
# Check the autoscript for special restrictions on the originator of a specific effect. 
# If the card does not validate all the restrictions included in the autoscript, we reject it
# For example Darth Vader 41/2 requires that he is attacking before his effect takes place. In this case we'd check that he is currently attacking and return True is he is
   debugNotify(">>> checkOriginatorRestrictions() {}".format(extraASDebug(Autoscript))) #Debug
   debugNotify("Card: {}".format(card)) #Debug
   validCard = True
   Autoscript = scrubTransferTargets(Autoscript)
   if re.search(r'ifOrigParticipating',Autoscript):
      if card.highlight != AttackColor and card.highlight != DefendColor and card.highlight != InitiateColor: validCard = False
   if re.search(r'ifOrigNotParticipating',Autoscript) and (card.highlight == AttackColor or card.highlight == DefendColor or card.highlight == InitiateColor): validCard = False
   markerName = re.search(r'-ifOrigHasMarker{([\w :]+)}',Autoscript) # Checking if we need specific markers on the card.
   if markerName: #If we're looking for markers, then we go through each targeted card and check if it has any relevant markers
      debugNotify("Checking marker restrictions")# Debug
      debugNotify("Marker Name: {}".format(markerName.group(1)))# Debug
      marker = findMarker(card, markerName.group(1))
      if not marker: validCard = False
   markerNeg = re.search(r'-ifOrigHasntMarker{([\w ]+)}',Autoscript) # Checking if we need to not have specific markers on the card.
   if markerNeg: #If we're looking for markers, then we go through each targeted card and check if it has any relevant markers
      debugNotify("Checking negative marker restrictions")# Debug
      debugNotify("Marker Name: {}".format(markerNeg.group(1)))# Debug
      marker = findMarker(card, markerNeg.group(1))
      if marker: validCard = False
   # Checking if the originator needs to have a property at a certiain value. 
   propertyReq = re.search(r'-ifOrigHasProperty{([\w ]+)}(eq|le|ge|gt|lt)([0-9])',Autoscript) 
   if propertyReq and validCard: validCard = compareValue(propertyReq.group(2), num(card.properties[propertyReq.group(1)]), num(propertyReq.group(3))) # We don't want to check if validCard is already False
   # Checking if the target needs to have a markers at a particular value.
   MarkerReq = re.search(r'-ifOrigmarkers{([\w ]+)}(eq|le|ge|gt|lt)([0-9])',Autoscript)
   if MarkerReq and validCard: validCard = compareValue(MarkerReq.group(2), card.markers.get(findMarker(card, MarkerReq.group(1)),0), num(MarkerReq.group(3)))
   # Checking if the DS Dial needs to be at a specific value
   debugNotify("<<< checkOriginatorRestrictions() with return {}".format(validCard)) #Debug
   return validCard

def scrubTransferTargets(Autoscript): # This functions clears the targeting modulators used by source and destination cards of the Transfer core command
   debugNotify(">>> scrubTransferTargets() with Autoscript: {}".format(Autoscript))
   if re.search(r'Transfer[0-9]',Autoscript): # If we're using the Transfer core command, then we're going to have source and destination conditions which will mess checks. We need to remove them.
      debugNotify("We got Transfer core command",2)
      newASregex = re.search(r'(Transfer.*?)-source',Autoscript) # We search until '-source' which is where the Transfer modulator's targeting regex starts
      if newASregex: debugNotify('newASregex = {}'.format(newASregex.groups()),2)
      else: debugNotify("Script could not find newASregex. Will error",2)
      Autoscript = newASregex.group(1) # We keep only everything in the basic targetting
   debugNotify("<<< scrubTransferTargets() with return {}".format(Autoscript))
   return Autoscript

   
def compareValue(comparison, value, requirement):
   debugNotify(">>> compareValue()")
   debugNotify("comparison = {}, value = {}, requirement = {}".format(comparison, value, requirement))
   if comparison == 'eq' and value != requirement: return False # 'eq' stands for "Equal to"
   if comparison == 'le' and value > requirement: return False # 'le' stands for "Less or Equal"
   if comparison == 'ge' and value < requirement: return False # 'ge' stands for "Greater or Equal"
   if comparison == 'lt' and value >= requirement: return False # 'lt' stands for "Less Than"
   if comparison == 'gt' and value <= requirement: return False # 'gt' stands for "Greater Than"
   debugNotify("<<< compareValue() with return True")
   return True # If none of the requirements fail, we return true
     
   
def chkPlayer(Autoscript, controller, manual, targetChk = False, player = me): # Function for figuring out if an autoscript is supposed to target an opponent's cards or ours.
# Function returns 1 if the card is not only for rivals, or if it is for rivals and the card being activated it not ours.
# This is then multiplied by the multiplier, which means that if the card activated only works for Rival's cards, our cards will have a 0 gain.
# This will probably make no sense when I read it in 10 years...
   debugNotify(">>> chkPlayer(). Controller is: {}".format(controller)) #Debug
   debugNotify("Autoscript = {}".format(Autoscript),3)
   try:
      validPlayer = 1 # We always succeed unless a check fails
      if targetChk: # If set to true, it means we're checking from the findTarget() function, which needs a different keyword in case we end up with two checks on a card's controller on the same script (e.g. Darth Vader)
         debugNotify("Doing targetChk",3)
         byOpponent = re.search(r'targetOpponents', Autoscript)
         byAlly = re.search(r'targetAllied', Autoscript)
         byMe = re.search(r'targetMine', Autoscript)
      else:
         debugNotify("Doing normal chk",3)
         byOpponent = re.search(r'(byOpponent|forOpponent)', Autoscript)
         byAlly = re.search(r'(byAlly|forAlly)', Autoscript)
         byMe = re.search(r'(byMe|forMe)', Autoscript)
      if re.search(r'duringOpponentTurn', Autoscript) and re.search(r'{}'.format(controller.getGlobalVariable('Side')),getGlobalVariable('Phase')): 
         debugNotify("!!! Failing because ability is for {} opponent's turn.".format(controller))
         validPlayer = 0 # If the card can only fire furing its controller's opponent's turn
      elif re.search(r'duringMyTurn', Autoscript) and not re.search(r'{}'.format(controller.getGlobalVariable('Side')),getGlobalVariable('Phase')): 
         debugNotify("!!! Failing because ability is for {}'s turn.".format(controller))
         validPlayer = 0 # If the card can only fire furing its controller's turn
      elif byOpponent and controller in fetchAllAllies(player): 
         debugNotify("!!! Failing because ability is byOpponent and controller is an Ally")
         validPlayer =  0 # If the card needs to be played by a rival.
      elif byAlly and controller in fetchAllOpponents(player): 
         debugNotify("!!! Failing because ability is for byAlly and controller is {}".format(controller))
         validPlayer =  0 # If the card needs to be played by us.
      elif byMe and controller != player: 
         debugNotify("!!! Failing because ability is for byMe and controller is {}".format(controller))
         validPlayer =  0 # If the card needs to be played by us.
      else: debugNotify("!!! Succeeding by Default") # Debug
      if manual or len(players) == 1: 
         debugNotify("!!! Force Succeeding for Manual/Debug")         
         validPlayer = 1 # On a manual or debug run we always succeed
      debugNotify("<<< chkPlayer() with validPlayer: {}".format(validPlayer)) # Debug
      return validPlayer
   except: 
      notify("!!!ERROR!!! Null value on chkPlayer()")
      return 0

def chkWarn(card, Autoscript): # Function for checking that an autoscript announces a warning to the player
   debugNotify(">>> chkWarn(){}".format(extraASDebug(Autoscript))) #Debug
   global AfterRunInf, AfterTraceInf
   warning = re.search(r'warn([A-Z][A-Za-z0-9 ]+)-?', Autoscript)
   if warning:
      if warning.group(1) == 'Discard': 
         if not confirm("This action requires that you discard some cards. Have you done this already?"):
            whisper(":> Aborting action. Please discard the necessary amount of cards and run this action again")
            return 'ABORT'
      if warning.group(1) == 'ReshuffleOpponent': 
         if not confirm("This action will reshuffle your opponent's pile(s). Are you sure?\n\n[Important: Please ask your opponent not to take any clicks with their piles until this clicks is complete or the game might crash]"):
            whisper(":> Aborting action.")
            return 'ABORT'
      if warning.group(1) == 'GiveToOpponent': confirm('This card has an effect which if meant for your opponent. Please use the menu option "pass control to" to give them control.')
      if warning.group(1) == 'Reshuffle': 
         if not confirm("This action will reshuffle your piles. Are you sure?"):
            whisper(":> Aborting action.")
            return 'ABORT'
      if warning.group(1) == 'Workaround':
         notify(":::Note:::{} is using a workaround autoscript".format(me))
      if warning.group(1) == 'LotsofStuff': 
         if not confirm("This card modify the cards on the table significantly and very difficult to undo. Are you ready to proceed?"):
            whisper(":> Aborting action.")
            return 'ABORT'
   debugNotify("<<< chkWarn() gracefully") 
   return 'OK'

def per(Autoscript, card = None, count = 0, targetCards = None, notification = None): # This function goes through the autoscript and looks for the words "per<Something>". Then figures out what the card multiplies its effect with, and returns the appropriate multiplier.
   debugNotify(">>> per(){}".format(extraASDebug(Autoscript))) #Debug
   if targetCards is None: targetCards = []
   div = 1
   ignore = 0
   max = 0 # A maximum of 0 means no limit
   per = re.search(r'\b(per|upto)(Target|Host|Every)?([A-Z][^-]*)-?', Autoscript) # We're searching for the word per, and grabbing all after that, until the first dash "-" as the variable.   
   if per: # If the  search was successful...
      multiplier = 0
      debugNotify("Groups: {}. Count: {}".format(per.groups(),count)) #Debug
      if per.group(2) and (per.group(2) == 'Target' or per.group(2) == 'Every'): # If we're looking for a target or any specific type of card, we need to scour the requested group for targets.
         debugNotify("Checking for Targeted per")
         if per.group(2) == 'Target' and len(targetCards) == 0: 
            delayed_whisper(":::ERROR::: Script expected a card targeted but found none! Exiting with 0 multiplier.")
            # If we were expecting a target card and we have none we shouldn't even be in here. But in any case, we return a multiplier of 0
         elif per.group(2) == 'Every' and len(targetCards) == 0: pass #If we looking for a number of cards and we found none, then obviously we return 0
         else:
            if per.group(2) == 'Host': targetCards = [fetchHost(card)]
            for perCard in targetCards:
               if not checkSpecialRestrictions(Autoscript,perCard): continue
               debugNotify("perCard = {}".format(perCard))
               if re.search(r'Marker',per.group(3)):
                  markerName = re.search(r'Marker{([\w :]+)}',per.group(3)) # I don't understand why I had to make the curly brackets optional, but it seens atTurnStart/End completely eats them when it parses the CardsAS.get(card.model,'')
                  marker = findMarker(perCard, markerName.group(1))
                  if marker: multiplier += perCard.markers[marker]
               elif re.search(r'Property',per.group(3)):
                  property = re.search(r'Property{([\w ]+)}',per.group(3))
                  multiplier += compileCardStat(perCard,property.group(1))
               else: multiplier += 1 # If there's no special conditions, then we just add one multiplier per valid (auto)target. Ef. "-perEvery-AutoTargeted-onICE" would give 1 multiplier per ICE on the table
         if per.group(2) == 'Every': # If we're checking every card of a specific trait, we may have cards that give bonus to that amount (e.g. Echo base), so we look for those bonuses now.
            for c in table: # We check for cards for give bonus objective traits (e.g. Echo Base)
               Autoscripts = CardsAS.get(c.model,'').split('||')
               for autoS in Autoscripts:
                  debugNotify("Checking {} for Objective Trait boosting AS: {}".format(c,autoS))
                  TraitRegex = re.search(r'Trait\{([A-Za-z_ ]+)\}([0-9])Bonus',autoS)
                  if TraitRegex: 
                     if debugVerbosity >= 3: notify("TraitRegex found. Groups = {}".format(TraitRegex.groups()))
                     TraitsList = TraitRegex.group(1).split('_and_') # We make a list of all the traits the bonus effect of the cardprovides
                     if debugVerbosity >= 4: notify("### TraitsList = {}".format(TraitsList)) 
                     TraitsRestrictions = prepareRestrictions(Autoscript) # Then we gather the trait restrictions the original effect was looking for
                     debugNotify("TraitsRestrictions = {}".format(TraitsRestrictions),4)
                     if checkCardRestrictions(TraitsList, TraitsRestrictions) and checkSpecialRestrictions(Autoscript,c): # Finally we compare the bonus traits of the card we found, wit  h the traits the original effect was polling for.
                        multiplier += num(TraitRegex.group(2)) * chkPlayer(autoS, c.controller, False, True) # If they match, we increase our multiplier by the relevant number, if the card has the appropriate controller according to its effect.
      else: #If we're not looking for a particular target, then we check for everything else.
         debugNotify("Doing no table lookup") # Debug.
         if per.group(3) == 'X': multiplier = count # Probably not needed and the next elif can handle alone anyway.
         elif count: multiplier = num(count) * chkPlayer(Autoscript, card.controller, False) # All non-special-rules per<somcething> requests use this formula.
                                                                                              # Usually there is a count sent to this function (eg, number of favour purchased) with which to multiply the end result with
                                                                                              # and some cards may only work when a rival owns or does something.
         elif re.search(r'Marker',per.group(3)):
            markerName = re.search(r'Marker{([\w :]+)}',per.group(3)) # I don't understand why I had to make the curly brackets optional, but it seens atTurnStart/End completely eats them when it parses the CardsAS.get(card.model,'')
            marker = findMarker(card, markerName.group(1))
            if marker: multiplier = card.markers[marker]
            else: multiplier = 0
         elif re.search(r'Property',per.group(3)):
            property = re.search(r'Property{([\w ]+)}',per.group(3))           
            multiplier = compileCardStat(card,property.group(1)) 
         elif re.search(r'Opponent',per.group(3)): multiplier = len(fetchAllOpponents())
         elif re.search(r'Ally',per.group(3)): multiplier = len(fetchAllAllies()) - 1 # -1 because we exclude ourselves.
         elif re.search(r'Reserves',per.group(3)):
            if not card: debugNotify("0 Reserves multiplier because card is Null")
            else:
               reservesTotal = 0
               if re.search(r'ReservesTeam',per.group(3)):
                  for player in fetchAllAllies(card.controller): reservesTotal += len(player.piles['Common Reserve'])
               elif re.search(r'ReservesAllied',per.group(3)):
                  for player in fetchAllAllies(card.controller): 
                     if player != card.controller: reservesTotal += len(player.piles['Common Reserve'])
               elif re.search(r'ReservesOpponents',per.group(3)):
                  for player in fetchAllOpponents(card.controller): reservesTotal += len(player.piles['Common Reserve'])
               elif re.search(r'ReservesMyself',per.group(3)):
                  reservesTotal += len(card.controller.piles['Common Reserve'])
               multiplier = reservesTotal
      debugNotify("Checking ignore") # Debug.            
      ignS = re.search(r'-ignore([0-9]+)',Autoscript)
      if ignS: ignore = num(ignS.group(1))
      debugNotify("Checking div") # Debug.            
      divS = re.search(r'-div([0-9]+)',Autoscript)
      if divS: div = num(divS.group(1))
      debugNotify("Checking max") # Debug.            
      maxS = re.search(r'-max([0-9]+)',Autoscript)
      if maxS: max = num(maxS.group(1))
   else: multiplier = 1
   finalMultiplier = (multiplier - ignore) / div
   if max and finalMultiplier > max: 
      debugNotify("Reducing Multiplier to Max",2)
      finalMultiplier = max
   debugNotify("<<< per() with Multiplier: {}".format(finalMultiplier)) # Debug
   return finalMultiplier
   
