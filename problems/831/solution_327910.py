def lingua_p(palavra):
    """Função que irá receber uma palavra em português e retornará essa mesma palavra traduzida para a língua do P. Para fazer essa tradução após cada vogal deve ser a inserida a letra p e a vogal original. Não deve haver distinção entre minúsculas e maiúsculas e toda a palavra deve ser retornada em minúscula.
        str -> str"""

    palavra = str.lower(palavra)
    palavra_P =str.()
    for letra in palavra:
        if letra in "aeiouáéíóúâêîôûãõ":
            palavra_P = palavra_P + letra + 'p' + letra
		else:
            palavra_P = palavra_P + letra
    return palavra_P