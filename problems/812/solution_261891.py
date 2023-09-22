def retira_pontuacao(frase):
    '''função que recebe uma frase e retorna uma frase onde todos os caracteres de pontuação foram substituídos por espaço.
    entrada: string 
    saída: string'''
    
    return str.strip(frase, '!' or '.' or '?' or '...' or '/' or ';' or ':' or ',')