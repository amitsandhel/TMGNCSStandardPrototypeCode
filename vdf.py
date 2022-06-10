#VDF
import csv 

class VDF():
    def __init__(self, subclass, lane_capacity):
        #self.name = name # the mmain class name can be addded in later if nneeded be seems additional data that is not needed
        self.subclass = subclass
        self.lane_capacity = lane_capacity
    
    def __get__(self):
        return self.subclass, self.lane_capacity

def changeVDF():
    dataList = []
    dataList.append({"nc16": VDF("Freeway", 1800), 
                    "nc22": VDF("Freeway", 2000)})
    dataList.append({"nc16": VDF("Expressway", 1800), 
                    "nc22": VDF("Expressway", 2000) })
    dataList.append({"nc16": VDF("Toll highway", 1800), 
                    "nc22": VDF("Toll highway", 2000) })
    dataList.append({"nc16": VDF("Freeway/expressway HOV", 1800), 
                    "nc22": VDF("Freeway/expressway HOV", 2000) })

    for item in dataList:
        if item["nc16"].lane_capacity != item["nc22"].lane_capacity:
            item["nc16"].lane_capacity = item["nc22"].lane_capacity
        

            # print get values
        print ("nc16: ", item["nc16"].__get__()) 
        print ("nc22: " ,item["nc22"].__get__())

    print("Done ran successfully!")


def main():
    changeVDF()

if __name__ == "__main__":
    main()

