import os
import re
continueLoop = True
pattern = r"!\[\[.*?\]\]"
pattern2 = r"\[(.*?)\]"
pattern3 = r"#.*"
pattern4 = r"\n\n#.*"

# This is my first ever file handling project!

replacement: list[str] = []
exportFilePath = ""
content = ""

while continueLoop:
    replacement.clear()

    initialMdPath= input("pls enter the file path of the .md file here: ")
    initialMdPath = initialMdPath.replace("\\", "")

    if os.path.isfile(initialMdPath):
        print("the file path found successfully!")
    else:
        print("sorry, you entered a wrong file path.")
        print("pls try again!")
        continue

    try:
        with open(initialMdPath, "r") as file:
            content = file.read().replace(".png", ".jpg", -1).replace("==", "", -1)
            result = re.findall(pattern=pattern, string=content)
            result2: list[str] = []
            for x in result:
                result2.append(f"[{x.replace("![[", "").replace("]]","")}]")
            result3 = re.findall(pattern3, content)
            # result4 = re.findall(pattern4, content)

            for x in result2:
                temp = x.replace(" ", "_").replace("[", "").replace("]", "")
                replacement.append(f"!{x}(Archive/{temp})")


    except:
        print("**\n** error while trying to read the file from the given file path. **\n**")
        break

    exportFilePath = "/Users/david_an/Documents/coding projects active/001/Outputs/outputMd.md"

    newResult2: list[str] = []

    try:
        with open(exportFilePath, "w") as file:
            finalContent = content
            checker = re.findall(pattern=pattern4, string=finalContent)

            for index, y in enumerate(replacement):
                finalContent = finalContent.replace(f"{result[index]}", f"{y}", 1)

            for index in range(0, len(result3)):
                if not f"\n\n{result3[index]}" in checker:
                    finalContent = finalContent.replace(f"{result3[index]}", f"\n{result3[index]}", 1)
            print("done")
            file.write(finalContent)
    #         f"\n{result3[index]}"
    except:
        print("error while trying to write the file!")