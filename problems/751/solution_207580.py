# Dada uma frase, queremos o número de palavras que ela
# possui.
# Resolução:
# 1. Aplica a função str.strip a fim de eliminar os
#    espaços no início e no final, se existirem;
# 2. Então, ao resultado acima, aplica a função str.split
#    a fim de devolver uma lista com os elementos da
#    string que antes eram espaçados, ou seja, as palavras;
# 3. Ao resultado obtido aplica a função len a fim de contar
#    os elementos da lista;
# 4. Devolver.

# string -> int

def quant_palavras(frase):
    """Dada uma frase, queremos o número de palavras 
    que ela possui
    str -> int"""
    return len(str.split(str.strip(frase)))