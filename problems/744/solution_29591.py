# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Função que retorna determinada string s com hasthag(#) no inicio, no meio e no fim dela
    entrada: string
    saida: string"""
    x = len(s) 
    y = x//2
    a = s[0:y]
    b = s[y:]
    "#" + a + "#" + b + "#"