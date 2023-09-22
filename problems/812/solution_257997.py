def retira_pontuacao(frase):
    '''retorna a frase onde todos os caracteres de ointuação são substituídos por 
    espaço.
    str -> str'''
    
    if ',' in frase:
        return str.replace(frase,',',' ')
	elif '?' in frase:
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
   elif ',' and '.' in frase:
        return str.replace(frase,',' and'.',' ')