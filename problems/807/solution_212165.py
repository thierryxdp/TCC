def conta_frases(texto):
    """Função que recebe um texto e retorna o número de frases contidas neste texto;str->int"""
    pontof=str.count(texto,'.')
    reticencias=str.count(texto,'...')
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    if pontof>=1 and reticencias>=1:
        return (pontof-(reticencias*3))+reticencias+interrogacao+exclamacao
    elif pontof>=1 and reticencias==0:
        return pontof+interrogacao+exclamacao
    elif pontof==0 and reticencias>=1:
        return reticencias+interrogacao+exclamacao
    else:
        return interrogacao+exclamacao