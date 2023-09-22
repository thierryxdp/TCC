def acima_da_media(lista):
    
    '''A função retornará as notas dos alunos que obtiveram grau superior a média
    da turma.
    
    dados de entrada -> lista
    dados de saída -. lista'''
    
    Q = len(lista)
    Soma = sum(lista)
    Media = Soma/Q
    Maiores = maiores(lista,Media)
	
    if Media in Maiores:
        return Maiores
    
    else:
	return Maiores