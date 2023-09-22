def uppCons(palavra):
    """Põe todas as consoantes de uma frase em maiusulo. str -> str"""
    i = 0
    while i < len(palavra):
        if palavra[i] in 'qwrtypsdfghjklçzxcvbnm':
            palavra = palavra.replace(palavra[i], palavra[i].upper())
        i = i + 1
    return palavra