def retira_pontuacao(frase):
    '''função que, a partir de uma frase, retira a pontuação da mesma, retornando um outra frase sem pontuação; str -> str'''
    
    if '-' or ',' or ':' or ';' or '.' in frase:
        frase1 = str.replace(frase,'-', ' ')
        frase2 = str.replace(frase1,',', ' ')
        frase3 = str.replace(frase2,':', ' ')
        frase4 = str.replace(frase3,';', ' ')
        frase5 = str.replace(frase4,'.', ' ')
        frase6 = str.replace(frase5,'!', ' ')
        frase7 = str.replace(frase6,'?', ' ')
        return frase6