import os
import re
import bext

patternImageEdit = r"!\[\[.*?\]\]"
patternImage = r"\[(.*?)\]"

patternTitleEdit = r"#.*"
patternTitle = r"\n\n#.*"

patternListEdit = r"\n-.*"
# this pattern is only for no-indentation lists, I am going to figure this out. TODO: figure this out, how to make this fit to all lists?
patternList = r"\n\n-.*"

patternIndentListEdit = r"\t-.*"
patternIndentList = r"\t*-.*"
# This is my first ever file handling project!

replacement: list[str] = []
exportFilePath = ""
content = ""

bext.fg("purple")
print("**Hi, welcome to md converter for Notion**")
print("\n*program initialized*\n\n")
bext.fg("reset")

menu_selection = True
while menu_selection:
    print("** select mode **")
    bext.bg('yellow')
    print(" 1 USER MANUAL (QUICK) ", end="")
    bext.bg('reset')
    print()
    bext.bg('yellow')
    print(" 2 START THE CONVERTER ", end="")
    bext.bg('reset')
    print()
    bext.bg('yellow')
    print(" 3 GET GITHUB REPO     ", end="")
    bext.bg('reset')

    print()
    
    
    answer = input("your choice:   ").replace(" ", "")

    if answer == "1":
        menu_selection = False
        # TODO: write the user manual here



    elif answer == "2":
        continueLoop = True
        menu_selection = False
        print("\n** converter initialized **")
        while continueLoop:
            replacement.clear()
            print("\n* you can press q to go back to the menu *")
            initialMdPath= input("pls enter the file path of the .md file you want to convert here: ")
            initialMdPath = initialMdPath.replace("\\", "")

            if initialMdPath.lower() == "q":
                print('\n')
                continueLoop = False
                menu_selection = True
                

            elif os.path.isfile(initialMdPath):
                print("the file path found successfully!")

                try:
                    with open(initialMdPath, "r") as file:
                        content = file.read().replace(".png", ".jpg", -1).replace("==", "", -1)
                        result = re.findall(pattern=patternImageEdit, string=content)
                        result2: list[str] = []

                        for x in result:
                            result2.append(f"[{x.replace("![[", "").replace("]]","")}]")

                        result3 = re.findall(patternTitleEdit, content)
                        result4 = re.findall(patternListEdit, content)
                        result5 = re.findall(patternIndentList, content)

                        for x in result2:
                            temp = x.replace(" ", "_").replace("[", "").replace("]", "")
                            replacement.append(f"!{x}(Archive/{temp})")


                except:
                    print("**\n** error while trying to read the file from the given file path. **\n**")
                    break

                exportFilePath = "../Outputs/outputMd.md"

                newResult2: list[str] = []

                try:
                    with open(exportFilePath, "w") as file:
                        finalContent = content
                        checkerForTitle = re.findall(pattern=patternTitle, string=finalContent)
                        checkerForList = re.findall(pattern=patternList, string=finalContent)
                        checkerForIndentList = re.findall(pattern=patternIndentList, string=finalContent)
                        for index, y in enumerate(replacement):
                            finalContent = finalContent.replace(f"{result[index]}", f"{y}", 1)

                        for index in range(0, len(result3)):
                            if not f"\n\n{result3[index]}" in checkerForTitle:
                                finalContent = finalContent.replace(f"{result3[index]}", f"\n{result3[index]}", 1)

                        for index in range(0, len(result4)):
                            if not f"\n\n{result4[index]}" in checkerForList:
                                finalContent = finalContent.replace(f"{result4[index]}", f"\n{result4[index]}", 1)

                        for index in range(0, len(result5)):
                            if not f"\n\n{result5[index]}" in checkerForIndentList:
                                finalContent = finalContent.replace(f"{result5[index]}", f"\n{result5[index]}", 1)

                        print("done")
                        file.write(finalContent)
                #         f"\n{result3[index]}"
                except:
                    print("error while trying to write the file!")
                else:
                    print("sorry, you entered a wrong file path.")
                    print("pls try again!")
                    continue

            



    elif answer == "3":
        menu_selection = False



    else:
        print("you didn't select anything valid, try again.\n")
        menu_selection = True

