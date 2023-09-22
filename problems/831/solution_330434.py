def lingua_p(palavra):
    """
    Recebe uma palavra e retorna essa mesma palavra na língua do P,
    onde após cada vogal, insere-se a letra p e repete-se a vogal;
    str -> str
    """
    final = ''
    for vogal in palavra:
        final = palavra.replace('a','apa')
        final = palavra.replace('e','epe')
        final = palavra.replace('i','ipi')
        final = palavra.replace('o','opo')
        final = palavra.replace('u','upu')
        return final