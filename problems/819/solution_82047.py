def filtraMultiplos (l_num: list[int], div:int = 1) -> list[int]:
    #Inicializando contador e acumulador
    i = 0
    lista_retorno = []
    #Criando while para percorrer lista
    while i < len(l_num):
        #Verificando se o número na posição i é divisível por div
        if l_num[i]%div == 0:
            #Adicionando o número da posição i na lista de retorno
            lista_retorno.append(l_num[i])
            
        i += 1
        
    return lista_retorno