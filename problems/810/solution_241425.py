def inverte(frase):
    """Recebe uma frase e retorna o contrario da composição das frases.
    str -> str"""
    
    
    def retira_pontuacao(frase):
    	"""Recebe uma string e retira a pontuação dessa.
    	string -> string"""
        
    	corrigida = frase.replace('-', ' ').lower
    	corrigida = corrigida.replace(',', ' ')
    	corrigida = corrigida.replace(':')
    	corrigida = corrigida.replace(';')
    	corrigida = corrigida.replace('.')
    	corrigida = corrigida.replace('...')
    	corrigida = corrigida.replace('!')
    	corrigida = corrigida.replace('?')
        
    	return corrigida
    txt = retira_pontuacao(frase)
    separado = reversed(txt.split())
    return ' '.join(separado)