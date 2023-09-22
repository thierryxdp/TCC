def bolos(A, B, C):
	AA = A//2
    BB = B//3
    CC = C//5
    if AA < BB and CC:
        return AA
    if BB < CC and AA:
        return BB
    if CC < AA and BB:
        return CC