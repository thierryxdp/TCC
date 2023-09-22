def lingua_p(palavra):
    lista= palavra.split(' ')
    i=0
    resultado=''
    for letra in lista:
        if letra in 'AEIOUaeiou':
            lista[i]=lista[i]+'p'+lista[i]
        i+=1
        resultado += letra.lower()
        
    return resultado