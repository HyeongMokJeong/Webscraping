import requests
res = requests.get("http://google.com")
res.raise_for_status() #문제 발생시 즉시 종료

# print("응답 코드: ", res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다.")
# else:
#     print("문제가 발생했습니다. [에러코드 ", res.status_code,']')

print(len(res.text))
open("mygoogle.html", 'w', encoding="utf-8")