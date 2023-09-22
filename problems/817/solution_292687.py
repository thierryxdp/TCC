'''Função que recebe uma lista com as notas de alunos de uma turma e retorne uma
nova lista ordenada com as notas que ficaram acima da média'''
'''list(floats) --> list(floats) '''
def acima_da_media(lista):
	media = sum(lista)/len(lista)
    x=[]
    for y in lista:
        if y > media:
            x.append(y)
    x.sort()
    return x