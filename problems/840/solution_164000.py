import math
def bolos(A, B, C):
    """
        Evaluates the number of cakes that can be made with the current
        ingredients.

    Parameters:
        A: int
        The number of wheat flour cups avaliable
        B: int
        The number of eggs avaliable
        C: int
        The number of tablespoons of milk avaliable

    Returns:
        int
        The number of cakes that can be made with the current ingredients
    """
    return math.floor(min(A/2, B/3, C/5))