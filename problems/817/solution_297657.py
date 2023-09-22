def acima_da media (media):
    '''funcao que retorne a nota acima da media e em ordem '''
notas = [0,0,0,0,0,0,0]
soma = 0
x = 0
while x < 5:
     notas[x] = float(input("Nota %d:" % x))
     soma += notas[x]
     x += 1
x = 0
while x < 5:
     return("Nota %d: %6.2f" % (x, notas[x]))
     x += 1
return("Média: %5.2f" % (soma/x))