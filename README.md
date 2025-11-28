This is a program that can turn obsidian .md files to notion-readable .md files.
You'll need:
- a folder contains all images that you used in the .md file
- the obsidian .md file

## PREPARATION

In this program, all you have to prepare is a .md text file 
which is the document that contains image hyperlinks
or other formats that only work for Obsidian so need format conversion, 
and a folder with the images that were used in the document.

^^
(You don't actually need the folder with images, 
you'll only need it before importing to Notion or other softwares.)
^^

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
