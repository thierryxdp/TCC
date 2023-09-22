def uppCons(frase):
    """Função que recebe uma frase e retorna todas as consoantes maiúsculas."""
    """String -> String"""
    i = 0
    nova_frase = ""
    while i < len(frase):
        if frase[i] not in 'AEIOUaeiou':
            nova_frase = nova_frase + frase[i].upper()
        i = i + 1
    return nova_frase