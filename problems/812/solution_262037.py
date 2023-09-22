def retira_pontuacao(frase):
    '''dada uma frase, retorna com os caracteres
    '-' ',' ':' ';' '.' trocados por espaço.
    str -> str'''
    
    	frase == str.replace(frase, '-', ' ')
    		str.replace(frase, ',', ' ')
    		str.replace(frase, ':', ' ')
    		str.replace(frase, ';', ' ')
    		str.replace(frase, '.', ' ')
            
 		return frase