def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
    import re 
    return re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', frase.decode('utf-8'))