def retira_pontuacao(frase):
    '''função que, a partir de uma frase, retira a pontuação da mesma, retornando um outra frase sem pontuação; str -> str'''
    
    if '-' or ',' or ':' or ';' or '.' in frase:
        str.replace(frase,'-', ' ') = frase1
        str.replace(frase1,',', ' ') = frase2
        str.replace(frase2,':', ' ') = frase3
        str.replace(frase3,';', ' ') = frase4
        str.replace(frase4,'.', ' ') = frase5 
        str.replace(frase5,'!', ' ') = frase6
        return frase6