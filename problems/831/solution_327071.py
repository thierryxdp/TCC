def lingua_p(palavra):
    palavra = palavra.lower()
    palavra_p = []
    
    for i in palavra:
        if i in "aãáàâeéèêiíìîoóòôuúùû":
            palavra_p.append(i+"p"+i)
        else:
        	palavra_p.append(i)
    palavra_p = (''.join(palavra_p))
    return palavra_p

# Primeiro, transformamos a palavra recebida totalmente em minúscula utilizando
# o método lower() e após isso criamos uma lista vazia, onde será armazenado 
# posteriormente nossa palavra na lingua p.

# Utilizando o método for, percorremos todas as letras da palavra passada como
# parâmetro e, caso seja uma consoantes, adicionamos a consoante à lista que
# criamos anteriormente e, caso seja uma vogal, adicionamos a vogal + p + vogal
# novamente.

# No final, apenas utilizamos o método join para juntar a lista em uma única palavra
# utilizando o método join().