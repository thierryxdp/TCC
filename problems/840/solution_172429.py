import math
def bolos (xicarasfarinha, ovos, colhersopaleite):
    """Calcula a quantidade de bolos que João pode fazer dado os ingredientes que tem; int ->int"""
    return min(xicarasfarinha//2, ovos//3, colhersopaleite//5)