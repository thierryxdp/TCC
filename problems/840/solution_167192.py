# 1 bolo - 2 ft 3 ovo 5 sl
# n bolo - a ft b ovo c sl
def bolos(A, B, C):
    n1 = A//2
    n2 = B//3
    n3 = C//5
    if n1 <= n2 and n1 <= n3:
        return n1
    if n2 <= n1 and n2 <= n3:
        return n2
    if n3 <= n1 and n3 <= n2:
        return n3