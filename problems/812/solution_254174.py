def retira_pontuacao(frase):
    '''função que, a partir de uma frase, retira a pontuação da mesma, retornando um outra frase sem pontuação; str -> str'''
    
    if '-' or ',' or ':' or ';' or '.' or '?' in frase:
        frase_pura = str.replace(frase,'-', ' '),',', ' '),':', ' '),';', ' '),'.', ' '),'!', ' '),'?', ' ')
     
        return frase_pura