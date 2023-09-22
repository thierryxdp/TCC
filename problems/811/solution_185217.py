# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef colchao(medidas,H,L):
def colchao(medidas,H,L):
    "essa funcao calcula uma lista com os tamanhos inteiros A,B e C, e H e L que sao os inteiros da largura e da porta e retorna em True caso o colchao passe ou False caso contrario; list, int, int-> bool"
    
    A= medidas[0]
    B= medidas[1]
  
    if (B<=H and A<=L) or (B<=L and A<=H):
        return True
    else:
        return False