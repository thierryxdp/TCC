def substitui(s,x,i):
    """retorna uma string igual a s, exceto que o elemento da posição i deve ser substituído pelo caractere x."""
    """str,str,int->str"""
    if i>len(s):
        return 'O inteiro i deve ser menor ou igual ao número de caracteres da string s.'
    else:
        return s[:i]+'x'+s[i+1:]