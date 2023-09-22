def hashtag(s):
    def hashtag(s):
    '''Retorna palabra com # no início, no meio e no fim.
    Inserir palavra entre aspas.
    str-> str '''
    
    caracter_meio = len(s)//2 #pega a letra do meio usando o tamanho da palavra dividido por 2 e pega só a parte inteira do resultado
    
    parte1 = s[0:caracter_meio] #pega as letras da palavra da primeira até a letra antes da do meio
    parte2 = s[caracter_meio:len(s)] #pega as letra da palavra da letra do meio até a última letra
    
    return '#' + parte1= '#' + parte2 + '#' #retorna a concatenação de strings