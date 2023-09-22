def lingua_p(x):
    x = x.lower()
    word = []
    for i in range(len(x)):
        if (x[i] == 'a' or 'e' or 'i' or 'o' or 'u'):
            return word.append('p')
           
        else:
            return word.append(x[i])