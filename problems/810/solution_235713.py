def retira_pontuacao(frase):
    '''Dada uma frase a função retorna a mesma mas substituindo todos os caracteres de pontuacao
       por espaço
       str -> str'''
    	frase = frase.replace('-', ' ')
        frase = frase.replace('.', ' ')
        frase = frase.replace(':', ' ')
        frase = frase.replace(',', ' ')                                                                  
    	frase = frase.replace(';', ' ')
        frase = frase.replace('!', ' ')                      
        frase = frase.replace('?', ' ')
        return frase
 
def separa_frase(frase)
	'''Dada uma frase, a função separa suas palavras e retorna uma lista c elas
       str -> lista'''
    frase_sem_pontuacao = retira_pontuacao(frase)
    return str.split(frase_sem_ponto, ' ')

def inverte(frase):
    '''inverte a lista fornecida, apresentando-a de tras para frente
       str -> str'''
    lista1 = separa_frase(frase)
    lista_invertida[::-1]
    return str.join(' ', lista_invertida)