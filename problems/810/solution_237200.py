def inverte(frase):
    '''Função que dada uma frase retorne a mesma sem pontuação e com letra maíscula
    Entrada(str e list)
    Saída(str)'''
    saida=str.replace(frase,'!',' ')
    saida=str.replace(saida,'?',' ')
    saida=str.replace(saida,'-',' ')
    saida=str.replace(saida,',',' ')
    saida=str.replace(saida,':',' ')
    saida=str.replace(saida,';',' ')
    saida=str.replace(saida,'.',' ')
    saida=str.lower(saida)
    saida=str.split(saida)
    saida=saida[len(saida)::-1]
    saida=str.join(' ',saida)
    return saida