def retira_pontuacao(frase):
    '''Faça uma função que retorne uma frase sem pontuacao, minúscula, str -> str'''
    pontuacao = str(' ')
    return str.lower(str.replace(frase,',',pontuacao).replace('.',pontuacao).replace('-',pontuacao).replace('?',pontuacao).replace('!',pontuacao))
    
def inverte(oracao):
    '''Faça uma funcao que retorne uma frase invertida, str, list -> str'''
    inverter = list(oracao)
    return oracao