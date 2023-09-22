def retira_pontuacao(funcao):
    """função que retorna a frase onde todos os caracteres de pontuação(incluindo travassão,vígula,dois pontos,ponto e vírgula além da pontuação de encerramento de frase)tenham sido substituídos por espaço"""
    if '-' in funcao:
        funcao=str.replace (funcao,'-',' ')
    if ',' in funcao:
        funcao=str.replace (funcao,',',' ')
    if ':' in funcao:
        funcao=str.replace (funcao,':',' ')
    if ';' in funcao:
        funcao=str.replace (funcao,';',' ')
    if '.' in funcao:
        funcao=str.replace (funcao,'.',' ')
    if '?' in funcao:
        funcao=str.replace (funcao,'?',' ')
    if '!' in funcao:
        funcao=str.replace (funcao,'!',' ')
    return funcao


def inverte(f):
    """ função que retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas, e sem pontuação."""
    funcao=str.lower(f)
    funcao=retira_pontuacao(f)
    funcao=str.split(f,' ')
    list.reverse(f)
    funcao=str.join(' ',f)
    return f