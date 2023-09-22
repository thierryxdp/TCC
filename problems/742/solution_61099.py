# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    '''função que retorna a substituição de um
    caractere da string (s) por um novo caractere
    (x), tal que seja substituído pela posiçao 
    escolhida (i);
    string,int,int-> string'''
    s[i] = str(x)
    s_resultante = s + x
    return s_resultante