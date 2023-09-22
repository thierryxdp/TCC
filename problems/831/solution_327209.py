def lingua_p(word):
    lword_ = word.lower()
    pword = ""
    for i in range(0, len(lword_)):
        if lword_[i] in "aeiou":
            pword += lword_[i] + "p" + lword_[i]
        else:
            pword += lword_[i]
    return pword