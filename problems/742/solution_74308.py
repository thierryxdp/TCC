def substitui (s,x,i):
'''Substitui letra na posição escolhida. Inserir palavra entre aspas.
str--> str'''

parte1 = s [0:i]
parte2 = s [i+1:len(s)]
return parte1 + x + parte2