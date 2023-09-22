import math
def acima_da_media(notas):
    """A função recebe uma lista com as notas dos alunos e 
	retorna as notas que ficaram acima da média;
    list -> list"""
    newlist = notas
    media = (int(sum(newlist)/len(notas)))+1
    list.append(newlist, media)
    list.sort(newlist)
    nposition = list.index(newlist, media)
    return newlist[nposition+1:]