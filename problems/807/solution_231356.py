def conta_frases(x):
    cont_ret = str.count(x,'...')
    t = str.replace(x,'...','')
    
    cont_pt = str..count(t,'.')
    cont_interrog = str.count(x,'?')
    cont_exclama = str.count(x,'!')
    
    return cont_ret + cont_pt + cont_interrog + cont_exclama