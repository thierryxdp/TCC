ef acima_da_media(grades):
    above_avg = []
    mean_val = sum(grades)/len(grades)
    for i in range(len(grades)):
        if grades[i] > above_avg:
            above_avg.append(grades[i])
    return above_avg