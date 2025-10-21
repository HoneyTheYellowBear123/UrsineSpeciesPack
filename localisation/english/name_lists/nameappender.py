#to quickly convert names from comments to a usable format

modprefixstring = "honeybear_ursinespecispack"
names = "Otso Karhu Ohto Kontio"
lines = names.split(" ")
localization = []
namelist = ""

for line in lines:
    prefixed = modprefixstring + "_" + line
    localizationstring = prefixed + ": " + line

    localization.append(localizationstring)
    namelist = namelist + " " + prefixed


print("put this in localization")
for l in localization:
    print(l)



print("put this in the common/namelist file")
print(namelist)
