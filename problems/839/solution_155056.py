def carros(x,y=5):
    """ A função retorna a quantidade de carros necessários dada a quantidade de pessoas
    obedecendo a condição de que os carros que não possuem capacidade 5 sejam considerados;
    int, int -> int """
    ppl_pla=int(x/y)
    if x//y>0:
        return ppl_pla + 1
    else:
        return ppl_pla