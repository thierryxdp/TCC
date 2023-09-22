def media_matriz(matriz):
    '''Fazer uma funcao que dada uma matriz de inteiros nao vazia retorne a media desses numeros(round de 2);
    list -> list'''
    
    numero = 0
    
    for i in matriz:
        for j in i:
            numero = numero + [j,]
            
    media = round(sum(numero)/len(numero),2)
    
    return media