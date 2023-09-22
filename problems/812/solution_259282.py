import string #Importando a biblioteca string.

def retira_pontuacao(frase):
    """Função que, dada uma frase, retorna a mesma, porém sem os caracteres de pontuação.
    string -> string. """
    
    nova_frase = frase #Criando uma variável baseada na entrada, para ser modificada.
	pontuacao = string.punctuation #Usando um recurso da biblioteca string para gerar todos os caracteres.

    for i in pontuacao:
    	nova_frase = nova_frase.replace(i, " ") #Trocando todos os caracteres que estiverem em string.punctuation por espaço na variável.
	
lista = map(retira_pontuacao, frase)

return lista