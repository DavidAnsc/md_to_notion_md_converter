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
exportFilePath = "outputs/outputMd.md"
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

        print("\n**\nwelcome to our user manual\n**\n")
        print("""
        This is a program that can turn obsidian .md files to notion-readable .md files.
        
        You'll need:
        - a folder contains all images that you used in the .md file
        - the obsidian .md file

        Here's the procedure guys:

        ## PREPARATION

        In this program, all you have to prepare is a .md text file 
        which is the document that contains image hyperlinks
        or other formats that only work for Obsidian so need format conversion, 
        and a folder with the images that were used in the document.
        
        *
        (You don't actually need the folder with images, 
        you'll only need it before importing to Notion or other softwares.)
        *

        ## CONVERSION

        After finishing the preparation, you can go to "2" and start the conversion,
        it will produce a file called "outputMd.md" file into a folder called "output"
        in the project directory.

        ## IMPORT

        Now, we need to import, to import to Notion, we're going to produce a .zip file.
        First, copy the folder with the image source files into the same directory as the
        .md file that generated. ** Next, rename the folder to "Archive" (this step 
        is important). ** Finally, select "outputMd.md" and the "Archive" folder,
        compress them into one .zip file and import it into Notion.

        (It might take longer than expected if you have a large Archive folder.)

        """)

        print("\n**\nuser manual ends\n**\n")



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

            



    elif answer == "3":
        menu_selection = True
        print("\n**  link:\nhttps://github.com/DavidAnsc/md_to_notion_md_converter\n**\n")
        # get the link here:



    else:
        print("you didn't select anything valid, try again.\n")
        menu_selection = True

