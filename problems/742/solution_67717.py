# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     x = str(x)
    if i<=len(s):
        return s[0:i] + x + s[i+1:len(s)]
    else:
        return 'Forneça um número entre 0 e o comprimento da string'