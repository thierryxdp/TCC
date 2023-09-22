def maiores(input_list):
    input_list.sort()
    tops=input_list[-3:]
    q=sorted(tops, reverse=True)
    return q