def retira_pontuacao(frase):
	""" Essa função irá retirar a pontuação de uma frase que será definida na varíavel
    frase e irá retornar essa varíavel sem pontuaçãp
    Entrada: String | Saída: String
    """
    frase = frase.replace('-', ' ').replace(', ', ' ').replace(':', ' ').replace(';', ' ').replace('!', ' ').replace('?', ' ').replace('...', ' ').replace('.', ' ')
    return frase

def inverte(frase):
    """Essa função irá inverter uma frase dada pela variável frase. Além de ter sua saída 
    como uma frase invertida, ela será devolvida sem pontuação.
    Entrada: String | Saída: String
    """
    frase = retira_pontuacao(frase)
    lista = frase.split(' ')
    lista.reverse()
    lista.remove('')
    frase = str.join(' ', lista).lower()
    return frase