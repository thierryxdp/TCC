def repetidos(lista):
    ''''''
i=0
cont=0
for i in range(0,len(lista)-1):
     if(lista[i]!=lista[i]):
        cont=+1
        i=+1
         return cont