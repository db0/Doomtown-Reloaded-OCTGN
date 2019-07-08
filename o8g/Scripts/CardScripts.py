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
GR0B1R0:Pull1Card-testHex9-spellEffects<Put2BulletShootoutMinus-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1,None>-onlyInShootouts||GR0B1R0:Pull1Card-testHex9-spellEffects<Put1BulletNoonMinus-Targeted-atDude++Put1InfluenceMinus-Targeted-atDude,None>-onlyInNoon
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
onPlay:CustomScript||onPlay:SimplyAnnounce{Reduce a player's draw rank by 2 hand ranks}
+++++

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
GR0B1R0:Pull1Card-testHexX-difficultyGrit-Targeted-isParticipating-spellEffects<SendHomeBootedTarget-Targeted-choose1,SendHomeBootedHost>
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
GR0B1R0:Pull1Card-testHexX-difficultyValue-Targeted-atDude-spellEffects<BootTarget-Targeted,None>
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
GR0B1R0:Pull1Card-testHexX-difficultyValue-Targeted-atDude-spellEffects<BootTarget-Targeted-atDude,None>
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
onPlay:CustomScript
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
GR0B0R0:Pull1Card-testMiracle9-spellEffects<UnbootTarget-DemiAutoTargeted-atDude_and_Law Dogs-targetMine-isBooted-choose1++UnbootMyself,BootMyself>
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
GR0B0R0:Pull1Card-testMiracle7-spellEffects<Put2BulletNoonPlus-Targeted-atDude++Put2InfluencePlus-Targeted-atDude++Put1High Noon:Stud-Targeted-atDude,None>
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
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atTotem_or_Improvement
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
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atDeed-targetMine
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
GR0B1R0:MoveTarget-Targeted-atDude-moveToDeed_or_Town Square_or_Outfit
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
onPay:Reduce1CostPlay-perEveryCard-AutoTargeted-atDude-hasMarker{Bounty}-targetMine||onPlay:UnbootMulti-AutoTargeted-atDude-hasMarker{Bounty}-targetMine
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
GR0B1R0:Put1BulletNoonMinus-Targeted-atDude-targetOpponents$$Put1ValueNoonMinus-Targeted-atDude-targetOpponents$$Put1InfluencePlus-Targeted-atDude-targetMine||GR0B1R0:Put1BulletNoonMinus-Targeted-atDude-targetOpponents$$Put1ValueNoonMinus-Targeted-atDude-targetOpponents$$Put1Noon:Huckster Skill Bonus-Targeted-atDude-targetMine
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
GR0B0R1:Retrieve1Card-grabSidekick-toTable-payCost-preHost
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
whileInPlay:Gain1Ghost Rock-foreachUsedJokerAced-ifPhaseGamblin
+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-atJoker-fromHand-choose1-isCost$$Gain1Ghost Rock$$Draw1Cards||GR1B1R0:Retrieve1Cards-fromBootHill-toDiscard-grabJoker
.....
Old Marge's Manor
-----
19bdb26b-0853-4520-9f72-71d7e4ab6c1d
-----

+++++
GR0B1R0:Remove999Ghost Rock-Targeted-isCost$$Put1Ghost Rock-perX||GR0B1R0:Put1Ghost Rock
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
Sophie Lacoste
-----
e54fe16d-a197-4461-9309-42718820a294
-----

+++++
GR1B0R1:Put1InfluencePlus-Targeted-atDude-targetMine
.....
"Crazy" Mike Draksil
-----
12bea32a-b544-47e8-b2c7-4355aa1606ac
-----

+++++

.....
Horace Manse
-----
5126c19e-76f4-4355-8dad-8023adab95e7
-----
+++++
GR0B0R0:Retrieve1Card-fromBootHill-grabAbomination$$DiscardTarget-DemiAutoTargeted-fromHand-choose1
.....
Jia Mein
-----
1a69a29f-8d3e-4b90-a4b0-8050855974df
-----

+++++
GR0B0R0:PlayTarget-DemiAutoTargeted-atCondition-fromHand--payCost-reduc2-choose1||GR1B0R1:BootTarget-AutoTargeted-atSpell-isUnbooted-onAttachment-choose1-isCost$$Retrieve1Card-grabCondition-fromDiscard
.....
Janosz Pratt
-----
b791fa54-dbe2-4cda-90dd-91a0df866ed1
-----

+++++
GR0B1R0:Retrieve1Cards-fromDiscard-grabGadget_and_Weapon-toTable-payCost-reduc2$$Put1Janosz Rig-AutoTargeted-atGadget_and_Weapon-onAttachment-choose1$$RehostTarget-AutoTargeted-atGadget_and_Weapon-onAttachment
.....
Vasilis the Boar
-----
20ff3990-e458-4fe7-a8c3-8f7839430e73
-----

+++++

.....
Luke, the Errand Boy
-----
06798ab4-80bd-4497-b6fe-d2093c788ba8
-----

+++++
GR0B0R0:RehostTarget-Targeted-atGadget_and_Goods
.....
Arnold McCadish
-----
1aa58444-fccc-4121-ac6c-482fd48e4b8e
-----

+++++
GR0B1R0:Pull1Card
.....
Rick Henderson
-----
198921ba-aafd-4379-bf9d-205b4a4c7763
-----

+++++
GR0B1R0:CustomScript
.....

Willa Mae MacGowan
-----
4be0dce0-1671-4ac1-9539-d721e8fa5b34
-----

+++++
GR0B0R0:AceMyself$$SendHomeBootedMulti-AutoTargeted-atDude-targetMine-isParticipating
.....
The Orphanage
-----
6d816729-b023-4801-8aee-426ebe657835
-----

+++++
GR0B1R0:Put2ProdPlus-AutoTargeted-atDeed-hasProperty{Control}ge2$$Put1ControlMinus-AutoTargeted-atDeed-hasProperty{Control}ge2$$Put2UpkeepPrePaid-AutoTargeted-atDeed-hasProperty{Control}ge2
.....
The Place
-----
c9534712-af16-422c-8fb5-dac7b8c82c65
-----

+++++
GR0B0R1:Put2ProdPlus-Targeted-atDeed
.....
Hawley's Rose
-----
f316fc32-d8a7-4810-bb75-7c1491058ad8
-----

+++++

.....
LeMat Revolver
-----
3347bf9b-ca97-4625-8409-521a4b90af3e
-----

+++++
GR0B1R0:SimplyAnnounce{increase their hand rank by this dude's bullet rating}
.....
Yagn's Mechanical Skeleton
-----
2fb05302-5326-458a-81bf-c5ad611e63e1
-----
onPlay:Put3ValueNoonPlus
+++++

.....
Fool's Gold
-----
8aad1d23-54ea-4439-8d94-e84b1c283d67
-----

+++++
GR0B1R0:Pull1Card-testHex5-spellEffects<Put1Bounty-AutoTargeted-atDude-onHost++UseCustomAbility,None>
.....
Mother Bear's Rage
-----
5d7757ad-32cf-4383-959e-594e8a7314be
-----

+++++
GR0B1R0:Pull1Card-testSpirit5-spellEffects<Spawn1Nature Spirit-modAction:CalloutTarget-Targeted-atDude-targetOpponents,None>
.....
Focusing Chi
-----
614b4a5f-6a75-4a4d-af99-269ce0c53375
-----
onPull:CustomScript||onPlay:Pull1Card
+++++

.....
Mugging
-----
1ba6917a-9efe-4e3e-a118-3270e1c36854
-----
onPlay:BootMulti-Targeted-atGoods_or_Action_or_Spell-targetOpponents$$StartJob-DemiAutoTargeted-atDude-choose1-targetOpponents-jobEffects<SendHomeBootedTarget-Targeted-atDude++AceMulti-Targeted-atGoods_or_Action_or_Spell-isBooted-targetOpponents-MarkNotTheTarget,None>
+++++

.....
Signing Over the Stores
-----
2d728020-2cf6-4908-8034-7325e9fcb394
-----
onPlay:StartJob-AutoTargeted-atTown Square-jobEffects<RequestInt{Discard how many cards?}-Max5++Draw1Cards-perX-toDiscard++Retrieve3Cards-grabGoods-fromDiscard-toTable-payCost-reduc2,None>
+++++

.....
No Funny Stuff
-----
b046d41f-0b5c-4c0c-8d71-507c7877807e
-----
onPlay:SimplyAnnounce{prevent shootout or non-cheatin resolution abilities}
+++++

.....
Arnold Stewart
-----
55c7c4fb-53ee-4fef-96f2-666ef2f1ec2d
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atGadget-onAttachment-isCost$$UseCustomAbility
.....
Companhurst's
-----
97babd64-ce97-4996-a4a5-f6782660c895
-----

+++++

.....
Auto-Gatling
-----
e3efb184-9dc0-4c4f-9b07-b7c01c66a424
-----

+++++

.....
Heretic Joker (Red)
-----
e2e638ff-27cb-4704-b324-bd318dc9170a
-----

+++++

.....
Heretic Joker (Black)
-----
57039087-1868-4430-a94b-fb7eedeb04a5
-----

+++++

.....
Ol' Howard
-----
f9f258f4-dd3b-43c8-9081-79939b5b76b0
-----

+++++
GR0B1R0:CustomScript
.....
Market Street
-----
e734385a-eb43-4dd0-931d-16b99750de17
-----

+++++
GR0B0R0:BootMyself
.....
Silent Sigil
-----
3e3fff09-9401-46d2-ab8e-cfce77ddde58
-----

+++++
GR0B0R0:CustomScript
.....
Notary Public
-----
98487814-4411-4701-85e6-3c45340679d0
-----

+++++
GR0B1R0:CustomScript
.....
Constance Daughtry
-----
7ab8a00e-d449-42ec-ae60-3dff03151dce
-----

+++++
GR0B0R0:UnbootMyself
.....
"Mahogany" Jackson
-----
8bb9b173-38ce-4b99-8874-3197a596b17e
-----
onParticipation:Draw2Cards-toDiscard
+++++

.....
Gomorra Lot Commission
-----
74d2d9ea-bcc7-4c61-b4a1-0a54856501dc
-----

+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-atDeed-fromHand-choose1-isCost$$Gain1Ghost Rock
.....
Requiem For A Good Boy
-----
b1db504d-513e-4ce8-8113-c64ded1b0ad5
-----
onPlay:DiscardTarget-DemiAutoTargeted-atSidekick-targetMine-isParticipating-isCost-choiceTitle{Choose the sidekick to discard}-choose1-isResolution$$UnbootTarget-DemiAutoTargeted-atDude-isParticipating-targetMine-choiceTitle{Choose the Host of the discarded Sidekick}-choose1$$SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choiceTitle{Choose the dude you're sending home booted}-choose1
+++++

.....
Crafty Hare
-----
b2371c67-bdd2-4ba6-b236-86a551e0f2c1
-----

+++++
GR0B1R0:Pull1Card-testSpiritX-difficultyValue-Targeted-atDude-isParticipating-targetOpponents-spellEffects<UnparticipateHost++MoveHost-moveToDeed_or_Town Square_or_Outfit,None>
.....
Framed
-----
92a85b68-c791-46ac-8515-22379ea67e99
-----
onPlay:CustomScript
+++++

.....
Rhonda Sageblossom
-----
a8b44597-b8b4-4a8a-b077-d6f0495248d7
-----

+++++

.....
Wagner Memorial Ranch
-----
aacdc6a0-f543-4cc2-8370-b2bec8eccc6a
-----

+++++
GR0B1R0:SimplyAnnounce{reduce the invention difficulty by 2}
.....
Fiddle Game
-----
2c318b93-e6b8-422d-b062-baecfc06e62a
-----
onPlay:StartJob-AutoTargeted-atOutfit-targetMine-jobEffects<RehostMyself-AutoTargeted-atOutfit-targetMine-isMark,None>
+++++

.....
Francisco Rosales
-----
f21a80e4-27f0-4c87-a44e-64661765a000
-----

+++++
GR0B1R0:StartJob-AutoTargeted-atTown Square-bootLeader-jobEffects<Retrieve1Cards-grabSidekick_or_Horse-fromDiscard-toTable-payCost-reduc2,None>
.....
Plague of Grasshoppers
-----
e27b4a68-2a7b-48e9-9dae-a42d02f8a66f
-----
onPlay:CustomScript
+++++

.....
Epidemic Laboratory
-----
df42a53c-8fab-4603-9294-f51d4a44e95e
-----

+++++
GR0B0R0:StartJob-bootLeader-DemiAutoTargeted-atEpidemic Laboratory-choose1-jobEffects<Put1PermControlPlus++Put1ProdPlus,None>
.....
Sunday Best
-----
63df2636-a2b4-4470-9b3f-596c2e311dd1
-----

+++++
GR0B1R0:MoveHost-moveToDeed_or_Town Square_or_Outfit
.....
Sight Beyond Sight
-----
27ddc945-bfc5-4dd9-84d8-d6bc44c904ae
-----

+++++
GR0B1R0:Pull1Card-testHex7-spellEffects<UseCustomAbility,None>
.....
Technological Exhibition
-----
083b92c1-bf91-4d5b-95e0-23a72bd0d05a
-----
onPlay:StartJob-DemiAutoTargeted-atDeed_or_Town Square_or_Outfit-choose1-jobEffects<UseCustomAbility,None>
+++++

.....
Carlton "Min" Rutherford
-----
8463332e-61fb-4744-b6cb-89fbcec18bdd
-----

+++++
GR1B0R0:UnbootMyself-ifRobinHood
.....
Walters Creek Distillery
-----
f7be47f3-b72b-4739-8391-e7d718868b90
-----

+++++
GR0B1R0:CustomScript
.....
A Piece Of The Action
-----
c5d383fa-b1e7-4135-bb1a-a530b9f8338d
-----
onPlay:CustomScript
+++++

.....
Foreboding Glance
-----
38c663b2-e6f8-4135-83d0-46122e5be7d6
-----
onPlay:CustomScript
+++++

.....
Spirit Steed
-----
ccc98846-eea5-4568-9726-2f86d9b90896
-----

+++++
GR0B1R0:MoveHost-moveToSpirit||GR0B0R1:BootTarget-DemiAutoTargeted-atSpirit-onAttachment-choose1-isCost$$MoveHost-moveToDeed_or_Town Square_or_Outfit
.....
Mountain Lion Friend
-----
54cd83d3-4735-4948-9a49-9570710da531
-----

+++++
GR0B0R0:DiscardMyself$$SimplyAnnounce{reduce their casualties by two}
.....
Ambrose Douglas
-----
62a29361-d2d6-4934-ac70-916435475094
-----

+++++
GR0B0R0:CustomScript
.....
Lucretia Fanzini
-----
c2d7e814-dddf-4f21-9315-d2d5993da004
-----

+++++

.....
Turtle's Guard
-----
28b4125d-61a9-4714-870c-2f27e4872e9f
-----

+++++
GR0B1R0:Pull1Card-testSpirit4-spellEffects<UseCustomAbility,None>
.....
Onward Christian Soldiers
-----
ed8fda6f-0cee-4d73-9af0-159fbb3db4e0
-----

+++++
GR0B1R0:Put1BulletShootoutPlus-AutoTargeted-atDude-targetMine-isParticipating$$Put1Shootout:Bullet Immunity-AutoTargeted-atDude-targetMine-isParticipating
.....
Pigging Out
-----
4964e22f-04f8-4d72-b70c-9b1c8d85a53a
-----
onPlay:Pull1Card
+++++
GR0B0R0:Draw5Cards-toDiscard$$Retrieve1Card-fromDiscard-grabTao of Zhu Bajie$$Put1Shootout:Pigging Out-Targeted-atDude-targetMine-isParticipating
.....
Tusk
-----
4b68dd9b-fb40-4912-8ff6-d7de771861dd
-----
onPlay:Draw1Card
+++++

.....
Darragh Meng
-----
991495ee-2b58-4e7f-92d0-11ffaca1cff5
-----

+++++

.....
Fool Me Once...
-----
61e47afb-cb64-46b5-86ae-893590b84139
-----
onPlay:Draw3Cards-onOpponent
+++++
GR0B0R1:CustomScript
.....
Henry Moran
-----
22df7ba7-5a3e-45de-b12a-a6c672ad6ccf
-----

+++++

.....
Tallulah "Lula" Morgan
-----
3c6ad64f-f716-4ee8-80db-f13602745d44
-----

+++++
GR0B0R1:Gain1Ghost Rock
.....
Theo Whateley-Boyer
-----
6bbd7290-5c98-4378-b581-0c044b96860a
-----

+++++
GR0B0R1:CustomScript
.....
Travis Moone
-----
cde1ec30-fedd-46de-af9b-110856d0f1c7
-----

+++++
GR0B1R0:Draw2Cards
.....
Caitlin McCue
-----
fe0b667f-b384-465c-8e3e-97b9f122031c
-----

+++++

.....
Bethany Shiile
-----
55f3b556-f7c1-4a0a-9f88-6f2a89635118
-----

+++++

.....
Tyxarglenak
-----
0e414687-3d4e-413a-93d1-eb7ccaf7364e
-----

+++++

.....
Dr. Dayl Burnett
-----
1f895c03-29d3-4c09-a884-2d24aea2c84e
-----

+++++
GR0B0R0:Remove1Bounty-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-isCost-choose1$$UseCustomAbility
.....
Maggie Harris
-----
7e03d2ef-dde6-4219-afd4-608280aee7bb
-----

+++++
GR0B1R0:StartJob-AutoTargeted-atOutfit-targetMine-bootLeader-jobEffects<Retrieve1Cards-grabHorse-fromDiscard-toTable-payCost-reduc1,None>
.....
Emilia Vivirias
-----
22e58549-c649-457b-a3da-4507ecfc30ec
-----

+++++

.....
"Professor" Duncan
-----
14d66d53-e32a-4077-a843-ec3b02e4b628
-----

+++++

.....
The Highbinder Hotel
-----
2dd93d6f-a777-4592-a4b2-224bd81bc08a
-----

+++++
GR0B1R0:SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetMine-choose1
.....
2nd Bank of Gomorra
-----
1db846be-917b-46a0-980d-4f43d2b83d2a
-----

+++++
GR0B1R0:Put2Ghost Rock||GR0B1R0:Gain1Ghost Rock-perMarker{Ghost Rock}$$Remove999Ghost Rock
.....
High Stakes Haven
-----
47391e41-4a0f-443b-91dc-e3b0e298fbf4
-----
whileInPlay:Lose1Ghost Rock-foreachCheatinRevealed-byMe-ifPhaseGamblin
+++++

.....
Culpability Scientizer
-----
e116ab3d-a5d5-46a3-860a-bc629bd0c63b
-----
onPlay:Put2Bounty-DemiAutoTargeted-atDude-choose1
+++++
GR0B0R0:DiscardMyself$$CalloutTarget-Targeted-atDude-hasMarker{Bounty}
.....
Espuelas
-----
05fc82d0-06e4-422e-9cd7-18110a50a244
-----

+++++
GR0B1R0:MoveHost-moveToDeed_or_Town Square_or_Outfit
.....
Rites of the Smoking Mirror
-----
aa2d0ea9-5ede-4074-b0f7-2e78656f0e15
-----

+++++
GR0B0R0:PlayTarget-DemiAutoTargeted-fromHand-atGoods_and_Mystical-choose1-payCost-isCost-reduc4$$AceMyself||GR0B0R0:UnbootTarget-Targeted-atDude$$DiscardMyself
.....
Essence of Armitage
-----
fc2842bf-c9b0-4b79-875b-3e35d91a5af2
-----

+++++

.....
Festering Grasp
-----
64605ce4-35a8-4167-8650-e9b99b0e0dd3
-----

+++++
GR0B1R0:Pull1Card-testHex13-spellEffects<Retrieve1Card-toTable-grabSidekick-fromDiscard-payCost-reduc2-preHost,None>
.....
Silver Pheasant's Bounty
-----
560d147e-37d3-4f17-91a5-33fcbd23deef
-----
onPlay:Put1ProdPlus-AutoTargeted-atDeed-onHost
+++++
GR0B1R0:Pull1Card-testSpirit6-spellEffects<BootHost-isCost++Gain2Ghost Rock,None>
.....
Comin' Up Roses
-----
2d97b6cb-9387-4081-8be5-85bb0bba0039
-----

+++++

.....
Run Rabbit Run
-----
53df6af3-7b21-4594-926d-9e3ec7e30274
-----
onPlay:Pull1Card
+++++
GR0B0R0:Draw5Cards-toDiscard$$Retrieve1Card-fromDiscard-grabTao of the Jade Rabbit$$Put1Shootout:Run Rabbit Run-Targeted-atDude-targetMine-isParticipating
.....
Putting the Pieces Together
-----
e42451a8-c431-4b2b-a454-9b94c187dca6
-----
onPlay:BootMyself||whileInPlay:BootMyself-foreachCheatinRevealed-byMe
+++++

.....
Someone Else's Problem
-----
8ac302b6-711f-41dc-9f0d-4ec19f16f813
-----
onPlay:Put1Shootout:Someone Elses Problem-Targeted-atDude-targetOpponents
+++++

.....
Lost to the Plague
-----
c22ec64d-d7d6-4c06-b09d-4a827c0dbad3
-----

+++++

.....
El Armadillo de Hierro
-----
8c1e6faf-c90d-4167-9834-793ffcaa47f7
-----

+++++
GR0B0R1:Put1BulletShootoutPlus
.....
Jim Hexter
-----
b1d4638a-0118-426f-a966-1a9c6ff0da5b
-----

+++++
GR0B0R1:Lose1Ghost Rock-isCost$$Gain1Ghost Rock-onOpponent$$Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Hupirika Sue
-----
d2e8e560-15ad-421d-931b-7bb9a8bc6b2c
-----

+++++
GR0B0R0:Put2BulletShootoutPlus-Targeted-atDude-targetOpponents
.....
The Mixer
-----
0c1b3abb-69eb-4f9b-9dfc-69942c2442a6
-----

+++++
GR0B0R1:Put1Shootout:Mixed Medicine-Targeted-atDude-isParticipating
.....
The Harvester
-----
51b3db35-9811-4adf-89f6-7dd48b031bba
-----

+++++

.....
Lucy Clover
-----
7477d1e2-14c6-45e8-8acd-9619ec2fa578
-----

+++++
GR0B0R1:Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud
.....
Buckin' Billy Ballard
-----
314f6ee6-e572-44a2-9412-78bd822be671
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atHorse-onAttachment-isCost$$Draw1Cards$$BootTarget-Targeted-atDude-noTargetingError
.....
Antoine Peterson
-----
1120919a-d4b6-4655-b369-4f732b016e14
-----
onPlay:CustomScript
+++++

.....
Denise Brancini
-----
be0ace53-d90a-4fff-a6a6-c5545667d83f
-----
onDiscard:CustomScript
+++++

.....
"Open Wound"
-----
7cc6fca2-a48a-4386-ba79-2fd94534b6ec
-----

+++++
GR1B0R1:MoveTarget-DemiAutoTargeted-atDude-targetMine-choose1-moveToDeed_or_Town Square_or_Outfit
.....
Long Strides Ranch
-----
fd144b71-3727-4333-be79-b57ab4fe3afc
-----

+++++
GR0B1R0:PlayTarget-DemiAutoTargeted-fromHand-atHorse-choose1-payCost-reduc2
.....
The Gomorra Gazette
-----
d03f58a7-ef6a-428e-a950-67e0b6245b66
-----

+++++
GR0B1R0:Gain1Ghost Rock-perTargetProperty{Influence}-Targeted-atDude-targetOpponents
.....
Bacillus Pasteuria
-----
2e323023-c293-41ce-a87c-12fddba592d5
-----

+++++
GR0B0R0:UnbootTarget-Targeted-atDude
.....
Doomsday Supply
-----
4461e319-d77d-4a76-ba9c-e401a4a99223
-----

+++++
GR0B1R0:Retrieve1Card-grabGoods-fromDiscard-toTable-payCost-reduc2
.....
The Blighted
-----
af22f9d8-738b-4e7f-a13a-599089e51507
-----

+++++

.....
Sun-Touched Raven
-----
8b505b63-7954-42b6-b072-85b5b794c0fa
-----

+++++
GR0B1R0:Pull1Card-testSpirit6-spellEffects<UseCustomAbility,None>
.....
Inner Struggle
-----
ba6d6429-9a34-4912-96c4-aee1649650f3
-----
onPlay:BootMyself$$UseCustomAbility||whileInPlay:BootMyself-foreachCheatinRevealed-byMe
+++++

.....
Lighting the Fuse
-----
49496e5f-974e-43f1-a85f-d9bda3de8325
-----

+++++

.....
One Fights As Many
-----
18f82dad-6f87-4a26-9dee-2859b4854b70
-----
onPlay:StartJob-AutoTargeted-atTown Square
+++++

.....
Serendipitous Arrival
-----
f8fc9a76-cbd9-4ad5-b2c7-5cd40f150e79
-----
onPlay:CustomScript
+++++

.....
Siege of the Orphanage
-----
059481a6-d607-4896-8584-fb596c4647f7
-----

+++++

.....
Seamus McCaffrey
-----
32e3dc80-38a5-41e5-a267-f5b0f3a55d22
-----

+++++

.....
Shi Long Peng
-----
f23323c6-2381-4f8a-961c-606f84147c56
-----

+++++

.....
Gene North Star
-----
ea7a82ee-ad0d-4508-bbd7-a0a7b9fd610a
-----

+++++
GR0B0R0:DiscardTarget-DemiAutoTargeted-atSpell-onAttachment-isCost-choose1$$Put2BulletShootoutPlus
.....
Speaks-with-Earth
-----
1bea3954-dab3-42ef-830d-4d03a779b7b6
-----

+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atDude-targetOpponents$$UnbootTarget-DemiAutoTargeted-atTotem-noTargetingError
.....
The Grey Man
-----
49e72f76-4b92-468d-90c9-325689b607b1
-----

+++++
GR0B0R0:BootTarget-DemiAutoTargeted-atDude
.....
Erin Knight
-----
b66bd108-b7f4-4eb4-8dab-bdcf67dab50c
-----

+++++

.....
Nicholas Kramer
-----
96ac4bcb-e022-4dc3-b87f-a9a0ddc4c723
-----

+++++

.....
Quimby R. Tuttlemeir
-----
5f270369-68b9-4ce9-9e67-1e74f313ea6f
-----

+++++
GR0B0R0:AceTarget-DemiAutoTargeted-atDude_and_Abomination-targetMine$$Put1PermInfluencePlus
.....
Pancho Castillo
-----
4e724dee-6a9f-42dc-92ee-00e0f55be29f
-----

+++++

.....
Grimoires & More
-----
ef1b01c0-82e5-4243-8839-2136df14d4b1
-----

+++++
GR0B1R0:CustomScript
.....
J.W. Byrne, P. I.
-----
576ef086-4950-47b3-8ab5-71f3fdbce794
-----

+++++
GR0B1R0:BootTarget-Targeted-atGrifter-targetMine
.....
Knight's Chasuble
-----
92cf4c1a-cd1b-4377-a0dd-e06d52edbbff
-----

+++++
GR0B1R0:UnbootHost
.....
Pedro
-----
66f1e08f-2b5a-4e3e-97d2-0289c6379700
-----
onPlay:Put3ValueNoonMinus
+++++

.....
Aetheric Shockwave Inducer
-----
b63cda5e-d4cb-436f-be79-79dc74124a57
-----

+++++
GR0B0R1:Pull1Card
.....
The Gambler's Gun
-----
fac96abf-efee-492f-ae9e-72a944e518a6
-----

+++++
GR0B1R0:SimplyAnnounce{increase their hand rank by 2}
.....
Calling the Cavalry
-----
4bc332e3-b672-4445-90af-f4b7e4816fee
-----
onPlay:Remove999Shootout:Draw-isSilent-DemiAutoTargeted-atDude-targetMine-isParticipating$$Put1Shootout:Stud-DemiAutoTargeted-atDude-targetMine-isParticipating
+++++

.....
Get Behind Me, Satan!
-----
f5359fcb-0095-4ef0-8264-e3eec905528d
-----

+++++
GR0B1R0:Pull1Card-testMiracle5-spellEffects<SimplyAnnounce{reduce casualties by their blessed rating},None>
.....
Ghostly Communion
-----
7469036b-d154-4cb5-9eff-7d77fbdbcdf0
-----

+++++
GR0B1R0:Pull1Card-testSpirit7-spellEffects<MoveHost-moveToDude_or_Deed_or_Town Square_or_Outfit++ParticipateHost,None>-onlyInShootouts||GR0B1R0:Pull1Card-testSpirit5-spellEffects<MoveHost-moveToDeed_or_Town Square_or_Outfit,None>-onlyInNoon
.....
All or Nothing
-----
22e8401c-bf60-42e0-8119-36ce05c5d893
-----

+++++
onPlay:StartJob-DemiAutoTargeted-atDeed_or_Town Square_or_Outfit-choose1-jobEffects<SendHomeBootedMulti-Targeted-atDude-targetOpponents,None>
.....
Rite of Profane Abstersion
-----
722d4849-79a2-4bf3-b3d6-109de8762773
-----

+++++

.....
Showboating
-----
d67fe646-d457-41bd-b8ce-ec8f836ca3a5
-----
onPlay:Put1PermControlPlus-Targeted-atDude-targetMine
+++++

.....
Mr. Outang
-----
ef12ef9a-b1c8-433f-a4ac-eac38f5ffaf1
-----

+++++

.....
Zui Waidan
-----
407fccf5-1007-4be6-a1f5-8a06bc2c0674
-----

+++++
GR0B0R0:BootTarget-Targeted-atDeed-targetMine-isCost$$PutShootout:KungFu Bonus:2-DemiAutoTargeted-atDude-isParticipating-targetMine-choose1
.....
Stevie Lyndon
-----
52674538-37bf-4dc3-bba9-164f11abb7c4
-----

+++++

.....
Eva Bright Eyes
-----
4e453b4b-da87-4042-8ebf-92ff9a25c25c
-----

+++++
GR0B0R0:BootTarget-AutoTargeted-atHorse-onAttachment-choose1-isCost$$SendHomeBootedMyself
.....
Wei Xu
-----
043e1e23-de64-403f-a5ae-6df84823538f
-----

+++++

.....
Mick Aduladi
-----
1c769e8e-e7d5-49e5-94c7-7f83dc3b1cc7
-----

+++++
GR0B0R0:MoveMyself-moveToHoly Ground
.....
Hattie DeLorre
-----
77e140fc-3d2d-4715-bc47-af208e671b3e
-----

+++++
GR0B0R0:Put5BulletShootoutMinus-DemiAutoTargeted-atDude-hasMarker{Bounty}-targetOpponents-choose1
.....
Father Tolarios
-----
c213a4b2-95ee-487c-b0a8-8cc09ac87a7d
-----

+++++
GR0B0R0:CustomScript    
.....
Jimmy &quot;The Saint&quot;
-----
163fc3b6-eea4-44ab-9edc-f03647046c3a
-----

+++++
GR0B0R0:Gain1Ghost Rock-perTargetProperty{Production}-Targeted-atDeed-targetMine
.....
Mario Crane
-----
2a6bafed-d2ea-4275-877a-f0f15aae4c85
-----

+++++
GR0B0R1:SimplyAnnounce{reduce their casualties by 2 this round}
.....
POST-A-TRON
-----
03c922cf-e0ef-4d47-bbb7-7c62428f90fb
-----

+++++
GR0B01R0:Gain3Ghost Rock
.....
Diego Linares
-----
82aaf3b6-9eb1-4fd2-9812-b6b727cf51b2
-----

+++++

.....
Christine Perfect
-----
75969ce9-d9e6-4cc1-b4e5-5ff29c3e8d69
-----

+++++
GR0B0R0:MoveMyself-moveToDude$$Put5ValueNoonMinus-Targeted-atDude-targetOpponents
.....
Absalom Hotchkiss
-----
2431b33e-b34c-4b53-9915-fa18ca6777e7
-----

+++++
GR0B0R0:MoveTarget-Targeted-atDude-targetMine-moveToAbsalom Hotchkiss
.....
The Caretaker
-----
543b1dab-41f2-4d79-80f5-a00fa3a0b6e8
-----
atPhaseGamblin:Put4ValueNoonPlus$$Put4BulletNoonPlus$$Put1High Noon:Stud
+++++
GR0B0R0:Remove4ValueNoonPlus$$Remove4BulletNoonPlus$$Remove1High Noon:Stud
.....
Gomorra Gaming Commission
-----
27194abd-3f50-4088-98f2-5dd70dfddd62
-----

+++++
GR0B1R0:Put1ProdPlus$$UseCustomAbility-isResolution
.....
Sherman Mortgage
-----
15b1a170-e713-40d5-ab39-6ed2f8cd97d6
-----
atPhaseShootoutStart:BootMyself
+++++

.....
Cliff's #4 Saloon
-----
76f4b9dd-7c1e-4ffd-a2ea-e7e2d0f253eb
-----

+++++
GR0B1R0:Remove999High Noon:Draw-DemiAutoTargeted-atDude-targetMine-choose1$$Put1High Noon:Stud-DemiAutoTargeted-atDude-targetMine-choose1
.....
Nickel Night Inn
-----
581c842b-d83b-4fcf-b525-7acad7f4a866
-----

+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atDude-targetOpponents-hasProperty{Value}le3-choose1
.....
Burn 'Em Out
-----
973b1148-56aa-421b-ba9a-5c6273710b6c
-----
OnPlay:StartJob-AutoTargeted-atOutfit-targetOpponents-bootLeader-bountyPosse-jobEffects<UseCustomAbility,None>
+++++

.....
The Law Goes Underground
-----
a149d4e1-b28c-4f5a-8202-9c12d7be2876
-----
onPlay:CustomScript
+++++

.....
Shiny Things
-----
3448fa9e-1adc-4094-80a9-7c2ed35db597
-----
onPlay:BootTarget-Targeted-atDude-targetOpponents$$Put2InfluencePlus-Targeted-atDude-targetOpponents$$Put7ValueNoonPlus-Targeted-atDude-targetOpponents$$Put1High Noon:Shiny Things-Targeted-atDude-targetOpponents
+++++

.....
Moving Forward
-----
eaf25cb8-16fb-4f52-ba4b-ce8a88295d2f
-----
onPlay:Retrieve1Card-fetchDeed-toTable-isResolution
+++++

.....
We Got a Beef!
-----
e4118ee1-a9eb-4738-a378-673ca6c918a7
-----
onPlay:CustomScript
+++++

.....
Baijiu Jar
-----
d88d3c39-4f35-40e9-b37b-046f6c9409de
-----

+++++
GR0B1R0:DiscardMulti-DemiAutoTargeted-fromHand-choose3-isCost$$Draw4Cards
.....
De Annulos Mysteriis
-----
765bff12-2d2b-44a0-a5ad-80920e291833
-----

+++++
GR0B0R0:CustomScript
.....
Rancher's Lariat
-----
08507600-22ab-4903-861e-1c3941a54e23
-----

+++++
GR0B1R0:BootTarget-Targeted-atWeapon-targetOpponents-noTargetingError$$Put1Shootout:Whipped-Targeted-atDude-isParticipating-targetOpponents
.....
Bowie Knife
-----
cb7e441a-1d78-4967-92ec-ab2d3a0f70fe
-----

+++++

.....
Hydro-Puncher
-----
86f8e98c-66a6-4a54-b0c0-48e7428dc891
-----

+++++
GR0B1R0:BootTarget-Targeted-atGoods_or_Spell-targetOpponents-noTargetingError$$BootTarget-Targeted-atDude-isParticipating-targetOpponents
.....
Heartseeker
-----
a12b3e09-b8af-4620-8479-20b5065df197
-----

+++++
GR0B1R0:Pull1Card-testHex5-spellEffects<SimplyAnnounce{mark the opposing shooter to be aced, and reduce the opponent's casualties by 3},None>-onlyInShootouts
.....
Amazing Grace
-----
1cd6c83a-2c5d-4f23-92d3-f9dd371413f0
-----

+++++
GR0B1R0:Pull1Card-testMiracle6-spellEffects<Put1InfluencePlus-AutoTargeted-atDude-onHost++Put1High Noon:Amazing Grace-AutoTargeted-atDude-onHost,None>
.....
Tse-Che-Nako's Weaving
-----
540d789b-98d5-47ac-8778-7a834851b10b
-----

+++++
GR0B1R0:Pull1Card-testSpirit6-spellEffects<MoveTarget-moveToDeed_or_Town Square_or_Outfit$$UseCustomAbility,None>
.....
Great Sage Matching Heaven
-----
39fa07ab-40d4-4ddd-b2a6-6c444a1f48cd
-----
onPlay:Pull1Card
+++++
GR0B0R0:Put1InfluencePlus$$Put1Shootout:Harrowed
.....
Two Hundred Fifty Rounds
-----
ea3990fa-ae15-4314-b8f7-d4d8aaf11788
-----
onPlay:Pull1Card
+++++
GR0B0R0:SimplyAnnounce{to reduce their casualties this round by 1}
.....
108 Drunken Masters
-----
72f2f4f7-2e0e-4994-aaa2-c6228fc3d8d9
-----

+++++
GR0B1R0:SimplyAnnounce{reduce the pull by the amount of saloons they control}
.....
Gateway to Beyond
-----
fd347528-2ce1-4cc5-9efb-a1052ee8603b
-----

+++++
GR0B1R0:CustomScript
.....
Justice in Exile
-----
e0943fa8-0024-451f-862f-644ee23011eb
-----

+++++
GR0B1R0:Gain2Ghost Rock
.....
Protection Racket
-----
e415100e-91bb-4d9e-87aa-ec2f23d63f84
-----

+++++
GR0B1R0:CustomScript
.....
Morgan Regulators
-----
b94ed693-16ed-4c7c-84d8-375498922a74
-----

+++++
GR0B1R0:MoveDude-moveToTown Square$$Put1High Noon:Stud-Targeted-atDude-targetMine$$UseCustomAbility
.....
Full Moon Brotherhood
-----
a9ec06b7-2fe5-4334-82f1-43e460b07967
-----

+++++
GR0B1R0:Put1High Noon:Brotherhood Mark-DemiAutoTargeted-atDude-targetOpponents-choose1
.....
"Thunder Boy" Nabbe
-----
1c4fd81f-8b08-4e7f-9325-8c63104f2694
-----

+++++
GR0B0R1:Put1BulletShootoutPlus-perProperty{Influence}$$Remove999Shootout:Draw-isSilent$$Put1Shootout:Stud-isSilent
.....
Dave "Slim" Gorman
-----
698ae5b9-1b37-45be-bbd2-118c03d64a30
-----

+++++
GR0B0R0:Remove999Shootout:Stud-isSilent-AutoTargeted-atDude-isParticipating$$Put1Shootout:Draw-isSilent-AutoTargeted-atDude-isParticipating
.....
Darius Hellstromme
-----
ae22bba2-cf1e-4038-b7bb-1d3429ca2daf
-----

+++++
GR0B1R0:CustomScript
.....
Ezekiah Grimme
-----
2733deda-5584-42e1-9dfd-d283ad68cf1f
-----

+++++
GR0B1R0:UseCustomAbility-isFirstCustom||GR0B1R0:UseCustomAbility-isSecondCustom
.....
Jasper Stone
-----
6bcacb58-f902-483e-8f25-6eef33e9dd18
-----

+++++
GR0B1R0:Put1Shootout:JasperCurse-DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1||GR0B0R1:Put1PermBulletPlus-Targeted-atDude-isMine$$Put1PermControlPlus-Targeted-atDude-isMine
.....
Raven
-----
1d0ac7a8-da18-4a99-9467-02edf80e6258
-----

+++++
GR0B1R0:Put1Noon:RavensCurse-DemiAutoTargeted-atDeed-choose1||GR0B0R1:Put1PermBulletPlus-DemiAutoTargeted-atDude-targetMine-choose1
.....
Wang Men Wu
-----
b1d048cf-7e94-4129-b817-5e0980038796
-----

+++++
GR0B0R0:Spawn1Gunslinger-modAction:ParticipateMyself
.....
Charging Bear
-----
0dff63ec-8e97-488d-87c1-d2505b44acc0
-----

+++++
GR0B0R0:AceTarget-Targeted-atDude-targetMine-chose1$$SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1$$Put1Shootout:Stud
.....
Fears No Owls
-----
51fa6f06-ba8e-432d-aca5-639123f2b9b9
-----

+++++
GR0B0R0:MoveTarget-DemiAutoTargeted-atDude-targetMine-choose1-moveToDeed_or_Holy Groung
.....
Black Owl
-----
08137945-5919-4b1d-be80-6aff3f89118b
-----

+++++
GR0B1R0:Put5ValueShootoutMinus-Targeted-atDude-isParticipating$$Put1Shootout:FirstCasualty-Targeted-atDude-isParticipating
.....
Zeb Whateley-Dupont
-----
f8adf6a9-c944-4b37-98eb-c167c5bce2e7
-----
onPlay:CustomScript||atPhaseGamblin:CustomScript
+++++

.....
Rosenbaum's Golem
-----
dafad1b5-7067-4efa-b063-67a4c5c2b42a
-----

+++++
GR0B0R0:CustomScript
.....
Stewart Davidson
-----
720083f1-9fd9-4608-a112-9e0a28de43d2
-----

+++++
GR0B0R0:CustomScript
.....
Sheriff Eli Waters
-----
fb433634-025d-4333-aa2b-e8c9d230d020
-----

+++++
GR0B0R1:CustomScript||GR0B0R1:MoveMyself-moveToDude-hasMarker{Bounty}||GR0B0R1:MoveMyself-moveToDude-hasMarker{Bounty}$$ParticipateMyself
.....
Adrian Vallejo
-----
3d38ea0c-31d3-456e-a7cd-f7a66476395d
-----

+++++
GR0B0R0:ParticipateMyself
.....
Prof. Aloysius Roe
-----
ad68435b-5503-4af0-bd4e-7e5b15c04866
-----

+++++
GR0B0R0:SimplyAnnounce{The value of the pull is increased by Prof. Roe's MS rating}
.....
Rabid Rance Hitchcock
-----
9f3d837e-e317-403c-a72d-c9b8a48f5bcf
-----

+++++
GR0B0R1:Put1PermControlPlus-Targeted-atDeed-chose1||GR0B0R1:Put1PermControlMinus-Targeted-atDeed-chose1||GR0B0R1:MoveMyself-moveToDeed_and_Out of Town||GR0B0R1:CustomScript
.....
Morgan Lash
-----
711deb54-4548-4206-81af-77d5dcc8793a
-----
onPay:ReduceSCostPlay
+++++

.....
Johnny Brocklehurst
-----
5c6b6541-1253-4da2-a454-ce912ffcf474
-----

+++++
GR0B0R0:Put1InfluencePlus-Targeted-atDude||GR0B0R0:Remove1InfluencePlus-Targeted-atDude
.....
Agent Provocateur
-----
06d454b8-8713-4bba-b0d6-d9152d52423a
-----

+++++
GR0B0R0:CustomScript
.....
F1 Burch
-----
b7eae322-2208-4ef6-8ff2-d7af7ef5d2a1
-----

+++++
GR0B0R0:MoveMyself-moveToDude-chose1||GR0B0R0:MoveMyself-moveToDude-chose1$$Retrieve1Card-grabGoods_and_nonGadget_and_nonUnique-fromDiscard-toTable-payCost-reduc1||GR0B0R0:MoveMyself-moveToDude-chose1$$PlayTarget-DemiAutoTargeted-atGoods_and_nonGadget_and_nonUnique-fromHand-choose1-payCost-reduc1
.....

Taff's Distillery
-----
0d2710a6-4ed9-447c-9cfb-2536d2def29c
-----

+++++
GR0B1R0:Draw1Card
.....
Mausoleum
-----
e8906b23-85f3-44f0-89bb-d1cff708e8b3
-----

+++++
GR0B1R0:Put1PermControlPlus
.....
Epitaph Branch Office
-----
d95fe205-8bcb-4bc5-a895-501fe91a52f3
-----

+++++
GR0B1R0:CustomScript
.....
Buffalo Emporium
-----
2ee14351-c57d-4944-850c-d58cb5c8c304
-----

+++++
GR0B1R0:CustomScript
.....
Explorer's Lodge
-----
67c733e3-1842-44fe-9c40-33d1aad47b4a
-----

+++++
GR0B1R0:CustomScript
.....
The Oriental
-----
162aaf13-fe99-4bb6-8fbe-9587d71bd666
-----

+++++
GR0B1R0:CustomScript
.....
Hellstromme Plant #9
-----
ed34d5f8-3376-4be1-9db7-64c50cdebab9
-----

+++++
GR1B1R0:UnbootTarget-Targeted-atHorse_or_Gadget-chose1
.....
Bilton Collection Agency
-----
381ea2d4-eb1c-46e0-8aad-a500c406709a
-----

+++++
GR0B1R0:Gain1Ghost Rock-perTargetProperty{Production}-DemiAutoTargeted-atDeed-targetMine
.....
Decimator Array
-----
e2fed23a-b50b-4632-858d-ffd622184e5c
-----
onPlay:CustomScript
+++++
GR0B1R0:SimplyAnnounce{Changing suit or value of the card}||GR0B0R1:Put3ValuePermPlus-AutoTargeted-atDude-onHost$$Put1ProdPlus-AutoTargeted-atDude-onHost||GR0B0R1:Put3ValuePermMinus-AutoTargeted-atDude-onHost$$Put1ProdMinus-AutoTargeted-atDude-onHost
.....
Devil's Six Gun
-----
14eb0493-5ea9-4b44-b955-303fcea47e64
-----

+++++
GR0B1R0:CustomScript
.....
Forsaken Hound
-----
1ae574d7-9dd2-4999-a73f-90008198c1b9
-----

+++++
GR0B1R0:Put1Shootout:Cannot Run This Round-Targeted-atDude-targetOpponents_and_atDude-onHost
.....
The Bloody Star
-----
3572042d-4197-4753-830f-d138500aff64
-----
onPlay:Put2Bounty-AutoTargeted-atDude-onHost
+++++

.....
Cavalry Escort
-----
e527c15a-fce5-451a-b34d-51c9050d9cac
-----

+++++
GR0B1R0:BootHost$$ParticipateHost
.....
Nightmare Realm
-----
e3c6f0bb-a585-46b4-b530-bbe6f3347ae8
-----

+++++
GR0B1R0:Pull1Card-testHex3-spellEffects<Put1Shootout:Nightmare-DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1++Put1BulletShootoutPlus-AutoTargeted-atDude-onHost,None>||GR0B0R1:Put1BulletShootoutMinus-Targeted-atDude-hasMarker{Nightmare}-isParticipating-targetOpponenes$$Put1ValueShootoutMinus-Targeted-atDude-hasMarker{Nightmare}isParticipating-targetOpponents
.....
Sentinel
-----
be8dd9d7-31f8-4cf6-aa37-5a18067bb067
-----

+++++
GR0B1R0:Pull1Card-testMiracle5-spellEffects<UseCustomAbility,None>
.....
Censure
-----
c13ad872-7c89-44fc-8572-2da526866207
-----

+++++
GR0B1R0:Pull1Card-testMiracle6-spellEffects<UseCustomAbility,None>
.....
Raven's Ruin
-----
2e57f90e-6852-49a8-abdc-9d24be7018fe
-----

+++++
GR0B1R0:Pull1Card-testSpirit8-spellEffects<UseCustomAbility,None>
.....
Remedy
-----
d9433ac9-20fb-4f2f-adb5-8b11ee9045ff
-----

+++++
GR0B1R0:Pull1Card-testSpirit7-spellEffects<Put1Shootout:Remedy-DemiAutoTargeted-atDude-isParticipating-choose1,None>
.....
Intercession
-----
f638e171-5064-4c25-b1b7-7e5d762025b1
-----

+++++
GR0B1R0:Pull1Card-testMiracle5-spellEffects<UseCustomAbility-isFirstCustom,None>||GR0B1R0:Pull1Card-testMiracle7-spellEffects<UseCustomAbility,None>
.....
Disarm
-----
6afef9d1-9502-437b-915f-6450a35b3f30
-----
onPlay:CustomScript
+++++

.....
Grim Servant O' Death
-----
71e424b2-d62f-43a4-95c8-4b6b77e0b83d
-----
onPlay:CustomScript
+++++

.....
Behold White Bull
-----
d759b266-2dbb-4ee8-8a8f-40e456cbd5ae
-----

+++++
GR0B0R0:BootTarget-Targeted-atDude-targetMine-chose1$$SimplyAnnounce{Increase the casualties of both posses this round by this dude's influence.Your opponent may send all dues in their posse home booted. BY PRESSING ESCAPE}||GR0B0R0:Put2PermControlPlus-DemiAtutoTargeted-atDude-targetMine-chose1$$UnbootTarget-DemiAtutoTargeted-atDude-targetMine-chose1
.....
You Had ONE Job!
-----
3560016d-7c5f-4ac3-beb8-c3360539bb11
-----
onPlay:CustomScript||onPlay:SimplyAnnounce{All players who revealed a legal hand may reduce their casualties by 2.}
+++++

.....
Friends in High Places
-----
2d759fe3-f3e0-46c2-82f1-1df7c5b32aac
-----
onPlay:CustomScript||onPlay:Put1Shootout:Stud-DemiAutoTargeted-atDude-targetMine-isParticipating-chose1
+++++

.....
Shan Fan Showdown!
-----
e94de78b-0021-4167-9681-81b7cc5a9544
-----
onPlay:UnbootTarget-Targeted-atDude-targetMine-isParticipating-chose1 $$ Put1Shootout:Stud-Targeted-atDude-targetMine-isParticipating $$ SimplyAnnounce{For the remainder of the shootout non Cheatin Resolution abilities cannot increase or decrease hand ranks or increase or decrease casualties.}
+++++

.....
108 Gracious Gifts
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10055
-----

+++++
GR2B1R0:UnbootTarget-DemiAutoTargeted-atDude-isBooted-targetMine-chose1


.....
Property Is Theft
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10053
-----

+++++
GR0B1R0:Draw1Card$$UseCustomAbility



.....
The Spiritual Society
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10056
-----
atPhaseSundown:CustomScript
+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atDude-isUnbooted-targetMine-choose1-isCost$$BootTarget-DemiAutoTargeted-atDude-targetOpponents-choose1



.....
Joe Vermilion
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10005
-----
onPlay:
+++++
GR1B0R0:Gain1Ghost Rock-onOpponent-isCost$$Gain1Ghost Rock-perTargetProperty{Production}-DemiAutoTargeted-atDeed-targetOpponents-choose1


.....
Ying-Ssi Chieh T'ang
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10004
-----
onPlay:
+++++
GR0B1R0:Gain1Ghost Rock-onOpponent-isCost-onlyInShootouts$$UseCustomAbility


.....
E Gui
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10003
-----
onPlay:
+++++
GR0B0R0:Gain1Ghost Rock-perTargetProperty{Production}-DemiAutoTargeted-atDeed-targetOpponents-choose1


.....
Buskers
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10001
-----
onPlay:
+++++
GR0B0R0:CustomScript


.....
Taiyari
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10002
-----
onPlay:
+++++
GR0B1R0:CustomScript


.....
Matilda Loomis
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10006
-----
onPlay:
+++++
GR0B1R0:


.....
Alexander Sequoia
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10010
-----
onPlay:
+++++
GR0B0R0:UnbootMyself


.....
Matthew Rising Sun
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10009
-----
onPlay:
+++++
GR0B1R0:


.....
Feichi Suitcase Lee
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10008
-----
onPlay:
+++++
GR0B1R0:CustomScript


.....
Geronimo
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10007
-----
onPlay:
+++++
GR0B0R0:DiscardTarget-DemiAutoTargeted-atGoods_or_Spell_or_Gadget-onAttachment-choose1-targetOpponents$$Gain1Ghost Rock


.....
Papa Marias
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10019
-----
onPlay:
+++++
GR0B0R0:Pull1Card-testHex7-spellEffects<MoveTarget-DemiAutoTargeted-atDude-targetMine-isUnbooted-choose1-moveToHere,None>-onlyInNoon



.....
Skinwalker
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10022
-----
onPlay:
+++++
GR0B0R0:BootTarget-DemiAutoTargeted-atAbomination-isParticipating-isMine-isCost-choose1$$Put2BulletShootoutPlus||GR0B0R0:BootTarget-DemiAutoTargeted-atAbomination-isParticipating-isMine-isCost-choose1$$BootTarget-DemiAutoTargeted-atGoods_or_Spell_or_Gadget-onAttachment-choose1-targetOpponents


.....
Tonton Macoute
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10021
-----
onPlay:
+++++
GR0B0R0:Put2BulletShootoutMinus-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1||GR0B0R0:BootTarget-DemiAutoTargeted--atWeapon-isCost-onlyInShootouts


.....
Kevin Wainwright (Exp.1)
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10020
-----
onPlay:
+++++
GR0B1R0:


.....
Padre Ernesto de Diaz
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10011
-----
onPlay:
+++++
GR0B0R1:BootTarget-DemiAutoTargeted-atSpell-onAttachment-isUnbooted-choose1-isCost$$Draw1Card



.....
Dr. Erik Yaple
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10013
-----
onPlay:
+++++
GR0B0R0:BootTarget-DemiAutoTargeted--atGadget_and_Weapon-isCost-onlyInShootouts$$Put1Bounty-DemiAutoTargeted-atDude-hasntMarker{Bounty}-choose1-targetOpponents


.....
Quincy Washburne
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10012
-----
onPlay:
+++++
GR0B0R0:UnbootMyself


.....
Xiong Wendy Cheng (Exp.1)
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10014
-----
onPlay:
+++++
GR0B1R0:BootMyself-isCost$$SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1$$SimplyAnnounce{If that dudes bounty was higher than their grit, discard them}



.....
Takahashi Jinrai
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10017
-----
onPlay:
+++++
GR0B1R0:StartJob-DemiAutoTargeted-atDeed-choose1-jobEffects<Put1ProdPlus-DemiAutoTargeted-atDeed-choose1, None>
.


.....
Handsome Dan Deeds
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10016
-----
onPlay:
+++++
GR0B1R0:BootMyself-isCost$$Put1ControlPlus$$Put1HandsomeCP-DemiAutotargeted-atDeed-choose1


.....
Vida Azul
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10018
-----
onPlay:
+++++
GR0B0R0:CustomScript


.....
Bartholomew P. Fountain
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10015
-----
onPlay:
+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atRanch-targetMine-isCost$$MoveTarget-DemiAutoTargeted-atDude-choose1-moveToDeed_or_Town Square_or_Outfit


.....
Ike Clanton
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10024
-----
onPlay:
+++++
GR0B1R0:Put1Rowdy Ike


.....
Frank Stillwell
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10023
-----
onPlay:
+++++
GR0B0R0:UnparticipateMyself$$SendHomeBootedMyself


.....
Silas Aims (Exp.1)
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10026
-----
onPlay:
+++++
GR0B0R0:CustomScript


.....
Larry Sevens Swift
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10025
-----
onPlay:
+++++
GR0B0R0:BootTarget-DemiAutoTargeted-atSpell-isUnbooted-onAttachment-choose1-isCost$$Put1Bounty$$BootTarget-DemiAutoTargeted-atGoods-targetOpponents-choose1


.....
Virginia Ann Earp
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10027
-----
onPlay:
+++++
GR0B1R0:


.....
Campbell &amp; Hatch Billiard Parlor
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10032
-----
onPlay:
+++++
GR0B1R0:SimplyAnnounce{For the remainder of the shootout, hand ranks cannot be modified Shootout, React, or non-Cheatin' Resolution abilities. Dudes cannot be discarded or aced by Shootout or non-Cheatin' Resolution abilities during the first round.}


.....
Clanton Ranch
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10030
-----
onPlay:
+++++
GR0B1R0:Gain1Ghost Rock


.....
Concordia Cemetery
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10029
-----
onPlay:
+++++
GR0B1R0:Put1ProdPlus||GR0B1R0:Put1ProdPlus$$Put1PermControlPlus


.....
Ike's Place
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10033
-----
onPlay:
+++++
GR0B1R0:Put1ProdMinus-perTargetProperty{Production}-DemiAutoTargeted-atDeed$-choose1$$Put1Control Minus-perTargetProperty{Control}-DemiAutoTargeted-atDeed-choose1$$Put1Ike Place-DemiAutoTargeted-atDeed-choose1



.....
Five Aces Gambling Hall
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10028
-----
onPlay:
+++++
GR0B1R0:ParticipateTarget-DemiAutoTargeted-atDude-targetMine-hasMarker{Bounty}-choose1-isNotParticipating


.....
Old Washoe Club
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10031
-----
onPlay:
+++++
GR0B1R0:SendHomeBootedTarget-DemiAutoTargeted-atDude-isParticipating-targetOpponents-hasProperty{Bullets}le1-choose1||GR0B1R0:DiscardTarget-DemiAutoTargeted-atSidekick-choose1



.....
Quarter Horse
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10034
-----
onPlay:
+++++
GR0B1R0:UnparticipateHost

.....
Electrostatic Pump Gun
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10038
-----
onPlay:
+++++
GR0B1R0:CustomScript


.....
Claws
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10036
-----
onPlay:
+++++
GR0B1R0:


.....
Analytical Cognisizer
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10039
-----
onPlay:CustomScript
+++++
GR0B1R0:DiscardTarget-DemiAutoTargeted-fromHand-atGoods-choose1-isCost$$SimplyAnnounce{The card was discarded to make pulled card's suit a heart}


.....
Ranger's Bible
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10035
-----
onPlay:
+++++
GR0B1R0:SimplyAnnounce{uses Ranger's Bible to lower players hand rank by dudes influence}


.....
Stone's Colt Dragoons
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10037
-----
onPlay:
+++++
GR0B1R0:BootTarget-DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1$$Put1NoUnboot-DemiAutoTargeted-atDude-targetOpponents-isParticipating-choose1


.....
Bedazzle
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10041
-----
onPlay:
+++++
GR0B1R0:Put1BulletShootoutMinus-DemiAutoTargeted-atDude-perTargetProperty{Bullets}-isParticipating-choose1$$SimplyAnnounce{ lowers players hand rank by 2}


.....
Exultant Translocation
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10045
-----
onPlay:
+++++
GR0B1R0:Pull1Card-testMiracle6-spellEffects<BootHost++Put1NoUnboot-Targeted-atDude-targetMine++SendHomeBootedTarget-Targeted-atDude-targetMine,None>


.....
Retribution
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10044
-----
onPlay:
+++++
GR0B1R0:Pull1Card-testMiracleX-difficultyValue-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1-spellEffects<Put1Shootout:Retribution-DemiAutoTargeted-atDude-isParticipating-targetOpponents-choose1,None>

.....
Gateway
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10040
-----
onPlay:
+++++
GR0B1R0:


.....
Guiding Wind
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10042
-----
onPlay:
+++++
GR0B1R0:


.....
Mischievous Coyote
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10043
-----
onPlay:
+++++
GR0B1R0:


.....
Murdered in Tombstone
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10051
-----
onPlay:
+++++
GR0B1R0:


.....
Hostile Takeover
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10050
-----
onPlay:
+++++
GR0B1R0:


.....
Jade King Stance
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10054
-----
onPlay:
+++++
GR0B1R0:


.....
Heist
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10048
-----
onPlay:
+++++
GR0B1R0:


.....
I'm Your Huckleberry
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10047
-----
onPlay:
+++++
GR0B1R0:


.....
Monkey Goes to the Mountain
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10052
-----
onPlay:
+++++
GR0B1R0:


.....
Curse of Failure
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10046
-----
onPlay:
+++++
GR0B1R0:


.....
Ricochet
-----
ae22bba2-cf1e-4038-b7bb-1d3429c10049
-----
onPlay:
+++++
GR0B1R0:




.....
ENDSCRIPTS
=====
'''
