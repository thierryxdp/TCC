def lingua_p(palavra):
    """
    Recebe uma palavra e retorna essa mesma palavra na língua do P,
    onde após cada vogal, insere-se a letra p e repete-se a vogal;
    str -> str
    """
    palavra = palavra.replace('a','apa')
    palavra = palavra.replace('e','epe')
    palavra = palavra.replace('i','ipi')
    palavra = palavra.replace('o','opo')
    palavra = palavra.replace('u','upu')
    return palavra