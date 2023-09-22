### funcao da questao anterior
def retira_pontuacao(frase):
    """Essa função substitui toda a pontuação de uma frase por espaço
    string --> string"""
    
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"..."," "),"."," "),","," "),":"," "),";"," "),"!"," "),"?"," "),"-"," ")



### funcao dessa questao

def inverte(frase):
    """Essa função inverte a posição das palavras dado uma string
    string --> string"""
	
    x = retira_pontuacao(frase)
    
    # retira a pontuacao e transforma em minusculo
   	
	
    # retira espacos no final e comeco da frase
    # divide a atring em uma lista, inverte a posição e concatena
    y = str.join(" ",list.reverse(str.split(str.strip(x," "))))

    z = str.lower(y)
    
    return z