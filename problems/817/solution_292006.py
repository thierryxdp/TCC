#str->list
def acima_da_media(lista):
    "Função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da da média."
    list.append(lista,n)
    list.sort(lista)
    posicao=list.index(lista,n)
    lista=lista[:posicao:-1]
    list.reverse(lista)
    soma_das_notas=sum(lista)
    qtd_de_notas = len(lista)
    media_das_notas = soma_das_notas / qtd_de_notas
    return lista