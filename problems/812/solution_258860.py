import re
def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase onde todos os caracteres de
    pontuação sejam substituídos por espaço;
    string->string"""
    x=re.split('[- , : ; . ! ?]',frase)
    z=string.join(' ',x)
    return z