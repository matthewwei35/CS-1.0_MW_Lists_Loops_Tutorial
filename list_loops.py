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

# Option 1
for song in songs:
    print(song)
# Option 2
for i in range(len(songs)):
    print(songs[i])

animals = ["Lizard", "Bird", "Ant"]
animals.append("Dog")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)