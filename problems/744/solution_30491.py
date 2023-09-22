# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """retorna a string s com a inserção de # no início, no meio e no fim da string s;
    	(str->str)"""
    a = len(s)
    b = (a//2)
    c = b+1
    return "#" + s[0:b] + "#" + s[b:a]