# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que dado uma str's' um caractere 'x'
    e um inteiro (i) retorna str 's' exceto se (i)
    deva ser substituido por 'x'. Entrada str-str-int
    ,saida:str"""
    if 0<=i<=len(s):
        return s[0:i]+x+s[i+1:]