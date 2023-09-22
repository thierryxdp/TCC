def substitui(s,x,i):
    'substitui um caracter x, de uma string s, na posicao i'
    'entrada: str,str,int'
    'saida: str'
    dividir1=s[:i]
    dividir2=s[i-1:]
    soma= dividir1+x+dividir2
    return soma