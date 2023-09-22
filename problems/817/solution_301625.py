def acima_da_media(nota):
    """ Função que dada uma lista com as notas do alunos,
    retorna uma lista ordenada com as notas que ficaram
    acima da média
    Entrada:list
    Saída: list """
    soma = sum(nota)
    ni=len(nota)
    media=(soma//ni)
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
    return lista