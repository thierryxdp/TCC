def maiores(lista2,n):
    l= lista2
    a= [b for b in l if b > n]
    x=a.sort()
    return a
def acima_da_media(lista):
    '''função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista
    ordenada com as notas que ficaram acima da média:
    str -> str'''
    media = sum(lista)/len(lista)
    return maiores(lista,media)