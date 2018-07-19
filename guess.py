
import random

start = input ('please input the start value: ')
end = input ('please input the end value: ')
start = int(start)
end = int(end)


n = random.randint(start, end)
i = 0
while True:
    i += 1
    number = input ('please input the number: ')
    number = int(number)
    if number == n:
    	print ('You are right')
    	print ('一共猜了', i, '次')  # break前要印出
    	break
    elif number > n: 
    	print ('bigger than the answer')
    elif number < n: 
    	print ('smaller than the answer')
    print ('一共猜了', i, '次')