def uppCons(phrase):
    answer = ""
    i = 0
    while i < len(phrase):
        if phrase[i] not in "aãeéêiíoóôõuuúAEIOU":
            answer = answer + phrase[i].upper()
        else:
            answer = answer + phrase[i]
        i += 1
    return answer