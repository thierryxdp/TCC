def acima_da_media (nota):
    """função que dada uma lista com as notas dos alunos de uma turma retorne uma lista com os que ficaram acima da media"""
    
    soma=sum(nota)
    ni=len(nota)
    media=(soma//ni)
    list.append(nota,media)
    list.sort(nota)
    list.reverse(nota)
    i=list.index(nota,media)
    lista=nota[0:i]
    list.sort(lista)
    return list