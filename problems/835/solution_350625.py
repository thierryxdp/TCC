def melhor_volta(matriz):
    """Função que retorna uma tupla com (e nessa ordem): quem fez, qual o tempo e em qual volta)"""
    """Parâmetros de entrada:list"""
    """Parâmetros de saída:tup"""
    melhores_voltas=()
    for i in matriz:
           melhores_voltas.append((i.index(min(i))+1,min(i),i+1))
    for best_volta in melhores_voltas:
        return melhores_voltas[best_volta][1]