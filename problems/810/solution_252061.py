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
        inversa, esm letras maiusculas, e sem a pontuacao. str->str"""
        f=str.lower(f)
        f=retira_pontuacao(f)
        
        return f