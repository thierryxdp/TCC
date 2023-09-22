def posLetra(lista,l,n):
    i=0
    ocorrencia=0
    list2=[]
    
    while i<len(lista):
        if list.count(lista,l)<n:
            ocorrencia=-1
        else:
            while len(list2)<n:
                
                if lista[i]==l:
                    list2=list2+[l]
                    i=i+1
                    ocorrencia=cocorrencia+i
                 
    return ocorrencia