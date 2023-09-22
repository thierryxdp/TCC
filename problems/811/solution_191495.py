# Função que calcula se o colchão passa na porta
def compara_dimensoes(colchao, h, l):
    # condições que compara cada dimensão
    if colchao[1] > h:
        if colchao[1] > l:
            if colchao[2] > h:
                if colchao[2] > l:
                    return False
                else:
                    return True
            else:
                return True
        else:
            return True
    else:
        return True

# entradas teste
entrada1 = [25,120,220]
H1 = 200
L1 = 100
    
entrada2 = [25,205,220]
H2 = 200
L2 = 100
    
entrada3 = [25,200,220]
H3 = 200
L3 = 100# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis