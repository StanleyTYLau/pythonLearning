actors = [
  "Nathan Fillion",
  "Gina Torres",
  "Alan Tudyk",
  "Morena Baccarin",
  "Adam Baldwin",
  "Jewel Staite",
  "Sean Maher",
  "Summer Glau",
  "Ron Glass"
]

roles = [
  "Captin Malcolm Reynolds",
  "Zoe Washbuirn",
  "Hoban Wasburn",
  "Inara Serra",
  "Jayne Cobb",
  "Kayless Fyre",
  "Dr. Simon",
  "RIver Tam",
  "Derrial Book"
]

print("Featiring: \n =-=-=-=-=-= \n")

for index in range(len(actors)):
  print(actors[index], "as", roles[index])

a = enumerate(actors)
print(list(a))
