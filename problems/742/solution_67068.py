def substitui(s,x,i):
    """
    	Função que recebe uma string s, um caractere x e um número
        inteiro i (entre 0 e o len(s)), retornando a string s, com o 
        elemento i substituido pelo caractere x
    	string,string,int->string
    """
    s = x+s[1:]
    return s