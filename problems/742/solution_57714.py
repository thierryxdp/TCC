# recebe uma string s e substitui o caractere correspondente a posicao i pelo caractere x
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    x = str(x)
    return s.replace(s[i],x)