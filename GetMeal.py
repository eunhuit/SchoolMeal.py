import json
from unittest import result
import requests

global KEY
KEY = "API 키" # 키가 없으면 실행하지 못합니다.

# 학교정보 불러오기
def get_school(School_Name):
    # 정보 요청
    url = f"https://open.neis.go.kr/hub/schoolInfo"
    params = {
        "KEY": KEY,
        "Type": "json",
        "SCHUL_NM": School_Name
    }
    req = requests.post(url, params=params)

    # 정보 처리
    j = json.loads(req.text)

    # 정보가 존재 할때
    try:
        Area_Code = j["schoolInfo"][1]["row"][0]["ATPT_OFCDC_SC_CODE"]
        School_Code = j["schoolInfo"][1]["row"][0]["SD_SCHUL_CODE"]

        return Area_Code, School_Code
    
    # 정보가 존재하지 않을때
    except:
        #print(j["RESULT"]["MESSAGE"])
        result = j["RESULT"]["MESSAGE"] 
        return result
        
# 학교정보 불러오기
def get_meal(ATPT_OFCDC_SC_CODE, SD_SCHUL_CODE, MLSV_YMD):
    # 정보 요청
    url = f"https://open.neis.go.kr/hub/mealServiceDietInfo"
    params = {
        "KEY": KEY,
        "Type": "json",
        "ATPT_OFCDC_SC_CODE": ATPT_OFCDC_SC_CODE,
        "SD_SCHUL_CODE": SD_SCHUL_CODE,
        "MLSV_YMD": MLSV_YMD
    }
    req = requests.post(url, params=params)

    # 정보 처리
    j = json.loads(req.text)

    # 정보가 존재 할때
    try:
        ham2 = j["mealServiceDietInfo"][0]["head"][0]["list_total_count"]
        #print(ham2)

        #result = meal.replace("<br/>","\n")
        #print(meal)

    # 정보가 존재하지 않을때
    except:
        #print(j["RESULT"]["MESSAGE"])
        result = j["RESULT"]["MESSAGE"]
        return result
    
    if ham2 == 1:
        try:
            lunch = j["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            meal = (f"---------중식---------\n{lunch}")
            result = meal.replace("<br/>","\n")
            return result
        except:
            print(j["RESULT"]["MESSAGE"])
    
    if ham2 == 2:
        try:    
            breakfast = lunch = j["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            lunch = j["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"]
            meal = (f"---------조식---------\n{breakfast}\n---------중식---------\n{lunch}")
            result = meal.replace("<br/>","\n")
            return result
        except:
            print(j["RESULT"]["MESSAGE"])

    
    if ham2 == 3:
        try:
            breakfast = j["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
            lunch = j["mealServiceDietInfo"][1]["row"][1]["DDISH_NM"]
            dinner = j["mealServiceDietInfo"][1]["row"][2]["DDISH_NM"]
            meal = (f"---------조식---------\n{breakfast}\n---------중식---------\n{lunch}\n---------석식---------\n{dinner}")
            result = meal.replace("<br/>","\n")
            return result
        except:
            print(j["RESULT"]["MESSAGE"])
