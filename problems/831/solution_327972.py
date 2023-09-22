def lingua_p(frase):
    result = ''
    for i, letra in enumerate(frase):
        result += letra
        if i < len(frase) - 1 and letra == frase[i + 1]:
            result += 'x'
    return result