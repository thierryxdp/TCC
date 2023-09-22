# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """"Substituir o caracter da posição indicada pelo caracter dado.
    A partir dos valores de entrada: string, caracter e um numero inteiro para a posicao"""
    palavraAlterada = s[0:i]+x+s[i+1:len(s)]
    return (palavraAlterada)