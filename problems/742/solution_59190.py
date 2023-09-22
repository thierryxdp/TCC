# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    ''' A partir de uma string 's', um inteio 'i' e um caractere 'x';
    retorna uma nova string substituindo o elemento de índice 'i', por 'x';
    str,str,int => str'''
    lista = list(str(s))
    list.pop(lista,int(i))
    return ''.join(map(str,lista[int(i):int(i)]=x))