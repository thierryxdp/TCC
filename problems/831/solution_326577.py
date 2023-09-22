def lingua_p(palavra):
    """Função que recebe uma palavra como parametro e retorna esta mesma palavra
    traduzida para ligua do P
    str -> str"""
    palavra1 = ''
    
    for i in palavra:
        if i in 'AEIOUaeiou':
            palavra1 = palavra1 + i + 'p' + i
		else:
            palavra1 = palavra1 + i
	return palavra1