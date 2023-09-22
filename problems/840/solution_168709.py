def bolos(A, B, C):
    """."""
    if A//2 <= B//3 and A//2 <= C//5:
        return A//2 
    if B//3 <= A//2 and B//3 <= C//5:
        return B//3
    if C//5 <= A//2 and C//5 <= B//3:
        return C//5