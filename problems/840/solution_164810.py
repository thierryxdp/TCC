def bolos(A,B,C):
'''Calcula o maior número de bolos que joão pode fazer dados a quantidade de farinha de trigo 
"A", ovos"B" e colheres de sopa de leite "C";int||float, int||float->int'''
return math.floor(min(A/2,B/3,C/5))