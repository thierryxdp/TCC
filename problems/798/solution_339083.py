def freq_palavras(frase):
    """
    	Recebe uma frase e retorna um dicionário
        em que a chave do dícionário é cada palavra contida
        na frase e o valor é quantas vezes essa palavra se repete
        na frase.
        str --> dict
    """
    listaDePalavras = str.split(frase, " ")
    palavrasQuantidade = {}
    for palavra in listaDePalavras:
        palavrasQuantidade[palavra] = list.count(listaDePalavras, palavra)
    return palavrasQuantidade