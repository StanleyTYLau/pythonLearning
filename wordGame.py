phrase = "Just as I arrived at ________ (Place), I realized I had forgotten my ________ (Object)."
print(phrase)

print("Give me a place: ")
blank1 = input()

phrase = phrase.replace("________ (Place)", blank1)
print(phrase)

print("Give me an object: ")
blank2 = input()

phrase = phrase.replace("________ (Object)", blank2)
print(phrase)