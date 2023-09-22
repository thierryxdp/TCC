def freq_palavras(frases):
    '''Função que retorna um dicionário com as palavras de uma frase e o número de vezes que foram repetidas, dado a frase;str->dict'''
    palavras=str.split(frases)
    ja_apareceu=[]
    frequencia={}
    for a in palavras:
        if a not in ja_apareceu:
            frequencia[a]=list.count(palavras,a)
        list.append(ja_apareceu,a)
    return frequencia