def filtraMultiplos(lista,n):

   """
   lista,int--->lista
   A função diz que enquanto a variavel i(posição do valor dentro da
   lista de entrada) for menor que o tamanho da lista, haverá a prova
   se o resto do numero da lista dividido pelo que foi dado na entrada
   é 0. Caso seja, soma-se 1 ao i(proxima posição da lista) e adiciona
   esse valor a nova lista. Caso não seja, apenas se vai para a proxima
   posicao da lista
   
   """
    
    
    i=0
    
    novalista=[]
    
    while i<len(lista):
        if lista[i]%n==0:
            x=lista[i]
            novalista.append(x)
            i += 1
        
        else:
            i += 1
    
    return novalista