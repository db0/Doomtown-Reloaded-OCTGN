#---------------------------------------------------------------------------
# Constants
#---------------------------------------------------------------------------
import re

phases = [
    '{} is currently in the Pre-game Setup Phase'.format(me),
    "It is now GAMBLIN' time. Play Lowball!",
    "The time has come to pay your UPKEEP",
    "It is now HIGH NOON",
    "SUNDOWN has come."]

### Highlight Colours ###
DoesntUnbootColor = "#ffffff"
AttackColor = "#ff0000"
DefendColor = "#0000ff"
DrawHandColor = "#000000"
EventColor = "#00ff00"
DummyColor = "#005566"
InitiateColor = "#ff8700"


### Deprecated Markers ###
HarrowedMarker = ("harrowed", "661f2771-6b73-414b-b0b1-3e2b50386b71")
SHActivatedMarker = ("Shootout Ability", "197d8de5-d63f-4455-9144-7a106b192a02")
#InfluencePlusMarker = ("+1 Influence", "43a4a6ba-d63b-46fd-8305-f9ffedf74f6d")
#InfluenceMinusMarker = ("-1 Influence", "b59df5b4-708b-481a-8b38-2d50eac48465")
#ControlPlusMarker = ("+1 Control", "6dbe2df7-4e9f-4e52-ab7d-c80afd7356ae")
#ControlMinusMarker = ("-1 Control", "474f95a6-f1a9-4e23-ba4a-8eaba8b7cc0b")
#ProdPlusMarker = ("+1 Production", "ddba0f0a-0c34-48b5-b7ea-ad1e1ab07c12")
#ProdMinusMarker = ("-1 Production", "869eebe2-f503-4d9f-8fa3-af708c7ad70c")
#ValuePlusMarker = ("+1 Value", "baff5422-3654-4f74-86fa-782805082fab")
#ValueMinusMarker = ("-1 Value", "7fa426df-689e-41f5-91b8-5d06cbc46463")
#BulletPlusMarker = ("+1 Bullet", "5f740820-4c72-4042-b6eb-dcedc77c82ed")
#BulletMinusMarker = ("-1 Bullet", "093166b4-fddb-4e67-b6e4-86277faedc91")
#WinnerMarker = ("Winner", "eeb5f447-f9fc-46b4-846a-a9a40e575cbc")


mdict = { # A dictionary which holds all the hard coded markers (in the markers file)
    'Bounty'               : ("Bounty",                     "0a5fabc8-fe56-481a-b45a-a9ad6917d0d9"),
    'Harrowed'             : ("Harrowed",                   "661f2771-6b73-414b-b0b1-3e2b50386b71"),
    'Ghost Rock'           : ("Ghost Rock",                 "42f8f2f3-2995-4556-b4d0-374f91811c82"),
    'UsedAbility'          : ("Used Ability",               "836dfd81-805b-489a-a3d6-b55d68ff5a71"),
    'SHActivated'          : ("Shootout Ability",           "197d8de5-d63f-4455-9144-7a106b192a02"),
    'PermInfluence'        : ("+1 Permanent Influence",     "2428921d-f3d0-4d01-9a4a-393f1557aab4"),
    'InfluencePlus'        : ("+1 Influence",               "43a4a6ba-d63b-46fd-8305-f9ffedf74f6d"),
    'InfluenceMinus'       : ("-1 Influence",               "b59df5b4-708b-481a-8b38-2d50eac48465"),
    'PermControl'          : ("+1 Permanent Control",       "e2c21df1-cc34-4a0e-aacf-9c458e6fd11d"),
    'ControlPlus'          : ("+1 Control",                 "6dbe2df7-4e9f-4e52-ab7d-c80afd7356ae"),
    'ControlMinus'         : ("-1 Control",                 "474f95a6-f1a9-4e23-ba4a-8eaba8b7cc0b"),
    'ProdPlus'             : ("+1 Production",              "ddba0f0a-0c34-48b5-b7ea-ad1e1ab07c12"),
    'ProdMinus'            : ("-1 Production",              "869eebe2-f503-4d9f-8fa3-af708c7ad70c"),
    'ValuePlus'            : ("+1 Value",                   "baff5422-3654-4f74-86fa-782805082fab"),
    'ValueMinus'           : ("-1 Value",                   "7fa426df-689e-41f5-91b8-5d06cbc46463"),
    'BulletNoonPlus'       : ("+1 High Noon Bullet",        "5f740820-4c72-4042-b6eb-dcedc77c82ed"),
    'BulletShootoutPlus'   : ("+1 Shootout Bullet",         "093166b4-fddb-4e67-b6e4-86277faedc91"),
    'PermBullet'           : ("+1 Permanent Bullet",        "a249871c-3cc6-4c7a-85d1-4d0fa7bbfead"),
    'BulletNoonMinus'      : ("-1 High Noon Bullet",        "909d3755-8f49-4f46-a263-91427f275447"),
    'BulletShootoutMinus'  : ("-1 Shootout Bullet",         "15a965ec-5289-4e87-97c3-6e56bcc59ced"),
    'VPPlus'               : ("+1 VP",                      "dd40e5b9-f2c1-491c-b2b6-3312aa2d10d5"),
    'VPMinus'              : ("-1 VP",                      "8660fdc1-f8a5-40b1-a570-12018d17d654"),
    'Winner'               : ("Winner",                     "eeb5f447-f9fc-46b4-846a-a9a40e575cbc"),
    'Traded'               : ("Traded",                     "8ba2d501-e8b7-4df0-a168-be2d16b26daf")
}

regexHooks = dict( # A dictionary which holds the regex that then trigger each core command. 
                   # This is so that I can modify these "hooks" only in one place as I add core commands and modulators.
                  GainX =              re.compile(r'\b(Gain|Lose|SetTo)([0-9]+)'),
                  CreateDummy =        re.compile(r'\bCreateDummy'),
                  ReshuffleX =         re.compile(r'\bReshuffle([A-Za-z& ]+)'),
                  RollX =              re.compile(r'\bRoll([0-9]+)'),
                  RequestInt =         re.compile(r'\bRequestInt'),
                  DiscardX =           re.compile(r'\bDiscard[0-9]+'),
                  TokensX =            re.compile(r'\b(Put|Remove|Refill|Use|Deal|Transfer)([0-9]+)'),
                  DrawX =              re.compile(r'\bDraw([0-9]+)'),
                  RetrieveX =          re.compile(r'\bRetrieve([0-9]+)'),
                  ShuffleX =           re.compile(r'\bShuffle([A-Za-z& ]+)'),
                  ModifyStatus =       re.compile(r'(?<!modAction):(Boot|Unboot|SendHomeBooted|Discard|Ace|Return|Play|SendToBottom|Takeover|Participate|Unparticipate|Callout|Move)(Target|Host|Multi|Myself)'),
                  SimplyAnnounce =     re.compile(r'\bSimplyAnnounce'),
                  GameX =              re.compile(r'\b(Lose|Win)Game'),
                  ChooseKeyword =      re.compile(r'\bChooseKeyword'),
                  StartJob =           re.compile(r'\bStartJob'),
                  PullX =              re.compile(r'\bPull'),
                  SpawnX =             re.compile(r'\bSpawn'),
                  CustomScript =       re.compile(r'\bCustomScript'),
                  UseCustomAbility =   re.compile(r'\bUseCustomAbility'))


### Misc ###
CardWidth = 90
CardHeight = 126

loud = 'loud' # So that I don't have to use the quotes all the time in my function calls
silent = 'silent' # Same as above
shootout = 'shootout' # Same as above
Xaxis = 'x'  # Same as above
Yaxis = 'y'	 # Same as above

specialHostPlacementAlgs = {} # A Dictionary which holds tuples of X and Y placement offsets, for cards which place their hosted cards differently to normal.
