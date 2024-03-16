<img align="left" width="128" height="128" src="https://raw.githubusercontent.com/SiriusBYT/Vanimol/main/icon.png">

# Vanimol
A Lethal Company QoL Modpack that DOESN'T give a single advantage in skill based situations.

## Why choose this modpack instead of other Vanilla/Client-Side Only ones?
Here's one huge problem I have with those. **They always adds something that gives you an advantage**. These modpacks always adds crap like removing the jump delay, which I find very problematic because I'm somewhat of a purist. The philosophy of this modpack is that none of the added mods should give you an advantage in any situations, even in the smallest ones (for example, I refuse to add mods that makes switching items faster as it gives you an advantage when you want to drop off all your items when you want to evade a Forest Giant).

This modpack obviously allows you to join vanilla lobbies.


# Version 0.3.X Changelogs
## Vanimol 0.3.2
- Updated CullFactory to v0.9.2
- Updated IntroTweaks to v1.5.0
- Updated LethalCompany_InputUtils to v0.7.1
- Updated Immersive_Visor to v0.3.2

## Vanimol 0.3.1
- Updated SmartItemSaving (v1.2.0 -> v1.2.1)
- Updated SpaceSunshine (v1.2.1 -> v1.3.0 )
- Updated FriendPatches (v1.0.1 -> v1.0.3)

## Vanimol 0.3.0
- Added DissonanceVoiceSettings (May remove in a future update, not enough people use this so I can't tell the difference if it would break too much the game's immersion/provide an advantage cause you wouldn't have to deal with your teammate's unmuffled microphones, I hope that the game does enough of a good job to muffle player's voices when far away while providing crystal clear audio when your buddy is next to you.)
- Updated Coroner (v1.6.0 -> v1.6.2)
- CONFIG: Control_Company_Detector:
    - No longer showing the [CC] prefix, the big ass purple overlay is enough of an indicator.
    - Ignore friend lobbies is now set to False
- CONFIG: BetterClock
    - Disabled visibility of the clock even when the override is on
- CONFIG: ShipLootPlus
    - Disabled the "Reset Duration Timer on Scan" due to issues where if you continued to spam it, the ship loot stats would still stay up which could provide an advantage.
    - Display Duration is now 2s instead of 2.5s
- CONFIG: FPS_Counter
    - Refresh frequency is now 1s instead of 0.4s
- CONFIG: CoilHeadSate
    - Time Until Stae is now 4s instead of 5s
    - Max State Distance is now 8 instead of 6
    - Head Turn Speed is now 0.1 instead of 0.2
- CONFIG: GeneralImprovements
    - ShipInternalCamSizeMultiplier is now 1 instead of 5 (completely useless)
    - ShipInternalCamFPS is now 12 instead of 30 (ditto)
    - ShipExternalCamSizeMultiplier is now 1 instead of 5 (Gameplay Advantage)
    - ShipExternalCamFPS is now 24FPS instead of 30 (that camera is barely getting used, might as well save a bit of performance there, if people complain I'll revert back to 30FPS)
    - SellCounterItemLimit is now 96 instead of 69
    - HideEmptySubtextOfScanNodes is now set to True
- CONFIG: IntroTweaks
    - bRemoveLaunchedInLanText is now set to False
- CONFIG: MoreBlood
    - NumberOfBloodPools has been reduced from 32 to 8
    - BloodScale is now 2 instead of 1
- CONFIG: NameplateTweaks
    - Reduced NameplateVisibilityDistance from 20 to 0 (Vanilla Behavior)
- Removed HDLethalCompany (Honestly the hell was I thinking?! Even my RTX 3070 can't handle this shit, why did I ever think this was a good idea?!)
- Removed HDVanillaPosters (I kept the low resolution of the game anyways so this was literally useless, couldn't see a different, additional VRAM usage for no reason.)
- Removed SaveStealer (Doesn't work)
    - Removed LethalAPI_Terminal (SaveStealer Dependency)