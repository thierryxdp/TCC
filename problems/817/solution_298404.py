def insere(lista,n):
    list.append(lista,n)
    list.sort(lista)
    return lista

def maiores(lista,n):
    if n in lista:
        list.sort(lista)
        indice=list.index(lista,n)
        return lista[indice+1:]
    else:
        insere(lista,n)
        indice=list.index(lista,n)
        return lista[indice + 1:]
    
def acima_da_media(notas):
    num_alunos=len(notas)
    media=int(sum(notas)/num_alunos)
    lista= maiores(notas,media)
    return lista