def retira_pontuacao(frase):
    '''retorna a frase onde todos os caracteres de ointuação são substituídos por 
    espaço.
    str -> str'''
    
    if ',' in frase:
        if '?' in frase:
        	return str.replace(frase,'?',' ')
        return str.replace(frase,',',' ')
	if '?' in frase:
        return str.replace(frase,'?',' ')
    elif '!' in frase:
        return str.replace(frase,'!',' ')
    elif ':' in frase:
        return str.replace(frase,':',' ')
    elif ';' in frase:
        return str.replace(frase,';',' ')
    elif '.' in frase:
        return str.replace(frase,'.',' ')
    elif '-' in frase:
        return str.replace(frase,'-',' ')