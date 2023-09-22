def acima_da_media(list):
    '''
    Função onde dada uma lista com as notas dos alunos de uma turma, retorna uma
    lista ordenada com as notas que ficaram acima da média
    '''
	list = list.split(",")

    s = sum(list)
    l = len(list)
    m = float(s/l)
    return(m)