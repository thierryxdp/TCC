def posLetra(palavra,letra,n):
    ''' '''
    ocorrencia= str.count(palavra,letra)
    ocorrencia2=str.find(palavra,letra,ocorrencia[n])
   
    return ocorrencia2