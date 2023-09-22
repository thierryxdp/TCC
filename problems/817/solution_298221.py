def acima_da_media(notas):
    '''função que retorna as notas dos alunos que conseguiram ficar acima da média; str => str'''
    soma = sum(notas)
    Ni = len(notas)
    media = (soma//Ni)
    list.append(notas,media)
    list.sort(notas)
    list.reverse(notas)
    i = list.index(notas,media)
    listagem = notas[0:i]
    list.sort(listagem)
    return listagem