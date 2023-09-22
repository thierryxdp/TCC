def maiores(lista,n):
    '''funcao que dada uma lista e um numero n retorna outra lista com todos os numeros maiores que n'''
    nova=[]
    lista.append(n)
    lista.sort()
    indice=lista.index(n)
    nova=lista[indice+1:]
    return nova

def acima_da_media(lista):
    '''funcao que dada uma lista de notas de alunos retorna as notas que ficaram acima da media. list -> list'''
    media= sum(lista)/len(lista)
    return maiores(lista,media)