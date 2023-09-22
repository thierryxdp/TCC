def conta_numero(numero,matriz):
'retorna quantas vezes um numero dado o parametro aparece na matriz;list--int'
i=0
contator=0
while i<len(matriz):
    if matriz[i][j]==numero:
        contator+=1
    j+=1
i+=1
return contador