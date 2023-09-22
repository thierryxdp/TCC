def intercala(lista1, lista2):
    """Retorna uma lista de tamanho 6 formada pela intercalação 
    dos elementos das listas 1 e 2 (de tamanho 3 cada) dadas
    como entrada.
    list, list -> list"""
    return lista1[0:1]+lista2[0:1]+lista1[1:2]+lista2[1:2]+lista1[2:]+lista2[2:]

# Casos de testes:
# intercala([2,7,9],[4,8,11]) == [2,4,7,8,9,11]
# intercala([-3,0,3],[-1,2,4]) == [-3,-1,0,2,3,4]
# intercala(["Oi","tudo bem?","também"],["olá","sim, e você?","que bom!"]) == ["Oi","olá","tudo bem?","sim, e você?","também","que bom!"]