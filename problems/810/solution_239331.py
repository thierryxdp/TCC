def inverte(f):
    listap=str.split(removePontuacao(f),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte