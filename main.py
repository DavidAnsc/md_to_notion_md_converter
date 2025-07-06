import os
import re
continueLoop = True
pattern = r"\w+ \d+-\d+-\d+ \w+ \d+.\d+.\d+ \w+.\w+]]"
imagesFilePath = "/Users/david_an/Pictures/Others/Archive"

while continueLoop:
    initialMdPath= input("pls enter the file path of the .md file here: ")
    initialMdPath = initialMdPath.replace("\\", "")

    if os.path.isfile(initialMdPath):
        print("the file path found successfully!")
    else:
        print("sorry, you entered a wrong file path.")
        print("pls try again!")
        continue

    try:
        with open(initialMdPath, "w") as file:
            content = file.read()
            result = re.findall(pattern=pattern, string=content)


    except:
        print("error!")
        break