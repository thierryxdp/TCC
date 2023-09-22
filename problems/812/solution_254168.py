def retira_pontuacao(frase):
    '''função que, a partir de uma frase, retira a pontuação da mesma, retornando um outra frase sem pontuação; str -> str'''
    
    if '-' or ',' or ':' or ';' or '.' in frase:
        str.replace(frase,'-', ' ')
        str.replace(frase,',', ' ')
        str.replace(frase,':', ' ')
        str.replace(frase,';', ' ')
        str.replace(frase,'.', ' ')
        str.replace(frase,'!', ' ')
        return str.replace(frase,'-', ' ') str.replace(frase,',', ' ') str.replace(frase,':', ' ') str.replace(frase,';', ' ') str.replace(frase,'.', ' ') str.replace(frase,'!', ' ')