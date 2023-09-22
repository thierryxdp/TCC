'''Com base em uma lista de notas dos alunos, o programa
returna uma lista ordenada com todas as notas acima da media.
list -> list'''

def acima_da_media(notas):
    media = sum(notas)//len(notas)
    list.insert(notas, 0, media)
    list.sort(notas)
    list.reverse(notas)
    posicao = list.index(notas, media)
    lista = notas[:posicao][:]
    list.reverse(lista)
    return lista