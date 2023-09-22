def acima_da_media(notas):
    '''Funcao que, dada a lista com as notas dos alunos, retorne uma lista ordenada das notas acima da media.list,int->list'''
    soma = sum(notas)
    med = sum(notas)/len(notas)
    if med in notas:
        list.sort(notas)
        x = list.index(notas,med)
        return notas[x+1:]
    else:
        notas.append(med)
        list.sort(notas)
        y = list.index(notas,med)
        return notas[y+1:]