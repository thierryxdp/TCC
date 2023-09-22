def lingua_p(palavra):
    lista=palavra.split()
    i=0
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            lista[i]=letra[i]+'p'+letra[i]
        i+=1
        
    for x in lista:
        resultado += x.lower()
        
    return resultado