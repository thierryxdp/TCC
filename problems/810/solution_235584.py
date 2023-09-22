def inverte(frase):
    saida=str.replace(frase,'!',' ')
    saida=str.replace(saida,'?',' ')
    saida=str.replace(saida,'-',' ')
    saida=str.replace(saida,',',' ')
    saida=str.replace(saida,':',' ')
    saida=str.replace(saida,';',' ')
    saida=str.replace(saida,'.',' ')
    saida=saida[::-1]
    return saida