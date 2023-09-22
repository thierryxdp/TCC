from string import punctuation

def retira_pontuacao(frase):
    """Função que, dada uma frase, retona a mesma, porém sem caracteres de pontuação.
    string -> string."""
    
    #lista = frase.split()
    #erro = ['!', ',', '.', '?']
    
    #for i in range(len(lista)):
     #   if erro in lista[i]:
      #      return str.replace(lista, '!', ' ')
    
    sem_pont = frase.translate(str.maketrans('', '', string.punctuation))
    
    return sem_pont