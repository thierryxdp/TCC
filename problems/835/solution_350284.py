def melhor_volta(matriz):
    """Função que retorna uma tupla com (e nessa ordem): quem fez, qual o tempo e em qual volta)"""
    """Parâmetros de entrada:list"""
    """Parâmetros de saída:tup"""
    melhores_voltas=[]
    for lista_interna in matriz:
        for item in lista_interna:
            melhores_voltas.append(lista_interna,matriz[lista_interna][item],item)    
    return (lista_interna,min(matriz[lista_interna][item]),item)