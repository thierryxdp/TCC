def acima_da_media(notas):
    '''funcao que dada uma lista com notas de alunos da turma retorne as notas dos alunos acima da media'''
    ''' list -> list '''
    lista = []
    media = sum(notas) / len(notas)
    
    for elemento in notas:
        if elemento > media:
            lista.append(elemento)
    lista.sort()
    return lista