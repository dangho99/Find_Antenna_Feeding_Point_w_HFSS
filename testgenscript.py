

def hfssCreateRegularPolyhedron(fid,Name, Center, Start, Height, NumSides, WhichAxis, Units):

	fid.write('\n')
	fid.write('oEditor.CreateRegularPolyhedron _\n')
	fid.write('Array("NAME:CylinderParameters", _\n')
	fid.write('"XCenter:=", "%f%s", _\n'% (Center[0], Units))
	fid.write('"YCenter:=", "%f%s", _\n'% (Center[1], Units))
	fid.write('"ZCenter:=", "%f%s", _\n'% (Center[2], Units))

	fid.write('"XStart:=", "%f%s", _\n'% (Start[0], Units))
	fid.write('"YStart:=", "%f%s", _\n'% (Start[1], Units))
	fid.write('"ZStart:=", "%f%s", _\n'% (Start[2], Units))

	fid.write('"Height:=", "%f%s", _\n'% (Height, Units))
	fid.write('"NumSides:=", "%f", _\n'% (NumSides))
	fid.write('"WhichAxis:=", "%s"), _\n'% (WhichAxis))

	# Cylinder Properties.
	fid.write('Array("NAME:Attributes", _\n')
	fid.write('"Name:=", "%s", _\n'% (Name))
	fid.write('"Flags:=", "", _\n')
	fid.write('"Color:=", "(132 132 193)", _\n')
	fid.write('"Transparency:=", 0, _\n')
	fid.write('"PartCoordinateSystem:=", "Global", _\n')
	fid.write('"MaterialName:=", "vacuum", _\n')
	fid.write('"SolveInside:=", true)\n')
	fid.write('\n')


def hfssCreateRegularPolygon(fid,Name, Center, Start, NumSides, WhichAxis, Units):

	fid.write('\n')
	fid.write('oEditor.CreateRegularPolygon _\n')
	fid.write('Array("NAME:CylinderParameters", _\n')
	fid.write('"XCenter:=", "%f%s", _\n'% (Center[0], Units))
	fid.write('"YCenter:=", "%f%s", _\n'% (Center[1], Units))
	fid.write('"ZCenter:=", "%f%s", _\n'% (Center[2], Units))

	fid.write('"XStart:=", "%f%s", _\n'% (Start[0], Units))
	fid.write('"YStart:=", "%f%s", _\n'% (Start[1], Units))
	fid.write('"ZStart:=", "%f%s", _\n'% (Start[2], Units))

	#fid.write('"Height:=", "%f%s", _\n'% (Height, Units))
	fid.write('"NumSides:=", "%f", _\n'% (NumSides))
	fid.write('"WhichAxis:=", "%s"), _\n'% (WhichAxis))

	# Cylinder Properties.
	fid.write('Array("NAME:Attributes", _\n')
	fid.write('"Name:=", "%s", _\n'% (Name))
	fid.write('"Flags:=", "", _\n')
	fid.write('"Color:=", "(132 132 193)", _\n')
	fid.write('"Transparency:=", 0, _\n')
	fid.write('"PartCoordinateSystem:=", "Global", _\n')
	fid.write('"MaterialName:=", "vacuum", _\n')
	fid.write('"SolveInside:=", true)\n')
	fid.write('\n')


import HFSS as hfss
import math
import geopandas as gpd
from shapely.geometry import Polygon
import geopandas.geoseries as geose 

radius = 10
MaxX = 2*radius
MaxY = math.sqrt(3)*radius
list_point = [(0,radius*math.sqrt(3)/2), (radius/2, 0), (radius/2 + radius, 0), (radius*2, radius*math.sqrt(3)/2), (radius/2 + radius\
	, radius*math.sqrt(3)), (radius/2, radius*math.sqrt(3))]

Center = [radius, radius*math.sqrt(3)/2, -1.5]
Start = [0, radius*math.sqrt(3)/2, -1.5]

polys = gpd.GeoSeries(Polygon(list_point))
df = gpd.GeoDataFrame({'geometry': polys})
#df.plot()

point = geose.Point(0,0) # check point 
#  poly_list[i].intersects(coaxial_check)[0] # checking command. 

###########
x = []
y = []
for i in range(len(list_point)):
	x.append(list_point[i][0])
	y.append(list_point[i][1])

import matplotlib.pyplot as plt 
#plt.plot(x,y,'ro')

#########

tmpScriptFile = "C:\\Users\\DELL\\Desktop\\test.vbs"
fid = open(tmpScriptFile, 'w')
# create a new HFSS project.
hfss.hfssNewProject(fid)
hfss.hfssInsertDesign(fid, 'NxN_uStrip_Patch')
# hfssCreateRegularPolyhedron(fid, 'okok', Center, Start, 1.5, 6, 'Z', 'mm')
hfssCreateRegularPolygon(fid, 'okok', Center, Start, 6, 'Z', 'mm')





