def carros(pessoas, capacidade = 5):

    '''
        informados a quantidade de pessoas e quanto os carros comportam
        retorna quantos carros serão necessários para a viagem

        caso não seja informada a capacidade dos carros
        assume-se que os carros possuem capacidade convencional

        int, int -> int
    '''

    import math
    return math.ceil(pessoas/capacidade)