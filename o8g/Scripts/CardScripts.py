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
onPlay:StartJob-AutoTargeted-atTown Square
+++++

.....
Abram Grothe 
-----
44946fbc-1bc0-4a1a-9a55-6138b795bfc8
-----

+++++
GR0B1R0:StartJob-DemiAutoTargeted-atDeed_and_Holy Ground-choose1
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
onPlay:StartJob-DemiAutoTargeted-atDude-bootLeader-choose1-targetOpponents
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
onPlay:StartJob-DemiAutoTargeted-atDeed-choose1
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
GR0B1R0:StartJob-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-choose1
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
onPlay:StartJob-DemiAutoTargeted-atDude-choose1-bootLeader-bountyPosse-targetOpponents
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
GR0B0R1:Put1Bounty-AutoTargeted-atDude-isParticipating-TargetOpponents
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
onPlay:Put1Shootout:Pinned Down-Targeted-atDude-isParticipating-targetOpponents$$Put3BulletShootoutMinus-Targeted-atDude-isParticipating-targetOpponents
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
onPlay:StartJob-AutoTargeted-atTown Square
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
onPlay:CalloutTarget-Targeted-atDude-targetOpponents-leaderTarget{Dude}
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
ENDSCRIPTS
=====
'''
