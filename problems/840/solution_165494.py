import math
def bolos (A:int,B:int,C:int)->int:
	"""esse programa mostra a quantidades de 
	bolos que podem ser feitos"""
    return int((A//2)+(B//3)+(C//5))