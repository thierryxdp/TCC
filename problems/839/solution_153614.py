def carros(x,y=5):
    ppl_pla=int(x//y)
    if x%y>0:
        return ppl_pla + 1
    else:
        return ppl_pla