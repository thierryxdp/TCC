def freq_palavras(frase):
    """
    	Recebe uma frase e retorna um dicionário
        em que a chave do dícionário é cada palavra contida
        na frase e o valor é quantas vezes essa palavra se repete
        na frase.
        str --> dict
    """
    dic = {}
    listaDePalavras = str.split(frase, " ")
    list.sort(particao)
    for elemento in particao:
        count = str.count(frase, elemento)
        dic[str(elemento)] = count
    return dic