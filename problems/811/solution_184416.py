# Criei a lista com as devidas dimensoes do colcão
#Sendo A e B maior que a largura e altura a função retorna False
#Se não, a condicional usada é True
# Escolha nomes elucidativos para suas variáveis
def colchao(medida, H, L):
    [A, B, C] = medida
    if A and B>H and L:
        return False
    else:
        return True