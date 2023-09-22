def lingua_p(palavra):
    for letra in palavra:
        if letra == 'a':
            palavra = str.replace(palavra, 'a', 'apa',2)
        elif letra == 'e':
            palavra = str.replace(palavra, 'e', 'epe',2)
        elif letra == 'i':
            palavra = str.replace(palavra, 'i', 'ipi',2)
        elif letra == 'o':
            palavra = str.replace(palavra, 'o', 'opo',2)
        elif letra == 'u':
            palavra = str.replace(palavra, 'u', 'upu',2)
    palavra = str.lower(palavra)
    return palavra