import os

def readFromFile(file):
    current_directory = os.path.abspath(os.path.join(__file__ ,"../.."))

    data = {}
    first_row = True 

    with open(newline="",file=current_directory + "/Files/" + file, mode="r") as f:
        for row in f:

            if first_row==True:
                first_row=False
                continue

            footballerData = row.rstrip().split(", ")
            key = footballerData[0]  

            if key not in data:
                data[key] = []  


            values = footballerData[1:] 
            data[key].extend(values)

    return data  


def readFootballPlayerData(file,name):
     current_directory = os.path.abspath(os.path.join(__file__ ,"../.."))
     print(current_directory)
     with open(newline="",file=current_directory + "/Files/" + file, mode="r") as f:
        for row in f:
            current_row=row.strip().split(", ")
            if current_row[0]==name:
                print(f"{name} => {current_row}")
                return current_row

        return []