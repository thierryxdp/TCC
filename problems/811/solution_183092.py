# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Retorna se é possível ou não passar um colchão de dimensões AxBxC através de uma porta de altur H e largura L, list, int, int -> string """
    A = int(medidas[0]);
    B = int(medidas[1]);
    C = int(medidas[2]);
    if(H>A and L>B):
        return "True";
    else:
        if(A>H or A>L or B>H or B>L or C>H or C>L):
            return "False";
        if(H>A and L>C):
            return "True";
        if(H>B and L>C):
            return "True";