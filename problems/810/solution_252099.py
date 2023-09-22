def retira_pontuacao(f):
    """dada uma frase retira todos os caracteres de pontuacao e troca por espacos str->str"""
    if '-' in f:
        f=str.replace(f,'-',' ')
    if ',' in f:
        f=str.replace(f,',',' ')
    if ':' in f:
        f=str.replace(f,':',' ')
    if ';' in f:
        f=str.replace(f,';',' ')
    if '.' in f:
        f=str.replace(f,'.',' ')
    if '?' in f:
        f=str.replace(f,'?',' ')
    if '!' in f:
        f=str.replace(f,'!',' ')
    return f
    
    
def inverte(f):
    """dada uma frase, retorna outra frase que contenha as mesmas palavras da anterior na ordem
inversa, em letras maiusculas, e sem a pontuacao. str->str"""
    a=str.lower(f)
    b=retira_pontuacao(a)
    c=str.split(b,' ')
    f=list.reverse(c)
    return f