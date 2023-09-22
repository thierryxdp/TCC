#função substitui o lugar 'i' pelo caractere 'x'
#
def substitui(s,x,i):
    if (i!=int):
        return Por favor coloque um numero inteiro na variavel i
    return s[0:i]+str(x)+ s[(1+i):]