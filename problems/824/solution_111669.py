def uppCons(frase):
    """Função que recebe uma frase e retorna todas as consoantes maiúsculas."""
    """String -> String"""
    i = 0
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            frase[i].upper()
        i = i + 1
    return frase