songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[2])
print(songs[1:3])

songs[2] = "Like You Do"
print(songs)

songs.append("Pretty Boy")
songs.extend(["Ew", "High Hopes"])
songs.remove("Ew")
print(songs)