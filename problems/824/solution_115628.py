def uppCons(frase):
    """Função que retorna todas as consoantes de uma frase, em maiuscula"""
    """str -> str"""
    i = 0
    novaFrase = ''
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxywzç':
            novaFrase += frase[i].upper()
        else:
            novaFrase += frase[i]
        i = i + 1
    return novaFrase