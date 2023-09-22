'''
	A função pega o i-ésimo termo da string s e substitui
    pelo caractere x.
    i->int
    x->str de len(x)==1
    s->str
'''
# string, int, int -> string
def substitui(s,x,i):
        s[:(i-1)]+x+s[(i+1):]