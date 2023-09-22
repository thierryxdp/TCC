def lingua_p(palavra):
    lista= palavra.split(' ')
    i=0
    resultado=''
    for letra in lista:
        if letra in 'AEIOUaeiou':
            lista[i]+= [letra+'p'+letra]
        resultado += lista[i].lower()
        i+=1
        
    return resultado