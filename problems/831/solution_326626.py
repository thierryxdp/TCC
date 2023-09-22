def linguas_p(palavra):
    
    palavra.lower()
    vogal=áaaaaaeeeeiiioooouuuu'
    string=str()
    for i in palavra: 
        if i in vogal:
            string += 1 + 'b'+ 1
        else:
            string= ''
    return string