import GetMeal
from datetime import datetime, timedelta

now = datetime.now()
yes = now - timedelta(days=1)
tom = now + timedelta(days=1)

date_mapping = {
    "오늘": now.strftime('%m%d'),
    "내일": tom.strftime('%m%d'),
    "어제": yes.strftime('%m%d'),
}

school = input("-----학교를 입력해주세요:")
schoolname = school
Area_Code, School_Code = GetMeal.get_school(schoolname)

date_input = input("-----원하는 날짜를 입력해주세요 Ex) 10/04 :")
date = date_mapping.get(date_input, date_input).replace('/', '')

date = str(now.year) + date
Area_Code, School_Code = Area_Code, School_Code

result = GetMeal.get_meal(Area_Code, School_Code, date)
print(result)
