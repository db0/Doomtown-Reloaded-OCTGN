### ANR CARD SCRIPTS ###
# 5 Equal Signs (=) signifiies a break between the description (what you're currently reading) and the code
# 5 Dashes  (-) signifies a break between the card name, the GUID and the card scripts. The card name is ignored by the code, only the GUID and Scripts are used.
# 5 Plus Signs (+) signifies a break between AutoActions and AutoScripts for the same card
# 5 Dots (.) signifies a break between different cards.
# Card names which start with * have special custom code just for them (cards which use CustomScript or useCustomAbility don't have *)
# Do not edit below the line
ScriptsLocal = '''
=====
1st Baptist Church
-----
94c55a0c-1599-4eee-8699-ad9c63e375a1
-----
constantAbility:HandSizePlus1
+++++

.....
A Coach Comes to Town
-----
6656eabf-4a69-4854-950d-f30d7771c4ae
-----
onPlay:StartJob-AutoTargeted-atTown Square-jobEffects<Gain4Ghost Rock,Gain4Ghost Rock-onOpponent>
+++++

.....
Abram Grothe 
-----
44946fbc-1bc0-4a1a-9a55-6138b795bfc8
-----

+++++
GR0B1R0:StartJob-DemiAutoTargeted-atDeed_and_Holy Ground-choose1-jobEffects<DiscardMulti-Targeted-atDude-MarkNotTheTarget,None>
.....
Ace in the Hole
-----
cf239340-c794-4a91-a241-e3cbafec2f6e
-----

+++++
GR0B1R0:BootHost-isCost$$Pull1Card-testHex6-spellEffects<AceTarget-DemiAutoTargeted-isDrawHand-choose1-isCost++SendToDrawTarget-DemiAutoTargeted-fromHand-choose1,None>
.....
Allie Hensman
-----
dfd2d635-4b88-4cea-9939-14deec3896cf
-----

+++++
GR0B1R0:Put1PermControlPlus
.....
Ambush
-----
cc2092bd-b575-4a26-8e96-aa13f8736d75
-----
onPlay:StartJob-DemiAutoTargeted-atDude-bootLeader-choose1-targetOpponents-jobEffects<AceTarget,None>
+++++

.....
Andreas Andregg
-----
97061219-899d-4db0-b4a2-ab59bd651df6
-----

+++++

.....
Androcles Brocklehurst
-----
ecfa0567-5576-427f-a829-a049e817f4b0
-----

+++++
GR0B1R0:Gain1Ghost Rock-perTargetProperty{Influence}-Targeted-atDude-targetOpponents
.....
Arnold McCadish
-----
1aa58444-fccc-4121-ac6c-482fd48e4b8e
-----

+++++
GR0B1R0:Pull1Card
.....
Auction
-----
57763c43-994c-4682-ab8d-d8d732fe915e
-----

+++++

.....
Auto Cattle-Feeder
-----
20376d1c-4d9a-42ce-8b34-a95a175f1623
-----

+++++
GR0B1R0:Gain1Ghost Rock
.....
Automatic Mini-Revolver
-----
239ef52d-12a1-47b6-8838-28a8c021a251
-----

+++++

.....
Avie Cline
-----
2871b5b3-fd14-40d1-90e5-f7ea4dae30ba
-----

+++++

.....
B&amp;B Attorneys
-----
232f0a41-2ef5-47a0-9c32-6ccb8eb3c84e
-----

+++++
GR0B1R0:Put1Bounty-Targeted-atDude-hasMarker{Bounty}||GR0B1R0:Remove1Bounty-Targeted-atDude
.....
Bad Company
-----
9a18cd02-63dd-4381-ba9f-49d80fac935a
-----
onPlay:Put3BulletNoonPlus-Targeted-atDude-hasMarker{Bounty}$$Put1Bad Company-Targeted-atDude-hasMarker{Bounty}$$Remove999High Noon:Draw-Targeted-atDude-hasMarker{Bounty}-isSilent$$Put1High Noon:Stud-Targeted-atDude-hasMarker{Bounty}-isSilent
+++++

.....
Bank of California
-----
3c904ee6-15de-4478-8837-61e394bb31ee
-----

+++++

.....
Barton Everest
-----
c3638e9f-f664-43a6-abe0-645aab082455
-----

+++++
GR0B0R1:SimplyAnnounce{increase their draw hand rank by 1}
.....
Blake Ranch
-----
2ad321e1-eaa0-4984-bdd0-a8d088045588
-----

+++++

.....
Blood Curse
-----
597ff0fc-a578-4215-9c6d-c5452d387870
-----

+++++
GR0B1R0:Pull1Card-testHex9-spellEffects<Put2BulletShootoutMinus-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1,None>-onlyInShootouts||GR0B1R0:Pull1Card-testHex9-spellEffects<Put1BulletNoonMinus-Targeted-atDude-targetOpponents++Put1InfluenceMinus-Targeted-atDude-targetOpponents,None>-onlyInNoon
.....
Bluetick
-----
a914540e-8564-44a4-b4cf-64f9f392218b
-----

+++++
GR0B1R0:MoveHost-moveToDude-hasMarker{Bounty}
.....
Bobo
-----
abb271cf-7cbb-4a15-bd45-0458366c6f65
-----

+++++

.....
Bottom Dealin'
-----
1a3e8af5-302b-47e5-8c30-901b8ed995bc
-----
onPlay:CustomScript
+++++

.....
Bounty Hunter
-----
5cd89aa8-b973-4fa6-be81-087b5e369ed4
-----
onPlay:Spawn1Gunslinger-modAction:CalloutTarget-Targeted-atDude-targetOpponents-hasMarker{Bounty}
+++++

.....
Buffalo Rifle
-----
efaf839b-f06f-4aff-982b-a99ae00f340c
-----

+++++

.....
Bunkhouse
-----
9cba89ca-5a3f-4dad-aff0-91d62581dc31
-----

+++++

.....
Carter's Bounties
-----
6560b478-c5fe-4717-a2d1-40ef7c6effa6
-----

+++++
GR0B1R0:ParticipateTarget-DemiAutoTargeted-atDude-targetMine-choose1-isNotParticipating
.....
Cattle Market
-----
2cd7a17c-ce6a-4ffd-92b0-06fe310c7d6c
-----

+++++

.....
Charlie's Place
-----
57528427-b65a-4056-9fea-082bba8ef4a9
-----

+++++
GR0B1R0:Put2BulletNoonPlus-Targeted-atDude||GR0B1R0:Put2BulletNoonMinus-Targeted-atDude
.....
Cheatin' Varmint
-----
3029937b-17cc-4c87-a109-9888747f3134
-----

+++++
onPlay:Pay5Ghost Rock-isCost$$SimplyAnnounce{Reduce a player's draw rank by 2 hand ranks}||SimplyAnnounce{Reduce a player's draw rank by 2 hand ranks}
.....
Circle M Ranch
-----
ec741b63-8ac4-4b5a-9767-9854e05b91c3
-----

+++++
GR0B1R0:Draw1Card
.....
Clear Out!
-----
37d550e3-6bb5-4744-a544-fcbba0153780
-----

+++++

.....
Clementine Lepp
-----
5d610a44-7f13-4333-a941-ee5e1fa2fb37
-----

+++++

.....
Clint Ramsey
-----
077d03fd-1509-43a2-8844-c2bd8d62b837
-----

+++++

.....
Clyde Owens
-----
27d3649c-fdcf-4b40-83ec-d7d04543cefe
-----

+++++
GR0B0R0:CalloutTarget-Targeted-atDude
.....
Coachwhip
-----
0c41f0c4-2491-4723-8cf9-d8ab3e071e05
-----
onPlay:CustomScript
+++++

.....
Concealed Weapons
-----
9c4f6a3b-70e0-40d8-adde-e26c4e5eab12
-----
onPlay:CreateDummy$$SimplyAnnounce{use shoppin' as a Shootout play, and at any location}||atPhaseSundown:DiscardMyself-onlyforDummy
+++++

.....
Dead Dog Tavern
-----
9fe6ced8-a97c-49e8-8806-0ba465f535f6
-----

+++++

.....
Doyle's Hoyle
-----
0482af4d-f834-4f73-88fc-9f57e44c465a
-----

+++++

.....
Dr. Dawn Edwards
-----
36c91361-cab3-4988-bed2-2c3401746695
-----

+++++
GR0B0R1:DiscardMyself$$Retrieve1Card-toTable-grabEve Henry
.....
Elander Boldman
-----
8e50a03b-b42c-4207-9d0d-7a144ad31e3b
-----

+++++
GR0B0R0:CustomScript
.....
Establishin' Who's in Charge
-----
2ae1a463-0106-426c-b9fd-6bb22df27aff
-----
onPlay:StartJob-DemiAutoTargeted-atDeed-choose1-jobEffects<Put1PermControlPlus,None>
+++++

.....
Eve Henry
-----
f149dcc9-44a4-4399-8786-62d2496559e4
-----

+++++
GR0B0R1:DiscardMyself$$Retrieve1Card-toTable-grabDr. Dawn Edwards
.....
Extortion
-----
b61dc1ab-393c-4827-a6ec-4f9ffb870491
-----
onPlay:Gain1Ghost Rock-perTargetProperty{Production}-Targeted-atDeed-targetMine
+++++

.....
Flame-Thrower
-----
c20de5e3-daea-4dce-a8ce-eaa5349c8187
-----

+++++
GR0B1R0:RequestInt{Boost your Flamethrower by how much?}-Min1-Max3$$Lose1Ghost Rock-perX-isCost$$Put1BulletShootoutPlus-perX
.....
Force Field
-----
40302c3e-668e-474f-a2ae-7ab1bbdf9d63
-----

+++++
GR1B0R1:SimplyAnnounce{increase their hand rank by 1}
.....
Fred Aims
-----
fa1e44a1-2064-4d70-8286-854d80b50da2
-----

+++++

.....
Fresh Horses
-----
51b788af-7a36-4af4-9f2e-302441634966
-----
onPlay:UnbootMulti-Targeted-atHorse
+++++

.....
General Store
-----
45438749-ab3b-4f88-adb3-8c3cc65cfd54
-----

+++++
GR0B1R0:PlayTarget-DemiAutoTargeted-fromHand-atGoods_or_Spell-choose1-payCost-reduc2
.....
Gomorra Parish
-----
972201b6-4fc1-44ed-8ed0-a16b1d609265
-----

+++++
GR0B1R0:AceTarget-DemiAutoTargeted-fromHand-choose1$$Gain1Ghost Rock
.....
Good Stiff Drink
-----
74fbc995-aeca-4026-a4f4-682684e6feb1
-----
onPlay:Remove1UsedAbility-DemiAutoTargeted-atDude-hasMarker{UsedAbility}-choose1
+++++

.....
Harold Aimslee
-----
f64c8b68-0d63-4f5d-a898-f38576024f75
-----

+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-choose1-fromHand$$Retrieve1Cards-fromDiscard-grabGadget_and_nonWeapon
.....
Hex Slingin'
-----
7a949a25-df55-47e3-9d6e-674b51cc0f0f
-----
onPlay:DiscardTarget-Targeted-atHex-targetMine
+++++

.....
Hiding in the Shadows
-----
5c5b6579-a2de-419d-b531-6d08c1eba77d
-----
onPlay:Put1Hiding in the Shadows-Targeted-atDude
+++++

.....
Hired Guns
-----
fd307ab6-2c39-438c-8b2e-b6ffd74b15bc
-----
onPlay:Retrieve1Card-fromDiscard-grabDude
+++++

.....
Hot Lead Flyin'
-----
460fcab1-be68-41f1-90bf-41ee11aa17c4
-----
onPlay:Pull1Card
+++++

.....
Irving Patterson
-----
d9586ca6-50bc-446e-aa3b-fc84b0545dcd
-----
onParticipation:Gain1Ghost Rock
+++++

.....
Ivor Hawley
-----
b072a22f-6c55-441f-8cce-4351038ed15c
-----

+++++
GR0B0R0:Put1Huckster Skill Bonus
.....
Jackson's Strike
-----
0eeba3c3-792a-4d39-879a-aab77b0f3981
-----

+++++

.....
James Ghetty
-----
feb37a5b-a95c-4c03-92e0-acd27d7a3ef3
-----
onParticipation:Put4Ghost Rock||onUnparticipation:Remove999Ghost Rock-isSilent
+++++
GR0B0R1:Remove1Ghost Rock-isCost-isSilent$$Gain1Ghost Rock
.....
Jarrett Blake
-----
c57efc28-77d3-492b-81ad-f3c5ce130041
-----

+++++
GR0B0R0:CustomScript
.....
Jia Mein
-----
2419a7fc-569e-43bc-b5b7-360d41133e0c
-----

+++++
GR0B0R0:PlayTarget-DemiAutoTargeted-fromHand-atSpell-choose1-payCost-isCost$$Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Jon Longstride
-----
0c0087d0-6356-44a4-8237-15f86573716a
-----

+++++
GR0B0R0:UnbootTarget-AutoTargeted-atHorse-onAttachment$$Remove1Used Ability-AutoTargeted-atHorse-onAttachment-isSilent
.....
Jonah Essex
-----
f95140da-3b72-4210-95fb-bfe7efe2cca4
-----

+++++

.....
Judge Harry Somerset
-----
9c2ec4f0-65cf-4408-81ff-b377e37f7ecb
-----

+++++
GR0B1R0:StartJob-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-choose1-jobEffects<AceTarget,None>
.....
Kevin Wainwright
-----
03c50bb2-d027-4d02-b8b6-4bc542dceddb
-----

+++++
GR0B0R0:MoveMyself-moveToDude_and_Huckster$$Remove999High Noon:Draw-isSilent$$Put1High Noon:Stud
.....
Kidnappin'
-----
e11367a5-6fad-40a4-b22a-a2571eb7c330
-----
onPlay:StartJob-DemiAutoTargeted-atDude-choose1-bootLeader-bountyPosse-targetOpponents-jobEffects<DiscardTarget,None>
+++++

.....
Killer Bunnies Casino
-----
b4442f8d-71d0-4d12-9000-4df27ea78643
-----

+++++

.....
Lady Luck
-----
aced4a1e-d5c9-423d-8d47-892c19c6a859
-----

+++++

.....
Lane Healey
-----
c263b2ff-3d4b-4beb-aa3b-d4e1f72e56ff
-----

+++++

.....
Law Dogs
-----
e6bee3e6-0ccd-40e6-a447-28cb032b7448
-----

+++++
GR0B1R0:Put1Bounty-Targeted-atDude-targetOpponents-choose1$$BootMulti-Targeted-atDude-targetMine
.....
Lawrence Blackwood
-----
8ed33c69-c79e-4ced-a180-3fe57bf0d25d
-----

+++++
GR0B1R0:Put1ControlPlus
.....
Legendary Holster
-----
677bbf45-1f98-49aa-b8cc-b63b8f3d5146
-----

+++++
GR0B1R0:Pull1Card
.....
Lucinda "Lucy" Clover
-----
567d93e7-2497-4ddb-aa04-01c927f00bc8
-----

+++++
GR0B0R1:Put1Bounty-AutoTargeted-atDude-isParticipating-targetOpponents
.....
Magical Distraction
-----
72853004-7ce4-4d66-a486-fc28bb87a048
-----
onPlay:DiscardTarget-Targeted-asSpell-targetMine$$Pull1Card
+++++

.....
Make the Smart Choice
-----
9ead8579-7077-45e4-a44d-cf284f55b3e5
-----
onPlay:Put1BulletShootoutMinus-DemiAutoTargeted-atDude-perTargetProperty{Influence}-isParticipating-choose1
+++++

.....
Marion Seville
-----
3bd5addb-ac4e-45aa-9971-bd445222344e
-----

+++++

.....
Max Baine
-----
4ad6e3d4-3c6c-43a4-a612-293586609150
-----

+++++
GR0B0R1:Refill1PermControlPlus
.....
Mechanical Horse
-----
aa1dec3f-9913-4bf1-bbcd-5d29457f6a80
-----

+++++
GR2B0R1:MoveHost-moveToDeed_or_Town Square_or_Outfit
.....
Micah Ryse
-----
6d31cb7e-a409-4256-8bba-26778de6c5f4
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atSpell-isUnbooted-onAttachment-choose1-isCost$$MoveMyself-moveToDeed_or_Town Square_or_Outfit
.....
Missed!
-----
00a45909-a052-457d-a71b-119e415c03c7
-----
onPlay:UnbootTarget-Targeted-atDude-isParticipating
+++++

.....
Mongwau the Mighty
-----
18866ac8-9a24-45d7-8f67-df20afdc2dbb
-----

+++++
GR0B0R0:DiscardTarget-DemiAutoTargeted-atSpell-onAttachment-isCost-choose1$$Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Morgan Cattle Co.
-----
4f21000a-fb64-4e4b-8e8a-1c5d588dc577
-----

+++++
GR0B1R0:CustomScript
.....
Mustang
-----
9aa68e21-1eee-4d44-993e-dd8cf60ed613
-----

+++++
GR0B1R0:MoveHost-moveToDeed_or_Town Square_or_Outfit
.....
Olivia Jenks
-----
65d4cd16-fc61-4412-8a39-a6ad384fa766
-----

+++++

.....
One Good Turn
-----
1950bc30-abf5-4ed4-b20a-e56bb4032de0
-----
onPlay:Draw1Card||onPlay:Gain3Ghost Rock
+++++

.....
Pair of Six-Shooters
-----
2dbddcbc-d228-451d-8cde-32b65abe769e
-----

+++++
GR0B1R0:SimplyAnnounce{change one card in their draw hand to the suit and value of their choice.}
.....
Pancho Castillo
-----
d9d621f3-1905-4a99-8f5a-f1feb9639a64
-----

+++++

.....
Pat's Perch
-----
69ccb375-f660-4d91-a405-2103b578f100
-----

+++++

.....
Peacemaker
-----
022097bf-7e34-4b78-b7ca-3d60ca13eddd
-----

+++++

.....
Pearl-handled Revolver
-----
c8453a00-e4f9-4dbe-922c-3daf79586cef
-----

+++++

.....
Pearly's Palace
-----
ed26a010-8947-456f-b8f7-2741e083b54a
-----

+++++
GR0B1R0:SimplyAnnounce{make a Shootout play before anyone else}
.....
Philip Swinford
-----
fb5f0076-bbb3-486e-9420-02084643592b
-----

+++++
GR0B0R1:DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost$$Draw1Card
.....
Pinned Down
-----
b5fbbe61-aba3-4de7-b501-4feb1f9cf203
-----
onPlay:Put1Shootout:Pinned Down-Targeted-atDude-isParticipating-targetOpponents
+++++

.....
Pinto
-----
9e712f98-1a8b-4137-997e-e61e6549102c
-----

+++++
GR0B1R0:ParticipateHost
.....
Pistol Whip
-----
1536769f-42f4-4840-9360-96d2e7e3f366
-----
onPlay:Put1BulletShootoutMinus-Targeted-atDude-isParticipating-isUnbooted-targetMine$$BootTarget-DemiAutoTargeted-atDude-isParticipating-isUnbooted-targetMine-choose1-isCost$$SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1
+++++

.....
Point Blank
-----
498d4eca-db79-40db-9a42-cc053abcfc43
-----
onPlay:BootTarget-DemiAutoTargeted-atDude-isParticipating-isUnbooted-isStudDude-targetMine-choose1-isCost$$SimplyAnnounce{force their opponent to ace a dude with less bullets}
+++++

.....
Pony Express
-----
a9b3a2b8-9f22-474d-b35a-59a380c0921f
-----

+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost$$Draw1Card
.....
Prescott Utter
-----
ab7172e2-0e3f-408d-81ec-afb478385cfe
-----

+++++

.....
Prof Eustace True
-----
f8437fa5-c088-41b2-b6c9-2060f69ec7be
-----

+++++
GR0B0R0:DiscardTarget-DemiAutoTargeted-atGadget-onAttachment-choose1-isCost$$MoveMyself-moveToDeed_or_Town Square_or_Outfit
.....
Railroad Station
-----
fa907076-61c7-4f1f-b9a4-87a1df59bfae
-----

+++++
GR0B1R0:MoveTarget-Targeted-atDude-moveToDeed_or_Town Square_or_Outfit
.....
Raising Hell
-----
0ab4453e-e9bd-4899-96e1-1eb6757ecd94
-----

+++++
GR0B1R0:Pull1Card-testHex8-spellEffects<AceTarget-DemiAutoTargeted-fromHand-choose1++Retrieve1Card-fromBootHill-toTable-grabAbomination-payCost++AceMyself,None>-onlyInShootouts
.....
Ramiro Mendoza
-----
d677fa1e-61f3-422a-9b95-745692c7b800
-----
onParticipation:Lose1Ghost Rock-isCost
+++++

.....
Recruitment Drive
-----
9ef9abea-373c-4265-b7fc-3d8391095f64
-----
onPlay:StartJob-AutoTargeted-atTown Square-jobEffects<Retrieve1Card-grabDeed_or_Dude-fromDiscard-toTable-payCost-reduc5,None>
+++++

.....
Remy Lapointe
-----
cb15bd27-76a2-48db-b324-99589b14982b
-----

+++++
GR0B0R0:RequestInt{Combien de ghost rock veux tu depenser pour augmenter ton niveau de bullet?}$$Lose1Ghost Rock-isCost-perX$$Put1BulletShootoutPlus-perX
.....
Reserves
-----
0672772c-7380-4b36-be78-1c7b23b3d950
-----
onPlay:Gain1Ghost Rock
+++++

.....
Roan
-----
ff6f51e6-ab2f-4fb9-8670-1715b278cc8c
-----

+++++

.....
Rumors
-----
d7e770dd-793f-4a53-a404-e3873a762ad1
-----
onPlay:Put1InfluenceMinus-Targeted-atDude-targetOpponents$$Put1Rumors-Targeted-atDude-targetOpponents
+++++

.....
Run 'em Down!
-----
3a1296d2-79f5-4a8a-9ea3-cabc4564e9eb
-----
onPlay:BootTarget-Targeted-atDude-targetOpponents$$MoveMulti-Targeted-atDude-targetMine-moveToDude-isBooted
+++++

.....
Sanford Taylor
-----
e686782d-1d7c-464d-82ed-910fcaa2945d
-----

+++++
GR0B1R0:CalloutTarget-Targeted-atDude
.....
Shadow Walk
-----
f9714fff-14d9-433c-b2cc-05068006c388
-----

+++++
GR0B1R0:Pull1Card-testHex7-spellEffects<MoveHost-moveToDude_or_Deed_or_Town Square_or_Outfit++ParticipateHost,None>-onlyInShootouts||GR0B1R0:Pull1Card-testHex7-spellEffects<MoveHost-moveToDeed_or_Town Square_or_Outfit,None>-onlyInNoon
.....
Sherriff Dave Montreal
-----
2af1e511-ca73-4f12-a1ae-9a7a340738da
-----

+++++

.....
Shotgun
-----
ac681d62-c7df-469f-8ac6-80816c781136
-----

+++++
GR0B1R0:AceTarget-Targeted-atDude-isParticipating
.....
Silas Aims
-----
28b5d3c7-bb58-4b63-aae5-659e86fee876
-----

+++++
GR0B0R1:Gain1PermBulletPlus
.....
Sloane
-----
8209b72a-15c4-440b-9ad7-8614a9d2f452
-----

+++++

.....
Soul Blast
-----
bf1c8173-843a-4a20-be3b-f4ae650cfdd2
-----

+++++
GR0B1R0:Pull1Card-testHexX-difficultyGrit-spellEffects<SendHomeBootedTarget-DemiAutoTargeted-isParticipating-choose1,SendHomeBootedHost>
.....
Stagecoach Office
-----
2c51b78f-b130-4663-9c78-0cc69a20a059
-----

+++++

.....
Steele Archer
-----
d9a3a80d-deef-47a7-9a5a-e1c7e0109697
-----

+++++

.....
Steven Wiles
-----
335662d9-0d7c-430e-a556-11693385f5aa
-----

+++++

.....
Sun in Yer Eyes
-----
fcc6f54f-e9d1-40a6-9870-1be438eeef12
-----
onPlay:Put2BulletShootoutMinus-Targeted-atDude-isParticipating-targetOpponents$$Remove999Shootout:Stud-isSilent-Targeted-atDude-isParticipating$$Put1Shootout:Draw-isSilent-Targeted-atDude-isParticipating
+++++

.....
Takin' Yer With Me
-----
452fd385-a516-45d9-8408-8628f4788fa5
-----
onPlay:SimplyAnnounce{your opponent to take 1 casualty}
+++++

.....
Telegraph Office
-----
08d1664d-5d98-4093-88c3-e93b0c6cc84f
-----

+++++
GR0B1R0:Gain1Ghost Rock-perTargetProperty{Influence}-Targeted-atDude
.....
The Fourth Ring
-----
4137ced8-eb93-4ca6-9253-240b46b15886
-----

+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost$$Draw1Card$$Gain1Ghost Rock
.....
The Ghostly Gun
-----
91863a08-01d9-4b7e-9eff-0bb62826f433
-----

+++++
GR0B0R1:SimplyAnnounce{put The Ghostly Gun into their draw hand}
.....
The Morgan Research Institute
-----
75e35d17-de1e-457f-88e0-42e2bc9301bc
-----

+++++
GR0B1R0:Put2High Noon:Skill Bonus-Targeted-atDude||GR0B1R0:Put2High Noon:Skill Penalty-Targeted-atDude
.....
The Pharmacy
-----
84e33474-5247-4969-b7d1-e335b720a566
-----

+++++
GR0B1R0:UnbootTarget-DemiAutoTargeted-atDude-choose1
.....
The Sloane Gang
-----
f7b4b246-da6f-44e4-9eee-46bb8bfb931a
-----

+++++
GR0B1R0:BootTarget-Targeted-atDude-isCost$$Put1Come Git Some-Targeted-atDude
.....
The Stakes Just Rose
-----
8649f082-f7cd-414d-b360-9b1b72f6172b
-----
onPlay:ParticipateTarget-Targeted-atDude-targetMine$$Remove999Shootout:Draw-Targeted-atDude-targetMine-isSilent$$Put1Shootout:Stud-Targeted-atDude-targetMine
+++++

.....
The Town Hall
-----
7378c899-a9c3-46d4-8d68-f452c9640734
-----

+++++
GR0B1R0:Put1Town Hall-Targeted-atDude
.....
The Union Casino
-----
d340ff50-aec3-4800-a993-c76c954c34a9
-----

+++++
GR0B1R0:CustomScript
.....
This is a Holdup!
-----
7779228b-f33c-4c36-ae90-17fdf54cd142
-----
onPlay:CustomScript
+++++

.....
Tommy Harden
-----
2e81c214-539a-4b49-b2d0-69258204b240
-----

+++++
GR0B0R1:SimplyAnnounce{increase their draw hand rank by 1}
.....
Travis Moone
-----
03341e26-42b4-4545-897e-8626de5e3dd7
-----

+++++
GR0B1R0:ReshuffleHand$$Draw5Cards
.....
Tresspassin'
-----
d4133356-c738-4b89-82ac-9a6d5e35a744
-----

+++++

.....
Tyxarglenak
-----
e6db104b-d882-41c5-9285-84ed77a74eac
-----

+++++

.....
Undertaker
-----
a8843dcd-cd66-4f38-b6a9-12fbf5fd8bba
-----

+++++
GR0B0R1:Gain2Ghost Rock
.....
Unprepared
-----
1f230385-e07c-43e2-a205-79547ce18380
-----
onPlay:CustomScript
+++++

.....
War Paint
-----
b3140484-bfe8-4eb4-963f-27e8d9334b8a
-----
onPlay:Put2BulletNoonPlus-Targeted-atDude
+++++

.....
Whisky Flask
-----
80d43d02-7885-4e2e-98e5-62ba2b189155
-----

+++++
GR0B1R0:BootHost-isCost$$DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost$$Draw1Card
.....
Xiong "Wendy" Cheng
-----
e22efbb0-e796-4c72-9793-23ed7635dfce
-----

+++++
GR0B1R0:SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1
.....
Yan Li's Tailoring
-----
b999405d-e2ca-4703-beda-67f9697fc977
-----

+++++
GR0B1R0:Put1InfluencePlus-Targeted-atDude
.....
Back Ways
-----
ef91b1f5-46b8-4246-8e58-401a39ebbf6f
-----
onPlay:MoveTarget-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetMine-choose1-moveToDeed_or_Town Square_or_Outfit
+++++

.....
Kyle Wagner
-----
826655e8-00b7-43ae-a3fb-4cea781176ad
-----

+++++
GR0B1R0:UnbootTarget-Targeted-atRanch-targetMine$$Remove1Used Ability-Targeted-atRanch-targetMine-isSilent
.....
Telepathy Helmet
-----
b65c9b55-7a81-4052-87dd-70eb515b8b2f
-----

+++++
GR1B0R1:CustomScript
.....
Town Council
-----
aa9e21f5-9a84-479b-90f8-497b6084467b
-----

+++++

.....
Faithful Hound
-----
bf48f3c1-bd08-4542-a8c6-6af0a8e7cfa4
-----

+++++
GR0B1R0:Pull1Card
.....
Plasma Drill
-----
d6c082a2-8e92-404b-b427-a1f7a7cab4aa
-----

+++++
GR1B1R0:BootHost-isCost$$UseCustomAbility
.....
Slade Lighboy
-----
d9aefb8f-ea66-4782-8fee-1e5c88c257af
-----

+++++
GR0B0R0:AceTarget-DemiAutoTargeted-atSpell-onAttachment-isBooted-choose1-isCost$$Pull1Card
.....
The R&amp;D Ranch
-----
ce8a1161-2c83-4a6f-a0de-7a6c19b47a6e
-----

+++++
GR0B1R0:CustomScript
.....
Wilber Crowley
-----
c765b5ba-c7b1-491c-b504-fcce730bb8a0
-----

+++++

.....
Hired Help
-----
1b68d5c9-e336-4822-aeb9-5ca0cace82a8
-----
onPlay:Spawn1Gunslinger-modAction:ParticipateMyself
+++++

.....
Roderick Byre
-----
0203a928-b0b6-4a95-8e71-d82b02a48e9a
-----

+++++

.....
Rafi Hamid
-----
dec376dc-2dcd-4cb8-b1ae-9c4dc7c7dd7e
-----

+++++
GR0B0R0:MoveTarget-Targeted-atDeputy-moveToGovernment$$ParticipateTarget-Targeted-atDeputy
.....
Ulysses Marks
-----
15fda041-c825-4278-a5de-15bc00cab80d
-----

+++++
GR0B0R0:MoveTarget-Targeted-atDude-moveToTown Square$$BootTarget-Targeted-atDude
.....
Paralysis Mark
-----
18e06cc3-eb57-451a-ba28-18665727999d
-----

+++++
GR0B1R0:Pull1Card-testHexX-difficultyValue-spellEffects<BootTarget-DemiAutoTargeted-atDude-choose1,None>
.....
Wylie Jenks
-----
cbb6be72-e387-4742-99cb-b5681e88de82
-----

+++++

.....
Too Much Attention
-----
519a9e2e-56e9-42a2-8cda-64d1a7cd934f
-----
onPlay:BootTarget-Targeted
+++++

.....
Make 'em Sweat
-----
7bb386d8-73a0-4d31-bbd1-5204fcde0302
-----
onPlay:CustomScript
+++++

.....
Dulf Zug
-----
77653869-e142-4428-8595-c74886e8c8c8
-----

+++++

.....
Lillian Morgan
-----
32f4797f-7584-453c-b6a3-9cf3656dcc96
-----
onParticipation:Put3Ghost Rock||onUnparticipation:Remove999Ghost Rock-isSilent
+++++
GR0B0R1:Remove1Ghost Rock-isCost-isSilent$$Gain1Ghost Rock
.....
Alice Stowe
-----
55257be5-9428-4699-8df6-9b397f9fe258
-----

+++++

.....
Dr. Emanuel Ashbel
-----
17760a8d-adc3-40cc-9c85-578b7f2b30c5
-----

+++++
GR0B0R0:Pull1Cards
.....
..It's who you know
-----
48c8526d-6dee-4ee8-9636-01d3891db8f8
-----
onPlay:CalloutTarget-Targeted-atDude-targetOpponents-leaderTarget{Dude}$$Put1Shootout:Stud-Targeted-atDude-targetMine
+++++

.....
Horse Wranglin'
-----
f51e5631-7582-492f-8351-e1e808d39d19
-----
onPlay:Retrieve1Cards-grabHorse-toTable-payCost||onPlay:Retrieve1Cards-grabHorse-toTable-payCost-fromDiscard
+++++

.....
It's Not What You Know...
-----
a23d36e0-8231-49e7-bbc4-4e56c179b045
-----

+++++
onPlay:SimplyAnnounce{Reduce a player's draw rank by 1 hand rank}||SimplyAnnounce{Reduce a player's draw rank by 4 hand ranks}-isResolution
.....
Baird's Build and Loan
-----
949e9f9d-bc65-4486-b115-a1d364aaae0d
-----

+++++
GR0B1R0:PlayTarget-DemiAutoTargeted-fromHand-atDeed-choose1-payCost-reduc2
.....
Leonardo "Leon" Cavallo
-----
90b3fbde-2834-4c49-9577-1d8723feadd4
-----

+++++
GR0B1R0:Pull1Card-testHexX-difficultyValue-spellEffects<BootTarget-Targeted,None>
.....
Gang Yi
-----
631a3c9a-b970-47f5-a196-c078ad913d56
-----

+++++
GR0B0R0:CustomScript
.....
Angelica Espinosa
-----
08fbd7c6-0413-4b5b-872e-a9ba16e3276d
-----

+++++
GR0B0R0:ParticipateMyself
.....
Jose Morales
-----
1e61fcd0-65fa-414f-8838-d76f1394b041
-----
constantAbility:Skill Bonus:1-perProperty{Bullets}-isParticipating
+++++

.....
Tallulah "Lula" Morgan
-----
434353cb-3040-4709-a7d5-e4f36006128b
-----

+++++
GR1B1R0:Gain1Ghost Rock-perTargetProperty{Production}-Targeted-atDeed-targetMine
.....
Ballot Counter
-----
ffed2e8d-67cf-42ab-8a34-110110b59c72
-----

+++++
GR1B0R1:Put1InfluencePlus
.....
Holy Wheel Gun
-----
dba818f0-4802-474c-91c8-07536e32fb3d
-----

+++++
GR0B1R0:Put1BulletShootoutMinus-Targeted-atDude-isParticipating$$Put1Shootout:Holy Wheel Gun Mark-Targeted-atAbomination-isParticipating-noTargetingError
.....
Stone Idol
-----
f94631b0-20f6-492b-b732-e36b816e523f
-----

+++++
GR0B1R0:Put3ValueNoonMinus-Targeted-atDude
.....
Corporeal Twist
-----
8272e52f-aa01-403e-9ea4-0408bdcf3fdc
-----

+++++
GR0B1R0:Pull1Card-testHex5-spellEffects<Put1BulletShootoutMinus-Targeted-atDude-isParticipating-targetOpponents++Put2ValueShootoutMinus-Targeted-atDude-isParticipating-targetOpponents,None>
.....
Forget
-----
0857fa1d-c061-4606-bb55-4736edcfd2e9
-----

+++++
GR0B1R0:Pull1Card-testHex5-spellEffects<Put1High Noon:Forget-Targeted-atDude,None>
.....
Surveyor's Office
-----
cdc1e1d2-d985-400f-ab3c-f91744619eed
-----

+++++
GR0B1R0:MoveTarget-DemiAutoTargeted-atDude-targetMine-choose1-moveToDeed_or_Town Square_or_Outfit
.....
Genesee "Gina" Tailfeathers
-----
437cd8a9-fe8a-497f-9625-9054511f91ea
-----

+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost$$Draw2Cards
.....
Richard Slavin
-----
68b6d3d2-207c-47ed-9311-0949f86308b9
-----

+++++
GR0B1R0:Pull1Card
.....
Fetch
-----
f138c8f1-00cc-4ca4-b145-e9c5105dc76a
-----

+++++
GR0B1R0:Pull1Card-isResolution
.....
The Brute
-----
13cdc52f-986e-4f3b-b053-c3261267790d
-----

+++++

.....
Smiling Tom
-----
d90e5abe-ed12-4dad-9007-16aa47afa2cc
-----

+++++

.....
Philip Swinford
-----
f1012bb4-2429-4ec3-9b89-6ebcb3f94184
-----

+++++
GR0B0R1:Draw1Card$$DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost
.....
Drew Beauman
-----
19fc7ff8-d4da-492f-8a41-7a838490c9e4
-----

+++++
GR0B0R1:PlayTarget-DemiAutoTargeted-fromHand-atGadget-choose1-payCost-isCost
.....
Dr. Arden Gillman
-----
95b9d8df-a95d-4b5e-aeed-98f8e99ca5a5
-----

+++++
GR0B1R0:Pull1Card
.....
Arvid Mardh
-----
33b97a88-5b7f-4073-8e30-5c66da9060c5
-----

+++++

.....
Allie Hensman
-----
28c37361-c5ac-4561-b1bc-5f41113e0625
-----

+++++
GR0B0R0:StartJob-DemiAutoTargeted-atDude-bootLeader-choose1-targetOpponents-jobEffects<UseCustomAbility,None>
.....
Milt Clemons
-----
cd99ead2-3b50-4989-8331-59f76b5edb0b
-----

+++++

.....
Jake Smiley
-----
36c80330-39fc-4fdc-8736-4c8d47758063
-----
onPlay:Put2PermInfluencePlus
+++++

.....
QUATERMAN
-----
144991c0-f3f4-4914-a075-ab2093991411
-----

+++++

.....
Angela Payne
-----
6b01cb98-4ae3-4b6e-b7d1-29fe035c9e2d
-----

+++++
GR0B1R0:Gain2Ghost Rock
.....
The Mayor's Office
-----
90568a28-333b-4836-b55c-8ebbef266ad1
-----

+++++
GR0B1R0:Put1InfluencePlus-Targeted-atDude||GR0B1R0:Put1InfluenceMinus-Targeted-atDude
.....
Hunter Protections
-----
1f6dc79e-65ad-4727-bf8e-1c42eee98fe1
-----

+++++
GR0B1R0:BootTarget-Targeted-atDude-isUnbooted-hasntMarker{PermControlPlus}-isCost$$Put2Bounty-Targeted-atDude-hasntMarker{PermControlPlus}$$Put1PermControlPlus-Targeted-atDude-hasntMarker{PermControlPlus}
.....
The Evidence
-----
9687ab08-0ae9-4a15-8304-6e9797edc87e
-----

+++++
GR0B0R0:Remove999Bounty-Targeted-atDude-hasMarker{Bounty}$$DiscardMyself||GR1B0R0:Put2Bounty-Targeted-atDude$$AceMyself
.....
Teleportation Device
-----
28d66d3e-bc96-4c2c-9ebb-38dfabceb440
-----

+++++
GR1B0R1:Pull1Card
.....
Mayfair Family Deck
-----
68310bec-735a-46bc-be6c-949e26bc5758
-----

+++++

.....
Puppet
-----
146c6a48-ffb5-4201-b07e-74e5560da771
-----

+++++
GR0B1R0:Pull1Cards
.....
Summoning
-----
791de7a5-3292-43cd-b907-40f737dc8600
-----

+++++
GR0B1R0:Pull1Card-testHex5-spellEffects<StartJob-AutoTargeted-atTown Square,None>
.....
Ridden Down
-----
cd378a50-f1c7-4a1f-a99d-80436806feea
-----
onPlay:BootTarget-DemiAutoTargeted-atHorse-isUnbooted-targetMine-choose1-isCost$$SendHomeBootedTarget-DemiAutoTargeted-atDude-targetOpponents-choose1
+++++

.....
Tail Between Yer Legs
-----
ff26cca7-830f-440a-90cd-08e32c629d7e
-----
onPlay:Put2BulletShootoutMinus-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1
+++++

.....
Election Day Slaughter
-----
25787651-53b5-456e-bb42-8f38fd7b3caf
-----
onPlay:StartJob-AutoTargeted-atTown Square 
+++++

.....
Faster on the Draw
-----
07c1a52a-fcdc-4775-b42c-f352465942da
-----
onPlay:Put2BulletShootoutMinus-Targeted-atDude-isParticipating-targetOpponents$$Put1BulletShootoutPlus-Targeted-atDude-isParticipating-targetMine$$Put1Shootout:Stud-isSilent-Targeted-atDude_and_Deputy-isParticipating-targetMine-noTargetingError
+++++

.....
Swinford Finds Trouble
-----
0b1ae36c-6359-4871-b34b-16808e639243
-----

+++++

.....
Under the Weather
-----
adf4a674-bc8a-4158-ae1a-cb7224fbb850
-----
onPlay:Pull1Card
+++++

.....
This'll Hurt in the Mornin
-----
546a4107-75f3-49f6-84a1-4396ca3c61c1
-----
onPlay:CustomScript-isResolution
+++++

.....
Prayer
-----
e12da368-0c9a-435b-91e7-e08378a6363c
-----
onPlay:Put1Prayer-Targeted-atDude-targetMine$$CreateDummy$$SimplyAnnounce{allow the dude to use shoppin' for Miracles as a Shootout play, and at any location}||atPhaseSundown:Remove999Prayer-AutoTargeted-atDude-hasMarker{Prayer}$$DiscardMyself-onlyforDummy
+++++

.....
Meet The New Boss
-----
c27e60e9-8450-4e6e-9c2e-73d19caec7c1
-----
onPlay:StartJob-AutoTargeted-atTown Square-jobEffects<Put1PermControlPlus-Targeted-LeaderIsTarget++Put1PermInfluencePlus-Targeted++AceMyself,AceMyself>
+++++

.....
Pettigrew's Pawnshop
-----
1b2b9609-05a4-4aed-ab98-06ddf6dbe400
-----
whileInPlay:Gain1Ghost Rock-foreachCardPlayed-typeGoods_and_notGadget
+++++

.....
California Tax Office
-----
c5bf5c92-9d15-42fa-aacf-67163913518a
-----
onPlay:BootMyself
+++++
GR0B1R0:CustomScript
.....
St. Anthony's Chapel
-----
4bd2615b-6a1b-465e-a16d-923fd77ee443
-----

+++++

.....
The Whateley Estate
-----
e77f6e44-7900-4d0e-b370-defa7cd6796d
-----

+++++
GR0B1R0:Retrieve1Cards-fromBootHill-toDiscard-grabnonDude
.....
Outlaw Mask
-----
4827d51e-458b-4945-8242-ddfd2fdd9821
-----

+++++

.....
Mirror, Mirror
-----
9b76ed8e-e25b-47a5-b8d7-e7c020e7a230
-----

+++++
GR0B1R0:Pull1Card-testHex4-spellEffects<UseCustomAbility-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1-isFirstCustom,None>||GR0B1R0:Pull1Card-testHex6-spellEffects<UseCustomAbility-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1-isSecondCustom,None>
.....
Lay on Hands
-----
8d8fa80c-580b-44b3-8e66-b89392299200
-----

+++++
GR0B1R0:Pull1Card-testMiracle8-spellEffects<BootHost++Put1NoUnboot-Targeted-atDude-targetMine++SendHomeBootedTarget-Targeted-atDude-targetMine,None>
.....
Holy Roller
-----
a806a33f-8bb2-4a47-9bdc-f3dc7d2058ea
-----

+++++
GR0B1R0:Pull1Card-testMiracle6-spellEffects<Put1BulletShootoutPlus-AutoTargeted-atDude-onHost++Put1Shootout:Holy Roller-AutoTargeted-atDude-onHost,None>
.....
The Lord Provides
-----
c5c2fed5-010f-4ece-a5e2-2cf200695064
-----

+++++
GR0B1R0:Pull1Card-testMiracle9-spellEffects<Retrieve1Cards-grabAction++DiscardMyself,None>
.....
Walk the Path
-----
77df4257-28e1-4865-8d20-5e0087fcd8d5
-----

+++++
GR0B1R0:Pull1Card-testMiracle7-spellEffects<MoveTarget-Targeted-atDude-targetMine-moveToHere++UnbootTarget-Targeted-atDude-targetMine++ParticipateTarget-Targeted-atDude-targetMine,None>-onlyInShootouts||GR0B1R0:Pull1Card-testMiracle6-spellEffects<MoveTarget-DemiAutoTargeted-atDude-targetMine-choose1-moveToHere,None>-onlyInNoon
.....
Phantasm
-----
c7d43986-30a5-46ac-99a3-01d94ceda540
-----

+++++
GR0B1R0:Pull1Card-testHex9-spellEffects<MoveTarget-DemiAutoTargeted-atDude-targetOpponents-isUnbooted-choose1-moveToDeed_or_Town Square_or_Outfit,None>||GR0B1R0:Pull1Card-testHex12-spellEffects<MoveTarget-DemiAutoTargeted-atDude-targetOpponents-isBooted-choose1-moveToDeed_or_Town Square_or_Outfit,None>
.....
Soothe
-----
4eba0738-ddf4-4bce-9c3c-ecb06d3381ff
-----

+++++
GR0B1R0:Pull1Card-testMiracle10-spellEffects<BootHost-isCost++UnbootTarget-DemiAutoTargeted-atDude-targetMine-isBooted-choose1,None>
.....
Evanor
-----
a0c826bd-311f-4918-aeeb-9c2a14b176c3
-----

+++++
GR0B1R0:SimplyAnnounce{Increase the casualties they inflict if they win, by 1}
.....
Clown Carriage
-----
a8546fc6-be73-41eb-b33a-62b2b8158696
-----

+++++
GR0B1R0:PlayTarget-DemiAutoTargeted-fromHand-atAbomination-choose1-payCost
.....
Bio-Charged Neutralizer
-----
bc4af72b-b53c-44ef-858b-04d33e1e6a4b
-----

+++++

.....
Sister Lois Otwell
-----
2923cd38-686c-4ab3-8996-94fd989bff9b
-----

+++++
GR0B0R0:BootTarget-DemiAutoTargeted-atMiracle-isUnbooted-onAttachment-choose1-isCost$$Put1BulletShootoutPlus-Targeted-atDude-isParticipating-targetMine$$Put3ValueShootoutPlus-Targeted-atDude-isParticipating-targetMine
.....
Felix Amador
-----
38b1ca04-c236-4d51-80dd-1c283957095e
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atMiracle-isUnbooted-onAttachment-choose1-isCost$$UseCustomAbility
.....
Nicodemus Whateley
-----
35a3cffb-6a57-4a90-ab93-63f519910c99
-----

+++++
GR0B0R1:BootTarget-Targeted-atDude-targetMine$$Put1ControlPlus
.....
Rev. Perry Inbody
-----
da32c302-02de-4a5b-89c4-8227dba9f3c7
-----

+++++
GR0B1R0:Pull1Card-testMiracle9-spellEffects<UnbootHost++UnbootTarget-DemiAutoTargeted-atDude_and_Law Dogs-targetMine-isBooted-choose1,None>
.....
Zoe Halbrook
-----
cdfcd050-f5f1-40df-a10a-4039fb74935d
-----

+++++

.....
Abram Grothe
-----
5167ca6e-657d-4d96-a72b-247b2298abf9
-----

+++++
GR0B0R0:BootMulti-AutoTargeted-atWeapon-targetOpponents-isParticipating$$Put1BulletShootoutPlus
.....
William Specks
-----
5a2cbed4-9d68-4c5d-acb6-93e2d25b268f
-----

+++++
GR0B1R0:PlayTarget-DemiAutoTargeted-fromHand-atRanch_or_Out of Town_or_Gadget-choose1-payCost-reduc2
.....
Chuan "Jen" Qi
-----
7d2d0bb3-f477-4076-8739-9479911b95a6
-----

+++++

.....
Lane Healey
-----
a2b5195e-4d31-41e9-8407-c40ce54cc334
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atHorse-isUnbooted-onAttachment-isCost$$BootTarget-Targeted-atDude-targetOpponents$$MoveMyself-moveToDude-targetOpponents$$CalloutTarget-Targeted-atDude-targetOpponents
.....
The Fixer
-----
dfb10d22-9e8f-4031-9249-50cd13ee7203
-----

+++++
GR0B1R0:CustomScript
.....
Maria Kingsford
-----
9937f528-6b65-4625-85d8-05a51af488d2
-----
constantAbility:Skill Bonus:1-perMarker{Bounty}-isParticipating
+++++

.....
Makiao Kaleo, Esq.
-----
933eccf1-ad0d-4153-8381-a23c6de97a60
-----

+++++
GR0B0R0:Remove1Bounty-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetMine-choose1-choiceTitle{Choose from which dude to remove the Bounty}$$Put1Bounty-DemiAutoTargeted-atDude-targetMine-choose1-choiceTitle{Choose which dude should receive the Bounty}
.....
Pagliaccio
-----
6a4d1a94-7e29-465e-9a41-f78389ef49cf
-----

+++++
GR0B1R0:Put1BulletShootoutMinus-Targeted-atDude-targetOpponents-isParticipating$$Put1ValueShootoutMinus-Targeted-atDude-targetOpponents-isParticipating
.....
Valeria Batten
-----
aba65d32-3cb2-4677-b000-f4b905c4a16e
-----

+++++

.....
Micah Ryse
-----
1ff5d90e-e801-4199-80bc-7313bc8cf99e
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atHex-isUnbooted-onAttachment-choose1-isCost$$Put3ValueShootoutMinus-Targeted-atDude-isParticipating-targetOpponents
.....
The Arsenal
-----
b6cfa257-5898-4f1a-968c-8f36956f499b
-----

+++++
GR0B0R1:BootTarget-DemiAutoTargeted-atGadget_or_Spell-isUnbooted-choose1-targetMine-isCost$$CalloutTarget-Targeted-atDude-targetOpponents-leaderTarget{Dude}
.....
Morgan Gadgetorium
-----
6db17405-bbd3-4c0c-b00f-b89991925291
-----

+++++
GR0B1R0:SimplyAnnounce{optimize the gadget creation}
.....
Desolation Row
-----
5669e37c-fab7-4954-acb8-7f841ca7a762
-----

+++++
GR0B1R0:StartJob-AutoTargeted-atTown Square-jobEffects<UseCustomAbility-LeaderIsTarget,None>
.....
Oddities of Nature
-----
d5ed8e5d-c9f9-4e9e-8bc9-48da7c938045
-----

+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atAbomination-targetMine-isUnbooted-choose1-isCost$$Gain1Ghost Rock$$BootTarget-Targeted-atDude-targetOpponents-noTargetingError
.....
Funtime Freddy
-----
2fab82a8-2a4d-4545-855a-9d1ea011a8c9
-----

+++++
GR0B1R0:CustomScript
.....
The Flying Popescus
-----
7d58d611-07a2-41e6-ad4d-fc51cc794847
-----

+++++
GR0B0R0:Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Andrew Burton
-----
7b51deb6-fb5f-4624-8473-32533ec7309c
-----

+++++
GR0B1R0:Put1Bounty-Targeted-atDude$$DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost$$Draw1Cards
.....
Elmore Rhine
-----
e341450b-9b41-4ae1-a1aa-fa50ac743f90
-----

+++++
GR0B1R0:Gain1GhostRock-perTargetMarker{Bounty}
.....
Howard Aswell
-----
a44b9e09-8941-4e30-ab0e-c2171949e8d5
-----

+++++
GR0B0R0:CustomScript
.....
Louis Pasteur
-----
bc36b880-9e3c-458b-8ef4-9730a926bf38
-----

+++++
GR1B0R1:Pull1Card-testMad Science10-spellEffects<UnbootTarget-Targeted-atDude-targetMine,None>
.....
Benny McGill
-----
135a9ce8-4e8b-463a-9fcc-23f0168e4762
-----

+++++
GR0B0R0:BootTarget-DemiAutoTargeted-atSpell_and_Hex-onAttachment-choose1-isCost$$CalloutTarget-Targeted-atDude
.....
Marion Seville
-----
9440378f-dd04-426c-9696-f24e0789e528
-----

+++++
GR0B0R0:Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud$$BootTarget-DemiAutoTargeted-atWeapon_and_Melee-targetOpponents-choose1
.....
J.W. Byrne
-----
fde8c18b-58e2-40ab-b407-fe42a4fe549d
-----

+++++

.....
Shane &amp; Graves Security
-----
18df456c-38ac-4e2b-b4ab-f309849d2cb7
-----

+++++
GR0B1R0:Spawn1Gunslinger-modAction:ParticipateMyself
.....
Gomorra Jail
-----
edc1d27d-2cd3-494f-90d8-36f9edfdbb61
-----

+++++
GR0B1R0:Put1PermControlPlus
.....
Diable en Boite
-----
438f980e-0981-473e-a9c5-0a8d07ee4634
-----

+++++
GR0B1R0:SendHomeBootedTarget-DemiAutoTargeted-isParticipating-choose1$$Draw1Card
.....
Legal Instruments
-----
caff0709-27f0-4596-8cbb-ad1b403a2368
-----

+++++

.....
Recursive Motion Machine
-----
4e59a712-6f55-4703-a420-a1f62b483afa
-----
onPlay:Put1ProdPlus-AutoTargeted-atGadget-onHost-noTargetingError
+++++
GR0B1R0:Put1Ghost Rock
.....
Winchester Model 1873
-----
c5a6c2ba-866e-4854-bbaf-4e3fd6ea49de
-----

+++++
GR0B1R0:BootHost-isCost$$Put1BulletShootoutPlus-AutoTargeted-atDude-onHost$$Remove999Shootout:Draw-isSilent-AutoTargeted-atDude-onHost$$Put1Shootout:Stud-AutoTargeted-atDude-onHost
.....
Fancy New Hat
-----
bb4aad56-6d02-4088-9f20-f64c571f593b
-----

+++++

.....
Confession
-----
51b83721-61e5-42bc-be9e-8b671f0668d4
-----

+++++
GR0B1R0:Pull1Card-testMiracle6-spellEffects<BootHost-isCost++Put1Bounty-Targeted-atDude,None>||GR0B1R0:Pull1Card-testMiracle7-spellEffects<Remove1Bounty-Targeted-atDude-isCost++Gain1Ghost Rock,None>
.....
Shield of Faith
-----
ae0d585d-25e0-4495-8757-71ef0efffb0e
-----

+++++
GR0B1R0:Pull1Card-testMiracle7-spellEffects<SimplyAnnounce{prevent dudes from being aced or discarded during this shootout and reduce their casualties by 1 for this round},None>
.....
Rope and Ride
-----
1e6f4bb8-762f-4e61-9f19-b3585c0f5186
-----
onPlay:MoveTarget-DemiAutoTargeted-atDude-targetMine-choose1-moveToDeed_or_Town Square_or_Outfit$$MoveTarget-DemiAutoTargeted-atDude-targetOpponents-choose1-moveToDeed_or_Town Square_or_Outfit$$BootTarget-DemiAutoTargeted-atDude-targetOpponents-choose1
+++++

.....
Incubation
-----
f36622a2-667f-43bc-ac16-0f8c8dabec00
-----
onPlay:Put1PermInfluenceMinus-AutoTargeted-atDude-onHost$$Put1PermBulletMinus-AutoTargeted-atDude-onHost$$Put3ValuePermMinus-AutoTargeted-atDude-onHost
+++++

.....
Flight of the Lepus
-----
3e1d8cfb-03b1-433a-a7ae-b12f124fb7ef
-----
onPlay:SendHomeBootedMulti-doNotBoot-Targeted-atDude-isParticipating-targetMine-onlyInShootouts-noTargetingError$$SendHomeBootedMulti-Targeted-atDude-isParticipating-targetOpponents-onlyInShootouts-noTargetingError||onPlay:SendHomeBootedMulti-doNotBoot-Targeted-atDude-onlyInNoon
+++++

.....
Avie Cline
-----
2cba8b31-062a-4701-a9a4-76a330681bb7
-----

+++++
GR0B1R0:MoveTarget-Targeted-atDude-moveToDeed
.....
Judge Harry Sommerset
-----
04e204a6-8879-477b-8153-adcda50b1f51
-----

+++++
GR0B1R0:StartJob-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-choose1-jobEffects<DiscardTarget,None>$$Spawn1Gunslinger-modAction:ParticipateMyself
.....
Ebenezer Springfield
-----
799ea10c-9dc3-414e-bd72-c1d9fa662926
-----

+++++
GR0B0R0:Put1Bounty-Targeted-atDude-targetOpponents
.....
Elander Boldman
-----
294a7ce9-af00-46e1-b33c-aab21ebf3b09
-----

+++++
GR0B1R0:CustomScript
.....
Antheia Pansofia
-----
56fd7d6b-d14a-4b9d-a29c-40102bf4377b
-----

+++++

.....
Harry Highbinder
-----
fffb2b62-4d83-4b3c-9696-2905477d892f
-----

+++++

.....
Max Baine
-----
4d2ffa2b-f09d-47ef-845b-d227b060b603
-----

+++++
GR0B1R0:PlayTarget-Targeted-atDude-fromHand-payCost-reduc3
.....
El Grajo
-----
9eada35c-a9a5-485f-9513-305661421944
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atWeapon_and_Melee-onAttachment$$Gain2Bullets$$Remove999Shootout:Draw-isSilent
.....
Jacqueline Isham
-----
c65152fd-434e-4729-ac44-cf61d1affbdc
-----

+++++
GR0B0R1:Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Huntsmen's Society
-----
0334ecdd-6da1-47bf-a3d0-b4988bdf8a07
-----

+++++
GR0B0R1:Put1ProdPlus-Targeted-atDude
.....
Secured Stockyard
-----
5af04c4c-8282-4abf-9e55-a13ace8a998b
-----

+++++
GR0B1R0:Gain1Ghost Rock
.....
La Quema
-----
68bce669-132a-43ca-9727-8de86b3b039c
-----

+++++
GR0B1R0:ParticipateHost$$BootTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1
.....
Asyncoil Gun
-----
34970b97-c353-47a5-bf1c-4cdc0351eef5
-----

+++++
GR0B1R0:Pull1Card
.....
Scoop Hound
-----
b756df9e-6c24-4b33-a6f1-ff6b82dd51e5
-----

+++++
GR0B1R0:SimplyAnnounce{prevent dudes from joining or leaving the shootout via shootout actions}
.....
Rapier
-----
2950ad4b-c835-415f-a24c-b61c9702c728
-----

+++++

.....
Vitality Tonic
-----
03dc1c9f-3b91-4bf6-af64-6bcbdca36839
-----

+++++
GR2B0R1:Pull1Card
.....
Consecration
-----
00867833-050d-4214-bccb-d1e787f15baf
-----

+++++
GR0B0R0:Pull1Card-testMiracle6-spellEffects<Put2BulletNoonPlus-Targeted-atDude++Put2InfluenceMinus-Targeted-atDude++Put1High Noon:Stud-Targeted-atDude,None>
.....
Mark of Pestilence
-----
12d7d9e6-cffa-46ef-8ae7-d8fbbeb88e4c
-----

+++++
GR0B1R0:Pull1Card-testHex9-spellEffects<BootMultiple-AutoTargeted-atDude-isParticipating++UnbootMyself,None>
.....
Cookin' Up Trouble
-----
f7d5aaa2-b476-4156-bef1-697cd39d7dd7
-----
onPlay:CustomScript
+++++

.....
Ol' Fashioned Hangin'
-----
0453a270-56fb-4714-b3d7-41129bf4ccd5
-----
onPlay:StartJob-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-choose1-jobEffects<AceTarget,None>
+++++

.....
No Turning Back
-----
b308c49b-6871-4067-a269-9aa7f8917bdc
-----

+++++

.....
Junior
-----
85989968-0332-4dc2-a5eb-9921267453ff
-----
onPlay:Retrieve1Card-toTable-grabGoods_and_Mystical_and_nonGadget-payCost-searchComplete
+++++

.....
The Fabulous Mister Miss
-----
4b50bf0d-29e3-4e93-8acc-f77c60b80e57
-----

+++++
GR0B0R1:Put3InfluenceMinus-Targeted-atDude-targetOpponents
.....
Sister Mary Gideon
-----
92d9bfc1-4be6-4973-b820-0ac65e5d7b01
-----

+++++

.....
Nathan Shane
-----
65b724a9-49e4-4c1c-9db8-e3f3081fa3fe
-----

+++++
GR0B1R0:CustomScript
.....
Warren Graves
-----
e20afd82-c3d7-4152-aac9-4392a29733b8
-----

+++++
GR0B0R0:SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetMine-choose1$$ParticipateMyself
.....
Jack O'Hara
-----
c4b260a0-1861-4300-8c96-6064f7367cb5
-----

+++++

.....
John "Aces" Radcliffe
-----
686696a5-da6b-46d7-92b2-2ba051a3153e
-----

+++++

.....
Steele Archer
-----
ef19f3d5-a52f-403a-a342-ae32f3753120
-----

+++++
GR0B0R0:UnbootTarget-DemiAutoTargeted-atHex-choose1
.....
Old Man McDroste
-----
8628bdf2-3900-4e36-941e-043560d81757
-----

+++++
GR0B1R0:Put5InfluenceMinus-Targeted-atDude
.....
Flint's Amusements
-----
29add78a-5369-43d9-80d9-4006f6757a6e
-----
whileInPlay:Gain1Ghost Rock-foreachResolution-typeAction
+++++
GR0B1R0:Draw1Card
.....
Lula's Exploit
-----
5529098d-fd5f-41c1-9121-58a4c2b41c89
-----
atPhaseGamblin:Refill2Ghost Rock
+++++
GR0B0R1:Remove1Ghost Rock-isCost-isSilent$$Gain1Ghost Rock
.....
Testing Range
-----
5448fd9b-6cce-4973-a40a-f4769b7f6f47
-----

+++++
GR2B1R0:UnbootTarget-DemiAutoTargeted-atMad Scientist-isBooted||GR0B1R0:Pull1Card
.....
Dog's Duster
-----
6da3418d-0c64-425c-8191-680e7f2480b3
-----

+++++
GR0B1R0:CalloutTarget-Targeted-atDude-hasMarker{Bounty}
.....
Stoker's Sabre
-----
0c37b916-b5e6-4e43-8640-8a970465b70e
-----

+++++
GR0B1R0:UnbootTarget-Targeted-atSpell$$Remove1Used Ability-Targeted-atSpell-targetMine-isSilent
.....
Fate Dispenser
-----
80905177-39e7-49fd-a244-aa6c70baa9e8
-----

+++++
GR0B1R0:Draw1Card
.....
Soul Cage
-----
59978194-81c0-482e-8748-1df5b3a6245f
-----

+++++
GR0B1R0:Retrieve1Card-fromBootHill-toTable-grabAbomination-searchComplete
.....
For Such a Time as This
-----
abed8d3b-d73f-4426-bbeb-6e0124aae9fb
-----

+++++
GR0B1R0:Pull1Card-testMiracle9-spellEffects<StartJob-AutoTargeted-atTown Square,None>||GR0B0R1:Retrieve1Card-toTable-grabDude-searchComplete-payCost-reduc4
.....
Sword of the Spirit
-----
39e4ddd4-987b-450b-a3dd-260a20db35a0
-----

+++++
GR0B0R0:Pull1Card-testMiracle7-spellEffects<Put1BulletNoonPlus-Targeted-atDude++Put1High Noon:Stud-Targeted-atDude,None>
.....
A Fight They'll Never Forget
-----
3f0bc78c-6b5d-4951-bcd1-a3ab3b08481e
-----

+++++

.....
Buried Treasure
-----
e5e6dd23-04d0-4614-a8da-a9a74785a7c2
-----
onPlay:Retrieve1Card-fromDiscard-toBootHill$$Gain3Ghost Rock$$Draw1Card
+++++

.....
Nightmare at Noon
-----
590b905c-f114-48d2-930f-66e446458c84
-----
onPlay:Put1BulletShootoutMinus-AutoTargeted-atDude-isParticipating-targetOpponents$$Put1Shootout:Draw-isSilent-AutoTargeted-atDude-isParticipating-isStudDude-hasProperty{Bullets}le1
+++++

.....
Raking Dragons
-----
c946d5d9-276e-4464-8958-c1bf3045a817
-----
onPlay:Pull1Card
+++++
GR0B0R0:BootTarget-Targeted-atDude-targetOpponents-isParticipating$$Put2ValueShootoutMinus-Targeted-atDude-targetOpponents-isParticipating
.....
Shifu Speaks
-----
12fb4862-f1e1-4ad3-b28f-2206b1a194e9
-----
onPlay:Pull1Card
+++++
GR0B0R0:Put1Influence-Targeted-atDude_and_Kung Fu-targetMine$$RequestInt{Discard how many cards?}-Min-Max5$$Draw1Card-toDiscard-perX
.....
Rabbit's Lunar Leap
-----
ceaefbb7-2540-44cf-abaf-755042f318ae
-----
onPlay:Pull1Card
+++++
GR0B0R0:ParticipateTarget-Targeted-atDude_and_Kung Fu-targetMine$$UnbootTarget-Targeted-atDude_and_Kung Fu-targetMine
.....
Zhu's Reward
-----
23a1a9a2-cfc2-478c-9d93-46c23cb6a567
-----
onPlay:Pull1Card
+++++
GR0B0R0:BootTarget-DemiAutoTargeted-atDude_and_Kung Fu-TargetMine-isParticipating-choose1-isCost$$SendHomeBootedMulti-Targeted-atDude-targetOpponents-isParticipating
.....
Zhu's Ferocity
-----
c77c3030-224b-4cb2-bf27-7be6cf6d5fcc
-----
onPlay:Pull1Card
+++++
GR0B0R0:Put1BulletShootoutMinus-Targeted-atDude-isParticipating-targetOpponents$$Put1BulletShootoutPlus-Targeted-atDude_and_Kung Fu-isParticipating-targetMine
.....
Richard Faulkner
-----
1456fe5c-9edb-4521-abd7-3a029851222d
-----

+++++

.....
Mazatl
-----
3b853568-7da7-40d2-952c-72b611330f11
-----

+++++
GR0B0R0:MoveMyself-moveToDeed_or_Town Square_or_Outfit
.....
Marcia Ridge
-----
381e141f-b745-4c05-b455-b4fe3c1fc73c
-----

+++++
GR0B0R1:UseCustomAbility-DemiAutoTargeted-atDeed-targetOpponents-choose1
.....
Black Elk
-----
d9beac18-b2a7-451d-a17f-6b5202cd3b1a
-----

+++++

.....
Lydia Bear-Hands
-----
ff016aea-9c16-44a6-bacf-4ee2ca9a913e
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atSpell-isUnbooted-onAttachment-choose1-isCost$$Put1Shootout:Harrowed-DemiAutoTargeted-atDude-isParticipating-TargetMine-choose1
.....
Jackson Trouble
-----
1086db48-f246-4e5f-a6d2-2bd6ebce9ba8
-----

+++++

.....
Three-Eyed Hawk
-----
3b3815a8-ca49-48c0-96eb-d50d1d493d68
-----

+++++
GR0B0R1:Gain1Ghost Rock
.....
Bloody Teeth
-----
b49ca811-796c-4cb9-abd4-9657d88a9ceb
-----

+++++

.....
Butch Deuces
-----
2256eecb-02d3-4d01-b407-3417a109691e
-----

+++++
GR0B1R0:CustomScript
.....
Smiling Frog
-----
c665872f-61b0-4a23-b923-12ea6d5d8c95
-----

+++++
GR0B0R0:CustomScript
.....
Sarah Meoquanee
-----
245f816f-f407-41e7-b8e6-9fb6cd638bf3
-----

+++++
GR0B0R0:ParticipateMyself$$Put1Shootout:Stud
.....
Chief Stephen Seven-Eagles
-----
eed9713a-5a8b-4a10-91b1-4ecd27eee125
-----

+++++
GR0B1R0:SimplyAnnounce{make Chief Stephen Seven Eagles worth 1 control point per card attached to a deed they control}
.....
Laughing Crow
-----
7d921e83-5ac4-40c7-a756-4f596b1fe8ee
-----

+++++
GR0B0R0:CustomScript
.....
Benjamin Washington
-----
942e1f7e-d6d0-4882-b8e7-68135e9d52fc
-----

+++++
GR0B1R0:CustomScript
.....
Randall
-----
1b7d462c-4ba6-4317-904e-7efc49b4a15e
-----

+++++
GR0B0R1:Draw1Card
.....
Longwei Fu
-----
bcc0f3cf-105d-4030-a4fc-b45d978bfc7e
-----

+++++

.....
Xui Yin Chen
-----
910c051f-f36d-4245-88db-767d80998fc1
-----

+++++
GR0B1R0:Remove999Shootout:Draw-isSilent-AutoTargeted-atDude-targetMine-isParticipating$$Put1Shootout:Stud-AutoTargeted-atDude-targetMine-isParticipating
.....
Natalya
-----
48e2565e-1c96-45c8-837a-85533efc554b
-----

+++++
GR0B0R0:Gain1Ghost Rock-perTargetProperty{Production}-Targeted-atDeed
.....
Hamshanks
-----
05b9067b-7356-4fbf-b5a7-ee96c3135b9f
-----

+++++

.....
Hiram Capatch
-----
7a390eac-db25-477b-80a9-7bbc051d87da
-----

+++++

.....
Yunxu Jiang
-----
3c9f4821-0e6c-4e68-9666-d1784a0eca4e
-----

+++++

.....
Abuelita Espinoza
-----
f58ccb1d-d0f7-4339-abc7-6c017bac34c4
-----

+++++

.....
Bai Yang Chen
-----
306a6cce-32c1-480f-b8a6-e239dad1379c
-----

+++++
GR0B0R1:Draw2Cards$$Put1ProdPlus
.....
Daomei Wang
-----
1c3b7ec1-882e-458d-9409-21e23fef5f2d
-----
onPlay:MoveTarget-DemiAutoTargeted-atDude_and_108 Glorious Bandits-targetMine-choose1-moveToDeed_or_Town Square_or_Outfit
+++++

.....
Xiaodan Li
-----
ed07deb6-3693-4ede-ae62-0f132d538211
-----

+++++

.....
T'ou Chi Chow
-----
e5c43d70-6280-43e4-a0c6-8bc4239382e7
-----

+++++
GR0B0R1:BootTarget-Targeted-atDeed-targetMine-isCost$$UnbootTarget-Targeted-atDude-targetMine
.....
Nunchucks
-----
06c47afe-528b-416e-b068-5b609225afe0
-----
constantAbility:Kung Fu Bonus:1-isParticipating
+++++
GR0B1R0:SimplyAnnounce{reduce the pull by this dude's Kung Fu rating}
.....
Idol of Tlazolteotl
-----
f0e6f9a4-1a55-4cd6-9296-e06c823e22b2
-----

+++++
GR0B1R0:RehostTarget-Targeted-atTotem_or_Improvement_or_Condition
.....
Eagle Wardens
-----
dfb469f4-efc8-46f9-84df-66f5f973c09c
-----

+++++
GR0B1R0:UseCustomAbility-DemiAutoTargeted-atDude-isUnbooted-targetMine-choose1
.....
108 Righteous Bandits
-----
94c5b661-8f3d-46ea-975e-482ff0e2be8a
-----

+++++
GR0B1R0:MoveTarget-Targeted-atDude-moveToDude
.....
Spirit Guidance
-----
d6931afe-58cd-430f-9fe2-178738614cf8
-----

+++++
GR0B1R0:Pull1Card-testSpirit7-spellEffects<DiscardTarget-DemiAutoTargeted-fromHand-choose1-isCost++Draw1Card,None>||GR0B1R0:Pull1Card-testSpirit10-spellEffects<Draw2Cards++DiscardTarget-DemiAutoTargeted-fromHand-choose1++DiscardTarget-DemiAutoTargeted-fromHand-choose1,None>
.....
The Pack Awakens
-----
79254945-f5f3-48ab-90d9-f1da1dd15d74
-----

+++++
GR0B1R0:Pull1Card-testSpirit8-spellEffects<Spawn1Nature Spirit-modAction:ParticipateMyself,None>
.....
Spirit Trail
-----
a655edaa-c2e8-41d3-9710-e96bf21fae1b
-----

+++++
GR0B1R0:Pull1Card-testSpirit6-spellEffects<MoveTarget-Targeted-atDude-targetMine-moveToDeed_or_Town Square_or_Outfit,None>
.....
Many Speak as One
-----
889fa2dd-dd3e-4830-8d59-7cb242e1c68e
-----

+++++
GR0B1R0:Pull1Card-testSpirit9-spellEffects<Spawn1Ancestor Spirit,None>
.....
Spirit Dance
-----
e4b062de-79ef-4005-a1e0-7ce0a4ed9d34
-----

+++++
GR0B1R0:Pull1Card-testSpirit10-spellEffects<Spawn1Nature Spirit-modAction:ParticipateMyself,None>
.....
Ancestor Spirit
-----
53a212a6-34a6-47b0-bb24-45f1888bebf6
-----

+++++

.....
Nature Spirit
-----
c4689399-c350-46b3-a79a-f8c62d926cd5
-----

+++++

.....
Rabbit's Deception
-----
ba290d31-e66f-427d-bc33-65200b20ad52
-----
onPlay:Pull1Card
+++++
GR0B0R0:SendHomeBootedTarget-DemiAutoTargeted-atDude_and_Kung Fu-isParticipating-targetMine-choose1$$SendHomeBootedTarget-Targeted-atDude-isParticipating-targetOpponents-noTargetingError
.....
A Hero's Passing
-----
d332f810-af0a-42ee-9649-a4b34809a6e1
-----

+++++

.....
Tummy Twister
-----
82cd476b-6ff5-4f49-adad-a3a283f8928a
-----

+++++
GR0B0R0:RehostMyself-Targeted-atDude$$Put1ProdMinus-AutoTargeted-onHost
.....
Backroom Deals
-----
59fba6dd-ae8f-4369-9596-1b6a44e6685e
-----
onPlay:Put1UpkeepPrePaid-perTargetProperty{Upkeep}-Targeted-atDude-targetMine-isSilent$$Put1ProdPlus-perTargetProperty{Upkeep}-Targeted-atDude-targetMine
+++++

.....
Civil War
-----
b4a04153-f279-4feb-aa29-a9e86607dd3b
-----
onPlay:SimplyAnnounce{to force their opponent to move one of theit targeted dudes to another location}
+++++

.....
Forced Quarantine
-----
ea2b5db4-659a-4524-8ca3-e84ae8d1f9b5
-----
onPlay:StartJob-Targeted-atDude-bootLeader-jobEffects<RehostMyself-AutoTargeted-atDude-isMark++BootHost,None>||atPhaseGamblin:DiscardHost
+++++

.....
The Extra Bet
-----
ff370ba2-fd39-4996-ae02-abd3f46c9af7
-----

+++++
GR0B1R0:CustomScript
.....
Morgan Mining Company
-----
b5ef38d4-d929-4a54-8ac8-36871ba2d66a
-----
atPhaseUpkeep:Gain1Ghost Rock-perEveryCard-AutoTargeted-atStrike-targetMine
+++++

.....
Quarantine Tent
-----
9312b25c-db3d-4889-9c6e-8b4ec495f3a8
-----

+++++
GR0B1R0:BootTarget-Targeted-atDude-targetMine-isCost$$UnbootTarget-AutoTargeted-atOutfit-targetMine$$Remove1UsedAbility-AutoTargeted-atOutfit-targetMine-isSilent
.....
Cooke's Nightcap
-----
a2cae75c-ac0b-437b-a951-a9e891ce4034
-----

+++++

.....
Margaret Hagerty
-----
89b1a934-a4a5-4900-a3b7-f2c5c98f1d1d
-----

+++++

.....
The Wretched
-----
2c14e947-f0de-4049-8016-9d4679f9b2a5
-----
onPlay:AceTarget-AutoTargeted-atDude-targetMine-choose1$$Put2Bounty-DemiAutoTargeted-atDude_and_Mad Scientist-targetMine-choose1-noTargetingError
+++++

.....
Deborah West
-----
d775dd42-183d-4165-83ed-3d825ea051a2
-----

+++++
GR0B0R1:Put1Shootout:Stud
.....
Abram Grothe
-----
11c7f4dc-334e-466f-868a-d5df9157322e
-----
onPay:Reduce1CostPlay-perEveryCardMarker{Bounty}-AutoTargeted-atDude-hasMarker{Bounty}-targetOpponents
+++++
GR0B0R0:UnbootMulti-Targeted-atDude_and_Deputy-targetMine$$UnbootMyself
.....
"Dead" Billy Jones
-----
5005c7d4-a6f3-440d-ae61-dc75412266fb
-----

+++++
GR0B0R0:MoveTarget-Targeted-atDude-moveToDeed_or_Town Square_or_Outfit
.....
Lillian Morgan
-----
a17a638e-7ad1-4216-8748-f9526be7107a
-----
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atRanch_or_Horse-targetMine
+++++
GR0B0R0:Retrieve1Card-fromDiscard-grabAction-toTable-payCost
.....
Jim Cheveyo
-----
ca460412-7ba2-4b04-8ec2-44c86460ce1a
-----

+++++

.....
Enapay
-----
ea2ecabb-966e-466f-a285-29028dba628b
-----

+++++
GR0B1R0:Put1InfluencePlus-Targeted-atDude
.....
Danny Wilde
-----
aae392c5-3374-42af-827d-653a9ced3e9b
-----

+++++

.....
Michael "The Badger" Dodge
-----
a0a7fb60-18a3-4a8e-8dd1-a92931e724b1
-----

+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atDude-isParticipating-choose1$$Pull1Card
.....
Asakichi Cooke
-----
ad7f9fb2-c845-49bd-82e2-0a94037e1d77
-----

+++++
GR0B0R0:DiscardTarget-DemiAutoTargeted-fromHand-isCost-choose1$$MoveTarget-Targeted-atDude-targetMine-moveToDeed_or_Town Square_or_Outfit
.....
Emre, The Turkish Bear
-----
45a5acd3-3659-4654-8033-44ef084e1dba
-----

+++++
GR0B0R0:Pull1Card$$Remove999High Noon:Draw-isSilent$$Put1High Noon:Stud
.....
Dabney Scuttlesby
-----
ad157676-5166-40b3-99a4-9cbe1300366d
-----

+++++

.....
Ivor Hawley
-----
e1d93d5b-222d-4a82-b18f-62728f7791c0
-----
onPay:ReduceSCostPlay||onPlay:Retrieve2Cards-fromBootHill-grabAbomination_or_Hex-toTable-payCost-reduc3
+++++

.....
Samantha "Sammy" Cooke
-----
8aa596d9-7b03-4939-9217-3b150fbe77d1
-----

+++++
GR1B1R0:DiscardTarget-Targeted-atGoods$$Put1Bounty
.....
Sloane
-----
6a8c7f99-7f5c-4824-99b7-a9c5f9d9d715
-----
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atDude-hasMarker{Bounty}-targetMine||onPlay:Put1Bounty-perEveryCard-AutoTargeted-atDude-hasMarker{Bounty}-targetMine
+++++

.....
Mutant Cattle
-----
88967399-9c8c-4502-bf63-5f442aff836b
-----

+++++

.....
Monte Bank
-----
95d23e7f-daa9-44ef-bcd3-50683340db62
-----

+++++

.....
Wendy's Teethkickers
-----
31a6a524-0191-4034-a20c-ec3008d28a6e
-----

+++++
GR0B1R0:UnbootHost$$Put1InfluencePlus-AutoTargeted-onHost
.....
Rich Man's Guard Dog
-----
2a59bc29-adca-4b5c-94f3-e9c94353d4b5
-----

+++++
GR0B1R0:Pull1Card
.....
Devil's Joker (red)
-----
e5aa241d-bc8c-46ee-a250-dac44616415e
-----

+++++

.....
Devil's Joker (black)
-----
c8311233-937c-4468-89f1-8c667ced576b
-----

+++++

.....
Abram's Crusaders
-----
24d74ad6-5532-4a11-ac66-a8b9f258cbf9
-----

+++++
GR0B1R0:Put1High Noon:Deputy-Targeted-atDude-targetMine
.....
The Sanatorium
-----
6f9a4a04-411a-4c2b-b4c2-4db8d6c18157
-----

+++++
GR0B1R0:Put1BulletNoonMinus-Targeted-atDude-targetOpponents$$Put1ValueNoonMinus-Targeted-atDude-targetOpponents$$Put1InfluencePlus-Targeted-atDude-targetMine||GR0B1R0:Put1BulletNoonMinus-targetOpponents$$Put1ValueNoonMinus-targetOpponents$$Put1Noon:Huckster Skill Bonus-Targeted-atDude-targetMine
.....
Den of Thieves
-----
922a0a4b-c9b6-404a-b26b-87f079fc7a6c
-----

+++++
GR0B1R0:Put1Bounty-DemiAutoTargeted-atDude_and_Grifter-targetMine-choose1$$Gain1Ghost Rock$$UseCustomAbility
.....
Dumbstruck
-----
c5f02d5f-ad42-452f-8a7d-b48f58c6e76b
-----

+++++
GR0B1R0:Pull1Card-testMiracle9-spellEffects<UnbootHost++Put1High Noon:Dumbstruck Protected-AutoTargeted-onHost,None>-onlyInNoon||GR0B1R0:Pull1Card-testMiracle9-spellEffects<UnbootHost++Put1Shootout:Dumbstruck Protected-AutoTargeted-onHost,None>-onlyInShootouts
.....
Fiery Rhetoric
-----
507348af-e310-42c1-9878-c8c605882128
-----

+++++
GR0B1R0:Pull1Card-testMiracle6-spellEffects<StartJob-AutoTargeted-atTown Square,None>
.....
Strength of the Ancestors
-----
98b3a9a9-3ab6-4413-b6c0-cc113ed26731
-----

+++++
GR0B1R0:Pull1Card-testSpirit5-spellEffects<Put3BulletNoonPlus-AutoTargeted-atDude-onHost++Remove999High Noon:Draw-AutTargeted-atDude-onHost-isSilent++Put1High Noon:Stud-AutoTargeted-atDude-onHost++Refill1High Noon:Strength of Ancestors-AutoTargeted-atDude-onHost-isSilent,None>
.....
Phantom Fingers
-----
899f3c84-3f9f-4589-83d9-2c2fe663d6a2
-----

+++++
GR0B1R0:Pull1Card-testHex6-spellEffects<BootTarget-Targeted-atGoods-targetOpponents++Refill1Phantom Fingers-Targeted-atGoods-targetOpponents-isSilent++UseCustomAbility-Targeted-atGoods-targetOpponents,None>
.....
Red Horse's Tail
-----
aea19556-2c30-4e03-a677-d0e6f6fa6c66
-----

+++++
GR0B1R0:Pull1Card-testSpiritX-difficultyValue-Targeted-atDude-spellEffects<BootTarget-Targeted-atDude,None>-onlyInNoon||GR0B1R0:Pull1Card-testSpiritX-difficultyGrit-Targeted-atDude-spellEffects<SendHomeBootedTarget-Targeted-atDude-targetOpponents,None>-onlyInShootouts
.....
Fire of Nanahbozho
-----
03da32d4-2e32-43d3-94c7-f3457414d298
-----

+++++
GR0B1R0:Pull1Card-testSpirit8-spellEffects<UnbootTarget-Targeted-atDude,None>
.....
Xiang Fang
-----
5c204eb2-3416-4f3e-8822-ac93c5f66978
-----
onPlay:Gain1Ghost Rock-perTargetProperty{Production}-Targeted-atDeed_or_Outfit$$Put1ProdMinus-perTargetProperty{Production}-Targeted-atDeed-targetOpponents-noTargetingError-isSilent$$Put1ProductionPrePaid-perTargetProperty{Production}-Targeted-atDeed-targetOpponents-noTargetingError-isSilent$$Put1ProdMinus-perTargetProperty{Production}-Targeted-atOutfit-targetMine-noTargetingError-isSilent$$Put1ProductionPrePaid-perTargetProperty{Production}-Targeted-atOutfit-targetMine-noTargetingError-isSilent
+++++

.....
He Fang
-----
555ee88e-b7a2-41b9-a781-357a9fc53f65
-----

+++++
GR0B1R0:PlayTarget-DemiAutoTargeted-fromHand-atAbomination_and_nonGadget-choose1-payCost-reduc2
.....
Kabeda Hakurei
-----
934a695a-50c9-4fcc-8434-cb87d6c5e967
-----

+++++

.....
Zachary Deloria
-----
4c2da757-17a9-43ed-b7cd-c26efcbc0ff7
-----

+++++

.....
Karl Odett
-----
1ee1c912-a6d1-4c74-8fb7-a3430a2cd1c8
-----

+++++
GR0B0R1:Put3PermInfluencePlus
.....
Erik Samson
-----
8cc64eef-41b5-4e60-a68a-e35384d41a7a
-----

+++++

.....
Dr. Brian Foxworth
-----
08c8a178-3613-4b03-a885-5fc205e7e68e
-----

+++++
GR0B0R1:SimplyAnnounce{reduce their casualties by this dude's influence}$$DiscardMyself
.....
Buford Hurley
-----
654372b0-0c12-4d64-9f78-128adf6d6457
-----

+++++
GR0B0R0:Put1ProdPlus$$Put1ProdMinus-Targeted-atDeed
.....
Doris Powell
-----
0f21f34d-76ba-4a54-b690-fafa160ef170
-----

+++++
GR0B0R0:Put1ControlPlus
.....
Rico Rodegain
-----
d760b8cd-7d30-4e1b-a4e6-9b7163eedf85
-----

+++++
GR0B1R0:CustomScript
.....
Maza Gang Hideout
-----
381aa2d3-aa99-49a9-8d53-6b09f8f4bceb
-----

+++++
GR0B0R0:Put1ProdPlus
.....
Miasmatic Purifier
-----
9c101ef5-5214-4d20-8e45-906f8fcc23b3
-----
atSundown:CustomScript
+++++

.....
Disgenuine Currency Press
-----
4bef1feb-f6b5-44ff-8af4-790d121d12e7
-----
onPlay:Gain5Ghost Rock$$UnbootHost
+++++

.....
Tlaloc's Furies
-----
774ebaf2-a983-414b-acc3-7250bd61b9f2
-----
constantAbility:Skill Bonus:1-perEveryCard-AutoTargeted-atTlaloc's Furies
+++++

.....
Personal Ornithopter
-----
e258726e-3705-4d0f-ae7a-d37ce2952b82
-----

+++++
GR1B0R1:ParticipateHost||GR0B1R0:SendHomeBootedHost
.....
Jael's Guile
-----
7eb84c0d-be8e-40b5-891c-b1b4c95b55af
-----

+++++
GR0B1R0:CustomScript
.....
Hustled
-----
0967a396-2be7-4a61-afe9-a119034266fc
-----
onPlay:BootTarget-DemiAutoTargeted-atDude-targetMine-choose1$$Gain2Ghost Rock$$BootTarget-Targeted-targetOpposing-noTargetingError
+++++

.....
An Accidental Reunion
-----
79ec0f19-cc3a-4f63-930e-f3dadf2645f7
-----
onPlay:SimplyAnnounce{force each cheating player to take 2 casualties}$$Lose2Ghost Rock-isCost-isOptional$$UninstallMyself
+++++

.....
A Slight Modification
-----
2c8fd25e-ff8b-4129-8a6c-2c6f3590c455
-----
onPlay:BootTarget-DemiAutoTargeted-atGoods_and_Gadget-targetMine-choose1$$SimplyAnnounce{cancel the shootout action}
+++++

.....
Rabbit Takes Revenge
-----
2f4ad55c-0be5-422e-bb47-ccb1a6fe21e0
-----
onPlay:Pull1Card
+++++

.....
Morgan Stables
-----
668fb674-5e1f-4bc9-98ae-ca7120277ea9
-----

+++++
GR0B0R1:PlayTarget-DemiAutoTargeted-atHorse-fromHand-choose1-payCost-reduc1||GR0B1R0:UseCustomAbility
.....
108 Worldly Desires
-----
fb84426c-6b63-4dee-a2df-2d3c7b89c230
-----

+++++
GR0B0R1:Draw1Card-toDrawHand$$DiscardTarget-DemiAutoTargeted-fromDrawHand-choose1
.....
Beyond the Veil 
-----
d47cff43-d675-4410-929c-508475fd7814
-----

+++++
GR0B1R0:BootTarget-Targeted-atTotem-targetMine-isCost$$MoveTarget-Targeted-atDude-targetMine-moveToTotem
.....
Shizeng Lu
-----
bc2f230e-1c4a-47fe-ab97-31a58112e473
-----

+++++

.....
"Lucky" Sky Borne
-----
16d4df2b-4494-4e65-b910-2c35e07d604c
-----

+++++
GR0B0R1:Retrieve1Card-grabSidekick-toTable-payCost
.....
Riorden O'Lithen
-----
644870b4-541c-4824-af19-3e9a5cd28264
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atSpell-isUnbooted-onAttachment-choose1-isCost$$Put1Bounty-Targeted-atDude
.....
Mariel Lewis
-----
45f31939-bdaf-49ee-850f-b08f5c809dc0
-----

+++++
GR0B0R0:UnparticipateTarget-Targeted-atDude-targetOpponents$$MoveTarget-Targeted-atDude-moveToOutfit-targetOpponents
.....
Miranda Clarke
-----
43abee45-ec1d-4e5f-8997-e8501d66ed5b
-----

+++++

.....
Elliot Smithson
-----
662dd66d-9cb9-48f6-84bd-4496b3484d01
-----

+++++
GR0B0R0:Gain1Ghost Rock$$UnbootTarget-Targeted-atDude
.....
Forster Cooke
-----
1d283fb4-9fe2-4143-83e2-b6080149df3f
-----

+++++

.....
The Tattooed Man
-----
f1d866bc-8056-4cc8-976a-ee76afca5054
-----

+++++

.....
Joseph Dusty Hill
-----
7f2d6abb-5b50-4d3c-8a2d-aeb447ea5fbd
-----

+++++

.....
Shelby Hunt
-----
41a8c1e5-03e8-427e-a1f2-ffc59dbc420b
-----

+++++
GR0B0R0:Put1BulletShootoutPlus$$Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Xemo's Turban
-----
288545a8-9c7b-4e31-ad00-c97910b19b17
-----

+++++
GR0B1R1:UseCustomAbility
.....
Guide Horse
-----
aa1c1ffa-db99-464b-849d-5cb6264245b7
-----

+++++
GR0B1R0:MoveHost-moveToTown Square
.....
Blight Serum
-----
0ed71726-f276-419e-b037-17eb62294489
-----

+++++
GR0B0R1:SendHomeBootedTarget-Targeted-atDude$$AceMyself||GR0B1R0:RehostMyself
.....
Marty
-----
fcac7bbf-dd62-43de-8ade-8ba9893a986f
-----

+++++
GR0B1R0:BootMyself-isCost$$UnbootHost
.....
The Joker's Smile
-----
d3a57ce1-7abd-45b0-82d7-fa0d6324a91d
-----
whileInPlay:Gain1Ghost Rock-foreachUsedJokerAced
+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-atJoker-fromHand-choose1-isCost$$Gain1Ghost Rock$$Draw1Cards||GR1B1R0:Retrieve1Cards-fromBootHill-toDiscard-grabJoker
.....
Old Marge's Manor
-----
19bdb26b-0853-4520-9f72-71d7e4ab6c1d
-----

+++++
GR0B1R0:Remove999Ghost Rock-Targeted-isCost$$Put1Ghost Rock-perX||GR0B1R0:Put1Ghost Rock||GR0B0R1:Remove1Ghost Rock-isCost$$Gain1Ghost Rock
.....
Owl's Insight
-----
e530bd2e-0fae-4f00-a522-ba5801904a44
-----

+++++
GR0B1R0:Pull1Card-testSpirit5-spellEffects<PlayMulti-Targeted-atGoods_or_Spell-payCost-reduc1-fromHand++Draw999Cards,None>
.....
Righteous Fury
-----
dd9cbe71-952b-4b3f-8b53-afa6144488ac
-----

+++++
GR0B1R0:Pull1Card-testMiracle8-spellEffects<SimplyAnnounce{increase their opponent's casualties by 2 if they win},None>||GR0B1R0:Pull1Card-testMiracle12-spellEffects<SimplyAnnounce{increase their opponent's casualties by 2}++AceMyself,None>
.....
Outgunned
-----
24bb7502-06a2-4871-9ede-fe28d7539eec
-----
onPlay:BootTarget-DemiAutoTargeted-atDude-targetMine-isParticipating-isCost-choose1-isResolution
+++++

.....
Martyr's Cry
-----
27d7356b-3c4d-4b2d-9c23-28aca5cc9c81
-----
onPlay:DiscardTarget-Targeted-atMiracle-targetMine-isResolution
+++++

.....
Deliberate Infection
-----
31ac9e9d-ff78-4f42-a8c1-9014c7df461e
-----
onPlay:Put1PermInfluenceMinus-AutoTargeted-atDude-onHost$$Put1ProdMinus-AutoTargeted-atDude-onHost
+++++

.....
ENDSCRIPTS
=====
'''
