def substitui(s,x,i):
    '''A função ao receber um string (s), um caractere (x) e um número inteiro (i), retorna um string igual a s, mas com o elemento da posição i substituido pelo caractere x.
    string, int, int -> string'''
    if i == 0:
        return x+s[1:]
    if i == [len(s)]:
        return s[len(s)] + x
    if i == i>0 :
        return s[0:i] + x + s[i+1]
    if i == i>0 :
        return s[0:i] + x + s[i+2]