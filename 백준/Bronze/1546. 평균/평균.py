count=int(input())
score=list(map(int, input().split(" ")))
i=0
sum=0
M=max(score)

for i in range(0, count):
      if(score[i])<=100:
            score[i]=score[i]/M*100
            sum=sum+score[i]
if(sum>0):
      average=sum/count
      print(average)