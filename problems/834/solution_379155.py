def media_matriz(matriz):
    '''Fazer uma funcao que dada uma matriz de inteiros nao vazia retorne a media desses numeros(round de 2);
    list -> list'''
    
    numero = []
    
    for linha in matriz:
        for coluna in linha:
            numero = numero + [coluna,]
            
    media = round(sum(numero)/len(numero),2)
    
    return media