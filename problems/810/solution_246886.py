def inverte (frase):
    '''
    função que dada uma frase podendo conter pontos e maiúsculas, retira os pontos e coloca a frase toda dada como parâmetro
    em minúscula e retorna a frase na ordem inversa
    str--->str
    '''
    texto1= str.replace(frase,"?"," ")
    texto2= str.replace(texto1,","," ")
    texto3= str.replace(texto2,"."," ")
    texto4= str.replace (texto3,"..."," ")
    texto5= str.replace (texto3,"!"," ")
    texto6= str.replace (texto3,"-"," ")
    minusculas=str.lower(texto6)
    ao_contrario= str.join(' ',(str.split(minusculas, ' ')[::-1]))
    
    return  ao_contrario