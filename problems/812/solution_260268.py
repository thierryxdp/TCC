def retira_pontuacao(string):
    """retorna uma frase string de entrada, se os caracteres
    de pontuacao"""
    s=string.replace('.','')
    s=s.replace('!','')
    s=s.replace('?','')
    s=s.replace(',','')
    s=s.replace(';','')
    s=s.replace(':','')
    s=s.replace('-','')
    return s