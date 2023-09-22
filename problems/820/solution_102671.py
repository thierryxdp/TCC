def posLetra(string,letra,n):
    '''Função que recebe como entrada uma string, um letra e
o número que indica a ocorrência dessa letra, e retorna a
posição da letra na string. Caso exista menos ocorrências da
letra do que a ocorrência de entrada, a função retorna -1;
    str,str,int -> int'''
    indice=0
    ocorrencia=0
    proximo=0
    while ocorrencia<n:
        indice=str.find(string,letra,proximo)
        proximo=indice+1
        ocorrencia=ocorrencia+1
    return indice