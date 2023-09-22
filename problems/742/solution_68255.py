def substitui (s,x,i):
    ''' função que que recebe uma str s, um caractere x e um
ńumero inteiro i entre 0 e o comprimento da string, e retorna uma string
igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x.
: str,str, int ---str '''
    s = (s[0:i]) + (str (x)) + (s[i+1:])
    if (0<=i<=len(s)):
        return s