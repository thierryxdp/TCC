def substitui(s,x,i):
    """função que recebe uma string s, um caractere x e um número inteiro i
    	sendo que 0<=i<=comprimento da string e retorna uma string igual a s
        porém com o elemento da posição i substituído pelo caractere x
        Exemplo:
        substitui(júlia,o,5)==júlio
        """
    return s[0:i]+x+s[i+1:len(s)]