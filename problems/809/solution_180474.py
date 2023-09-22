# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(L1, L2):
    '''funcao que dado duas listas L1 e L2 com 3 
    elementos cada retorna uma terceira lista L3 
    que corresponde as listas L1 e L2 intercaladas; 
    list,list -> list'''
    A = L1[0]
    B = L1[1]
    C = L1[2]
    D = L2[0]
    E = L2[1]
    F = L2[2]
    L3 = [A,D,B,E,C,F]
    return L3