def retira_pontuacao (frase):
    '''Função que retira a pontuação de uma frase
    string -> string'''
import re 
string_nova = re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ: ]', '', string_velha.decode('utf-8'))