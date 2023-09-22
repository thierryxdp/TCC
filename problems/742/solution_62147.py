#Quero uma função que forme uma palavra s, tal que uma das posições de s vai ser trocada pela letra x na posição i
#resolução:
#1.definir s,x e i
#2.fatiar a string
def substitui(s,x,i):
    """funcao da string s substituida pela string x na posicao i"""
    s="breno"
    x="k"
    i=3
    return s[0:3]+ "k" +s[5]