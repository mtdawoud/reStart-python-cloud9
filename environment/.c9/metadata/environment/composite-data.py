{"filter":false,"title":"composite-data.py","tooltip":"/composite-data.py","ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":5,"column":24},"end":{"row":5,"column":24},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"f1bd1007db47cc475e15ca86a7943b0a97342871","mime":"text/x-script.python","undoManager":{"mark":14,"position":14,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":2},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":3}],[{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["c"],"id":4},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["s"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["v"]}],[{"start":{"row":0,"column":10},"end":{"row":1,"column":0},"action":"insert","lines":["",""],"id":5},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"insert","lines":["i"]},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"insert","lines":["m"]},{"start":{"row":1,"column":2},"end":{"row":1,"column":3},"action":"insert","lines":["p"]},{"start":{"row":1,"column":3},"end":{"row":1,"column":4},"action":"insert","lines":["o"]},{"start":{"row":1,"column":4},"end":{"row":1,"column":5},"action":"insert","lines":["r"]},{"start":{"row":1,"column":5},"end":{"row":1,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":1,"column":6},"end":{"row":1,"column":7},"action":"insert","lines":[" "],"id":6},{"start":{"row":1,"column":7},"end":{"row":1,"column":8},"action":"insert","lines":["c"]},{"start":{"row":1,"column":8},"end":{"row":1,"column":9},"action":"insert","lines":["o"]},{"start":{"row":1,"column":9},"end":{"row":1,"column":10},"action":"insert","lines":["p"]},{"start":{"row":1,"column":10},"end":{"row":1,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":1,"column":11},"end":{"row":2,"column":0},"action":"insert","lines":["",""],"id":7},{"start":{"row":2,"column":0},"end":{"row":3,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":13,"column":0},"action":"insert","lines":["myVehicle = {","    \"vin\" : \"<empty>\",","    \"make\" : \"<empty>\" ,","    \"model\" : \"<empty>\" ,","    \"year\" : 0,","    \"range\" : 0,","    \"topSpeed\" : 0,","    \"zeroSixty\" : 0.0,","    \"mileage\" : 0","}",""],"id":8}],[{"start":{"row":13,"column":0},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":14,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["for key, value in myVehicle.items():","    print(\"{} : {}\".format(key,value))",""],"id":10}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":11}],[{"start":{"row":17,"column":0},"end":{"row":18,"column":0},"action":"insert","lines":["myInventoryList = []",""],"id":12}],[{"start":{"row":18,"column":0},"end":{"row":19,"column":0},"action":"insert","lines":["",""],"id":13}],[{"start":{"row":19,"column":0},"end":{"row":40,"column":0},"action":"insert","lines":["with open('car_fleet.csv') as csvFile:","    csvReader = csv.reader(csvFile, delimiter=',')  ","    lineCount = 0  ","    for row in csvReader:","        if lineCount == 0:","            print(f'Column names are: {\", \".join(row)}')  ","            lineCount += 1  ","        else:  ","            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  ","            currentVehicle = copy.deepcopy(myVehicle)  ","            currentVehicle[\"vin\"] = row[0]  ","            currentVehicle[\"make\"] = row[1]  ","            currentVehicle[\"model\"] = row[2]  ","            currentVehicle[\"year\"] = row[3]  ","            currentVehicle[\"range\"] = row[4]  ","            currentVehicle[\"topSpeed\"] = row[5]  ","            currentVehicle[\"zeroSixty\"] = row[6]  ","            currentVehicle[\"mileage\"] = row[7]  ","            myInventoryList.append(currentVehicle)  ","            lineCount += 1  ","    print(f'Processed {lineCount} lines.')",""],"id":14}],[{"start":{"row":40,"column":0},"end":{"row":41,"column":0},"action":"insert","lines":["",""],"id":15}],[{"start":{"row":41,"column":0},"end":{"row":45,"column":0},"action":"insert","lines":["for myCarProperties in myInventoryList:","    for key, value in myCarProperties.items():","        print(\"{} : {}\".format(key,value))","        print(\"-----\")",""],"id":16}]]},"timestamp":1670237316377}