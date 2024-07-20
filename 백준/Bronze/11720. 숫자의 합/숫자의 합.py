count=int(input())
number=str(input())
i=0
sum=0
if(count>=1 and count<=100):
    for i in range(0, count):
          sum=sum+int(number[i])
    print(sum)