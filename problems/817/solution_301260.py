def acima_da_media(x):
    '''
    Função onde dada uma lista com as notas dos alunos de uma turma, retorna uma
    lista ordenada com as notas que ficaram acima da média
    '''
	x = x.split(",")

    s = sum(x)
    l = len(x)
    m = float(s/l)
    return(m)