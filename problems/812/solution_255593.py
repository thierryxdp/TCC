def retira_pontuacao(frase):
    '''Função que recebe uma frase e retorna a frase sem as pontuacoes abaixo
Entrada(lista)
Saída(str)'''
    saida=str.replace(frase,'!',' ')
    saida=str.replace(saida,'?',' ')
    saida=str.replace(saida,'-',' ')
    saida=str.replace(saida,',',' ')
    saida=str.replace(saida,':',' ')
    saida=str.replace(saida,';',' ')
    saida=str.replace(saida,'.',' ')
    return saida