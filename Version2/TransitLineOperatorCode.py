#TransitLine

import csv 

class TransitLine():
    def __init__(self, name, tlCode):
        self.name = name
        self.tlCode = tlCode
        self.listx = []
    
    def __get__(self):
        return self.name, self.tlCode


def readFile():
    with open("transit_line_operator.csv", mode="r") as tranist_op_codes:
        transit_op_file = csv.reader(tranist_op_codes)
        next(transit_op_file)
        print (transit_op_file)
        for item in transit_op_file:
            if item[1] == item[2]:
                pass
            else: 
                print ('they are differnt')
                # here change system


def changeTransitLine():
    dataList = []
    dataList.append({"nc16": TransitLine("Brampton", "PB"), 
                    "nc22": TransitLine("Brampton", "B") })
    dataList.append({"nc16": TransitLine("GO Bus", "G"), 
                    "nc22": TransitLine("GO Bus", "GB") })
    dataList.append({"nc16": TransitLine("GO Rail", "G0"), 
                    "nc22": TransitLine("GO Rail", "GT") })
    dataList.append({"nc16": TransitLine("Grand River Transit", ""), 
                    "nc22": TransitLine("Grand River Transit", "K") })
    dataList.append({"nc16": TransitLine("Link Train at Pearson Intl’ Airport", ""), 
                    "nc22": TransitLine("Link Train at Pearson Intl’ Airport", "LNK") })
    dataList.append({"nc16": TransitLine("Mississauga", "PM"), 
                    "nc22": TransitLine("Mississauga", "M") })

    for item in dataList:
        if item["nc16"].name != item["nc22"].name:
            item["nc16"].name = item["nc22"].name
        if item["nc16"].tlCode != item["nc22"].tlCode:
            item["nc16"].tlCode = item["nc22"].tlCode
        

            # print get values
        print ("nc16: ", item["nc16"].__get__()) 
        print ("nc22: " ,item["nc22"].__get__())

    print("Done ran successfully!")


def main():
    readFile()

if __name__ == "__main__":
    main()

