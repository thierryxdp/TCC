def intercala(lista1,lista2):
    """Dada duas lista L1 e L2, a função gera uma lista L3, que intercala
    os elementos da lista L1 e L2. Exemplo: Dados L1=[5,7,9] e L2=[6,8,10]
    a função vai gerar L3=[5,6,7,9,10].
    Os parâmetros devem ser escritos entre colchetes[];
    list, list --> list"""
    lista3 = [lista1[0], + lista2[0], + lista1[1], +lista2[1], + lista1[2], + lista2[2]]
    return lista3