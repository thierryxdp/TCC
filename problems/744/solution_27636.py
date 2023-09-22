def hashtag(s):
    '''Função que, dada uma string como parâmetro, retorna uma nova string da seguinte forma: "abcd" -> "#ab#cd#"; str -> str.'''
    tamanho = len(s)
    s1 = s[:(tamanho // 2)]
    s2 = s[(tamanho // 2):]
    return "#" + s1 + "#" + s2 + "#"