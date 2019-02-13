foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

# 1) Get the median player-- That is, the player exactly in the middle of the league (hint: You can get the total number of players with `len(foosballers)` and then divide that number by 2; You may want to use integer division (see: Numbers section) for this calculation).
median = len(foosballers)//2
print("The median player: ", str(foosballers[median]))

# 2) Get the five players in the middle of the league-- That is, in addition to the median player, also get the players two above and the two below.
print("The five middle players: ", foosballers[median-2 : median+3])

# 3) Add a fake player, called "Average Player," to the exact middle of the list, to show clearly who is above and below average.
foosballers.insert(median, "Average Player")
print(foosballers)

# 4) Actually, that's not obvious enough. Find "Average Player," and change their name to uppercase: "AVERAGE PLAYER." That'll stand out.
foosballers[median] = "AVERAGE PLAYER"
print(foosballers)

# 5) Add five more players with names of your choosing, to the bottom of the list-- They are unranked and we must therefore assume they are terrible.
badPlayers = ["Stan", "Bob", "Po", "Fip", "Gob"]
foosballers = foosballers + badPlayers
print(foosballers)

# 6) Oh no-- Now "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this.
foosballers.remove("AVERAGE PLAYER")
median = len(foosballers)//2
foosballers.insert(median, "Average Player")
print("New list", foosballers)

# 7) Five more players show up, but they are ranked. Insert them at the appropriate location:

# - Lacy is one spot ahead of Hubert

# - Omar is one spot behind Rebecca

# - Otto is 8th best in the league

# - Chauncey is 10 spots from the bottom of the league
