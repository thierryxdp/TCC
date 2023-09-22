# Dada uma lista de números e um número n,
# queremos retornar uma lista com os múltiplos
# de n na lista inicial.
# Resolução:
# 1. Definir lista vazia para conter os múltiplos;
# 2. Se o resto da divisão do i-ésimo elemento da lista
#    inicial por n for zero, adcioná-lo à lista de (1);
# 3. Repetir de i = 0 até i = tamanho da lista menos 1;
# 4. Devolver a nova lista.

def filtraMultiplos(lista_numeros: list, n: int) -> list:
    '''Dada uma lista de números e um número n,
    retorna uma lista com os múltiplos de n na 
    lista inicial'''
    listaMultiplos = []
    i = 0
    while (i < len(lista_numeros)):
        if (lista_numeros[i] % n == 0):
            list.append(listaMultiplos, lista_numeros[i])
        i += 1
    return listaMultiplos