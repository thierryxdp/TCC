# string(s), int(x), int(i) -> string
'''a função age da seguinte forma: recebe os valores x, informação tipo string,x um caractere que substituirá i, sendo um int e i um número inteiro e por fim substitui o elemento em índice i por x sem modificar o resto da string''' 
def substitui(s,x,i):
    if i==0:
        return x+s[1:]
    if i==len(s):
        return s[0:len(s)] + x
    if i== i>0 and i<len(s):
        return s[0:i]+x+s[i:0]