# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna a string s mas com o caractere x colocado dentro da string na posição
       indicada pelo número i. str,str,int -> str'''
    s_str = s
    sxi = s_str[0:i] + x + s_str[-1:i:-1]
    return sxi