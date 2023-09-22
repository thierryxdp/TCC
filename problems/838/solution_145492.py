def media3(a,b,c):
    '''função que calcula e retorna a média de três números inteiros'''
    return (a+b+c)/3

def difmedia3(a,b,c):
    '''função que retorna, dados três números, a diferença do maior deles com a média'''
    return (max(a,b,c)-media3(a,b,c))

def sommedia3(a,b,c):
    '''função que retorna, dados três números, a soma do mennor deles com a média'''
    return (min(a,b,c)+media3(a,b,c))

def delta(a,b,c):
    '''função que dados os coeficientes a, b e c, calcula o delta de um polinômio do segundo grau.'''
    return ((b**2)-(4*a*c))

import math

def raiz1(a,b,c):
    '''uma função que calcula a primeira raiz real de uma equação do segundo grau dados os coeficientes a, b e c'''
    return (-b+math.sqrt(delta(a,b,c)))/(2*a)

def raiz2(a,b,c):
    '''uma função que calcula a segunda raiz real de uma equação do segundo grau dados os coeficientes a, b e c'''
    return (-b-math.sqrt(delta(a,b,c)))/(2*a)

def termopa(a1,an,r):
    '''função que calcula o número de termos dado o termo inicial, o termo final e a razão'''
    return (((an-a1)/(r))+1)

def somapa(a1,an,r):
    '''função que calcula a soma da PA dadoo termo inicial, o termo final e a razão'''
    return (((a1+an)*termopa(a1,an,r))/2)

def dist_pontos(x1,y1,x2,y2):
    '''função que calcule a distância entre dois pontos(p1 e p2) em um plano dadas suas coordenadas (x1 e y1 para p1, x2 e y2 para p2)'''
    return math.sqrt((y2-y1)**2+(x2-x1)**2)

def per_trianguloreto(a,b):
    '''função que calcula o perímetro de um triângulo reto dados os catetos'''
    return ((a)+(b)+math.sqrt(a**2+b**2))

def eq_fundamentaltrig(a):
    '''função que calcula a soma do quadrado do seno com o quadrado do cosseno de um ângulo, conhecida como equação fundamental da trigonometria'''
    return math.sin(a)**2+math.cos(a)**2
     
def pi():
    '''função que dá o valor de pi'''
    return 3.14

def areasetorcirc(r,x=360):
    '''função que calcula a área de um setor circular, dados o raio e o ângulo em graus, de modo que se nenhum ângulo for informado, a função retorna a área do círculo
inteiro'''
    return (x/360)*pi()*r**2


#Escreva sua função aqui. Pode apagar essa linha.