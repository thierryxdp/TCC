def posLetra(frase,letra,numero):
    '''Função que recebe como entrada uma frase, uma letra, e um número que indica a ocorrência desejada para a letra na frase e retorna a posição na frase que a ocorrência se encontra.
       parâmetros de entrada:str,str,int
       valor de retorno:int'''
    ocorrencia=['naoconta',]
    contador=0
    while contador < len(frase):
        if frase[contador] in letra:
            ocorrencia=ocorrencia+[str.index(frase,letra,contador)]
        contador= contador+1
    if numero>(len(ocorrencia)-1):
        return -1
    else:
        return ocorrencia[numero]