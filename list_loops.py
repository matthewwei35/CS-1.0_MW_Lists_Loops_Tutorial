# ---- Q1 ----
songs = ["ROCKSTAR", "Do It", "For The Night"]

# ---- Q2 ----
print(songs[0])
print(songs[2])
print(songs[1:3])

# ---- Q3 ----
songs[2] = "Like You Do"
print(songs)

# ---- Q4 ----
songs.append("Pretty Boy")
songs.extend(["Ew", "High Hopes"])
songs.remove("Ew")
print(songs)

# ---- Q5 ----
'''
# Option 1
for song in songs:
    print(song)
# Option 2
for i in range(len(songs)):
    print(songs[i])
'''

# ---- Q6 ----
animals = ["Cat", "Dog", "Bird"]
animals.append("Hamster")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)