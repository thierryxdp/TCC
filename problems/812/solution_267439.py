import re
def retira_pontuacao(texto):
    """
    """
    string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', string_velha.decode('utf-8'))