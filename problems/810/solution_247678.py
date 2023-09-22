### funcao da questao anterior
def retira_pontuacao(frase):
    """Essa função substitui toda a pontuação de uma frase por espaço
    string --> string"""
    
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"..."," "),"."," "),","," "),":"," "),";"," "),"!"," "),"?"," "),"-"," ")



### funcao dessa questao

def inverte(frase):
    """Essa função inverte a posição das palavras dado uma string
    string --> string"""
	
    # retira a pontuacao e transforma em minusculo
   	y = str.lower(retira_pontuacao(frase))
	
    # retira espacos no final e comeco da frase
    # divide a atring em uma lista, inverte a posição e concatena
    z = str.join(" ",list.reverse(str.split(str.strip(y," "))))

    return z