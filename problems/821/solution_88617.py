# Dado um número, queremos seu fatorial.
# Resolução:
# 1. Se o número é zero, fatorial é 1;
# 2. Se é positivo, multiplica o numero por seu antecessor;
# 3. Multiplica (2) pelo antecessor do antecessor do numero inicial;
# 4. Repete até chegar a 1;
# 5. Se o número for negativo, calcula o fatorial de
#    seu simétrico e acrescenta um sinal negativo;
# 6. Devolve

def fatorial(numero: int) -> int:
    '''Dado um número, devolve seu fatorial'''
    i = numero
    fatorial = numero
    if (numero == 0):
        fatorial = 1
    elif (numero > 0):
        while (i != 1):
            numero -= 1
            fatorial = fatorial * numero
            i -= 1
    else:
        fatorial = -fatorial(-numero)
    return fatorial