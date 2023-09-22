def lingua_p(palavra: str)-> str:
    """Dada uma palavra, a função retorna esta mesma palavra traduzida para
    a língua P, ou seja, após cada vogal da palavra original, é inserida
    a letra p mais a vogal original. Ex: então = epentãpãopo.
    Obs: a resposta deve ignorar a diferença entre minúsculas e maiúsculas e
    retornar a palavra traduzida toda em minúsculas"""
    palavraP = list()
    for letra in palavra:
        if (str.lower(letra) in "aeiouáàâãéêíóôõú"):
            list.append(palavraP, letra + "p" + letra)
        else:
            list.append(palavraP, letra)
    return "".join(palavraP)