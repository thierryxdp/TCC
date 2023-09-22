# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
     """ determina uma string igual a (s), exceto que o elemento
da posicao (i) sera substituido pelo caractere (x).
assinatura:str, str, int --> str
teste:
substitui("paralelepípedo", "tr", 4) == 'paratrelepípedo'
substitui("banana", "t", 2) == 'batana'
"""
        return s[:i] + str(x) + s[(i+1):]