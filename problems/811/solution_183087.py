# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
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