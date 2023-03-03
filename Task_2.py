array=[[2,2,6],[3,7,2],[5,6,2],[2,9,4],[2,2,9],[3,2,9],[2,5,9]]
maxima=True
points=[]

for i in range(len(array)):
    maxima=True
    for j in range(len(array)):
        if i!=j and array[i][0]<=array[j][0] and array[i][1]<=array[j][1] and array[i][2]<=array[j][2]:
            maxima=False
            break
    if maxima==True:
        points.append(array[i])
print(points)
        
