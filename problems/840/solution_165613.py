def bolos (A, B, C):
    import math
    bolosfarinha=math.floor(A/2)
    round A/2
	B=math.floor(B/3)
    round B/3
	C=math.floor(C/5)
    round C/5
    return min([bolosfarinha,B,C])