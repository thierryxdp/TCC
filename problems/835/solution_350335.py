#Exercício_04:
''' Essa função recbe uma matriz 6x10 que contem o tempo dos pilotos e retorna o piloto do menor tempo, o tempo e a 
    volta que ele foi feito. '''
''' list ---> tuple. '''

def melhor_volta(matriz):
    
    nlin = len(matriz)
    ncol = len(matriz[0])
    list_numbers = []
    
    for i in range(nlin):
        for j in range(ncol):
            list_numbers += [matriz[i][j], ]
    
    list.sort(list_numbers)
    mt = list_numbers[0]
    
    corredor = ''
    volta = ''
    
    for i in range(nlin):
        for j in range(ncol):
            if matriz[i][j] == mt:
                corredor = 'corredor_' + str(i+1)
                volta = str(j+1) + '° volta'
                tempo = str(mt) + ' minutos'
                return (corredor, tempo + " na " + volta)