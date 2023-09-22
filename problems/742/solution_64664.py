#recebe uma string, um caractere x e um numero inteiro i entre 0 e o comprimento da string e retorna uma string = s
# string, int, int -> string
def substitui(s,x,i):
    if i >=0 and i<=len(s):
        isub = i-1
        isub2 = i+1
        return s[:isub2] + x + s[isub1:]