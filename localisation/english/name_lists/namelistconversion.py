#read the list, copy all things of a category that you define to the clipboard
# and write a copy of the file so you can double check
import pyperclip

#file to use
file = "./name_list_honeybear_ursinespeciespack_URS1_l_english.yml"
copyfile = file[:-4] + "copy.yml"
#get the section you want
keyValue = "planets"
prefix = "URSINE1_PLANET_"
pyperclipString = ""

lines = []
with open(file, 'r') as file:
    lines = file.readlines()


section = False
newlines = []
for line in lines:
    if section:
        newline = line.strip()
        newline = newline.strip("#")
        if newline == "":
            newline = "\n"
            section = False
            newlines.append(newline)
            continue
        newline = " " + prefix + newline
        pyperclipString = pyperclipString + newline
        newline = " " + newline + "\n"
    else:
        newline = line
        if keyValue in line:
            section = True #we have arrived at the correct section
    newlines.append(newline)

print("wowee")
pyperclip.copy(pyperclipString)

with open(copyfile, 'w') as file:
    file.writelines(newlines)