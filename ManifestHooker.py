""" Return of the fabled Manifest Hooker. Except this time this isn't for Flashcord.
This file is used to automatically regenerate the dependencies section of the manifest.json file. """
import json; ModList = []
with open("ModList.txt", "r", encoding="utf8") as ModList_File:
    for line in ModList_File: ModList.append(line.replace("\n",""))
with open("manifest.json", "r", encoding="utf8") as Manifest: Manifest = json.load(Manifest)
with open("manifest.json", "w", encoding="utf8") as Manifest_File: Manifest["dependencies"] = ModList; Manifest_File.write(json.dumps(Manifest, indent = 1))