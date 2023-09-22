# recebe uma string s e substitui o caractere correspondente a posicao i pelo caractere x
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    x = str(x)
    sub1 = s[:i]
    sub2 = s[(i+1):]
    return sub1+x+sub2