# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     """Dada a string /s/, retorna uma string igual a /s/, exceto pelo
elemento da posição /i/, que será substituído por /x/.
assinatura: str, int, int --> str
testes:

"""
    if i <= len(s):
        return str(s) + str(x(str(s)[i]))