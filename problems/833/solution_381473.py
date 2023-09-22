def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    elemento = 0
    contagem = []
    linhas = len(matriz)
    colunas = len(matriz[elemento])
    
    while elemento < colunas:
        if elemento == numero:
            contagem.append(elemento)
            elemento += 1
  		return len(contagem)