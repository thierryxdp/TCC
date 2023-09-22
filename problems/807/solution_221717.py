def conta_frases(t):
    if '...' in t:
        ret_t=str.replace(t,'...','*')
        f_ret= str.count(ret_t,'*')
        f_pon= str.count(ret_t,'.')
        f_exc= str.count(t,'!')
        f_int= str.count(t,'?')
        return f_pon+f_exc+f_int+f_ret
    else:
        f_pon= str.count(t,'.')
        f_exc= str.count(t,'!')
        f_int= str.count(t,'?')
        return f_pon+f_exc+f_int