def colchao_passa_na_porta(dimensoes,H,L):
    '''funcao que dadas as dimensoes de um colchao,a altura H e a largura L retorna True ou False se o colchao puder passar pela porta
    lista,int,int->bool'''
    if (dimensoes[0]<=H and dimensoes[1]<=L) or(dimensoes[0]<=L and dimensoes[1]<=H):
        return True
    elif (dimensoes[0]<=H and dimensoes[2]<=L) or(dimensoes[0]<=L and dimensoes[2]<=H):
         return True
    elif (dimensoes[2]<=H and dimensoes[1]<=L) or(dimensoes[2]<=L and dimensoes[1]<=H):
        return True
    else:
        return False# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis