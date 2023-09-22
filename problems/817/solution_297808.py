def maiores(lista,n):
    nova_lista=lista+[n]
    list.sort(nova_lista)
    posicao=list.index(nova_lista,n)
    return nova_lista[posicao+1:]

def acima_da_media(nota_alunos):
    media=sum(nota_alunos)/len(nota_alunos)
    return maiores(nota_alunos,media)