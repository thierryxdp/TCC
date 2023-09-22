def acima_da_media(notas):
    '''função que dada uma lista com notas de alunos, retorna a lista de notas ordenada e com as notas que ficaram acima da media    ent-> lista   saida-> lista '''
    
	notas_validas = [nota for nota in notas if nota > 5]
    return notas_validas