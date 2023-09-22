def substitui(s,x,i):
'''a função colocará o caracter (x) na posição (i) da string (s).
string, string, int -> string'''
q(s) = len (s)
parte1 = s [0:i]
parte2 = s [i+1:q(s)]
return parte1 + x + parte2