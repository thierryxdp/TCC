def bolos(A,B,C):
"""Calcular a quantidade máxima de bolos que João consegue fazer, sendo A a quantidade de farinha de trigo disponível, 
B a de ovos e C a de leite disponível.
int, int -> int"""
return min(A//2, B//3, C//5)