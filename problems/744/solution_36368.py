# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que manipula strings pondo no início,meio e fim um hashtag.
    Assinatura: str->str"""
    n=int(len(s))
    p=n//2
    i=(n-1)//2
    s= round
    if n%2==0:
        return str("#")+s[0:p]+str("#")+s[p:n+1]+str("#")
    elif n%2!=0:
        return str("#")+s[0:i]+str("#")+s[(i:]+str("#")