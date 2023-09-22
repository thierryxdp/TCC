def conta_numero(numero, matriz):
    """Função que me dado um nuemro inteiro e uma matriz de numeros inteiros de qualquer tamanho
conta ela e me retorna quantas vezes este numero aparace na minha matriz de entrada
    matriz. int, list-->int."""
    aparece = 0
    for m in matriz:
        for inteiro in matriz:
            if inteiro == numero:
                aparece = aparece + 1
    return aparece