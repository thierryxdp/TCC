# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """Recebe uma string 's', um caractere 'x' e um número inteiro 'i', cujo
    valor deverá ser de 0 ao valor do comprimento da string 's', e retorna
    uma string igual a 's', de modo que o elemento na posição 'i' seja
    substituído pelo valor de 'x'.
    tupla(str, str, int) -> str"""
    if str.index(s,s[i])<i and str.index(s,s[i],i)>i:
        return str.replace(s,s[i],x,-(i+1))
    elif str.index(s,s[i])==i and str.index(s,s[i],i)==0:
        return str.replace(s,s[i],x,i)
    elif str.index(s,s[i])==i and str.index(s,s[i],i)!=0:
        return str.replace(s,s[i],x,i+1)
    elif str.index(s,s[i])<i and str.index(a,s[i],i)==0:
    	return str.replace(s,s[i],x)