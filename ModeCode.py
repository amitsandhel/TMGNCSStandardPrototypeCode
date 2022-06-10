#ModeCode
import csv 

class ModeCode():
    def __init__(self, desc, code):
        self.desc = desc #description but it never changed 
        #self.type = name #the type this field never changed as well commentd out 
        self.code = code
    
    def __get__(self):
        return self.desc, self.code

def changeModeCode():
    dataList = []
    dataList.append({"nc16": ModeCode("Light truck toll road", ""), 
                    "nc22": ModeCode("Light truck toll road", "D")})
    dataList.append({"nc16": ModeCode("Medium truck toll road", ""), 
                    "nc22": ModeCode("Medium truck toll road", "E") })
    dataList.append({"nc16": ModeCode("Heavy truck toll road", ""), 
                    "nc22": ModeCode("Heavy truck toll road", "F") })
    dataList.append({"nc16": ModeCode("E-bicycles", ""), 
                    "nc22": ModeCode("E-bicycles", "E") })
    dataList.append({"nc16": ModeCode("E-scooters", ""), 
                    "nc22": ModeCode("E-scooters", "N") })

    for item in dataList:
        if item["nc16"].code != item["nc22"].code:
            item["nc16"].code = item["nc22"].code
        

            # print get values
        print ("nc16: ", item["nc16"].__get__()) 
        print ("nc22: " ,item["nc22"].__get__())

    print("Done ran successfully!")


def main():
    changeModeCode()

if __name__ == "__main__":
    main()

