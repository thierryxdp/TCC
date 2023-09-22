# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    
    """ Dada uma string 's', um caractere 'x' e um número inteiro 'i' entre
    0 e ocomprimento da string 's', retorna uma string igual a 's', mas com o 
    elemento da posição 'i' substituído pelo caractere 'x'.
    string,string,int -> string"""
    
    if i > len(s):
        return ' O valor de i deve ser menor que o comprimento de s.'
    else:
        if i !=0:
            return s[0:i] + x + s[i+1:]