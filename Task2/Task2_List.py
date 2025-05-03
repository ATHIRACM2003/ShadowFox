#Task 2 - List
justice_league = ["Superman", "Batman", "WonderWoman", "Flash", "Aquaman", "Green Lantern"]
print("\nThe Justice League :\n",justice_league)

#1. Calculate the number of members
print("\nNumber of members in Justice League = ",len(justice_league))

#2. Add  Batgirl and Nightwing to your list
justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("\nJustice League after adding new members :\n",justice_league)

#3. Move Wonder Woman to the beginning of the list
justice_league.remove("WonderWoman")
justice_league.insert(0,"WonderWoman")
print("\nJustice League with Wonder Woman as the leader :\n",justice_league)

#4. Choose either "Green Lantern" or "Superman" and place between Aquaman and Flash
justice_league.remove("Superman")
aqua = justice_league.index("Aquaman")
flash = justice_league.index("Flash")
if aqua<flash:
    justice_league.insert(aqua+1,"Superman")
else:
    justice_league.insert(flash+1,"Superman")
print("\nJustice League after placing Superman in between Aquaman and Flash :\n", justice_league)
    
#5.  Superman decided to assembles a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "MartianManhunter", "Green Arrow"]
print("\nJustice League with a new team :\n",justice_league)

#6. Sort  alphabetically
justice_league.sort()
print("\nJustice League after sorting:\n",justice_league)

#7. Predict the new leader
print("\nNew Leader: ",justice_league[0])
