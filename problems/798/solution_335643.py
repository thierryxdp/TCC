def freq_palavras(frases):
    '''funcao que dada uma string retorna um dicionario com uma chave pra cada palavra e numero de vezes que ela aparece; str -> dicionario'''
    dicionarioPalavras = {}
    palavrasSeparadas = str.split(frases)
    for palavra in palavrasSeparadas:
        dicionarioPalavras {palavra} = list.count(palavrasSeparadas,palavra)
    return dicionarioPalavras