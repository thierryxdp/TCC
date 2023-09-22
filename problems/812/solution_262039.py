def retira_pontuacao(frase):
    '''dada uma frase, retorna com os caracteres
    '-' ',' ':' ';' '.' trocados por espaço.
    str -> str'''
    
    str.replace(frase, '-', ' ')
    str.replace(frase, ',', ' ')
    str.replace(frase, ':', ' ')
    str.replace(frase, ';', ' ')
    str.replace(frase, '.', ' ')
            
 		return frase