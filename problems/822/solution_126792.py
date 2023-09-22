def repetidos(lista:list)->int:
    x=0#contador
    y=0#occorrido
    while x<len(lista):#loop
        if(lista[x]==lista[x-1]):#teste de repetição
           y+=1
    	x+=1
    return y