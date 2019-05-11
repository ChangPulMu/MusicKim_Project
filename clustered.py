import pandas as pd
from sklearn.cluster import KMeans

music_data = pd.read_csv("SpotifyFeatures.csv")

ranged_music_data = music_data[["loudness", "danceability", "tempo", "energy"]]
ranged_music_data["tempo"] = ranged_music_data["tempo"] / 100
ranged_music_data["loudness"] = ranged_music_data["loudness"] / 60

ranged_music_data_values = ranged_music_data.values

kmeans = KMeans(n_clusters = 8).fit(ranged_music_data_values)

kmeans.labels_

ranged_music_data.loc[:, "cluster_id"] = kmeans.labels_

ranged_music_data.to_csv("Ranged_SpotifyFeatures.csv")

print("--------------------------------------------------------------------------")
print("Finished Your Clustering")
