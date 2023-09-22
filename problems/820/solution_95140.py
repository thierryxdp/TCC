def Letra(string,letra,ocorrencia):
    '''Retorna a posição dentro da string
       em que a letra está de acordo com
       a ocorrência inserida;str,str,int->int'''
    
    ''' A idei principal desta funcao
        é fazer com que voce escreva a sua
        funcao "index", sendo assim Nao 
        pode usa-la'''
        
    # contagem=str.count(string,letra)
    indice=0
    ocorrenciaDaVez = 0
    #tamanho=len(string)-1 # Nao consegui entebdee como essevparametro vai te ajudar a seguir com o laco de repeticao
    while ocorrenciaDaVez<ocorrencia:
        # index=str.index(string,letra,ocorrenciaDaVezz
        # Veriricando se é uma ocorrencia
        if string[indice] == letra:
            ocorrenciaDaVez += 1
            indice+=1 # A atualizacao deve estar dentro do while
    return indice