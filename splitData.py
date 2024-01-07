import json
import datetime;
import pandas as pd;
def split(filePath):
#    try:
        with open(filePath, 'r') as f:
            line = None;
            prevLine = None;
            dailyData = [];
            dailyPowerData = [];
            hourlyData = [];
            hourlyPowerData = dict();
            hourlyDiffData= dict();
            prevPowerEntry = None;
            powerProps = [
                "battery_charge_today",
                "battery_discharge_today",
                "battery_charge_total",
                "battery_discharge_total",
                "today_bought_from_grid",
                "today_sold_to_grid",
                "total_bought_from_grid",
                "total_sold_to_grid",
                "today_to_load",
                "total_to_load",
                "today_from_pv",
                "today_from_pv_s1",
                "today_from_pv_s2",
                "total_from_pv"
            ];
            prevDay = -1;
            day = -1;
            hour = -1;
            prevHour = -1;
            count = 0;
            jsonString = "";
            jsonSingle = None;
            prevJson = None;
            while True:
                prevLine = line; 
                line = f.readline();
                if not line:
                    break;
                if line == ",\n":
                    if prevLine !=  ",\n":
                        jsonPrev = jsonSingle;
                        try:
                            jsonSingle = json.loads(jsonString);
                            jsonString = "";
                            jsontimeString = jsonSingle["inverter_time"]["value"];
                            jsonTime = datetime.datetime.strptime(jsontimeString, "%Y-%m-%d %H:%M:%S");
                            day = jsonTime.day;
                            hour = jsonTime.hour;
                            if hour  != prevHour:
                                if prevHour != -1:
#                                    print(f"hour: {prevHour:02d} \n");
                                    hourlyData.append(jsonPrev);
                                    hourlyPowerEntry={};
                                    hourlyDiffEntry={};
#                                    hourlyPowerEntry["inverter_time"] = jsonPrev["inverter_time"]["value"];
                                    for powerProp in powerProps:
                                        hourlyPowerEntry[powerProp] = jsonPrev[powerProp]["value"];
                                        if (prevPowerEntry != None):
                                            hourlyDiffEntry[powerProp] = hourlyPowerEntry[powerProp];
                                            if (prevPowerEntry[powerProp]<=hourlyPowerEntry[powerProp]):
                                                hourlyDiffEntry[powerProp] -= prevPowerEntry[powerProp];
                                            hourlyDiffData[jsonPrev["inverter_time"]["value"]]=hourlyDiffEntry;
                                    prevPowerEntry = hourlyPowerEntry;
                                    hourlyPowerData[jsonPrev["inverter_time"]["value"]]=hourlyPowerEntry;
                                prevHour = hour;
                            if day  != prevDay:
                                if prevDay != -1:
                                    jsonPrevTimeString = jsonPrev["inverter_time"]["value"];
                                    jsonPrevTime = datetime.datetime.strptime(jsonPrevTimeString, "%Y-%m-%d %H:%M:%S");
                                    print(f"day: {jsonPrevTime.year}{jsonPrevTime.month:02d}{prevDay:02d} \n");
                                    dailyData.append(jsonPrev);
                                prevDay = day;                           
                        except Exception as e:
                            print("error parsing Json: " + str(e) + "\n<" +  jsonString + ">");
                            jsonString = "";                        
                else:                                
                    jsonString += line;                
                count +=1;
            print("linecount: " + str(count) +"\n");
            with open(f"hourly.json","w") as h:
                json.dump(hourlyData, h, indent=3);
                h.close();
            with open(f"hourlypower.json","w") as h:
                json.dump(hourlyPowerData, h, indent=3);
                h.close();
            with open("daily.json","w") as d:
                json.dump(dailyData, d, indent=3);
                d.close();
            df = pd.DataFrame.from_dict(hourlyPowerData,orient='index');
            df.to_csv("hourlypower.csv");
            diffDf = pd.DataFrame.from_dict(hourlyDiffData,orient='index');
            diffDf.to_csv("hourlyDiffPower.csv");

#    except Exception as e:
#        print("exc: " + str(e) +"\n");
#    finally:
#        print("koniec\n");
        
split("deyenew.json");
        
                
                
            
                