# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que substitui um caractere x de uma string s no índice i 
    (0<i<tamanho da string). Entrada: string, string, int. Saída: string'''
    return s[:i] + x + s[i+1:]