def freq_palavras(frase):
    """dada uma string, retorna um dicionario tendo comoo numero de vezes em que aparece, sendo chave a propria palavra;
    str->dict"""
    from collections import Counter
    c=frase.split()
    return Counter(c)