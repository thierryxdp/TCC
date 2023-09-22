def freq_palavras(frases):
    """Função que dada uma string, retorna um dicionário onde
    cada palavra dessa string seja uma chave e tenha como
    valor a quantidade de vezes que aparece;
    str -> dic"""
    dic = {}
    string = str.split(frases)
    for palavra in string:
        if palavra not in dic:
            dic[palavra] = 0
        dic[palavra] = dic[palavra] + 1
    return dic