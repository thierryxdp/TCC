def lingua_p(palavra):
    lista= palavra.split(' ')
    i=0
    for letra in palavra:
        if letra in 'AEIOUaeiou':
            lista[i]=lista[i]+'p'+lista[i]
        i+=1
        
    for x in lista:
        resultado += x.lower()
        
    return resultado