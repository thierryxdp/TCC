# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ seja uma string, x um caractere e i um inteiro entre zero e o com da string.
    retornar string a qual o elemento de posição s seja trocado por x
    entradas s-> string, x->string, int e i->int
    saída ->string"""
    if 0<i<len(s):
        parte_1= s[:int(i)]
        parte_2=s[int(i+1):]
        if 0<i<len(s):
            return parte_1 + str(x) + parte_2