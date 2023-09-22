"""retorna, dados três parâmetros, uma string igual ao parâmetro s,
com a substituição do elemento i por x.string,int,int->string."""
def substitui(s,x,i):
    s[i]=x
    if (0<i<len(s)):
        return str(s)