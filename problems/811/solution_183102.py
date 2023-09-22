# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    """ Retorna se é possível ou não passar um colchão de dimensões AxBxC através de uma porta de altur H e largura L, list, int, int -> string """
    A = int(medidas[0]);
    B = int(medidas[1]);
    C = int(medidas[2]);
    if(H>=A and L>=B and C>H and C>L):
        return "True";
    else:
        if(H>=B and L>=A and C>H and C>L):
            return "True";
        if(H>=A and L>=C and B>H and B>L):
            return "True";
        if(H>=C and L>=A and B>H and B>L):
            return "True";
        if(H>=B and L>=C and A>H and A>L):
            return "True";
        if(H>=C and L>=B and A>H and A>L):
            return "True";
        if((A>H and B>L) or (B>H and A>L) or (A>H and C>L) or (C>H and A>L) or (B>H and C>L) and (C>H and B>L)):
            return "False"