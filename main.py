import os
import re
continueLoop = True
pattern = r"\b!\w+]"
while continueLoop:
    initialMdPath= input("pls enter the relative file path of the .md file here: ")

    if os.path.isfile(initialMdPath):
        print("the file path found successfully!")
    else:
        print("sorry, you entered a wrong file path.")
        print("pls try again!")
        continue

    try:
        with open(initialMdPath, "r") as file:
            content = file.read()
            result = re.findall(pattern=pattern, string=content)
        print(result.count)
    except:
        print("error!")
        break