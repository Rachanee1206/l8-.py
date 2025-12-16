t = input(("Enter a sentence to find prominant word: "))
t = t.split()
BigWord = 0

for wrd in t:
    lenW = len(wrd)
    if lenW>BigWord:
        BigWord = lenW

for wrd in t:
    lenW = len(wrd)
    if lenW==BigWord:
        print("Largest Word:",wrd)