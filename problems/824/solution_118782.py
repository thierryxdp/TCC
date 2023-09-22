def uppCons(cont_frase)
    '''
    função que retorna todas as consoantes de uma frase em maiusculo após recebe-la como entrada
    str->str
    '''
    
    letras_Consoantes=[]
    contador=0
    while contador<len(cont_frase):
        if cont_frase[contador] not in 'aeiouãóúíé':
            letras_Consoantes= letras_Consoantes+ [str.upper(cont_frase[contador])]
        else:
            letras_Consoantes= letras_Consoantes+ [cont_frase[contador]]
        contador=contador+1
    return str.join('',letras_Consoantes)