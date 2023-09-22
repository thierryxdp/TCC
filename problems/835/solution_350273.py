def melhor_volta(matriz):
    """Função que retorna uma tupla com (e nessa ordem): quem fez, qual o tempo e em qual volta)"""
    """Parâmetros de entrada:list"""
    """Parâmetros de saída:tup"""
    for lista_interna in matriz:
        for item in lista_interna:
            return (lista_interna,min(item),item)