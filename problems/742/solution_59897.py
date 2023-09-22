# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''Dados uma string 's', um caractere 'x' e um número inteiro 'i'
       entre 0 e o comprimento da string, a função retorna uma string
       igual a 's', exceto que o elemento da posição 'i' deve ser 
       substituído pelo caractere 'x'
       str, str, int -> str
       Parametros:
       s: string a ser escolhida e digitada
       x : caractere a ser escolhido e digitado
       i: número inteiro a ser escolhido e digitado'''
    return s.replace(s[i], x)