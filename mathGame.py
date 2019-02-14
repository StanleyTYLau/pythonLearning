questions = [[1,2], [2,3], [4,4]]
score = 0

for a, b in questions:
  response = int(input("What is the value of " + str(a) + " + " + str(b) + "?"))
  
  if response == (a + b):
    score += 1
    print("Correct!")
  else:
    print("Wrong!")

print("Final score: " + str(score))