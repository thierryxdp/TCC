import math
    def bolos(A,B,C):
        """Função que calcula o número de bolos que João pode fazer dado o número mínimo de ingredientes para se fazer 1 bolo."""
        return min((A//2) + (B//3) + (C//5))