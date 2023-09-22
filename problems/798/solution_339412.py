def freq_palavras(frases):
    """A função realiza a soma do numero de veses que uma palavra aparece na frase"""
    frase_fim=frases.lower()
    
    frase=frase_fim.split()
    dic = {}

    for palavra in frase:
        dic[palavra] = dic.get(palavra,0) + 1
    return dic
    #teste freq_palavras("Eu não tenho dinheiro pq o dinheiro é super valoriazado é dificil saber ou eu saber qual vale mais ")
    #"ultilize uma palavra que faça sentido ao inver de "i" em : for i in frase:"
     # não existe pra dicionario ?dic.append(i)"
      # Ultilize o print para ver o que esta fazendo. "print(dic)""