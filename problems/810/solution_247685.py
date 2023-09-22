### funcao da questao anterior
def retira_pontuacao(frase):
    """Essa função substitui toda a pontuação de uma frase por espaço
    string --> string"""
    
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"..."," "),"."," "),",",""),":"," "),";"," "),"!"," "),"?"," "),"-"," ")

### funcao dessa questao

def inverte(frase):
    """Essa função inverte a posição das palavras dado uma string
    string --> string"""

    # retira a pontuacao
    x = retira_pontuacao(frase)
	
    # retira espacos no final e comeco da frase
    # divide a string em uma lista, inverte a posição e concatena
    y = str.split(str.strip(x," ")," ")
    list.reverse(y)
    z = str.join(" ",y)

    # retorna as letras em minusculo
    return str.lower(z)