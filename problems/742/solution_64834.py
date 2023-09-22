'''Função que separa a string 's' em 2 partes, dependendo do valor int 'i' da posição que
for inserido.em duas partes, uma até a posição 'i', outra 1 termo acima de 'i' que vai
até o fim da string. No final, ela concatena as duas variáveis + a letra adicional 'x' '''




def substitui(s,x,i):
    H= s[0:i]
    U= s[i+1:len(s)]
    return H+x+U