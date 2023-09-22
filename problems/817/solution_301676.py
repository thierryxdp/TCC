def acima_da_media(lista_numeros):
    '''função que dada uma lista com as notas dos alunos de uma turma, retorne uma lista ordenada com as notas que ficaram acima da média;
       list -> list'''
    f1=sum(lista_numeros)/len(lista_numeros)
    if f1 not in lista_numeros:
        f2= lista_numeros+[f1]
        list.sort(f2)
        a=list.index(f2, f1)
        return f2[a+1:]
    if f1 in lista_numeros:
        f2= lista_numeros
        list.sort(f2)
        a=list.index(f2, f1)
        return f2[a+1:]