# Changelog

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

## Vanimol 0.2.0
- Added LethalStats Mod (Having stats sounds interesting, slightly concerned about privacy though, may remove in the future if I don't like it.)
    - Added Coroner (Dependency for LethalStats, also honestly it is a good to have.)
- Added LC Masked Fix (Forced to DC/Reconnect is annoying)
- Updated FPSCounter (v1.1.0 -> v1.2.0)
- Updated SmartItemSaving (v1.3.0 -> v1.4.0)
- Removed ReverbOnDeath (Gameplay Advantage)

## Vanimol 0.1.1
- Updated GeneralImprovements (v1.1.10 -> v1.1.11)

## Vanimol 0.1.0
- Updated all mods
- CONFIG: General Improvements
    - Removed the ability by default to pull the level if you're not the host
- Removed FontFixer (causes major graphical bugs)
- Epic change to the Version number on the bottom on the main menu, there is now Vanimol's version too.
- Removed CozyImprovements (Honestly not that useful thanks to General Improvements)
- Removed CleanerLogs (Broken? No real difference found)
- Removed FixRPCLag (Ditto)
- Removed TerminalConflictFix (Terminal is a bigger pain to use, I'd rather buy 10 TVs accidentally instead.)
- Removed ModelReplacementAPI (Left over from me testing out suits mods)
- Removed LethalLib (Ditto)
- Removed LC_API (Ditto)
- Removed useless config files

## Vanimol 0.0.2
- Updated all mods
- Removed ChangeName mod (broken)

## Vanimol 0.0.1
- Initial Release
