# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que dados uma string (s), um caractér (x) e um número 
    inteiro (i) aleatórios e respectivamente, retorna uma string igual
    a "s", exceto que o elemento da posição "i" é substituído pelo 
    caracter "x".
    Parâmetros de Entrada: Str, Str, Int
    Valores de Saída: Str'''
    
    return s[0:i] + x + s[(i + 1):]