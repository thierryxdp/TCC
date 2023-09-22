def uppCons(texto):
    """frase que retorna a frase com todas as consoantes
    em maiusculas"""
    passador = 0
    fraseFinal = ''
    while passador < len(texto):
        if texto[passador] not in 'AEIOUaeiou':
            fraseFinal += texto[passador]
        passador += 1
    return fraseFinal