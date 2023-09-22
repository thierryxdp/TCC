def lingua_p(palavra):
    """retorna a palavra em português na linguagem do p
    str->str"""
    
    vogal = 'aeiouáéíóú'
    
    palavra = palavra.lower()
    
    palavra_p = ''
    
    for l in palavra:
        if l in vogal:
            palavra_p = palavra_p+l+'p'+l
    	else:
            palavra_p = palavra_p+l
	return palavra_p