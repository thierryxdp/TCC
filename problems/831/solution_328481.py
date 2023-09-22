def lingua_p(palavra):
    """funcao que recebe uma palavra como entrada, traduz ela para a lingua do P e retorna a nova palavra formada.
    entrada->str
    saida->str"""
    nova=""
    c=0
    for i in range(0,len(palavra)):
        if palavra[i] in "aeiouáéíóúâôêîûãõAÁÉÍÓÚÂÊÎÔÛÃÕEIOU":
            nova= nova+palavra[c:i+1] +"p"
            c=i
    nova= nova+palavra[c:]    

    return nova