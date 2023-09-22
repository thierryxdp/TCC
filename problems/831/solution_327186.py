def lingua_p (frase: str) ->str:
    """Retorna uma versão de frase, minúscula, onde toda vogal 'x' precede
    'xp' nesta nova frase. Exemplo: (Camael -> capamapaepel)."""
    frase=str.lower(frase)
    frase_auxiliar = ''
    for letra in frase:
        if letra not in "bcdfghjklmnpqrtsvxwyz":
            frase_auxiliar+= letra + "p" + letra
        else:
            frase_auxiliar+=letra
    return frase_auxiliar