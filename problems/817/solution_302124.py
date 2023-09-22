from math import ceil

def acima_da_media(notas):
    '''função que dada uma lista de notas de um aluno calcula a sua média
    e retorna as notas que estão acima da média
    list->list'''
    
  
    media_lista = list()
    media = sum(notas)/len(notas)
    for n in notas:
        if n>media:
            media_lista.append(n)
    media_lista.sort()
    return media_lista