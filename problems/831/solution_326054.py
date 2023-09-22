def lingua_p(palavra):
    """ função que traduz um palavra para a lingua P;
    str-> str"""
    traduz=[]
    for i in range(0, len(palavra)):
        if palavra[i] in "aeiouáéíóúãõâêîôû":
            list.append(traduz, palavra[i]+"p"+palavra[i])
        else:
            list.append(traduz, palavra[i])
    return str.join("",traduz)