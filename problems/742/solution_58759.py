# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    "dada a string 's', retorna ela mesma, porém com o caractere que ocupa a posição 'i' dela substituido pelo caractere 'x'. str, str, int -> str"
    return s.replace (s[i], x)