def conta_frases(x):
    cont_ret = str.count(x,'...')
    t= str.replace(x.'...','')
    cont_pt = str.count(t,'.')
    cont_excla= str.count(x,'!')
    return cont_ret + cont_pt + cont_excla