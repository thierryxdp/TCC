def retira_pontuacao(frase):
    '''retorna uma frase onde todos os caracteres de pontuação são substituídos por
    	espaço.
        str -> str'''
    
    if '!' and or ':' and or '-' and or ',' and or ';' and or '.' and or '?'in 'frase':
        return str.replace(frase, "'!' and or ':' and or '-' 
                and or ',' and or ';' and or '.' and or '?'", " ")