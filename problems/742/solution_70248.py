def substitui(s,x,i):
    comprimento_str = len(s)
    numero_inteiro = i >= 0 and i <=comprimento_str
    string_1 = s[:i]+x
    mudanca= i+1
    string_2=s[mudanca:]
    return string_1+string_2