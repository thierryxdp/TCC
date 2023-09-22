import math

def bolos(a:int, b:int, c:int) -> int:
    "Quant. de bolos, dados: farinha, ovos e leite."
    return min ((a//2),(b//3),(c//5))