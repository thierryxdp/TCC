def retira_pontuacao(frase):
    """Dada uma frase.Retorna a frase sem pontuações.
    str->str"""
    x=frase
    if '-' in x:
        x=str.replace(x,'-',' ')
    if ',' in x:
        x=str.replace(x,',',' ')
    if ':' in x:
        x=str.replace(x,':',' ')
    if ';' in x:
        x=str.replace(x,';',' ')
    if '.' in x:
        x=str.replace(x,'.',' ')
    if '?' in x:
        x=str.replace(x,'?',' ')
    if '!' in x:
        x=str.replace(x,'!',' ')
    if '...' in x:
        x=str.replace(x,'...',' ')
    return x

def inverte(frase):
    """Dada uma frase, retorna a frase, sem pontuações, sem letras maiúsculas e em ordem inversa.
    str->str"""
    x=retira_pontuacao(frase)
    y=str.lower(x)
    z=str.split(y)
    w=z[::-1]
    v=str.join(" ",w)
    return v