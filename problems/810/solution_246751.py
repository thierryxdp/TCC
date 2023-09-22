def retira_pontuacao(texto):
    """ Função que retira a pontuação de uma frase sobre uma str.
    entr>str de lista criada
    saida> str da frase sem pontuação.
   """
    resp=(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'.',' '),',',' '),':',' '),';',' '),'-',' '),'!',' '),'?',' '))
    return resp


def inverte(texto):
    """Função que retorna um exto de trás para frente(invertido).
    Meio de Codificação de mensagens.
    *obs: Utiliza outra função já inserida(retira_pontuacao)
    ent> texto através de uma string
    saida> texto/frase sem pontuação e codificada
 """
    alfa=(retira_pontuacao(texto))
    beta=texto.invert(alfa)