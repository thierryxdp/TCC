def substitui(s,x,i):
    """função que recebe uma string s, um número inteiro i e um caractere x e substitui o caractere de posição i da palavra s pelo x.
    str,str,int -> str
    Explicação:basta criarmos duas listas, para que possamos concatená-las, uma para a string s e outra para o caracter a ser substituído. Depois, precisamos somar a parte que vai até antes do caracter, o próprio x e o final da string recebida (a parte depois de i)."""
    lista1=s
    lista2=x
    return lista1[0:(i-1)]+lista2[0]+lista1[i:]