def conta_frases(frase):
    """Funcao que dado um texto, o separa de acordo com '!','?' e "..." e retorna a quantidade de frases"""
    """Lembrar de perguntar na aula como retirar o 'bug'"""
    w=frase.replace('...','.')
    x=w.replace('.','!')
    y=x.replace('?','!')
    z=y.split('!')
    bug=len(z)
    resposta=bug-1
    return resposta