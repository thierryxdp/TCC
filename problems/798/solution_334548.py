def freq_palavras(frases):
    """Funcao que tem uma string de entrada e retorna um dicionario,
    no qual cada palavra dessa string seja uma chave e tenha como
    valor o numero de vezes que a palavra aparece na frase;
    str -> dict"""
    lista_palavras=str.split(frases)
    dicionario_saida={}
    for chave in lista_palavras:
        if not chave in dicionario_saida:
            dicionario_saida[chave]=str.count(lista_palavras,chave)
    return dicionario_saida