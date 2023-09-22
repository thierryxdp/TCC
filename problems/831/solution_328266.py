def lingua_p_lista(palavra):
    '''função que entrega lista com palavras de lingua_p em ordem.'''
    linguap=[]
    palavra2=str.lower(palavra)
    vogais=['a','e','i','o','u','á','é','í','ó','ú']
    for i in palavra2:
        if i in vogais:
            linguap.append(str(i)+"p"+str(i))
        else:
            linguap.append(str(i))
    return linguap
def lingua_p(palavra):
    """função recebe uma palavra e a traduz a língua do p. str->str."""
    listap=lingua_p_lista(palavra)
    palavra=''
    for n in range(len(listap)):
        palavra+=listap[n]
    return palavra