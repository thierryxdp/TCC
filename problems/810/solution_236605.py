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

def inverte(frase):
    '''Função que inverte a ordem das palavras na frase inserida como argumento.
    Também remove as possíveis pontuações da frase. Entrada: str. Saída: str.'''
    frase= retira_pontuacao(frase)
    frase=str.lower(frase)
    lista=str.split(frase)
    return str.join(' ',lista[::-1])