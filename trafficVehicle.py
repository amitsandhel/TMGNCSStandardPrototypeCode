#TransitVehicle

import  csv

#change the transit vehcile

class TransitVehicle():
    def __init__(self, desc, code, mode, seat_cap, total_cap, auto_equi):
        self.description = desc  
        self.code = code
        self.mode = mode
        self.seat_cap = seat_cap
        self.total_cap = total_cap
        self.auto_equi = auto_equi
    
    def __get__(self):
        return self.description, self.code, self.mode, self.seat_cap, self.total_cap, self.auto_equi


def changeTransitVehicle():
    # QUESTION: CAN WE USE ZERO AS A PLACEHOLDER FOR SEAT AND TOTAL CAPACITY
    # IF THERE IS NO NEED TO SPECIFY VALUES
    mylist = []
    mylist.append({"nc16":TransitVehicle("GO Train (12-car)", "GoTrain12", "r", 1900, 1900, None), 
                    "nc22":TransitVehicle("GO Train (12-car)", "GoTrain12", "r", 1900, 2400, None) })
    
    mylist.append({"nc16":TransitVehicle("GO Train (10-car)", "GoTrain10", "r", 1600, 1600, None), 
                    "nc22":TransitVehicle("GO Train (10-car)", "GoTrain10", "r", 1600, 1760, None)})  
    
    mylist.append({"nc16":TransitVehicle("Subway (6-car, Rocket)", "Sub6carRkt", "m", 400, 1100, None), 
                    "nc22":TransitVehicle("Subway (6-car, Rocket)", "Sub6carRkt", "m", 400, 1160, None)})
    
    mylist.append({"nc16":TransitVehicle("Subway (6-car, T1)", "Sub6carT1", "m", 400, 1000, None), 
                    "nc22":TransitVehicle("Subway (6-car, T1)", "Sub6carT1", "m", 400, 1000, None)})

    mylist.append({"nc16":TransitVehicle("ICTS train (SRT)", "SRT4car", "m", 120, 220, None), 
                    "nc22":TransitVehicle("ICTS train (SRT)", "SRT4car", "m", 260, 740, None)})
    
    mylist.append({"nc16":TransitVehicle("Subway (4-car, T1)", "Sub4carT1", "m", 260, 670, None), 
                    "nc22":TransitVehicle("Subway (4-car, T1)", "Sub4carT1", "m", 260, 670, None)})

    mylist.append({"nc16":TransitVehicle("UP Express", "UPX3car", "r", 173, 173, None), 
                    "nc22":TransitVehicle("UP Express", "UPX3car", "r", 173, 307, None)})

    mylist.append({"nc16":TransitVehicle("ION LRV", "", "", 0, 0, None), 
                    "nc22":TransitVehicle("ION LRV", "LRVion", "l", 56, 160, None)})

    for item in mylist:
        if item["nc16"].description != item["nc22"].description:
            item["nc16"].description = item["nc22"].description
            
        if item["nc16"].code != item["nc22"].code:
            item["nc16"].code = item["nc22"].code
        
        if item["nc16"].mode != item["nc22"].mode:
            item["nc16"].mode = item["nc22"].mode

        if item["nc16"].seat_cap != item["nc22"].seat_cap:
            item["nc16"].seat_cap = item["nc22"].seat_cap

        if item["nc16"].total_cap != item["nc22"].total_cap:
            item["nc16"].total_cap = item["nc22"].total_cap

        if item["nc16"].auto_equi != item["nc22"].auto_equi:
            item["nc16"].auto_equi = item["nc22"].auto_equi
            
        # print get values
        print ("nc16: ", item["nc16"].__get__()) 
        print ("nc22: " ,item["nc22"].__get__())


def main():
    changeTransitVehicle()

if __name__ == "__main__":
    main()
