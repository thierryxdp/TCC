def maiores(lista,n):
    l=list.append(lista,n)
    l1=list.sort(lista)
    l2=list.index(lista,n)
    l3=lista[l2:]
    return l3
def acima_da_media(lis_aluno):
    quant_aluno=len(lis_aluno)
    soma_nota=sum(lis_aluno)
    media=soma_nota/quant_aluno
    l3=maiores(lis_aluno,media)
    lista=list.remove(l3,media)
    return l3