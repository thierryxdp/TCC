def posLetra(string,letra,vezes):
    '''Diz onde ocorre uma letra em uma string;
    string,string,int -> int'''
    posicao = 0
    ocorrencia = 0
    palavra = list(string)
    if string.count(letra) >= vezes or string.count(letra.upper()) >= vezes:
        while ocorrencia != vezes:
          if letra in palavra[posicao]:
             ocorrencia = ocorrencia + 1
             posicao = posicao + 1 
          
          elif letra not in palavra[posicao]:
              posicao = posicao + 1
          
    else:
        return -1
    
    
    return posicao -1