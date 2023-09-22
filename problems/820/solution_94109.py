def posLetra (F,L,O):
    "Função que tem string, letra e numero indicando a ocorrência da letra que deve retornar a posição da str daquela ocorrência que a letra está; str, str, int ->int"
    indice = 0
    p = str.find(F,L)
    while indice < O -1: