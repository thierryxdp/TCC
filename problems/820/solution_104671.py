def posLetra(texto,letra,numero):
    '''Retorna a posição de uma letra em uma dada string, sendo sua ocorrência ditada por um número
    entrada: str, str, int
    saída: int
    '''
    if numero==1:
        indice=str.find(texto,letra)
    else:
        ocorrencias=0
        while ocorrencias<numero:
            if numero <= str.count (texto, letra):
                textoajustado= str.replace(texto,letra,'_',1)
                ocorrencias=0+1 #substitui as ocorrências anteriores por '_'. Note que a função while não é exatamente necessária no caso
            else:
                return -1
        indice=str.find(textoajustado,letra)
    return indice