# Função que retorna a string s, exceto que o elemento da posicao i deve ser substituido pelo caractere x.
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    sub_s1 = s[i]
    return s.replace(sub_s1, x, 1)