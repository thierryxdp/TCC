def maiores(lista,n):
    l=list.append(lista,n)
    l1=list.sort(lista)
    l2=list.index(lista,n)
    l3=lista[l2+2:]
    return l3
def acima_da_media(lis_aluno):
    quant_aluno=len(lis_aluno)
    soma_nota=sum(lis_aluno)
    media=int(soma_nota/quant_aluno)
    return maiores(lis_aluno,media)