
from khaiii import KhaiiiApi
api = KhaiiiApi()

import pandas as pd

sentiment_data = pd.read_csv("KoreanSample.csv", encoding='CP949')
music_data = pd.read_csv("SpotifyFeatures.csv")
final_mdf = pd.read_csv("Ranged_SpotifyFeatures.csv")

# print(sentiment_data.shape)
# print(sentiment_data.columns)
# print(sentiment_data.loc[0:1])

# df2 = sentiment_data[["ngram"]]
# print(df2)

for word in api.analyze('나는 굉장히 슬픔'):

    i = 0

    while i < len(word.morphs):
        result = ""

        print(word.length)
        print(word.morphs[i].lex)
        print(word.morphs[i].tag)

        t = word.morphs[i].lex + '/' + word.morphs[i].tag
        tempdata = sentiment_data.loc[sentiment_data["ngram"].str[:] == t]

        print(tempdata)

        result = tempdata["SP/max.value"] + tempdata["Intensity/max.value"]

        final_result = result.loc[result.index.values]

        if not tempdata.empty and word.morphs[i].tag == "NNG":
            if final_result.item() == "POSHigh": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 1]        
            elif final_result.item() == "POSMedium": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 2]        
            elif final_result.item() == "POSLow": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 3]        
            elif final_result.item() == "NEUTHigh": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 4]        
            elif final_result.item() == "NEUTLow": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 5]        
            elif final_result.item() == "NEGHigh": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 6]        
            elif final_result.item() == "NEGMedium": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 7]        
            elif final_result.item() == "NEGLow": #item()으로 군집화 구별
                music = final_mdf.loc[final_mdf["cluster_id"] == 0]  
            else:
                i += 1
                continue
        else:
            i += 1
            continue

        fin = music_data.loc[music_data.index.values == music.sample().index.values]
        
        print(fin)
        print(final_result)

        i += 1
