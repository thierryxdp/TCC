# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Função que recebe a string 's', um caractere 'x' e um número inteiro 'i',
0 e o comprimento da string e retorna uma string igual a 's', exceto que o elemento
da posição 'i' será substituído pelo caractere 'x'
    string, int, int -> string
    '''
    return s[0:i]+str(x)+s[i+1:]