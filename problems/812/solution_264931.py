def retira_pontuacao(frase):
    '''
    Funçao que dada uma frase, a retorna com todos os caracteres de
    pontuaçao substituidos por espaço
    str -> str
    '''
    str.replace(frase,'-',' ')
    str.replace(frase,',',' ')
    str.replace(frase,':',' ')
    str.replace(frase,';',' ')
    str.replace(frase,'.',' ')
    return frase