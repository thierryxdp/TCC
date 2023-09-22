import string #Importando a biblioteca string.

def conta_caracter(c):
    
    nova_frase = frase #Criando uma variável baseada na entrada, para ser modificada.
	pontuacao = string.punctuation #Usando um recurso da biblioteca string para gerar todos os caracteres.
     
    for i in pontuacao:
    	nova_frase = nova_frase.replace(i, " ") #Trocando todos os caracteres que estiverem em string.punctuation por espaço na variável.
    
    return nova_frase
    
    #pontuacao = [string.punctuation]
    
    #return ' ' if c in pontuacao else c

def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a mesma, porém sem os caracteres de pontuação.
    string -> string. """    
	
	lista = str.join('', map(conta_caracter, frase))
    
    return lista