def maiores(lista,n):
    l=list.append(lista,n)
    l1=list.sort(lista)
    l2=list.index(lista,n)
    l3=lista[l2+1:]
    return l3
def acima_da_media(lis_aluno):
    media=sum(lis_aluno)/len(lis_aluno)
    lista=maiores(lis_aluno,media)
    lista1=list.remove(lista,media)
    return lista