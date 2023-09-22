# Função que recebe uma string s, um caractere x e 
# um numero inteiro i entre 0 e o comprimento da string;
# retorna uma string igual a s, exceto com troca do elemento 
# da posição i pelo caractere x
# string, int, int -> string
def substitui(s,x,i):
    X=s
    return X[0:i]+x+X[i+1:]