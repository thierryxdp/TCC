def substitui(s,x,i):
    '''função que substitui um caractére da função (x), de acordo com a oposição (i)
    str + str + int -> str'''
    stringTrocada = s[:i]+x+s[i+1:]
    
    return stringTrocada