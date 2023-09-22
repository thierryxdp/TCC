def hastag(string):
    #Colocar como entrada uma string e retornar a mesma com três 
    #hastags, uma no começo, outra no meio e outra no fim
    # str-> str
    metade = len(string) //2
    return "#" + string[0:metade]+ "#" + string[metade:] + "#"