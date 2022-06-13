#centroidRegion

import csv 

class CentroidRegion():
    def __init__(self, name, ncstart, ncend):
        self.name = name
        self.ncstart = ncstart
        self.ncend = ncend
        self.listx = []


def readDataFile():
    """
    function to read the data file
    """
    old_and_new_centroid_dict = {}
    with open("zone_centriods.csv", mode="r") as region_centroid:
        old_ncs_list = []
        new_ncs_list = []
        region_centroid_file = csv.reader(region_centroid)
        next(region_centroid_file)
        for region in region_centroid_file:
            print (region)
            #extract each of the four values from the list
            old_ncs_centroid_starts = int(region[1])
            old_ncs_centroid_ends = int(region[2])
            new_ncs_centroid_starts = int(region[3])
            new_ncs_centroid_ends = int(region[4])
            #print (old_ncs_centroid_ends)
            old_ncs_centroid_range = range(old_ncs_centroid_starts, old_ncs_centroid_ends)
            new_ncs_centroid_range  =  range(new_ncs_centroid_starts, new_ncs_centroid_ends)
            # list of old ncs 16 centroids
            for centroid in old_ncs_centroid_range:
                old_ncs_list.append(centroid)
            # list of new centroids nc22
            for centroid in new_ncs_centroid_range:
                new_ncs_list.append(centroid)
            for old_centroid_number in old_ncs_list:
                # find each number in the old ncs list
                # get the index value
                old_centroid = old_ncs_list.index(old_centroid_number)
                # get a dictionary of the old and new centroids 
                old_and_new_centroid_dict[old_centroid_number] = new_ncs_list[old_centroid]
                #print (old_and_new_centroid_dict)
            #open the second csv files
            with open("zone_centriods_map.csv", mode = 'r') as station_centroid:
                station_centroid_file = csv.reader(station_centroid)
                next(station_centroid_file)
                for centroid in station_centroid_file:
                    #print (centroid)
                    old_ncs_station_centroid = int(centroid[2])
                    new_ncs_station_centroid = int(centroid[3])
                    print (new_ncs_station_centroid, old_ncs_station_centroid)
                    if int(old_ncs_station_centroid) <= 0  or int(new_ncs_station_centroid) <= 0:
                        continue
                    old_ncs_list.append(old_ncs_station_centroid)
                    new_ncs_list.append(new_ncs_station_centroid)
        print (old_and_new_centroid_dict)
        return old_and_new_centroid_dict


def update_old_zone_centroids_number():
    
                

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
    #changeCentroiZone()
    readDataFile()

if __name__ == "__main__":
    main()
