def acima_da_media(l):
    '''
    Esta função recebe uma lista com notas de alunos de uma turma e retorna uma lista
    contendo as notas que ficaram acima da média da turma.
    
    Parametros
    ----------
    l (list) : lista
    '''
    m = sum(l)/len(l)
    l0 = []
    for i in range(len(l0)):
    	if l[i] > m:
            l0.append(l[i])
    return l0