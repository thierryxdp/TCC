def conta_frases(texto):
    """função que recebe texto e conta as frases.
    str--> int"""
contagem1 = texto.count('.')  #separa texto pelos pontos
contagem2 = texto.count('!')  #separa texto pelos pontos de exclamação
contagem3 = texto.count('?') #separa texto pelo ponto de interrogação
contagem4 = texto.count('...') #conta quantas reticências tem na frase
return contagem1 - contagem4 + contagem2 + contagem3

    #Pra cada reticência haverão duas frases a mais, isso acontece porque a contagem
    #de pontos contabiliza os pontos das reticências também
    #Contamos o número de reticência e tiramos do número de pontos, 
    #assim a contagem é feita sem interferências e não fica adulterada.