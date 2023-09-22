# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Funçao que substitui de uma string o caractere x dado 
    o numero inteiro da posiçao dados na entrada
    Entrada: string, string, int
    Saida: String'''
    return s[:i] + str(x) + s[i+1:]