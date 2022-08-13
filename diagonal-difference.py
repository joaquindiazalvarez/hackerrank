def diagonalDifference(arr):
    sum_diag1 = 0 
    sum_diag2 = 0
    #for recorre fila
    for i in range(len(arr)):    
    #for recorre columnas    
        for j in range(len(arr[i])):
            if j == i:
                sum_diag1 += arr[i][j]
                #print("diag1", arr[i][j])
            if i + j == len(arr) - 1:
                sum_diag2 += arr[i][j]
                #print("diag2", arr[i][j])
    dif = sum_diag1 - sum_diag2
    if dif < 0:
        return -(dif)
    else:  
        return dif
print(diagonalDifference([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]))