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
        if(A>H or B>L):
            return "False";
        if(H>B and L>A):
            return "True";
        if(B>H or A>L):
            return "False";
        if(H>A and L>C):
            return "True";
        if(A>H or C>L):
            return "False";
        if(H>C and L>A):
            return "True";
        if(C>H or A>L):
            return "False";
        if(H>B and L>C):
            return "True";
        if(B>H or A>C):
            return "False";
        if(H>C and L>B):
            return "True";
        if(C>H or B>L):
            return "False";