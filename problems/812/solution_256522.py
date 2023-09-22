def retira_pontuacao(f):
    '''Função que retorna a frase (f) em que os caracteres de pontuação (',',-,:,;,!,?,. e
    '...') são substituidos por espaços ' '. Entrada: str. Saída: str'''
    f=str.replace(f,'...',' ')
    f=str.replace(f,'?',' ')
    f=str.replace(f,'.',' ')
    f=str.replace(f,'-',' ')
    f=str.replace(f,',',' ')
    f=str.replace(f,';',' ')
    f=str.replace(f,':',' ')
    f=str.replace(f,'!',' ')
    
    return f