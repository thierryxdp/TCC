def substitui(s,x,i):
    '''rujrhuhuo
ent ->string, int, int ->
saida-> string'''
    quant_str= len(s)
    inteiro = i>=0 and i<=quant_str
    string_1 = s[:i]+x
    mudanca= i+1
    string_2=s[mudanca:]
    return string_1+string_2