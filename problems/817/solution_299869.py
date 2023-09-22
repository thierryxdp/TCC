def maiores(lista, n):
    maiores_numeros = list()
    for c in lista:
        if c >= n:
            maiores_numeros.append(c)
            
    return sorted(maiores_numeros)

def acima_da_media(notas):
        type(notas)==list
        media=sum(notas)//len(notas)
        return maiores(notas,media)