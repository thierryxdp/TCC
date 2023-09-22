def retira_pontuacao(text):
    '''retorna uma string retirando seus caracteres de pontuação
    str -> str'''
    text = str.replace(text,'!',' ')
    text = str.replace(text,'-','')
    text = str.replace(text,'?','')
    text = str.replace(text,'...',' ')
    text = str.replace(text,',',' ')
    text = str.replace(text,':','')
    text = str.replace(text,';','')
    text = str.replace(text,'.','')
    return text