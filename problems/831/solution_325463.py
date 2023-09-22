def lingua_p(palavra):
    """Função para traduzir da língua portuguesa para a língua do P.
       Onde: "palavra" - é a palavra que será traduzida.
    str --> str """
    palavra = palavra.lower()
    lista = list(palavra)
    traducao = ''
    for i in lista:
        if i in 'aeiouáéíóúâêô':
            traducao += i + 'p' + i
        else:
            traducao += i
    return traducao