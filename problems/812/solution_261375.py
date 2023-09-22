def retira_pontuacao (frase):
    '''
    	essa função recebe uma frase e retorna a mesma sem nenhuma pontuanção, substituindo-as
        por espaço 
        str-> str
    '''
    if '-' or ',' or ':' or ';' or '.' or '?' or '!' in frase:
        frase = str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,'-', ' '),',', ' '),':', ' '),';', ' '),'.', ' '),'!', ' '),'?', ' ')
    return frase