def lingua_p(palavra):
    result = ''
    for i, letra in enumerate(palavra):
        result += letra
        if i < len(palavra) - 1 and letra == palavra[i + 1]:
            result += 'p'
    return result