def retira_pontuacao(f):
    """função que retorna a frase onde todos os caracteres de pontuação(incluindo travassão,vígula,dois pontos,ponto e vírgula além da pontuação de encerramento de frase)tenham sido substituídos por espaço"""
    if '-' in f:
        f=str.replace (f,'-',' ')
    if ',' in f:
        f=str.replace (f,',','')
    if ':' in f:
        f=str.replace (f,':',' ')
    if ';' in f:
        f=str.replace (f,';','')
    if '.' in f:
        f=str.replace (f,'.','')
    if '?' in f:
        f=str.replace (f,'?','')
    if '!' in f:
        f=str.replace (f,'!','')
    return f


 def inverte(f):
    """ função que retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas, e sem pontuação str->str"""
    f=str.lower(f)
    f=retira_pontuacao(f)
    f=str.split(f,' ')
    list.reverse(f)
    f=str.join(' ',f)
    return f