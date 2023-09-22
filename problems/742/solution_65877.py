# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """retorna uma string igual a s,sendo o elemento da posição i substituído por x
    str,int,int->str"""
    antes=s[0:i]
    depois=s[(i+1):len(s)]
    return antes+x+depois