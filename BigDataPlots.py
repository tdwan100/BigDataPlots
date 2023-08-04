import matplotlib.pyplot as plt
import json,urllib.request
#importing json from url
handle = urllib.request.urlopen("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson")
rawdata = handle.read()
data = json.loads(rawdata)
data.keys()
#pulling magnitude data from json file
def getMagnitudeFromJsonData(earthquakeJson):
    output = []
    for row in earthquakeJson.get('features', []):
        properties = row.get('properties',  {})
        data = properties.get('mag', 0)
        output.append(data)
    return output
#pulling depth data from json file
def getDepthFromJsonData(earthquakeJson):
    output = []
    for row in earthquakeJson.get('features', []):
        geometry = row.get('geometry',  {})
        coordinates = geometry.get('coordinates', [])
        output.append(coordinates[2])
    return output
#calculating pearson correlation coeffecient
def correlation(xList, yList):

    if len(xList) != len(yList):
        print("Error: there are", len(xList), "x-values and", len(yList), "y-values")
        return 0
        
    import statistics
    xBar = statistics.mean(xList)
    yBar = statistics.mean(yList)
    xStd = statistics.stdev(xList)
    yStd = statistics.stdev(yList)
    total = 0.0
    for i in range(len(xList)):
        total = total + (xList[i] - xBar) * (yList[i] - yBar)
    value = total / ((len(xList) - 1) * xStd * yStd)
    return value
#plotting graph
fig = plt.figure()
ax  = fig.add_axes([0,0,2,2])

z = np.polyfit(mags, depths, 1)
p = np.poly1d(z)
plt.plot(mags, p(mags),"r")

text = "correlation = {0:.5f}".format(correlation(mags, depths))
plt.figtext(1, -0.5, text, ha="center", fontsize=18)

ax.scatter(mags, depths, color='b')
ax.set_xlabel('Magnitudes', size=18)
ax.set_ylabel('Depths', size=18)
ax.set_title('USGS Earthquake Data: Correlation of Magnitude vs Depth', size=20)
plt.figure(figsize=(2,2), dpi=400)
plt.show()
