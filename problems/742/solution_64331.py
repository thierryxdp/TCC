def substitui(s,x,i):
    """Dado a string s, o caractere x e um número inteiro i (de 0
    até o último número relacionado ao comprimento da string),
    a função retorna a string s com o elemento na posição i
    substituido pelo caracter x.
    Parametros de Entrada: str, str,int;
    Retorna: str"""
    auxiliar1= s[:i]
    auxiliar2= s[i+1:]
    return auxiliar1+x+auxiliar2