def conta_frases(x):
    '''Dado um texto armazenado em string, retorna o número de frases que aparecem no texto.
    str -> int'''
	resposta=()
    ponto=(len(str.split(x,'.',4)))-1
    exclamacao=(len(str.split(x,'!')))-1
    interrogacao=(len(str.split(x,'?')))-1
    reticencias=(len(str.split(x,'...')))-1
    return ponto+exclamacao+interrogacao+reticencias