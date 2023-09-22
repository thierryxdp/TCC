def posLetra(string,letra,numero):
    '''
	função que recebe uma string, uma letra e um número que indica a ocorrencia desejada da letra e retorna em que posição da string aquela ocorrencia está;
    str,str,int->int
    '''
    
    indicador = str.replace(string,letra,'Ç',numero)
    return str.find(indicador,'Ç')