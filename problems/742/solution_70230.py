def substitui(s,x,i):
    '''funcao que dado uma string s subistitui
    o termo i por um caractere qualquer x;
    str,str,int -> str'''
    return s[0:i] + x + s[i+1:]