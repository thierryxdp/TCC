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