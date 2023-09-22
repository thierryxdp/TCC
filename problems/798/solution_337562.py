def freq_palavras(frases):
    '''Função que recebe um string e retorna um dicionário onde cada palavra dessa string seja uma chave e tem como valor o número de vezes que a palavra aparece; str -> dic'''
    dic = {}
    for item in counter.items():
        dic[item[0]] = {'Total':item[1]}
    return dic