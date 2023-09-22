def lingua_p(palavra: str) -> str:
    """Essa função, dada uma palavra como parâmetro de entrada,
    é traduzida para a língua do p. A língua do P consiste em inserir,
    após cada vogal, a letra p + a vogal original """
    i = 0
    palavra = list(palavra.lower())
    for letra in palavra:
        if letra in "aãâáàeêéiíoóôõuú":
            letra_p ='p'+ letra
            palavra[i] = letra +'p'+ letra
    	i += 1
    palavra = "".join(palavra)
    return palavra