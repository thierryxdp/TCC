# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que manipula strings pondo no início,meio e fim um hashtag.
    Assinatura: str->str"""
    n=int(len(s))
    s= round
    if n%2==0:
        return str("#")+s[0:n//2]+str("#")+s[n//2:n+1]+str("#")
    elif n%2!=0:
        return str("#")+s[0:(n-1)//2]+str("#")+s[(n-1)//2:]+str("#")