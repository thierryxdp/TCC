def lingua_p(palavra):
    """função que recebe uma palavra e retorna a mesma traduzida para a lingua do P, inserindo o p após uma vogal e mais a vogal original
	str -> str"""
    
    palavra = list(palavra.lower())
    vogais = 'ãaáéeiíouú'
    i = 0
    
    for f in palavra:
        if f in vogais:
            conca = 'p' + f 
            palavra.insert(palavra.index(f,i)+1, conca)
		i += 1
	
    juntar = ''.join(palavra)
    
    return juntar