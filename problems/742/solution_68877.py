# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe uma string s, um caractere x e um número inteiro i entre
        0 e o comprimento da string e retorna uma string igual a s, mas o elemen
        to da posição i é substituído pelo caractere x.
        str,str,int -> str
    '''
    nova_str = str(s[0:i]) + str(x) + str(s[i+1:])
    return nova_str