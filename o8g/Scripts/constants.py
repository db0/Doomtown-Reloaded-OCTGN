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

mdict = { # A dictionary which holds all the hard coded markers (in the markers file)
    'Bounty'               : ("Bounty",                     "0a5fabc8-fe56-481a-b45a-a9ad6917d0d9"),
    'Harrowed'             : ("Harrowed",                   "661f2771-6b73-414b-b0b1-3e2b50386b71"),
    'Ghost Rock'           : ("Ghost Rock",                 "42f8f2f3-2995-4556-b4d0-374f91811c82"),
    'UsedAbility'          : ("Used Ability",               "836dfd81-805b-489a-a3d6-b55d68ff5a71"),
    'SHActivated'          : ("Shootout Ability",           "197d8de5-d63f-4455-9144-7a106b192a02"),
    'PermInfluence'        : ("+1 Permanent Influence",     "2428921d-f3d0-4d01-9a4a-393f1557aab4"),
    'PermInfluence'        : ("-1 Permanent Influence",     "18c9ae50-e098-4c20-8981-f0751a6d8497"),
    'InfluencePlus'        : ("+1 Influence",               "43a4a6ba-d63b-46fd-8305-f9ffedf74f6d"),
    'InfluenceMinus'       : ("-1 Influence",               "b59df5b4-708b-481a-8b38-2d50eac48465"),
    'PermControl'          : ("+1 Permanent Control",       "e2c21df1-cc34-4a0e-aacf-9c458e6fd11d"),
    'PermControl'          : ("-1 Permanent Control",       "df3a9d1d-f60b-4304-aa1d-80f4d79d9ef4"),
    'ControlPlus'          : ("+1 Control",                 "6dbe2df7-4e9f-4e52-ab7d-c80afd7356ae"),
    'ControlMinus'         : ("-1 Control",                 "474f95a6-f1a9-4e23-ba4a-8eaba8b7cc0b"),
    'ProdPlus'             : ("+1 Production",              "ddba0f0a-0c34-48b5-b7ea-ad1e1ab07c12"),
    'ProdMinus'            : ("-1 Production",              "869eebe2-f503-4d9f-8fa3-af708c7ad70c"),
    'ValueNoonPlus'        : ("+1 Value",                   "baff5422-3654-4f74-86fa-782805082fab"),
    'ValueNoonMinus'       : ("-1 Value",                   "7fa426df-689e-41f5-91b8-5d06cbc46463"),
    'ValueShootoutPlus'    : ("+1 Shootout Value",          "ad3c4ae0-265f-4dcf-abc2-61189a99b728"),
    'ValueShootoutMinus'   : ("-1 Shootout Value",          "c2e4293c-85be-4b6a-8def-260647612a4b"),
    'ValuePermPlus'        : ("+1 Permanent Value",         "9707333a-514e-40fb-aca3-ad17f17b0f6d"),
    'ValuePermMinus'       : ("-1 Permanent Value",         "2bcb73c4-2ae9-46ac-8eaa-2d06aa37c908"),
    'BulletNoonPlus'       : ("+1 High Noon Bullet",        "5f740820-4c72-4042-b6eb-dcedc77c82ed"),
    'BulletShootoutPlus'   : ("+1 Shootout Bullet",         "093166b4-fddb-4e67-b6e4-86277faedc91"),
    'PermBulletPlus'       : ("+1 Permanent Bullet",        "a249871c-3cc6-4c7a-85d1-4d0fa7bbfead"),
    'PermBulletMinus'      : ("-1 Permanent Bullet",        "f1a85393-f482-47be-b2fa-09ef5feaacde"),
    'BulletNoonMinus'      : ("-1 High Noon Bullet",        "909d3755-8f49-4f46-a263-91427f275447"),
    'BulletShootoutMinus'  : ("-1 Shootout Bullet",         "15a965ec-5289-4e87-97c3-6e56bcc59ced"),
    'VPPlus'               : ("+1 VP",                      "dd40e5b9-f2c1-491c-b2b6-3312aa2d10d5"),
    'VPMinus'              : ("-1 VP",                      "8660fdc1-f8a5-40b1-a570-12018d17d654"),
    'Winner'               : ("Winner",                     "eeb5f447-f9fc-46b4-846a-a9a40e575cbc"),
    'NoUnboot'             : ("Does not Unboot",            "d2fccdc3-e93a-4c66-8930-28081aebb23c"),
    'Traded'               : ("Traded",                     "8ba2d501-e8b7-4df0-a168-be2d16b26daf")
}

regexHooks = dict( # A dictionary which holds the regex that then trigger each core command. 
                   # This is so that I can modify these "hooks" only in one place as I add core commands and modulators.
                  GainX =              re.compile(r'(?<![<,+-])(Gain|Lose|SetTo)([0-9]+)'),
                  CreateDummy =        re.compile(r'(?<![<,+-])CreateDummy'),
                  ReshuffleX =         re.compile(r'(?<![<,+-])Reshuffle([A-Za-z& ]+)'),
                  RollX =              re.compile(r'(?<![<,+-])Roll([0-9]+)'),
                  RequestInt =         re.compile(r'(?<![<,+-])RequestInt'),
                  DiscardX =           re.compile(r'(?<![<,+-])Discard[0-9]+'),
                  TokensX =            re.compile(r'(?<![<,+-])(Put|Remove|Refill|Use|Deal|Transfer)([0-9]+)'),
                  DrawX =              re.compile(r'(?<![<,+-])Draw([0-9]+)'),
                  RetrieveX =          re.compile(r'(?<![<,+-])Retrieve([0-9]+)'),
                  ShuffleX =           re.compile(r'(?<![<,+-])Shuffle([A-Za-z& ]+)'),
                  ModifyStatus =       re.compile(r'(?<!modAction|[<,+-])(Boot|Unboot|SendHomeBooted|Discard|Ace|Return|Play|SendToBottom|SendToDraw|Takeover|Participate|Unparticipate|Callout|Move)(Target|Host|Multi|Myself)'),
                  SimplyAnnounce =     re.compile(r'(?<![<,+-])SimplyAnnounce'),
                  GameX =              re.compile(r'(?<![<,+-])(Lose|Win)Game'),
                  ChooseKeyword =      re.compile(r'(?<![<,+-])ChooseKeyword'),
                  StartJob =           re.compile(r'(?<![<,+-])StartJob'),
                  PullX =              re.compile(r'(?<![<,+-])Pull'),
                  SpawnX =             re.compile(r'(?<![<,+-])Spawn'),
                  CustomScript =       re.compile(r'(?<![<,+-])CustomScript'),
                  UseCustomAbility =   re.compile(r'(?<![<,+-])UseCustomAbility'))


### Misc ###
CardWidth = 90
CardHeight = 126

loud = 'loud' # So that I don't have to use the quotes all the time in my function calls
silent = 'silent' # Same as above
shootout = 'shootout' # Same as above
Xaxis = 'x'  # Same as above
Yaxis = 'y'	 # Same as above

specialHostPlacementAlgs = {} # A Dictionary which holds tuples of X and Y placement offsets, for cards which place their hosted cards differently to normal.
