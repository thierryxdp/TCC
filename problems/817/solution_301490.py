def maiores(lista,n):
    lista.insert(0,n)
    lista.sort()
    del lista[0:(lista.index(n)+1)]

    return lista

def acima_da_media(listanotas):
    
 

    tamanho = len(listanotas)
    soma = sum(listanotas)
    media = (soma)/(tamanho)
    
    return maiores(listanotas media)