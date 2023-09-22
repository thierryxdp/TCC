from math import *
import math
def bolo (A,B,C):
    """Calcula a quantidade de bolo que podem ser produzidos, dados os ingredientes"""
    return min(A//2,B//3,C//5)