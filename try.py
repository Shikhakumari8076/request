x=[1,7,9,3,6]
i=0
min=x[0]
while i<len(x):
    j=0
    min2=0
    while j<len(x):
        if x[i][j]<min:
            min=min2
            min=x[i]
        elif x[i][j]<min2:
            min2=x[i]
    i=i+1
print(min2)


