qnt = {}
frase = str(input('Digite uma frase para vermos quantas vezes cada palavra aparece: '))
frase = frase.split()
for i in range(len(frase)):
    qnt[frase[i]] += 1