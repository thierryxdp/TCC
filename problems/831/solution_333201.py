def lingua_p(palavra):
    for letra in palavra:
        if letra == 'a':
            palavra = str.replace(palavra, 'a', 'apa',1)
        elif letra == 'e':
            palavra = str.replace(palavra, 'e', 'epe',1)
        elif letra == 'i':
            palavra = str.replace(palavra, 'i', 'ipi',1)
        elif letra == 'o':
            palavra = str.replace(palavra, 'o', 'opo',1)
        elif letra == 'u':
            palavra = str.replace(palavra, 'u', 'upu',1)
    palavra = str.lower(palavra)
    return palavra