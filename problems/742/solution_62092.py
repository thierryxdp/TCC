# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """funcao que recebeuma str's' um caractere 'x'
    um inteiro 'i' entr 0 e o comprimento da strs's'
    retorna 's' exceto que 'i' tenha que ser substi-
    tuido por 'x'.Entrada str->caractere->inteiro.
    Saida->str"""
    if 0<i<len(s):
        return s
    else:
        if s[i]='x'
        return s[i]+x+s[i+1:]