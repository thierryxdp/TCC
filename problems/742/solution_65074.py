# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que recebe uma string s, um caractere x e um número inteiro i no
intervalo entre 0 e a posição do ultimo caractere de s, e retorna a string s
porém com a substituição do termo de posição i pelo caractere x, em string;
Entradas: string,string,int ; Retorno:string'''
    if 0<=i<len(s):
        return s[:i]+str(x)+s[i+1:]