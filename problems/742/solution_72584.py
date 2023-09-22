# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(string,caracterex,i):
    '''função que recebe uma string, um caractere e um numero
    inteiro,retornando uma string igual a s, exceto que o 
    elemento da posição i deve ser substituido pelo caractere;
        string,int,int-> string'''
    return string[:i]+caracterex+string[i+1:]