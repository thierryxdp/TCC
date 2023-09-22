def filtra_pares(t):
     for i in t:
            #Aqui faremos um loop para cada item na tupla, caso ele não for inteiro um aviso será dado, e aquela lista inicial será limpa, para que quando o loop for parado pelo break, o resultado estar vazio.
            if type(i) != int:
                return "todos os itens devem ser inteiros"
             elif i%2 == 0:
                 #Se ele for inteiro e par, será adicionado à lista.
                 lista.append(i)