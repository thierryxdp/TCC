def fatorial(num):
   """dada a entrada, retorna o fatorial desse numero"""
	fat = 1
    i = 2
    while i <= num:
        fat = fat*i
        i = i + 1
    return fat