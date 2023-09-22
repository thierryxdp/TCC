# funçao que recebe uma string s, um caracte x e um numero inteiro entre 0 e o comprimento da string e retorne uma string=s
# string, int, int -> string
def substitui(s,x,i):
    if i==0:
        b = s[i+1:]
            return x + b
        else:
            a = s[:i]
            b = s[i+1:]
            i = x
            return a + i + b