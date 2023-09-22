def inverte(frase):
    saida=str.replace(frase,'!',' ')
    saida=str.replace(saida,'?',' ')
    saida=str.replace(saida,'-',' ')
    saida=str.replace(saida,',',' ')
    saida=str.replace(saida,':',' ')
    saida=str.replace(saida,';',' ')
    saida=str.replace(saida,'.',' ')
    saida=str.lower(saida)
    saida=saida[len(saida)::-1]
    saida=str.join(' ',saida)
    return saida