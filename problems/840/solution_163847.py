def bolos(A,B,C):
    '''calcula a quantidade de bolos que João consegue fazer dado a quantidade de ingrediente que ele tem em casa; int, int, int -> int'''
    return min(int(A/2),int(B/3),int(C/5))