def substitui(s,x,i):	
'''Funcao que recebe uma string (s), um numero inteiro (i) entre 0 e 
o comprimento da string, retornando uma string igual a (s), onde a posicao i sera substiruida
pelo caractere x'''
nova_string = s[0:i]+str(x)+ s[i+1:]