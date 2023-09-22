def posLetra(string,letra,ocorrencia):
    """retorna em que posição da string a
ocorrencia da letra está
ex: posLetra('Leonardo lindo','l',2)
--- 9"""
    i=0
    if  str.find(string[ocorrencia:len(string)+1],letra) == -1:
        #função para voltar a primeira posição da letra a partir da ocorrencia
        #utilizado o 'len + 1' para pegar o resto da frase toda

        return -1
    else:

        posicao = str.find(string[ocorrencia:len(string)+1],letra,ocorrencia) + ocorrencia
 
        return posicao