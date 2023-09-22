def lingua_p(palavra):
    """ Função que dada uma palavra em português, traduz e retorna a palavra para
        a língua do P ( após cada vogal da palavra original é inserido a letra P
        mais a vogal original."""

    vogais = "aeiouãâáéêíîõóôûú"
    palavra = str.lower(palavra)
    palavraModificada = ""

    for p in range(len(palavra)):

        if palavra[p] in vogais:

            novo = palavra[p]+ "p" + palavra[p]

            palavraModificada = palavraModificada + novo
            
        else:
            
            palavraModificada = palavraModificada + palavra[p]

    return palavraModificada