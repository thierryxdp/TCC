def lingua_p(palavra):
    str.lower(palavra)
    palavra_nova = ''
    for i in palavra:
        if i in 'aeiou':
            palavra_nova = palavra_nova + i + 'p' + i
        if i not in 'aeiou':
            palavra_nova = palavra_nova + i
    return palavra_nova