# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(L1, l2):
    """
    Intercala duas listas. Como uma corrente, junta cada primeiro item, depois cada segunda e, por fim, cada último
    lst, lst -> lst
    """

    L3 = [L1[0], l2[0], L1[1], l2[1], L1[2], l2[2]]
    return L3

    #Caso teste intercalandoListas(["1", "2", "3"], ["4", "5", "6"]) -> ["1", "4", "2", "5", "3", "6"]
    #Caso teste intercalandoListas(["Oi", "bom", "Quanto"], ["tudo", "?", "tempo"]) -> ["Oi", "tudo", "bom", "?", "Quanto", "tempo"]