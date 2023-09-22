def substitui(s,x,i):
    """Função que recebe uma string s, um caractere x e um número 
    inteiro i entre 0 e o comprimento da string e retorna uma string 
    igual a s exceto que o elemento da posição i deve ser substituido 
    pelo caractere x"""
    i = int(0 <= i <= len('s'))
    return str(s) + str(x)[i]