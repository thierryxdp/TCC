def retira_pontuacao(funcao):
    """função que retorna a frase onde todos os caracteres de pontuação(incluindo travassão,vígula,dois pontos,ponto e vírgula além da pontuação de encerramento de frase)tenham sido substituídos por espaço"""
    if '-' in funcao:
        funcao=str.replace (funcao,'-',' ')
    if ',' in funcao:
        funcao=str.replace (funcao,',','')
    if ':' in funcao:
        funcao=str.replace (funcao,':',' ')
    if ';' in funcao:
        funcao=str.replace (funcao,';','')
    if '.' in funcao:
        funcao=str.replace (funcao,'.','')
    if '?' in funcao:
        funcao=str.replace (funcao,'?','')
    if '!' in funcao:
        funcao=str.replace (funcao,'!','')
    return funcao


 def inverte(funcao):
    """ função que retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa,sem letras maiúsculas, e sem pontuação str->str"""
    funcao = str.lower(funcao)
    funcao = retira_pontuacao(funcao)
    funcao = str.split(funcao,' ')
    list.reverse(funcao)
    funcao = str.join(' ',funcao)
    
    return funcao