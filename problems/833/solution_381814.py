def conta_numero(numero, matriz):
x=0 
y=0 
count=0
while x<=len(matriz) and y<=len(matriz[x]):
    if numero == matrix[x][y]:
        count=count+1
    x=x+1
    y=y+1
return count