def substitui(s,x,i):
    """ retorna a substituiçao do elemento da posiçao i da string s pelo caractere x, sendo i um numero entre 0 e o comprimento da string:
    string, caractere, int->string """
    return s.replace(s[i], x)