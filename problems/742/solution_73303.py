def substitui(s,x,i):
    '''funçã que substitui o caractere de numero i de uma string s pelo caractere x
    entrada: str, int, int
    saída:str'''
    return s[0:i]+str(x)+s[i+1:]