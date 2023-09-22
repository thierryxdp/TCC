def media_matriz(matriz):
    '''Função que Calcula a media de todos numeros
       da matriz, com duas casas decimais, sendo eles inteiros;
       list => float'''
    soma = ()
    contador = 0 
    
    for i in matriz:
        for e in i:
            soma = soma + e
            contador += 1
            
    media = soma/contador
    return round(media, 2)