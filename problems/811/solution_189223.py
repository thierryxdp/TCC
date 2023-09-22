# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def colchao(medidas,H,L):
    "Recebe uma lista de medidas, uma altura ('H') e uma largura ('L') e retorna se o colchão passa ou não pela porta; list, int, int -> bool"
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if(A or B or C <= L):
        if(B or c <= H):
            return True
        else:
            return False
    else:
        return False