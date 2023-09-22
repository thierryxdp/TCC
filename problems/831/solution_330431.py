def lingua_p(palavra):
    """
    Recebe uma palavra e retorna essa mesma palavra na língua do P,
    onde após cada vogal, insere-se a letra p e repete-se a vogal;
    str -> str
    """
    final = ''
    if 'a' in palavra:
        final = palavra.replace('a','apa')
    elif 'e' in palavra:
        final = palavra.replace('e','epe')
    elif 'i' in palavra:
        final = palavra.replace('i','ipi')
    elif 'o' in palavra:
        final = palavra.replace('o','opo')
    elif 'u' in palavra:
        final = palavra.replace('u','upu')
 	return final