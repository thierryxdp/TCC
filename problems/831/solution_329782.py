def lingua_p(palavra):
    '''funcao que recebe uma palavra em 
    portugues e retorna a mesma na lingua do 
    p 
    entrada: string
    saida: string
    '''
    indice= 0
    lista= list(palavra)
    while indice<len(lista):
        if lista[indice] in 'aeiou':
            px= 'p' + lista[indice]
            list.insert(lista, (indice+1), px)
        indice= indice + 1
    
    return ''.join(lista)