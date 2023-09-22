def hashtag(s):
    '''Escreva um texto entre "". O Retorno sera o texto com um # no inicio,
    no meio e no fim do texto.
    
    #parametros | in: str (texto que recebera os #) -> out: str (texto de retorno)'''
    
	metade=len(s)//2
	return "#"+s[:metade]+"#"+s[metade:]+"#"