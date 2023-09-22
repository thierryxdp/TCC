def substitui(s,x,i):
    """dado uma string s, a função substitui o caractere da posição
    i com o caractere x; str,str,int-> str"""
    return s[0: i] + x + s[i +1: len(s)]

#substitui ('abobora','v',3) == 'abovora'
#substitui ('vilao','t',2) == 'vitao'
#substitui ('olinda','h',1) == 'ohinda'