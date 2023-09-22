def retira_pontuacao(frase):
    '''funcao que recebe uma frase e retorna a frase em que caracteres de pontuacao sao trocados
    por espaco; str -> str'''
    resposta = str.replace(frase,',',' ')
    resposta1 = str.replace(resposta,':',' ')
    resposta2 = str.replace(resposta1,'-',' ')
    resposta3 = str.replace(resposta2,'.',' ')
    respostafinal = str.replace(resposta3,';',' ')
    return respostafinal