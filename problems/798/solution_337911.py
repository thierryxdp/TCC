def freq_palavras(frases):
    '''
	função que recebe uma string e retorna um dicionário onde cada palavra dessa string é uma chave e tem como valor o número de vezes que a palavra aparece;
    str -> dic
    '''
	dic = {}
    string = str.split(frases)
    for palavra in string:
        if palavra not in dic:
            dic[palavra] = 0
        dic[palavra] = dic[palavra] + 1
    return dic