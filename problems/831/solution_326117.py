def lingua_p(palavra: str) -> str:
    """Função que irá receber uma palavra em português e retornará essa mesma palavra traduzida para a língua do P. Para fazer essa tradução após cada vogal deve ser a inserida a letra p e a vogal original. Não deve haver distinção entre minúsculas e maiúsculas e toda a palavra deve ser retornada em minúscula.
        str -> str

        Parameters:
        palavra: palavra em português que deve ser traduzida para o língua do P
        
        Returns:
        palavra traduzida para a língua do P
    """

    palavra = str.lower(palavra)
    for letra in palavra:
        if letra in "aeiou":
            palavra = palavra + letra + "p" + letra
        else:
            palavra = palavra + letra