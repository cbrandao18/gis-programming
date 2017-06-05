#Christie Brandao - gdal-ogr Questions

#Question 1
#f = layer.GetFeature(0)
#geom = f.GetGeometryRef()
#print geom.GetEnvelope()
#print geom.GetArea()
#print geom.Centroid()
#(-111.79083818911886, -110.79024718818687, 44.473322348537295, 46.189460350135505)
#0.779005889637
#POINT (-111.172313600301464 45.536696893626988)

#The outputs of the area and centroid are reasonable because the envelope accruately
#represent west, east, south, and north points. The centroid makes sense because
#the numbers are in the scope of the envelope.

from osgeo import ogr
fname = raw_input("Enter the location of the shapefile: ")
driver = ogr.GetDriverByName("ESRI Shapefile")
vector = driver.Open(fname, 0)
layer = vector.GetLayer(0)
print 'Number of features: ', layer.GetFeatureCount()
f = layer.GetFeature(0)
print 'Number of fields: ', f.GetFieldCount()
print 'Name of each field: '
for i in range(f.GetFieldCount()):
    field_name = f.GetFieldDefnRef(i).GetName()
    print field_name
userin = raw_input("Enter an index number of a polygon feature: ")
donetext = "DONE"
while ((userin == donetext) == False):
    numfeatures = layer.GetFeatureCount()
    feature = int(userin)
    #the name and value for all attributes
    if feature < layer.GetFeatureCount():
        f = layer.GetFeature(feature)
        fieldcount = f.GetFieldCount()
        for i in range(fieldcount):
            field_name = f.GetFieldDefnRef(i).GetName()
            print 'Field', field_name, 'has a value of', f.GetField(field_name)
    #number of geometries in the feature
        geom = f.GetGeometryRef()
        print 'Number of geometries in feature: ', geom.GetGeometryCount()
    #centroid of the polygon
        print 'Centroid of the polygon: ', geom.Centroid()
    #size of the polygon
        print 'Size of the polygon: ', geom.GetArea()
    else:
        print 'Invalid index'
    userin = raw_input("Enter an index number of a polygon feature: ")
