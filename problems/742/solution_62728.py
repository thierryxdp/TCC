"""recebe uma string s qualquer e a retorna com o elemento da posiçao i substituido pelo caractere x
s->string
x->caractere
i->posição do carectere a ser substituido na string
string, int, int -> string"""
def substitui(s,x,i):
    s=s.replace(s[i],x,i)
    return s