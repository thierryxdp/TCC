# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ""funacao que dado um str 's'e um caractere'x' e um inteiro
     'i' retorna a str 's' exceto que tenh que ser substituido
        por 'x' entrada str-str-int saida str"""
        if 0<=i<=len(s):
        return s[0:i]+x+s[i+1:]