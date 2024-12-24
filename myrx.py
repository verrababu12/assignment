numbers=list(map(int,input().split()))

squares_list=[]
for i in numbers:
    squares=i**2
    squares_list.append(squares)
print(sorted(squares_list))    
