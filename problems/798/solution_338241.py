def freq_palavras(frases):
    """Recebe uma string e retorna um dicionário
com cada palavra dessa string como uma chave, e o número
de vezes que aparece como valor.
assinatura: str --> dict
casos de teste:
freq_palavras('dinheiro é dinheiro e vice versa') == {'dinheiro': 2, 'é': 1, 'e': 1, 'vice': 1, 'versa': 1}
freq_palavras('python é legal python é legal demais') == {'python': 2, 'é': 2, 'legal': 2, 'demais': 1}
freq_palavras('quem pode pode') == {'quem': 1, 'pode': 2}
"""
    frases = str.split(frases)
    dic = {}
    for palavras in frases:
        if palavras in dict.keys(dic):
            dic[palavras] += 1
        else:
            dic[palavras] =1
    return dic