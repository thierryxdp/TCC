def lingua_p(palavra):
    """Função que recebe uma palavra em português e a transforma para 'língua P', onde após cada vogal há a letra p. O retorno terá todas as letras minúsculas
    str -> str """

    palavra = palavra.lower()
    nova_palavra_lista = []

    for letra in palavra:
        if letra in "aeiouáéíóúàèìòùâêîôûãõu":
            nova_palavra_lista.append(letra + 'p' + letra)

        else:
            nova_palavra_lista.append(letra)


    nova_palavra = str.join("", nova_palavra_lista)
    

    return nova_palavra