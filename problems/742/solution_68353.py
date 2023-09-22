def substitui(s,x,i):
    ''' Esta função retorna a substuição de um elemento
na posição i de uma string s, pelo caractere x.
string, int, int -> string'''
    return s[0:i] + str(x) + s[i:len(s):i]