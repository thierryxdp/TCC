def retira_pontuacao(frase):
    '''Função que, dada uma frase(frase), retorna a frase com todos os caracteres de pontuação substituídos por espaço.
    parâmetro de entrada: str
    valor de retorno: str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    return frase