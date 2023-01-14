import os
import json
import numpy as np

def getMapDataForPath(path):
    mapDataName = ""
    if "info.dat" in os.listdir(f"{path}"):
        mapDataName = "info.dat"
    if "Info.dat" in os.listdir(f"{path}"):
        mapDataName = "Info.dat"
    with open(f"{path}/{mapDataName}", "r") as f:
        mapData = f.read()
        mapJson = json.loads(mapData)
        return mapJson

def getMapData(mapFolder, folder):
    return getMapDataForPath(f"{mapFolder}/{folder}")

def getDifficultyMapsForPath(path):
    difficultyMaps = []
    mapJson = getMapDataForPath(path)
    for d in mapJson["_difficultyBeatmapSets"][0]["_difficultyBeatmaps"]:
        difficultyMaps.append((d["_beatmapFilename"], d["_difficultyRank"]))
    return difficultyMaps

def getDifficultyMaps(mapFolder, folder):
    return getDifficultyMapsForPath(f"{mapFolder}/{folder}")

def getDifficultyMapDataForPath(path, file):
    filePath = f"{path}/{file}"
    with open(filePath, "r") as f:
        mapData = f.read()
        mapJson = json.loads(mapData)
        return mapJson

def getDifficultyMapData(mapFolder, folder, file):
    return getDifficultyMapDataForPath(f"{mapFolder}/{folder}", file)

def getMaps(mapFolder):
    maps = []
    for obj in os.listdir(f"{mapFolder}"):
        objPath = f"{mapFolder}/{obj}"
        if os.path.isdir(objPath) and ("info.dat" in os.listdir(objPath) or "Info.dat" in os.listdir(objPath)):
            maps.append(obj)
    return maps

def getNoteDensity(diffMapData, duration):
    notesList = diffMapData["_notes"]
    return len(notesList)/duration

def beatToSec(beat, bpm):
    return 60/bpm * beat

# heuristically, windowLength = 2.75, step = 0.25 is best
def getLocalNoteDensities(diffMapData, duration, bpm, windowLength=2.75, step=0.25):
    densities = []
    beatsPerWindow = bpm/60 * windowLength
    windowLower = 0
    windowUpper = windowLength
    while windowUpper < duration:
        numNotes = 0
        for n in diffMapData["_notes"]:
            noteTime = beatToSec(n["_time"], bpm)
            if windowLower <= noteTime and noteTime <= windowUpper:
                numNotes += 1
        densities.append(numNotes/windowLength)
        windowLower += step
        windowUpper += step
    return densities

def getLocalColumnVariety(diffMapData, duration, bpm, windowLength=2.75, step=0.25):
    variety = []
    beatsPerWindow = bpm/60 * windowLength
    windowLower = 0
    windowUpper = windowLength
    while windowUpper < duration:
        localVariety = np.array([0, 0, 0, 0])
        for n in diffMapData["_notes"]:
            noteTime = beatToSec(n["_time"], bpm)
            noteCol = n["_lineIndex"]
            if windowUpper <= noteTime:
                break
            if windowLower <= noteTime:
                localVariety[noteCol] += 1
            if np.linalg.norm(localVariety, 1) > 0:
                # L1-normalise or normalise for the amount of notes
                normLocalVariety = localVariety / np.linalg.norm(localVariety, 1)
                # maps with higher column variety will have a distribution closer to [.25, .25, .25, .25]
                score = np.linalg.norm(normLocalVariety - np.array([0.25, 0.25, 0.25, 0.25]), 2)
                # higher is better
                variety.append(-1 * score)

        windowLower += step
        windowUpper += step
    return variety
