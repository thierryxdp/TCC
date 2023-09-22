def lingua_p(palavra):
    limite = len(palavra)
    for letra in range(1,limite):
        if palavra[letra] == 'a':
            palavra = str.replace(palavra, 'a', 'apa')
        elif palavra[letra] == 'e':
            palavra = str.replace(palavra, 'e', 'epe')
        elif palavra[letra] == 'i':
            palavra = str.replace(palavra, 'i', 'ipi')
        elif palavra[letra] == 'o':
            palavra = str.replace(palavra, 'o', 'opo')
        elif palavra[letra] == 'u':
            palavra = str.replace(palavra, 'u', 'upu')
    palavra = str.lower(palavra)
    return palavra