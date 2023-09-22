def lingua_p(palavra):
    a = str.lower(palavra)
    for x in range(len(palavra)):
        if 'a' or 'e' or 'i' or 'o' or 'u' in palavra:
            str.replace(palavra, 'a', 'apa')
            str.replace(palavra, 'e', 'epe')
            str.replace(palavra, 'i', 'ipi')
            str.replace(palavra, 'o', 'opo')
            str.replace(palavra, 'u', 'upu')
            return palavra