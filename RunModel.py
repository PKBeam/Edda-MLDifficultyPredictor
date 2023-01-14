import sys
import numpy as np
import pandas
import joblib

# local import
import RagnarockMapUtils

def predictDifficulty(modelPath, mapFolder):
    predictedDiffs = []

    model = joblib.load(modelPath)
    featureRows = []
    mapData = RagnarockMapUtils.getMapDataForPath(mapFolder)
    songDuration = mapData["_songApproximativeDuration"]
    songBpm = mapData["_beatsPerMinute"]

    diffMaps = RagnarockMapUtils.getDifficultyMapsForPath(mapFolder)
    for diffMapObj in diffMaps:
        diffMap = diffMapObj[0]
        diffMapData = RagnarockMapUtils.getDifficultyMapDataForPath(mapFolder, diffMap)
        diffMapNoteDensity = RagnarockMapUtils.getNoteDensity(diffMapData, songDuration)
        diffMapLND2s = RagnarockMapUtils.getLocalNoteDensities(diffMapData, songDuration, songBpm, windowLength=2.75)
        maxND2s = np.quantile(diffMapLND2s, 0.95) if len(diffMapLND2s) > 0 else 0
        featureRows.append(pandas.DataFrame({
            "BPM": [songBpm],
            "NoteDensity": [diffMapNoteDensity],
            "HighNoteDensity2s": [maxND2s]
        }))

    for features in featureRows:
        pred = model.predict(features)
        predictedDiffs.append(pred[0])

    return predictedDiffs

if __name__ == "__main__":
    modelPath = sys.argv[1]
    mapFolder = sys.argv[2]

    for pred in predictDifficulty(modelPath, mapFolder):
        print(pred)



