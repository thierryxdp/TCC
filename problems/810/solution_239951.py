import re
def retira_pontuacao(frase):
    """Dada uma frase, retorna a frase onde todos os caracteres de
    pontuação sejam substituídos por espaço;
    string->string"""
    x=re.split('[- , : ; . ! ?]',frase)
    z=str.join(' ',x)
    return z
def inverte(frase):
    """Dada uma frase, retorna outra frase que contenha as mesmas palavras da frase,
    porém na ordem inversa, sem letras maiúsculas e pontuação;
    string->string"""
    frase=retira_pontuacao(frase)
    frase=str.lower(frase)
    x=str.split(frase)
    x=x[::-1]
    return str.join(' ',x)