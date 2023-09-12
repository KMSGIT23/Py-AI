import time

start=time.time() #시작 직전 시각을 기록
sum=0
for i in range(1, 100000001):
    sum=sum+i

end=time.time() #끝난 직후 시각을 기록

print("1+2+...+100000000=", sum)
print("소요 시간은", end-start, "초입니다.")
