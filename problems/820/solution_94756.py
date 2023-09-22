def posLetra(frase,l,n):
    i=0
    lista=[]
    
    if frase.count(l)<n:
        return -1
   
    while i<len(frase):
        if frase[i]==l:
                lista=lista+[i]
        i=i+1
    ocorrencia=lista[n-1]
                 
    return ocorrencia