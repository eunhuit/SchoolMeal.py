import GetMeal
from datetime import datetime

now = datetime.now() #현재날짜와 시간을 불러오는 함수

school = input("-----학교를 입력해주세요:") 

schoolname = school #학교이름은 입력받은 학교이름을 작성
Area_Code, School_Code = GetMeal.get_school(schoolname) #GetMeal.py에 get_school함수에 지정된 변수값을 넣고 쿼리

date = input("-----원하는 날짜를 입력해주세요 Ex) 10/04 :")

date = date.replace('/', '') #날짜사이에 / 제거
date = str(now.year) + date #현재 년도를 날짜앞에 추가
Area_Code = Area_Code 
School_Code = School_Code

result = GetMeal.get_meal(Area_Code, School_Code, date) #GetMeal.py에 get_meal함수에 변수값을 넣고 쿼리

print(result) #반횐된 출력값 출력