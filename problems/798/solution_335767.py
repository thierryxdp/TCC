def freq_palavras(frases):
    """
    Essa função recebe uma string e retorna um dicionario 
    com o valor de quantas vezes cada chave aparece;
    str -> dict
    """
    palavra = frases.split(' ')
    return {i: palavra.count(i) for i in palavra}