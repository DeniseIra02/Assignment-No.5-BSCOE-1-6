your_Age = int(input("Age: "))

if your_Age >= 0 and your_Age <= 12:
    print ("Kid")
elif your_Age >= 13 and your_Age <= 17:
    print("Teen")
elif your_Age == 18:
    print("Debut")
elif your_Age >= 19 and your_Age <= 59:
    print("Adult")
else:
    print("Senior")

print("Done")