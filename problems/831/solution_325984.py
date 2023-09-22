def lingua_p(palavra):
    """Função que recebe uma palavra em português e retorna ela traduzida para a língua do P
       A tradução para a língua do P funciona de modo que após cada vogal da palavra é inserida a letra "p" somada com essa mesma vogal
       Retornar a palavra com apenas letras em minúsculas
       str -> str"""
    palavra = str.lower(palavra)
    novaPalavra = ()
    for letra in palavra:
        if letra in "aeiouáéíóúâêôãõã":
            letra = letra,"p",letra
            novaPalavra = novaPalavra+letra
        else:
            novaPalavra = novaPalavra + tuple(letra)
    lista = list(novaPalavra)
    return:"".join(novaPalavra)