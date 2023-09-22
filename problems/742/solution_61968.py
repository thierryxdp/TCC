# Fatia a string até a posição i, concatena com o caractere x, e concatena com a string fatiada até o final sem o caractere da posição i
# string, string, int -> string
def substitui(s,x,i):
    return s[:i] + x + s[i+1:]