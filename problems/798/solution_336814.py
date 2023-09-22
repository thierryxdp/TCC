def freq_palavras(frase):
    """dada uma string, retorna um dicionario tendo comoo numero de vezes em que aparece, sendo chave a propria palavra;
    str->dict"""
    frase=frase.split()
    dicionario={}
    for palavra in frase:
        dicionario[palavra]=list.count(frase,palavra)
    return dicionario