def acima_da_media(notas):
    """ Dada uma lista com as notas dos alunos, vamos retornar quais estão acima da media, e
        retornaremos.
        Entrada --> list
        Saida   --> list   """
    soma = sum(notas)
    media = sum(notas)/len(notas)
    if media in notas:
        list.sort(notas)
        a = list.index(notas,media)
        return notas[a+1:]
    else:
        notas.append(media)
        list.sort(notas)
        b = list.index(notas,media)
        return notas[b+1:]



""" TESTE:
Resposta esperada:
1 - [10,9,8.5,4.7,3.2,6.5] --> [8.5, 9, 10]

Resposta obtida:
1 - >>> acima_da_media([10,9,8.5,4.7,3.2,6.5])
    [8.5, 9, 10]
"""