def posicao(s,i,x):
    return s[i]==x

def substitui(s,x,i):
    """corta a string s logo antes da letra no índice i, acrescenta a letra variável x, e, por fim, adiciona a parte faltante da string s (novamente excluíndo a letra no índice i, substituíndo-a por x)
        assinatura: string, int, int -> string """ 
    return s[0:i] + x + s[i + 1:]