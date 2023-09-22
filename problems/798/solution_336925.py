def freq_palavras(frases):
    '''função que recebe uma frase e retorna um dicionario onde cada palavra dessa string é uma chave e tem o valor o número de vezes que aparece.
    str -> dict
    Explicação: basta rodarmos uma palavra na lista de palavras que formam a frase com o for, relacionando essa palavra com a posição e quantidade e montando o dicionario.''''
    dic={}
    for s in frases.split():
        dic[e]=dic.get(e,0)+1
    return dic
# teste 1
# freq_palavras('oi tudo bem')
# saida esperada: {'oi':1,'tudo':1,'bem':1}