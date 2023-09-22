def total(lista,dicionario):
    '''Funcao que pega a lista de entrada, verifica quais produtos da lista estão contidos no dicionário de entrada
    	pega o contéudo das chave do dicionário. Por fim retorna a soma dos contéudos da chave.
        list,list→float
        dict,dict→float'''
    soma=0
    for produto in lista:
        valor=dicionario[produto]
        soma= soma + valor    
    return round(soma,2)