Changelog - Doomtown:Reloaded OCTGN Game Definition
===============================================

### 1.3.5.x

* Jobs now script their effects. If you press F10 when nobody has defended or during a shootout, it will ask if the job was successful and appropriately do the effects. 
* Jobs will now move you to the Mark's location

### 1.3.4.x

* Fixes Ulysses Marks
* Fixes Leon Cavallo
* After shootout ends, game will announce who was the leader.

### 1.3.3.x

* Added a new Town Square image. increased its size and made it anchored so that it cannot be moved.
* Fixed the cheatin' marker placement and size.

### 1.3.2.x

* Fixed It's Who You Know calling out with opposing dude
* Fixed Make 'Em Sweat targeting your own dude
* Fixed Mongwau always discarding his first spell
* Fixed Faithful hound costing 1
* Fixed Paying/Gaining Twice for Mendoza/Irving on jobs
* Fixed Surveyor's office not targeting correctly
* Fixed Recalculating counting draw hand cards

### 1.3.1.x

* Fixes error on Bottom Dealin'

### 1.3.0.x

** Double Dealin'** has arrived into town!

### 1.2.3.x

* Hired Help and Bounty Hunter will now properly spawn gunslingers
* Union Casino should work now
* Joker will not be aced from Pony Express anymore.

### 1.2.2.x

Various bugfixes

### 1.2.1.x

* Cheatin' Draw Hands will now have a little icon to make it more obvious, without having to look in the chat.
* Upkeep will now prompt you to discard dudes you cannot pay
* Upkeep will now prompt you if you want to pay dudes with >3 upkeep
* Game will now remind you to pay your upkeep if you try to take a high-noon action.
* Game will not block continuing to High Noon if other players have not done their upkeep yet.
* Once all players do upkeep, game will automatically move to High Noon
* Scripted the Telepathy Helmet
* Added "I'm Ready" announcement (Ctrl+R)
* Unprepared will now boot spells
* Mendoza and Irving will now lose/gain GR when they call out.
* Scripted Plasma Drill and the other SB1 scripts

### 1.2.0.x

** New Town, New Rules** has arrived into town!

### 1.1.5.x

* Fixed Flush and Pairs checking
* Fixed This is a Hold up
* Law Dogs home will now boot your targeted dudes, but it will only put a bounty on opposing dudes. (To use it to put bounty on your own dudes, do it manually)
* Cheatin' Varmint will announce.
* General Store will work for spells as well now.
* Micah's ability should work now.
* Remy's ability should cost GR now.
* Pharmacy should work now.

### 1.1.4.x

* Added last 3 cards

### 1.1.3.x

* Spell checks will now take into account Skill Bonus (e.g. Morgan Research Inst.)
* Morgan Research Inst. will properly clear at Sundown.
* Fixed Morgan Research Inst. choice menu

### 1.1.2.x

* Scripted Raising Hell

### 1.1.1.x

* Scripted all core spells except Raising Hell

### 1.1.0.x

* Added deck checking at the start. Game will also announce your home when the game starts.
* Fixed participation scripts
* Fixed Sloane's Ability

### 1.0.1.x

* Added inspect function (Ctrl+I)

### 1.0.0.x

Doomtown:Reloaded is now available on OCTGN!

Almost all cards are scripted, and a lot of mechanical effects are automated as well (look for a future how-to-play guide)

## Script Information

* **All Jobs:** Will help at organizing posses, but no effects scripted for success for now. Please take care of it manually
* **All Spells:** They will pull, but don't check for success and don't trigger the result. Please deal with it manually for now.
* **Location Based Abilities:** Location is not tracked, and thus anything that relies on being in a location, or controlling that location will not rules enforce. Just check those conditions manually before using those abilities (e.g. Allie Hensman, Bunkhouse or Extortion)
* 1st Baptist Church: Will take your intreased handsize into account at refill at Sundown, if you control that location
* Ambush: Won't give the extra bounty for targeting a non-wanted char.
* Arnold McCadish: Won't check for success. Just avoid discarding manually.
* Auction: Not scripted
* Bad Company: Won't give the extra money automatically.
* Bank of California: Won't prevent anything automatically.
* Bobo: Doesn't visibly update bullet value automatically
* Cattle Marker: Doesn't update automatically
* Circle M Ranch: Doesn't check existing handsize
* Doyle's Hoyle: Not Scripted
* Jonah Essex: Doesn't visibly increase bullets
* Doesn't check influence yet. Just adds bounty to the dude you've targeted. Boot your Law Dogs manually.
* Legendary Holster: Pulls but doesn't kill anyone automatically
* Lucinda: Manual use.
* Max Baine: Doesn't gain the CP automatically. Use his ability to gain a CP quickly
* Pair of Six Shooters: Just announces
* Peacemaker: Doesn't prevent the markers being added to the dude.
* Pinto: Doesn't move you to the location ofd the shootout.
* Prescott Utter: Doesn't change influence & bullets automatically
* Run 'em Down!: Doesn't do the callout. Do that manually.
* Telegraph Office. Doesn't check if the dude came into play this turn.
* Ghostly Gun: Just Announces
* Undertaker: Not scripted