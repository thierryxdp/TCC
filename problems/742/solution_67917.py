def substitui(s,x,i):
    '''Função que recebe uma string s, um caractere x e um numero inteiro i
    e retorna uma string s
    str,str,int->str'''
    if i==0:
        return x+s[1:]
    elif i==len(s):
        return s[0:len(s)]
    else:
        return s[0:i] + x + s[i+1:]