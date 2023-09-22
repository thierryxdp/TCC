def maiores(lista,n):
    nova_lista=lista+[n]
    list.sort(nova_lista)
    posicao=list.index(nova_lista,n)
    return nova_lista[posicao+1:]

def acima_da_media(nota_alunos):
    media=sum(nota_alunos)/len(nota_alunos)
    nova_lista=maiores(nota_alunos,media)
    if media in nota_alunos:
        list.remove(nova_lista,media)
        return nova_lista
    else: return maiores(nota_alunos,media)