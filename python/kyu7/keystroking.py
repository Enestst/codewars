def num_key_strokes(text):
    one_type = "qazwsxedcrfvtgb yhnujmik,./l;o'p][`1234567890-\="
    sum = 0
    for i in text:
        if i in one_type: sum += 1
        else: sum+=2
    return sum
