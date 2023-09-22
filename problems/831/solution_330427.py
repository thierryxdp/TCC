def lingua_p(palavra):
    """
    Recebe uma palavra e retorna essa mesma palavra na língua do P,
    onde após cada vogal, insere-se a letra p e repete-se a vogal;
    str -> str
    """
    final = ''
    if 'a' in palavra:
        final = palavra.replace('a','apa')
        return str(final)
    elif 'e' in palavra:
        final = palavra.replace('e','epe')
        return str(final)
    elif 'i' in palavra:
        final = palavra.replace('i','ipi')
        return str(final)
    elif 'o' in palavra:
        final = palavra.replace('o','opo')
        return str(final)
    elif 'u' in palavra:
        final = palavra.replace('u','upu')
        return str(final)
    else:
        return "problema"