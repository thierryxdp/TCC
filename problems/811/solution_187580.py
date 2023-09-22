def colchao(lista,altura = 1,largura = 1):

    """
        Função que verifica se um colchão passa ou não por uma porta

        (1) A função recebe como entrada uma lista contendo a dimensão do colchão (altura, largura e profundidade) e duas outras variáveis que são a altura e a
            largura da porta.
        (2) A função retorna um boleano, se o colchão passar pela porta a função retorna True, caso contrário retorna False.
        (3) Caso o usuário coloque um valor menor, ou igual, a 0 a função avisa que algum valor inválido foi inserido:
            ex:
                verifica_cochao([-1,2,3],4,1)

                retorno --> a lista que contem as dimensões do colchão tem um valor menos ou igual a 0, coloque um valor valido!
                
        (4) Para que o colchão consiga passar pela porta pelo menos duas das suas dimensões devem ser menor ou do mesmo tamanho que a largura ou a altura, para
            verificar se isso é verdade foi criada a variável cont. Caso essa variavel seja maior ou igual a 2 o colchão vai conseguir passar pela porta, caso
            contrário isso não será possível.
        
        
        caso seja iserido valores validos       ==>  list,float or int,float or int --> bool
        caso algum valor invalido seja inserido ==>  list,float or int, float or int --> str

        (5) Para ordenar a lista de entrada utilizamos a função .sort(), assim a lista foi ordenada do menor para o maior elemento.
        
    """

    lista.sort()
    cont = 0
    
    for i in [altura,largura]:
        if altura <= 0:
            return "Valor de altura menor ou igual a 0, coloque um valor valido!"
        elif largura <= 0:
            return "Valor de largura menor ou igual a 0, coloque um valor valido!"
    for j in lista:
        if j <= 0:
            return "A lista que contem as dimensões do colchão tem um valor menor ou igual a 0, coloque um valor valido!"

    for k in lista:
        if k <= altura:
            cont += 1
        elif k <= largura:
            cont += 1
    if cont >= 2:
        return True
    else:
        return False