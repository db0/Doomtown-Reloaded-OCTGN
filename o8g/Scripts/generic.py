#---------------------------------------------------------------------------
# Custom Windows Forms
#---------------------------------------------------------------------------

try:
   import clr
   clr.AddReference("System.Drawing")
   clr.AddReference("System.Windows.Forms")

   from System.Windows.Forms import *
   from System.Drawing import Color
except:
   Automations['WinForms'] = False
   
def calcStringLabelSize(STRING): 
# A function which returns a slowly expansing size for a label. The more characters, the more the width expands to allow more characters on the same line.
   newlines = 0
   for char in STRING:
      if char == '\n': newlines += 1
   STRINGwidth = 200 + (len(STRING) / 4)
   STRINGheight = 30 + ((20 - newlines) * newlines) + (30 * (STRINGwidth / 100))
   return (STRINGwidth, STRINGheight)
 
def calcStringButtonHeight(STRING): 
# A function which returns a slowly expansing size for a label. The more characters, the more the width expands to allow more characters on the same line.
   newlines = 0
   for char in STRING:
      if char == '\n': newlines += 1
   STRINGheight = 30 + (8 * newlines) + (8 * (len(STRING) / 20))
   return STRINGheight
   
def formStringEscape(STRING): # A function to escape some characters that are not otherwise displayed by WinForms, like amperasands '&'
   slist = list(STRING)
   escapedString = ''
   for s in slist:
      if s == '&': char = '&&'
      else: char = s
      escapedString += char
   return escapedString

class OKWindow(Form): # This is a WinForm which creates a simple window, with some text and an OK button to close it.
   def __init__(self,InfoTXT):
      self.StartPosition = FormStartPosition.CenterScreen
      (STRwidth, STRheight) = calcStringLabelSize(InfoTXT)
      FORMheight = 160 + STRheight
      FORMwidth = 100 + STRwidth
      self.Text = 'Information'
      self.Height = FORMheight
      self.Width = FORMwidth
      self.AutoSize = True
      self.MinimizeBox = False
      self.MaximizeBox = False
      self.TopMost = True
      
      labelPanel = Panel()
      labelPanel.Dock = DockStyle.Top
      labelPanel.AutoSize = True
      labelPanel.BackColor = Color.White

      self.timer_tries = 0
      self.timer = Timer()
      self.timer.Interval = 200
      self.timer.Tick += self.onTick
      self.timer.Start()
      
      label = Label()
      label.Text = formStringEscape(InfoTXT)
      if debugVerbosity >= 2: label.Text += '\n\nTopMost: ' + str(self.TopMost) # Debug
      label.Top = 30
      label.Left = (self.ClientSize.Width - STRwidth) / 2
      label.Height = STRheight
      label.Width = STRwidth
      labelPanel.Controls.Add(label)
      #label.AutoSize = True #Well, that's shit.

      button = Button()
      button.Text = "OK"
      button.Width = 100
      button.Top = FORMheight - 80
      button.Left = (FORMwidth - 100) / 2
      button.Anchor = AnchorStyles.Bottom

      button.Click += self.buttonPressed

      self.Controls.Add(labelPanel)
      self.Controls.Add(button)

   def buttonPressed(self, sender, args):
      self.timer.Stop()
      self.Close()

   def onTick(self, sender, event):
      if self.timer_tries < 3:
         self.TopMost = False
         self.Focus()
         self.Activate()
         self.TopMost = True
         self.timer_tries += 1
            
def information(Message):
   debugNotify(">>> information() with message: {}".format(Message))
   if Automations['WinForms']:
      Application.EnableVisualStyles()
      form = OKWindow(Message)
      form.BringToFront()
      showWinForm(form)
   else: 
      confirm(Message)
   
   
class SingleChoiceWindow(Form):
 
   def __init__(self, BoxTitle, BoxOptions, type, defaultOption, pages = 0, cancelButtonBool = True, cancelName = 'Cancel'):
      self.Text = "Select an Option"
      self.index = 0
      self.confirmValue = None
      self.MinimizeBox = False
      self.MaximizeBox = False
      self.StartPosition = FormStartPosition.CenterScreen
      self.AutoSize = True
      self.TopMost = True
      
      (STRwidth, STRheight) = calcStringLabelSize(BoxTitle)
      self.Width = STRwidth + 50

      self.timer_tries = 0
      self.timer = Timer()
      self.timer.Interval = 200
      self.timer.Tick += self.onTick
      self.timer.Start()
      
      labelPanel = Panel()
      labelPanel.Dock = DockStyle.Top
      labelPanel.AutoSize = True
      labelPanel.BackColor = Color.White
      
      separatorPanel = Panel()
      separatorPanel.Dock = DockStyle.Top
      separatorPanel.Height = 20
      
      choicePanel = Panel()
      choicePanel.Dock = DockStyle.Top
      choicePanel.AutoSize = True

      self.Controls.Add(labelPanel)
      labelPanel.BringToFront()
      self.Controls.Add(separatorPanel)
      separatorPanel.BringToFront()
      self.Controls.Add(choicePanel)
      choicePanel.BringToFront()

      label = Label()
      label.Text = formStringEscape(BoxTitle)
      if debugVerbosity >= 2: label.Text += '\n\nTopMost: ' + str(self.TopMost) # Debug
      label.Top = 30
      label.Left = (self.ClientSize.Width - STRwidth) / 2
      label.Height = STRheight
      label.Width = STRwidth
      labelPanel.Controls.Add(label)
      
      bufferPanel = Panel() # Just to put the radio buttons a bit more to the middle
      bufferPanel.Left = (self.ClientSize.Width - bufferPanel.Width) / 2
      bufferPanel.AutoSize = True
      choicePanel.Controls.Add(bufferPanel)
            
      for option in BoxOptions:
         if type == 'radio':
            btn = RadioButton()
            if defaultOption == self.index: btn.Checked = True
            else: btn.Checked = False
            btn.CheckedChanged += self.checkedChanged
         else: 
            btn = Button()
            btn.Height = calcStringButtonHeight(formStringEscape(option))
            btn.Click += self.choiceMade
         btn.Name = str(self.index)
         self.index = self.index + 1
         btn.Text = formStringEscape(option)
         btn.Dock = DockStyle.Top
         bufferPanel.Controls.Add(btn)
         btn.BringToFront()

      button = Button()
      button.Text = "Confirm"
      button.Width = 100
      button.Dock = DockStyle.Bottom
      button.Click += self.buttonPressed
      if type == 'radio': self.Controls.Add(button) # We only add the "Confirm" button on a radio menu.
 
      buttonNext = Button()
      buttonNext.Text = "Next Page"
      buttonNext.Width = 100
      buttonNext.Dock = DockStyle.Bottom
      buttonNext.Click += self.nextPage
      if pages > 1: self.Controls.Add(buttonNext) # We only add the "Confirm" button on a radio menu.

      cancelButton = Button() # We add a bytton to Cancel the selection
      cancelButton.Text = cancelName # We can rename the cancel button if we want to.
      cancelButton.Width = 100
      cancelButton.Dock = DockStyle.Bottom
      #button.Anchor = AnchorStyles.Bottom
      cancelButton.Click += self.cancelPressed
      if cancelButtonBool: self.Controls.Add(cancelButton)
      
   def buttonPressed(self, sender, args):
      self.timer.Stop()
      self.Close()

   def nextPage(self, sender, args):
      self.confirmValue = "Next Page"
      self.timer.Stop()
      self.Close()
 
   def cancelPressed(self, sender, args): # The function called from the cancelButton
      self.confirmValue = None # It replaces the choice list with an ABORT message which is parsed by the calling function
      self.timer.Stop()
      self.Close() # And then closes the form
      
   def checkedChanged(self, sender, args):
      self.confirmValue = sender.Name
      
   def choiceMade(self, sender, args):
      self.confirmValue = sender.Name
      self.timer.Stop()
      self.Close()
      
   def getIndex(self):
      return self.confirmValue

   def onTick(self, sender, event):
      if self.timer_tries < 3:
         self.TopMost = False
         self.Focus()
         self.Activate()
         self.TopMost = True
         self.timer_tries += 1

def SingleChoice(title, options, type = 'button', default = 0, cancelButton = True, cancelName = 'Cancel'):
   debugNotify(">>> SingleChoice()".format(title))
   ### Old WinForms code is (hopefully) obsolete now
   # if Automations['WinForms']:
      # optChunks=[options[x:x+7] for x in xrange(0, len(options), 7)]
      # optCurrent = 0
      # choice = "New"
      # while choice == "New" or choice == "Next Page" or (not choice and not cancelButton):
         # Application.EnableVisualStyles()
         # form = SingleChoiceWindow(title, optChunks[optCurrent], type, default, pages = len(optChunks), cancelButtonBool = cancelButton, cancelName = cancelName)
         # form.BringToFront()
         # showWinForm(form)
         # choice = form.getIndex()
         # debugNotify("choice is: {}".format(choice), 2)
         # if choice == "Next Page": 
            # debugNotify("Going to next page", 3)
            # optCurrent += 1
            # if optCurrent >= len(optChunks): optCurrent = 0
         # elif choice != None: 
            # choice = num(form.getIndex()) + (optCurrent * 7) # if the choice is not a next page, then we convert it to an integer and give that back, adding 8 per number of page passed
   # else:
   choice = "New"
   if cancelButton: customButtonsList = [cancelName]
   else: customButtonsList = []
   while choice == "New" or (choice == None and not cancelButton):
      choice = askChoice(title, options, customButtons = customButtonsList)
      debugNotify("choice is: {}".format(choice), 2)
      if choice > 0: choice -= 1 # Reducing by 1 because askChoice() starts from 1 but my code expects to start from 0
      elif choice <= 0: choice = None
   debugNotify("<<< SingleChoice() with return {}".format(choice), 3)
   return choice
 
   
class MultiChoiceWindow(Form):
 # This is a windows form which creates a multiple choice form, with a button for each choice. 
 # The player can select more than one, and they are then returned as a list of integers
   def __init__(self, FormTitle, FormChoices,CPType, pages = 0,currPage = 0, existingChoices = []): # We initialize our form, expecting 3 variables. 
                                                      # FormTitle is the title of the window itself
                                                      # FormChoices is a list of strings which we use for the names of the buttons
                                                      # CPType is combined with FormTitle to give a more thematic window name.
      self.Text = CPType # We just store the variable locally
      self.index = 0 # We use this variable to set a number to each button
      self.MinimizeBox = False # We hide the minimize button
      self.MaximizeBox = False # We hide the maximize button
      self.StartPosition = FormStartPosition.CenterScreen # We start the form at the center of the player's screen
      self.AutoSize = True # We allow the form to expand in size depending on its contents
      self.TopMost = True # We make sure our new form will be on the top of all other windows. If we didn't have this here, fullscreen OCTGN would hide the form.
      self.origTitle = formStringEscape(FormTitle) # Used when modifying the label from a button
      
      self.confirmValue = existingChoices
      debugNotify("existingChoices = {}".format(self.confirmValue))
      self.nextPageBool = False  # self.nextPageBool is just remembering if the player has just flipped the page.
      self.currPage = currPage
      
      self.timer_tries = 0 # Ugly hack to fix the form sometimes not staying on top of OCTGN
      self.timer = Timer() # Create a timer object
      self.timer.Interval = 200 # Speed is at one 'tick' per 0.2s
      self.timer.Tick += self.onTick # Activate the event function on each tick
      self.timer.Start() # Start the timer.
      
      (STRwidth, STRheight) = calcStringLabelSize(FormTitle) # We dynamically calculate the size of the text label to be displayed as info to the player.
      labelPanel = Panel() # We create a new panel (e.g. container) to store the label.
      labelPanel.Dock = DockStyle.Top # We Dock the label's container on the top of the form window
      labelPanel.Height = STRheight # We setup the dynamic size
      labelPanel.Width = STRwidth
      labelPanel.AutoSize = True # We allow the panel to expand dynamically according to the size of the label
      labelPanel.BackColor = Color.White
      
      choicePanel = Panel() # We create a panel to hold our buttons
      choicePanel.Dock = DockStyle.Top # We dock this below the label panel
      choicePanel.AutoSize = True # We allow it to expand in size dynamically
      #radioPanel.BackColor = Color.LightSalmon # Debug

      separatorPanel = Panel() # We create a panel to separate the labels from the buttons
      separatorPanel.Dock = DockStyle.Top # It's going to be docked to the middle of both
      separatorPanel.Height = 20 # Only 20 pixels high

      self.Controls.Add(labelPanel) # The panels need to be put in the form one by one
      labelPanel.BringToFront() # This basically tells that the last panel we added should go below all the others that are already there.
      self.Controls.Add(separatorPanel)
      separatorPanel.BringToFront() 
      self.Controls.Add(choicePanel) 
      choicePanel.BringToFront() 

      self.label = Label() # We create a label object which will hold the multiple choice description text
      #if len(self.confirmValue): self.label.Text = formStringEscape(FormTitle) + "\n\nYour current choices are:\n{}".format(self.confirmValue) # We display what choices we've made until now to the player.
      self.label.Text = formStringEscape(FormTitle) # We escape any strings that WinForms doesn't like, like ampersand and store it in the label
      if debugVerbosity >= 2: self.label.Text += '\n\nTopMost: ' + str(self.TopMost) # Debug
      self.label.Top = 30 # We place the label 30 pixels from the top size of its container panel, and 50 pixels from the left.
      self.label.Left = 50
      self.label.Height = STRheight # We set its dynamic size
      self.label.Width = STRwidth
      labelPanel.Controls.Add(self.label) # We add the label to its container
      
      choicePush = Panel() # An extra secondary container for the buttons, that is not docked, to allow us to slightly change its positioning
      choicePush.Left = (self.ClientSize.Width - choicePush.Width) / 2 # We move it 50 pixels to the left
      choicePush.AutoSize = True # We allow it to expand dynamically
      choicePanel.Controls.Add(choicePush) # We add it to its parent container
      
      for option in FormChoices: # We dynamically add as many buttons as we have options
         btn = Button() # We initialize a button object
         btn.Name = str(self.index) # We name the button equal to its numeric value, plus its effect.
         btn.Text = str(self.index) + ':--> ' + formStringEscape(option)
         self.index = self.index + 1 # The internal of the button is also the choice that will be put in our list of integers. 
         btn.Dock = DockStyle.Top # We dock the buttons one below the other, to the top of their container (choicePush)
         btn.AutoSize = True # Doesn't seem to do anything
         btn.Height = calcStringButtonHeight(formStringEscape(option))
         btn.Click += self.choiceMade # This triggers the function which records each choice into the confirmValue[] list
         choicePush.Controls.Add(btn) # We add each button to its panel
         btn.BringToFront() # Add new buttons to the bottom of existing ones (Otherwise the buttons would be placed in reverse numerical order)

      buttonNext = Button()
      buttonNext.Text = "Next Page"
      buttonNext.Width = 100
      buttonNext.Dock = DockStyle.Bottom
      buttonNext.Click += self.nextPage
      if pages > 1: self.Controls.Add(buttonNext) # We only add the "Confirm" button on a radio menu.

      finishButton = Button() # We add a button to Finish the selection
      finishButton.Text = "Finish Selection"
      finishButton.Width = 100
      finishButton.Dock = DockStyle.Bottom # We dock it to the bottom of the form.
      #button.Anchor = AnchorStyles.Bottom
      finishButton.Click += self.finishPressed # We call its function
      self.Controls.Add(finishButton) # We add the button to the form
 
      cancelButton = Button() # We add a bytton to Cancel the selection
      cancelButton.Text = "Cancel"
      cancelButton.Width = 100
      cancelButton.Dock = DockStyle.Bottom
      #button.Anchor = AnchorStyles.Bottom
      cancelButton.Click += self.cancelPressed
      self.Controls.Add(cancelButton)

   def nextPage(self, sender, args):
      self.nextPageBool = True
      self.timer.Stop()
      self.Close()
 
   def finishPressed(self, sender, args): # The function called from the finishButton.
      self.timer.Stop()
      self.Close()  # It just closes the form

   def cancelPressed(self, sender, args): # The function called from the cancelButton
      self.confirmValue = 'ABORT' # It replaces the choice list with an ABORT message which is parsed by the calling function
      self.timer.Stop()
      self.Close() # And then closes the form
 
   def choiceMade(self, sender, args): # The function called when pressing one of the choice buttons
      self.confirmValue.append((self.currPage * 7) + int(sender.Name)) # We append the button's name to the existing choices list
      self.label.Text = self.origTitle + "\n\nYour current choices are:\n{}".format(self.confirmValue) # We display what choices we've made until now to the player.
 
   def getIndex(self): # The function called after the form is closed, to grab its choices list
      if self.nextPageBool: 
         self.nextPageBool = False
         return "Next Page"
      else: return self.confirmValue

   def getStoredChoices(self): # The function called after the form is closed, to grab its choices list
      return self.confirmValue

   def onTick(self, sender, event): # Ugly hack required because sometimes the winform does not go on top of all
      if self.timer_tries < 3: # Try three times to bring the form on top
         if debugVerbosity >= 2: self.label.Text = self.origTitle + '\n\n### Timer Iter: ' + str(self.timer_tries)
         self.TopMost = False # Set the form as not on top
         self.Focus() # Focus it
         self.Activate() # Activate it
         self.TopMost = True # And re-send it to top
         self.timer_tries += 1 # Increment this counter to stop after 3 tries.

def multiChoice(title, options): # This displays a choice where the player can select more than one ability to trigger serially one after the other
   debugNotify(">>> multiChoice()".format(title))
   if Automations['WinForms']: # If the player has not disabled the custom WinForms, we use those
      optChunks=[options[x:x+7] for x in xrange(0, len(options), 7)]
      optCurrent = 0
      choices = "New"
      currChoices = []
      while choices == "New" or choices == "Next Page":
         Application.EnableVisualStyles() # To make the window look like all other windows in the user's system
         CPType = 'Control Panel'
         debugNotify("About to open form")
         if choices == "Next Page": nextPageBool = True
         else: nextPageBool = False
         form = MultiChoiceWindow(title, optChunks[optCurrent], CPType, pages = len(optChunks), currPage = optCurrent, existingChoices = currChoices) # We create an object called "form" which contains an instance of the MultiChoice windows form.
         showWinForm(form) # We bring the form to the front to allow the user to make their choices
         choices = form.getIndex() # Once the form is closed, we check an internal variable within the form object to grab what choices they made
         debugNotify("choices = {}".format(choices))
         if choices == "Next Page": 
            debugNotify("Going to next page", 4)
            optCurrent += 1
            if optCurrent >= len(optChunks): optCurrent = 0
            currChoices = form.getStoredChoices()
            debugNotify("currChoices = {}".format(currChoices))
   else: # If the user has disabled the windows forms, we use instead the OCTGN built-in askInteger function
      concatTXT = title + "\n\n(Tip: You can put multiple abilities one after the the other (e.g. '110'). Max 9 at once)\n\n" # We prepare the text of the window with a concat string
      for iter in range(len(options)): # We populate the concat string with the options
         concatTXT += '{}:--> {}\n'.format(iter,options[iter])
      choicesInteger = askInteger(concatTXT,0) # We now ask the user to put in an integer.
      if choicesInteger == None: choices = 'ABORT' # If the user just close the window, abort.
      else: 
         choices = list(str(choicesInteger)) # We convert our number into a list of numeric chars
         for iter in range(len(choices)): choices[iter] = int(choices[iter]) # we convert our list of chars into a list of integers      
   debugNotify("<<< multiChoice() with list: {}".format(choices), 3)
   return choices # We finally return a list of integers to the previous function. Those will in turn be iterated one-by-one serially.
      
#---------------------------------------------------------------------------
# General functions
#---------------------------------------------------------------------------
            
def num (s): 
# This function reads the value of a card and returns an integer. For some reason integer values of cards are not processed correctly
# see bug 373 https://octgn.16bugs.com/projects/3602/bugs/188805
# This function will also return 0 if a non-integer or an empty value is provided to it as it is required to avoid crashing your functions.
#   if s == '+*' or s == '*': return 0
   if not s: return 0
   try:
      return int(s)
   except ValueError:
      return 0

def defPlayerColor(): # Obsolete in OCTGN 3 but leaving it here in case I find another use for it.
# Provide a random highlight colour for the player which we use to simulate ownership
   global PlayerColor
   if len(PlayerColor) == 7 : return
   RGB = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
   for i in range(6): PlayerColor += RGB[rnd(0,15)]

def debugNotify(msg = 'Debug Ping!', level = 1):
   if not re.search(r'<<<',msg) and not re.search(r'>>>',msg):
      hashes = '#' 
      for iter in range(level): hashes += '#' # We add extra hashes at the start of debug messages equal to the level of the debug+1, to make them stand out more
      msg = hashes + ' ' +  msg
   if re.search(r'<<<',msg): level = 3 # We always request level debug logs to display function exist notifications.
   if debugVerbosity >= level: notify(msg)

def barNotifyAll(color, msg, remote = False): # A function that takes care to send barNotifyAll() messages to all players
   mute()
   for player in getPlayers():
      if player != me and not remote: remoteCall(player,'barNotifyAll',[color,msg,True])
   notifyBar(color,msg)
      
def delayed_whisper(text): # Because whispers for some reason execute before notifys
   rnd(1,10)
   whisper(text)

def numOrder(num):
    """Return the ordinal for each place in a zero-indexed list.

    list[0] (the first item) returns '1st', list[1] return '2nd', etc.
    """
    def int_to_ordinal(i):
        """Return the ordinal for an integer."""
        # if i is a teen (e.g. 14, 113, 2517), append 'th'
        if 10 <= i % 100 < 20:
            return str(i) + 'th'
        # elseif i ends in 1, 2 or 3 append 'st', 'nd' or 'rd'
        # otherwise append 'th'
        else:
            return  str(i) + {1 : 'st', 2 : 'nd', 3 : 'rd'}.get(i % 10, "th")
    return int_to_ordinal(num + 1)

def sortPriority(cardList):
   if debugVerbosity >= 1: notify(">>> sortPriority() with cardList: {}".format([c.name for c in cardList])) #Debug
   priority1 = []
   priority2 = []
   priority3 = []
   sortedList = []
   for card in cardList:
      if card.highlight == PriorityColor: # If a card is clearly highlighted for priority, we use its counters first.
         priority1.append(card)
      elif card.targetedBy and card.targetedBy == me: # If a card it targeted, we give it secondary priority in losing its counters.
         priority2.append(card)   
      else: # If a card is neither of the above, then the order is defined on how they were put on the table.
         priority3.append(card) 
   sortedList.extend(priority1)
   sortedList.extend(priority2)
   sortedList.extend(priority3)
   if debugVerbosity >= 3: 
      notify("<<< sortPriority() returning {}".format([sortTarget.name for sortTarget in sortedList])) #Debug
   return sortedList

def findMarker(card, markerDesc): # Goes through the markers on the card and looks if one exist with a specific description
   if debugVerbosity >= 1: notify(">>> findMarker(){}".format(extraASDebug())) #Debug
   foundKey = None
   if markerDesc in mdict: markerDesc = mdict[markerDesc][0] # If the marker description is the code of a known marker, then we need to grab the actual name of that.
   for key in card.markers:
      debugNotify("### Key: {}\nmarkerDesc: {}".format(key[0],markerDesc)) # Debug
      if re.search(r'{}'.format(markerDesc.replace('+','\+')),key[0]) or markerDesc == key[0]: # We need to replace any '+' in the marker names to escaped \+ otherwise the regex statement gets confused
         foundKey = key
         if debugVerbosity >= 2: notify("### Found {} on {}".format(key[0],card))
         break
   if debugVerbosity >= 3: notify("<<< findMarker() by returning: {}".format(foundKey))
   return foundKey
      
def getActivePlayers():
   return [player for player in getPlayers() if len(player.Deck) > 0 or len(player.piles['Discard Pile']) > 0 or len(player.hand) > 0]
   
def claimCard(card, player = me): # Requests the controller of a card to pass control to another player (script runner by default)
   if card.controller != player: # If the card is already ours, we do not need to do anything.
      prevController = card.controller
      prevGroup = card.group
      remoteCall(card.controller,'giveCard', [card,player])
       # We make sure all network calls have completed before continuing.
      count = 0
      while card.controller != player: 
         rnd(1,10)
         update()
         debugNotify("iteration {}. Controller is {} and it should be {}".format(count,card.controller, player), 4)
         count += 1
         if count >= 10:
            debugNotify(":::ERROR::: claimCard() failed. Card controller still {} instead of {}. Giving up".format(card.controller.name,player)) # This always seems to fail (https://github.com/kellyelton/OCTGN/issues/416#issuecomment-31157031)
            return
      #if prevGroup == table: autoscriptOtherPlayers('{}:CardTakeover:{}'.format(player,prevController),card)
   
def giveCard(card,player,pile = None): # Passes control of a card to a given player.
   mute()
   if card.group == table: 
      prevController = card.controller
      card.setController(player)
      autoscriptOtherPlayers('{}:CardTakeover:{}'.format(player,prevController),card)
   else: 
      if pile: card.moveTo(pile) # If we pass a pile variable, it means we likely want to return the card to its original location (say after an aborted capture)
      else: card.moveTo(player.ScriptingPile)
      # If the card is in one of our piles, we cannot pass control to another player since we control the whole pile. We need to move it to their scripting pile. 
      # This should automatically also pass control to the controller of that pile
   update()

def grabPileControl(pile, player = me):
   if pile.controller != player:
      if pile.controller != me: remoteCall(pile.controller,'passPileControl',[pile,player])
      else: passPileControl(pile,player) # We don't want to do a remote call if the current controller is ourself, as the call we go out after we finish all scripts, which will end up causing a delay later while the game is checking if control pass is done.
   count = 0
   while pile.controller != player: 
      if count >= 2 and not count % 2: notify("=> {} is still trying to take control of {}...".format(player,pileName(pile)))
      rnd(1,100)
      count += 1
      if count >= 3: 
         notify(":::ERROR::: Pile Control not passed! Will see errors.")
         break   

def passPileControl(pile,player):
   mute()
   update()
   pile.setController(player)
   
def fetchHost(card):
   host = None
   hostCards = eval(getGlobalVariable('Host Cards'))
   hostID = hostCards.get(card._id,None)
   if hostID: host = Card(hostID) 
   return host
         
#---------------------------------------------------------------------------
# Card Placement functions
#---------------------------------------------------------------------------

def cwidth(card = None, divisor = 10):
#if debugVerbosity >= 1: notify(">>> cwidth(){}".format(extraASDebug())) #Debug
# This function is used to always return the width of the card plus an offset that is based on the percentage of the width of the card used.
# The smaller the number given, the less the card is divided into pieces and thus the larger the offset added.
# For example if a card is 80px wide, a divisor of 4 will means that we will offset the card's size by 80/4 = 20.
# In other words, we will return 1 + 1/4 of the card width. 
# Thus, no matter what the size of the table and cards becomes, the distances used will be relatively the same.
# The default is to return an offset equal to 1/10 of the card width. A divisor of 0 means no offset.
   if divisor == 0: offset = 0
   else: offset = CardWidth / divisor
   return (CardWidth + offset)

def cheight(card = None, divisor = 10):
   #if debugVerbosity >= 1: notify(">>> cheight(){}".format(extraASDebug())) #Debug
   if divisor == 0: offset = 0
   else: offset = CardHeight / divisor
   return (CardHeight + offset)

def placeCard(card,type = None, dudecount = 0):
# This function automatically places a card on the table according to what type of card is being placed
# It is called by one of the various custom types and each type has a different value depending on if the player is on the X or Y axis.
   global strikeCount, posSideCount, negSideCount
   if playeraxis == Xaxis:
      if type == 'HireDude' or (type == None and card.Type == 'Dude'):
         # Move the dude next to where we expect the player's home card to be.
         card.moveToTable(homeDistance(card) + (playerside * cwidth(card,-4)), 0)
      if type == 'BuyDeed' or (type == None and card.Type == 'Deed'):
         if re.search('Out of Town', card.Keywords): # Check if we're bringing out an out of town deed
            card.moveToTable(homeDistance(card) + 2 * cardDistance(card), (-1 * cheight(card,4) * 2) + strikeCount * cheight(card))
            strikeCount += 1 # Increment this counter. Extra out of town deeds will be placed below the previous ones.
         else:
            if confirm("Do you want to place this deed on the bottom side of your street?"): # If it's a city deed, then ask the player where they want it.
               negSideCount += 1 #If it's on the bottom, increment the counter...
               card.moveToTable(homeDistance(card), negSideCount * cheight(card)) # ...and put the deed below all other deeds already there.
            else:
               posSideCount += 1 # Same as above but going upwards from home.
               card.moveToTable(homeDistance(card), -1 * (posSideCount * cheight(card)))     
      if type == 'SetupHome':
         card.moveToTable(homeDistance(card), 0) # We move it to one side depending on what side the player chose.
      if type == 'SetupDude':
         card.moveToTable(homeDistance(card) + cardDistance(card) + playerside * (dudecount * cwidth(card)), 0) 
         # We move them behind the house
      if type == 'SetupOther':
         card.moveToTable(playerside * (cwidth(card,4) * 3), playerside * -1 * cheight(card)) # We move the card around the player's area.      
   elif playeraxis == Yaxis:
      if type == 'HireDude' or (type == None and card.Type == 'Dude'):# Hire dudes on your home + one card height - 20% of a card height
         card.moveToTable(0,homeDistance(card) + (playerside * cheight(card,-4)))
      if type == 'BuyDeed' or (type == None and card.Type == 'Deed'): 
         if re.search('Out of Town', card.Keywords): # Check if we're bringing out an out of town deed
            card.moveToTable((playerside * cwidth(card,4) * 5) + strikeCount * cwidth(card) * playerside, homeDistance(card) + cardDistance(card))
            strikeCount += 1 
         else:
            if confirm("Do you want to place this deed on the right side of your street?"): # If it's a city deed, then ask the player where they want it.
               negSideCount += 1 #If it's on the right, increment the counter...
               card.moveToTable(negSideCount * cwidth(card),homeDistance(card)) # ...and put the deed below all other deeds already there.
            else:
               posSideCount += 1 # Same as above but going leftwards from home.
               card.moveToTable(-1 * (posSideCount * cwidth(card)),homeDistance(card))       
      if type == 'SetupHome':
         card.moveToTable(0,homeDistance(card)) 
      if type == 'SetupDude': # Setup your dudes one card height behind your home and in a horizontal line
         card.moveToTable(-cwidth(card) + (dudecount * cwidth(card)),homeDistance(card) + cardDistance(card)) 
      if type == 'SetupOther':
         card.moveToTable(playerside * -3 * cwidth(card), playerside * (cheight(card,4) * 3)) 
   else: card.moveToTable(0,0)
   
def homeDistance(card = None):
# This function retusn the distance from the middle each player's home will be setup towards their playerSide. 
# This makes the code more readable and allows me to tweak these values from one place
   if playeraxis == Xaxis:
      return (playerside * cwidth() * 5) # players on the X axis, are placed 5 times a card's width towards their side (left or right)
   elif playeraxis == Yaxis:
      return (playerside * cheight() * 3) # players on the Y axis, are placed 3 times a card's height towards their side (top or bottom)

def cardDistance(card = None):
# This function returns the size of the card towards a player's side. 
# This is useful when playing cards on the table, as you can always manipulate the location
#   by multiples of the card distance towards your side
# So for example, if a player is playing on the bottom side. This function will always return a positive cardheight.
#   Thus by adding this in a moveToTable's y integer, the card being placed will be moved towards your side by one multiple of card height
#   While if you remove it from the y integer, the card being placed will be moved towards the centre of the table by one multiple of card height.
   if playeraxis == Yaxis:
      return (playerside * cheight())
   else:
      return (playerside * cwidth())

#------------------------------------------------------------------------------
# Remote Calls
#------------------------------------------------------------------------------
      
def delCard(card,wait = False):
   mute()
   if card.controller == me:
      card.delete()
   else: 
      remoteCall(card.controller,"delCard",[card])
      if wait:
         count = 0
         try: # We need to do a try/except, because if the card has been deleted, then it won't have a group class to check.
            while card.group == table: # This is then only way to check if the card has been deleted yet.
               rnd(1,10)
               count += 1
               if count == 10: break
         except: pass # This means the card has been deleted.
      
def moveCard(card,x,y):
   mute()
   card.moveToTable(x, y)

def setPlayerVariable(var,value):
   mute()
   me.setGlobalVariable(var,value)