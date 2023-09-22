def uppCons(frase):
    
    listaFrase=list(frase)
    tamanho=len(listaFrase) 
    lista=[]
    i=0
    while i < tamanho:
        if str.lower(listaFrase[i]) in "bcdfghjklmnpqrstvxywzç":
            lista.append(str.upper(listaFrase[i]))         
        else:
            lista.append(listaFrase[i])
        i+=1
    return str.join("",lista)