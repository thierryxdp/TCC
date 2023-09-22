def substitui(s,x,i):
    """ recebe uma string s, um caractere x e um numero inteiro i(sendo ele entre 0 e o comprimento da string), e retorna a string s com o elemento da posiçao i substituido pelo caractere c;
    string,string,int->string """
    return s[0:i] + x + s[i + 1:]