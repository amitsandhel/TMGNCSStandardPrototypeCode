#here we will try a nested for loop
#then we will try a generator function to see if this speeds things up
# the genreator is not needed anymore since that may be more useful if and when we add files for now lets use the nested for loop and continue on 
# TodO: now is the time to add in all the remaining regions and then work on station and centroids


def test1():
    # save the data as a dictionary with the key being region name the list contains the ncs16 min and max range followed by 
    # ncs 22 min and max range in 
    data = {"city_of_toronto": [1, 1000, 1000, 1999],
            "durhamRegion": [1001, 2000, 2000, 2999],
            "york_region": [2001, 3000,  3000,3999],
            "peel_Region": [3001, 4000, 4000, 4999],
        }

    #iterate over the dictionary
    for region, value in data.items():
        print (region, value, value[0], value[1], value[2], value[3])
        #create a list of each type in reversed order
        cent16List = list(range(value[1], value[0]-1, -1))
        cent22List = list(range(value[3], value[2]-1, -1))
        print ('length of each  list ', len(cent16List), len(cent22List))
        #empty temporary dictionary to store the results

        region = {}
        # iterate over the ncs16 list and find the index of the number and then extract the same value from
        #ncs22 list
        for x in cent16List:
            # get the index value
            ind = cent16List.index(x)
            # update the dictionary 
            region[x] = cent22List[ind]
        #update the dictionary and add the dict to it 
        value.append(region)
        
    
    print (data["york_region"])
            
    #scenario.publish_network(network)
    print("Done ran successfully!")



def test3():
    # save the data as a dictionary with the key being region name the list contains the ncs16 min and max range followed by 
    # ncs 22 min and max range in 
    data = {"city_of_toronto": [1, 1000, 1000, 1999],
            "durhamRegion": [1001, 2000, 2000, 2999],
            "york_region": [2001, 3000,  3000,3999],
            "peel_Region": [3001, 4000, 4000, 4999],
        }
    #print (data)
    #print (data.keys())

    for region, value in data.items():
        print (region, value, value[0], value[1], value[2], value[3])
        # cent16List = list(reversed(range(value[1], value[0]+1))) #list(range(value[0], value[1], -1))
        # cent22List = list(reversed(range(value[3], value[2]+1))) #list(range(value[2], value[3]-1, -1))
        
        cent16List = list(range(value[1], value[0]-1, -1))
        cent22List = list(range(value[3], value[2]-1, -1))

        
        print (cent16List)
        print () 
        print (cent22List)
        print ('length of each  list ', len(cent16List), len(cent22List))
        region = {}
        for x in cent16List:
            # get the index value
            ind = cent16List.index(x)
            # update the dictionary 
            region[x] = cent22List[ind]
        #update the dictionary and add the dict to it 
        value.append(region)
        
    print (data.keys())
    print (data["york_region"])
    print("Done ran successfully!")


class CentroidRegion():
    def __init__(self, name, nc16start, nc16end, nc22start, nc22end):
        self.name = name
        self.nc16start = nc16start
        self.nc16end = nc16end
        self.nc22start = nc22start
        self.nc22end = nc22end
        self.listx = []

def changeCentroiZone():
    dataList = []
    dataList.append(CentroidRegion("city_of_toronto", 1, 1000, 1000, 1999))
    dataList.append(CentroidRegion("durhamRegion", 1001, 2000, 2000, 2999))
    dataList.append(CentroidRegion("york_region", 2001, 3000,  3000,3999))
    dataList.append(CentroidRegion("peel_Region", 3001, 4000, 4000, 4999))

    for item in dataList:
        cent16List = list(range(item.nc16end, item.nc16start-1, -1)) 
        cent22List = list(range(item.nc22end, item.nc22start-1, -1))
        region = {}
        for x in cent16List:
            #get the index value
            ind = cent16List.index(x)
            region[x] = cent22List[ind]
        #update the dictionary and add the dict to it 
        item.listx.append(region)

    print (dataList[0].name, dataList[0].listx)
    print("Done ran successfully!")


class TransitVehicle():
    def __init__(self, year, desc, code, mode, seat_cap, total_cap, auto_equi):
        self.year = year
        self.description = desc  
        self.code = code
        self.mode = mode
        self.seat_cap = seat_cap
        self.total_cap = total_cap
        self.auto_equi = auto_equi
    
    def __get__(self):
        return self.year, self.description, self.code, self.mode, self.seat_cap, self.total_cap, self.auto_equi


def changeTransitVehicle():
    mylist = []
    mylist.append({"nc16":TransitVehicle(16, "GO Train (12-car)", "GoTrain12", "r", 1900, 1900, None), "nc22":TransitVehicle(22, "GO Train (12-car)", "GoTrain12", "r", 1900, 2400, None) })
    mylist.append({"nc16":TransitVehicle(16, "GO Train (10-car)", "GoTrain10", "r", 1600, 1600, None), "nc22":TransitVehicle(22, "GO Train (10-car)", "GoTrain10", "r", 1600, 1760, None)})

    for item in mylist:
        if item["nc16"].year != item["nc22"].year:
             item["nc16"].year
        print (item["nc16"].year)
        #if item["nc16"] is not item["nc22"]
        #print (item["nc16"].__get__())
        #print (item["nc22"].__get__())


def main():
    #changeCentroiZone()
    changeTransitVehicle()

if __name__ == "__main__":
    main()


#change the transit vehcile

class TransitVehicle():
    def __init__(self, year, desc, code, mode, seat_cap, total_cap, auto_equi):
        self.year = year
        self.description = desc  
        self.code = code
        self.mode = mode
        self.seat_cap = seat_cap
        self.total_cap = total_cap
        self.auto_equi = auto_equi
    
    def __get__(self):
        return self.year, self.description, self.code, self.mode, self.seat_cap, self.total_cap, self.auto_equi


def changeTransitVehicle():
    mylist = []
    mylist.append({"nc16":TransitVehicle(16, "GO Train (12-car)", "GoTrain12", "r", 1900, 1900, None), "nc22":TransitVehicle(22, "GO Train (12-car)", "GoTrain12", "r", 1900, 2400, None) })
    mylist.append({"nc16":TransitVehicle(16, "GO Train (10-car)", "GoTrain10", "r", 1600, 1600, None), "nc22":TransitVehicle(22, "GO Train (10-car)", "GoTrain10", "r", 1600, 1760, None)})

    for item in mylist:
        if item["nc16"].seat_cap != item["nc22"].seat_cap:
            item["nc16"].seat_cap = item["nc22"].seat_cap
            
        if item["nc16"].total_cap != item["nc22"].total_cap:
            print('they are differnt')
            item["nc16"].total_cap = item["nc22"].total_cap
            
        print(item["nc16"].total_cap)
            
            
        #print (item["nc16"].__get__())
        #print (item["nc22"].__get__())

        
changeTransitVehicle()




# r 1 GoTrain10
# r 2 GoTrain12
# m 3 SRT4car
# m 4 Sub4carT1
# m 5 Sub6carT1
# m 6 Sub6carRkt
# l 7 LRV
# s 8 CLRV16
# s 9 ALRV23
# s 10 LFLRV30
# b 11 Bus9
# b 12 Bus12
# b 13 Deluxe12
# b 14 Deluxe18
# b 15 Bus18
# q 16 BRT
# g 17 GoBus
# g 18 DblDeckBus
# r 19 UPX3car
# done
# # how to use the transit vehicle
# description
# GO Train (12-car) 
# ncs16
# GoTrain12 
# r 
# 1900 1900 
# ncs22
# GoTrain12 
# r 
# 1900 2400 -----
