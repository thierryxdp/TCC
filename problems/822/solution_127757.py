def repetidos(lista):
    '''Retorna o número de repetições de um elemento na lista.'''
    
    lista=[]
    rep=0
    
    while k in range(0,len(lista)-1):
        if (lista[k]==lista[k+1])-1):
            rep+=1
            if(k==len(lista)-2):
                print(lista[k],',',rep+1)
                
        else:
            print(lista[k],',',rep+1)
            rep=0