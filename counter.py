counter = 0
for n in range (10, 100):
    s = str(n)
    if s[0] == "4" or s[1] == "4":
        counter = counter + 1
print(counter)