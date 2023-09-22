def bolos (A,B,C):
'''retorna quantos bolos podem ser feitos com A xícaras de farinha, B ovos e C colheres de sopa de leite'''
x=A//2
y=B//3
z=C//5
return min(x,y,z)