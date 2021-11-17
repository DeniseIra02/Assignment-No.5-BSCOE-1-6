import math
yourGrd_ =  float(input("Enter your grade: "))

if yourGrd_ >= 96.5 and yourGrd_ <= 100:
    print("Grade/Mark: 1.00")
    print("Description: Excellent")
elif yourGrd_ >= 93.5 and yourGrd_ <= 96.4:
    print("Grade/Mark: 1.25")
    print("Description: Excellent")
elif yourGrd_ >= 90.5 and yourGrd_ <= 93.4:
    print("Grade/Mark: 1.50")
    print("Description: Very Good")
elif yourGrd_ >= 87.5 and yourGrd_ <= 90.4:
    print("Grade/Mark: 1.75")
    print("Description: Very Good")
elif yourGrd_ >= 84.5 and yourGrd_ <= 87.4:
    print("Grade/Mark: 2.00")
    print("Description: Good")
elif yourGrd_ >= 81.5 and yourGrd_ <= 84.4:
    print("Grade/Mark: 2.25")
    print("Description: Good")
elif yourGrd_ >= 78.5 and yourGrd_ <= 81.4:
    print("Grade/Mark: 2.50")
    print("Description: Satisfactory")
elif yourGrd_ >= 75.5 and yourGrd_ <= 78.4:
    print("Grade/Mark: 2.75")
    print("Description: Satisfactory")
elif yourGrd_ >= 74.5 and yourGrd_ <= 75.4:
    print("Grade/Mark: 3.00")
    print("Description: Passing")
elif yourGrd_ >= 64.5 and yourGrd_ <= 74.4:
    print("Grade/Mark: 5.00")
    print("Description: Failure")
else:
    print("Invalid. Maybe it is Incomplete/Withdrawn/Dropeed")