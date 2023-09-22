# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    ''' Função recebe duas listas e intercala seus elementos;
    exemplo: L1 = [1,3,5] , L2 = [2,4,6] retorna L3 = [1,2,3,4,5,6];
    list,list => list'''
    x1,x2,x3 = lista1
    y1,y2,y3 = lista2
    return [x1,y1,x2,y2,x3,y3]