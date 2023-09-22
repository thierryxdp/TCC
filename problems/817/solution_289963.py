def acima_da_media(notas):
    """ Função que dada uma lista com as notas dos alunos de uma turma, retorna uma lista com as notas que ficaram acima da média
    	list-> list
    """
    n_notas= notas[:]
    quant_notas = int(str.split(n_notas))
    media = sum(notas)/quant_notas
    
    return media