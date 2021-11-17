def getThreeNum():
    firstN = int(input("First Number: "))
    secondN = int(input("Second Number: "))
    thirdN = int(input("Third Number: "))
    if firstN < secondN and firstN < thirdN:
        print(f"{firstN} is the lowest number.")
        return firstN
    elif secondN < firstN and secondN < thirdN:
        print(f"{secondN} is the lowest number.")
        return secondN
    else:
        print(f"{thirdN} is the lowest number.")
        return thirdN

three_Num = getThreeNum()

print("Done")