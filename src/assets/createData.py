##Create comparative data for each country

import json
import os
from pathlib import Path
import pickle

for baseFilename in os.listdir("src/assets/CountryData/"):
    if baseFilename.endswith(".pkl"):
        main = []
        baseCountry = Path(baseFilename).stem
        print("--" + baseCountry + "--")
        baseIds = pickle.load(open('src/assets/CountryData/'+baseFilename, 'rb'))
        for otherFilename in os.listdir("src/assets/CountryData/"):
            otherCountry = Path(otherFilename).stem
            similar = 0
            if otherFilename.endswith(".pkl"):
                otherIds = pickle.load(open('src/assets/CountryData/'+otherFilename, 'rb'))
                for baseId in baseIds:
                    for otherId in otherIds:
                        if baseId == otherId:
                            similar = similar + 1
            data = {}
            data['name'] = otherCountry
            data['weight'] = (similar/50)*100
            main.append(data)
        weightJson = json.dumps(main)
        print(weightJson)
        f = open("src/assets/WeightData/"+baseCountry+".json", "a")
        f.write(weightJson)
        f.close()