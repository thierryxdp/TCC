def posLetra(string,letra,ocorrencia_desejada):
    """ Função que recebe como entrada uma string, uma letra e
        um número que indica a ocorrência desejada da letra.
        Retorna em que posição da string aquela ocorrência da 
        letra está. Caso exista menos ocorrências da letra do 
        que a ocorrência pedida, a função retorna -1;
        string, string, int -> int"""
    ocorrencias = list.count(list(string),letra)
    if ocorrencias < ocorrencia_desejada:
        return -1
    i = 0 #representa a ocorrências da letra
    while i!=ocorrencia_desejada:
        posicao = str.find(string,letra)
        string = str.replace(string,letra,'-',1+n)
        i = i+1 
    return posicao