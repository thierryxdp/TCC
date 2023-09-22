def lingua_p(palavra):
    for letra in len(palavra):
        if letra == 'a':
            palavra = str.replace(palavra, 'a', 'apa')
        elif letra == 'e':
            palavra = str.replace(palavra, 'e', 'epe')
        elif letra == 'i':
            palavra = str.replace(palavra, 'i', 'ipi')
        elif letra == 'o':
            palavra = str.replace(palavra, 'o', 'opo')
        elif letra == 'u':
            palavra = str.replace(palavra, 'u', 'upu')
    palavra = str.lower(palavra)
    return palavra