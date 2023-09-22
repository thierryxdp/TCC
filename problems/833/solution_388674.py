def conta_numero(numero,matriz):
    """Calcula e retorna quantas vezes um termo(numero) aparece na matriz;
    int, list --> int"""
    repeticao=0
    for i in matriz:
        for numero in i:
            repeticao=repeticao+1
    return repeticao