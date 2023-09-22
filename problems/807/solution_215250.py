#2-
def conta_frases(frase):
    '''funcao q conta o numero de frases q aparecem no texto
    armazenado em uma string,levando em consideracao um ponto final,
    ponto de exclamacao,ponto de interrogacao, ou 
    tres pontos em sequencia'''
    '.' != '...'
    exclamacao = str.count(frase,'!',0)
    interrogacao = str.count(frase,'?',0)
    ponto = str.count(frase,'.',0)
    tres_pontos = str.count(frase,'...',0)
    return exclamacao+interrogacao+ponto+ -2* tres_pontos