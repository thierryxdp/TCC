def conta_frases(x):
    """ funcao ira receber um texto e retornar a contagem de frases de acordo com a pontuação
    entrada: string
    saida: int"""
    x = str.replace (x,"...","!")
    return (str.count(x,".") + str.count(x,"!") + str.count(x,"?")+str.count(x,"..."))