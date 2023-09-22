"recebe uma string s, um inteiro i e um caractere x e retorna a string s e troca o elemente da posição de i pelo caractere x"
def substitui(s,x,i):
    p=s+x+i
    return s + int(i[:len(p)//2]) + x[0:]