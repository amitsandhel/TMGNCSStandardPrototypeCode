#centroidRegion

import csv 

class CentroidRegion():
    def __init__(self, name, ncstart, ncend):
        self.name = name
        self.ncstart = ncstart
        self.ncend = ncend
        self.listx = []


def changeCentroiZone():
    dataList = []
    dataList.append({"nc16": CentroidRegion("city_of_toronto", 1, 1000), "nc22": CentroidRegion("city_of_toronto", 1000, 1999) })
    dataList.append({"nc16": CentroidRegion("durhamRegion", 1001, 2000), "nc22":CentroidRegion("durhamRegion", 2000, 2999)})
    dataList.append({"nc16": CentroidRegion("york_region", 2001, 3000), "nc22":CentroidRegion("york_region", 3000,3999)})
    dataList.append({"nc16": CentroidRegion("peel_Region", 3001, 4000), "nc22":CentroidRegion("peel_Region",4000, 4999)})

    for item in dataList:
        cent16List = list(range(item["nc16"].ncend, item["nc16"].ncstart-1, -1)) 
        cent22List = list(range(item["nc22"].ncend, item["nc22"].ncstart-1, -1))
        region = {}
        for x in cent16List:
            #get the index value
            ind = cent16List.index(x)
            region[x] = cent22List[ind]
        #update the dictionary and add the dict to it 
        item["nc16"].listx.append(region)

    # print the first elemnt in the list the dictionary
    print (dataList[0]["nc16"].name, dataList[0]["nc16"].listx)
    print("Done ran successfully!")

def main():
    changeCentroiZone()

if __name__ == "__main__":
    main()
