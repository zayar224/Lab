import re

licensenum = re.compile("(^.+)/(\d{5})/(\d{2}$)")
checknum = input("Enter Your Car License Number: ")
if licensenum.match(checknum) == None:
    print("Not Match")
else:
    if checknum == "B/12345/22":
        print("Match! Your Number is B/12345/22")
    else:
        print("Not Found")
