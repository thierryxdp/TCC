def bolos(A,B,C):
 '''funcao que calcula A, B e C e o numero de colher 
    de cada ingrediente para fazer os bolos
    int,int -> int'''
 bolo=(A//2,B//3,C//5)
 return min(bolo)