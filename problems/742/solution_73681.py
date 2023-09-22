# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """
    Função que dado uma string, um caractere e uma valor inteiro dentro do limite da
    string, retorne a string com o caractere substituido na posição solicitada.
    string, int, int -> string
    """
    lim = len(s)
    for lim <= i:
        s[i] = x
        return s