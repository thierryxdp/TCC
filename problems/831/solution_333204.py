def lingua_p(palavra):
    for letra in palavra:
        if letra == 'a':
            palavra = str.replace(palavra, 'a', 'pa',1)
        elif letra == 'e':
            palavra = str.replace(palavra, 'e', 'pe',1)
        elif letra == 'i':
            palavra = str.replace(palavra, 'i', 'pi',1)
        elif letra == 'o':
            palavra = str.replace(palavra, 'o', 'po',1)
        elif letra == 'u':
            palavra = str.replace(palavra, 'u', 'pu',1)
    palavra = str.lower(palavra)
    return palavra