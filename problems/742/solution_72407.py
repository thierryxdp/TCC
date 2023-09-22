# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''recebe uma string 's', um caractere 'x' e um número inteiro 'i'
    e retorna a string com o elemento de posição 'i' substituído pelo
    caractere 'x' (string, int, int -> string)'''
    y = s[0:i] + x + s[i+1:]