def inverteFrase(f):
    listap=str.split(remove_pontuacao(f),' ')
    strinverte=str.join(' ',listap[::-1])
    return strinverte