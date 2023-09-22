def acima_da_media(lista):
    '''Faça uma função que dada uma lista com as notas dos alunos de uma 
    turma, retorne a média da turma e uma lista ordenada com as notas que 
    ficaram acima da média.'''
    #int > int
    media = sum(lista)/len(lista)
    if media in lista:
        lista.sort()
        indice = lista.index(media)
        return lista[indice+1:]   
    if media not in lista:
        lista.append(media)
        lista.sort()
        indice = lista.index(media)
        return lista[indice+1:]