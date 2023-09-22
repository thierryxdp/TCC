def acima_da_media (nota):
    '''funcao que dada uma lista com as notas dos alunos
    de uma turma, retorna uma outra lista ordenada com
    as noitas que ficaram acima da media'''
    '''int -> int'''
    soma = sum(nota)
    n = len(nota)
    media = (soma//n)
    list.append(nota,media)
    i = list.index(nota,media)
    lista = nota[0:i]
    list(nota)
    list.sort(lista)
    return lista