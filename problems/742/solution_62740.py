"""recebe uma string s qualquer e a retorna com o elemento da posiçao i substituido pelo caractere x
s->string
x->caractere
i->posição do carectere a ser substituido na string
string, int, int -> string"""
def substitui(s,x,i):
    return s[0:i]+str(x)+s[-1,i]