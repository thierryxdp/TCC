# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' A partir de uma string 's', um inteiro 'i' e um caractere 'x';
    retorna uma nova string substituindo o elemento de índice 'i', por 'x';
    str,str,int => str'''
    list.pop(list(str(s)),int(i))
    list(str(s))[i:i] = x
    return ''.join(map(str,list(str(s))))