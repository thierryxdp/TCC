def uppCons(frase):
    """Função recebe uma frase e retorna a frase com todas as suas consoantes em maiúsculas
       Parametro: str -> str"""
    nova_frase = ''
    for letra in frase:
        if letra in 'bcdfghjklmnpqrstvxzç':
            letra = str.upper(letra)
        nova_frase = nova_frase + letra
    return nova_frase