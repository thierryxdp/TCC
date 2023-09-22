def maiores(lista,n):
    '''Função que dada uma lista de numeros inteiros
    e um numero inteiro n, retorna outra lista que
    contenha todos os numeros da lista original 
    maiores que n, ordenados em ordem crescente
    '''
    lista.insert(0,n)
    lista.sort()
    del lista[0:(lista.index(n)+1)]
    
    return lista


def acima_da_media(listanotas):
    
    tamanho=len(listanotas)
    soma=sum(listanotas)
    media=(soma)/(tamanho)
    
    if soma!=media:
        return maiores(listanotas,media)
    
    if soma=media:
        media+=0.5
        return maiores(listanotas,media)