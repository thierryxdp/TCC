def lingua_p(palavra):
    final = ''
    for letra in str.lower(palavra):
        final = final + letra
        if letra in ['a', 'á', 'â', 'ã', 'e', 'é', 'ê', 'i', 'í',
                     'o', 'ó', 'ô', 'õ', 'u', 'ú', 'û']:
            final = final + 'p' + letra
    return final