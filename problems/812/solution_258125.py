def retira_pontuacao(frase):
    """retorna frase onde os caracteres de pontuação são substituidos por espaços.
    str->str"""
    '.'= str.replace((frase),'.','')
    '!'= str.replace((frase),'!','')
    '?'= str.replace((frase),'?','')
    '...'= str.replace((frase),'...','')
    '-'= str.replace((frase),'-','')
    ','= str.replace((frase),',','')
    ':'= str.replace((frase),':','')
    ';'= str.replace((frase),'.','')