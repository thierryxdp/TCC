# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "retorna a string s substindo o caractere x pela posicao i da mesma" 
    if i==0:
        return (x) + s[1:]
    elif i== len(s):
        return s[0:len(s)] + (x)
    else:
        return s[0:i] + (x) + s[i+1:]