def acima_da_media(notas):
    '''função que dada uma lista com notas de alunos, retorna a lista de notas ordenada e com as notas que ficaram acima da media    ent-> lista   saida-> lista '''
    
	soma_das_notas = sum(notas)
    qtd_de_notas = len(notas)
    media = soma_das_notas/qtd_de_notas
    
    
    notas_validas = [nota for nota in notas if nota > media]
    list.sort(notas_validas)
    return notas_validas