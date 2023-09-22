def bolos(xicaras=2,ovos=3,colheres=5):
    """Função que retorna quantos bolos podem ser feitos dados o número de xicaras de farinha, ovos, e colheres de sopa."""
    return min(xicaras//2,ovos//3,colheres//5)