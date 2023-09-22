def freq_palavras(frases):
    """str -> dict
       Explicação: cada palavra da frase parâmetro corresponde a uma chave no dicionário retornado, tendo como valor seu número de ocorrências na str."""
    l = str.split(frases)
    d = {}
    for i in range(len(l)):
        d[l[i]] = list.count(l, l[i])
    return d
#Teste 1:
#freq_palavras('dinheiro é dinheiro e vice versa')--> {'dinheiro': 2, 'é': 1, 'e': 1, 'vice': 1, 'versa': 1}
#freq_palavras('o tempo perguntou ao tempo quanto tempo o tempo tem')--> {'o': 2, 'tempo': 4, 'perguntou': 1, 'ao': 1, 'quanto': 1, 'tem': 1}
#freq_palavras('o sabiá não sabia que o sábio sabia que o sabiá não sabia assobiar')--> {'o': 3, 'sabiá': 2, 'não': 2, 'sabia': 3, 'que': 2, 'sábio': 1, 'assobiar': 1}