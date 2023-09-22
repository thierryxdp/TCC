def posLetra(string,letra,numero):
    '''Função que retorna a posição da string que a ocorrência está
       str,str,int->int'''
    if str.count(string,letra)<numero:
        return -1
        else: cont = 0
            ocorrencia = 0
            while ocorrencia<numero:
                if string[cont] == letra:
                    ocorrencia = ocorrencia+1
                    cont=cont+1
                    return cont-1