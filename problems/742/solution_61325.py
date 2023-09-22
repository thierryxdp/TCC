# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string, int, int -> string
def substitui(s,x,i):
    """ função que modifica a palavra dada na entrada, de acordo com a letra que deseja adicionar em qualquer posição
 		entrada: string, string, int
        saida: string
        retorna:
        palavra nova = palavra antiga, letra nova, posição x
        substitui = na palavra antiga (aniversário), pela letra nova (A), na posição (0)
    """
       return s[0:i]+ x + s[(i+1):]