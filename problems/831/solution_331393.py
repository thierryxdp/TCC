def lingua_p(palavra):
    palavra.lower
    palavranova=palavra
    for i in range(len(palavra)):
        if palavra[i] in "aeiou":
    		palavranova = palavranova + palavranova[0+i:i+1]+"p"+palavra[i]+palavranova[i+1:-1-i]
  
    return palavranova