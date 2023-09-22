def substitui(s,x,i):
    '''Função que retorna uma string inserida, mas com o valor da segunda entrada, que se encontra no intervalo 0<=x<=len(s), substituindo
    o valor de s[i]
    str, int, int -> str'''
    if 0<i<len(s)-1:
        return s[0:i]+str(x)+s[i+1:len(s)]
    if i==0:
        return str(x)+s[1:len(s)]
    if i== len(s)-1:
        return s[0:len(s)-1]+str(x)]