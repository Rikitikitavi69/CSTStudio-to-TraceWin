from sys import argv
import os

txt = open(argv[1], 'rb')
originfilename = os.path.splitext(argv[1])[0]
ESX = open(originfilename+"output.esx", "w")
ESY = open(originfilename+"output.esy", "w")
ESZ = open(originfilename+"output.esz", "w")

xcrd = []
ycrd = []
zcrd = []
Ex = []
Ey = []
Ez = []
Bx = []
By = []
Bz = []

for line in txt:
	l = line.split()
	xcrd.append(float(l[0]))
	ycrd.append(float(l[1]))
	zcrd.append(float(l[2]))
	Ex.append(l[3])
	Ey.append(l[4])
	Ez.append(l[5])
	Bx.append(l[6])
	By.append(l[7])
	Bz.append(l[8])


def remdup(x):
	lst = []
	for i in x:
		if i not in lst:
			lst.append(i)
	floatlst = [float(x) for x in lst]
	return floatlst

uniquexcrd = remdup(xcrd)
uniqueycrd = remdup(ycrd)
uniquezcrd = remdup(zcrd)

def coordcount(x):
	count = 0
	firstvalue = x[0]
	firstvalue = float(firstvalue) #-0.48
	for i in x:
		i = float(i)
		if i != abs(firstvalue):
			count += 1
		else:
			break
	return count
xcount = str(coordcount(uniquexcrd))
ycount = str(coordcount(uniqueycrd))
zcount = str(coordcount(uniquezcrd))

minx = str(min(uniquexcrd))
maxx = str(max(uniquexcrd))
miny = str(min(uniqueycrd))
maxy = str(max(uniqueycrd))
absz = uniquezcrd[0]
absz = abs(absz)
absz = str(("%.3f" % absz))

header = str(zcount + " " + absz + "\n" + xcount + " " + minx + " " + maxx + "\n" + ycount + " " + miny + " " + maxy + "\n" + "1" + "\n")

def printofile(file, coordrow):
	file.write(header)
	for i in coordrow:
		file.write("  ")
		file.write(i.decode("utf-8"))
		file.write("\n")

printofile(ESX, Ex)
printofile(ESY, Ey)
printofile(ESZ, Ez)

if ESX.closed != "True":
    ESX.close()
if ESY.closed != "True":
    ESY.close()
if ESZ.closed != "True":
    ESZ.close()
