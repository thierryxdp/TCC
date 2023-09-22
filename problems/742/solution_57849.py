def substitui(s,x,i):
    """Dados: A string s, o caractere x e o inteiro i entre 0 e o comprimento da string, a função retorna uma string igual a s, sendo que o elemento referente a posição i será substituido pelo caractere x;
    str,str,int->str"""
    return s[0:i]+str(x)+s[i+1:]