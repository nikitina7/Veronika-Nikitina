def zvaigzne(user_text):
    new_text = ""
    ff = list(user_text)
    for simb in ff:
        if simb == " ":
            new_text += " "
        else:
            new_text += "*"
    return new_text


def index_burti(input_text, burts):
    start = 0
    index1 = []
    for burti in range(input_text.count(burts)):
        index = input_text[start:].find(burts)
        if index != -1:
            index1.append(start + index)
        start += index + 1
    return index1


def return_burti(text_zvaigz, burtu_index, user_burts):
    list_text = list(text_zvaigz)
    for index in burtu_index:
        list_text[index] = user_burts
    text_norm = "".join(list_text)
    return text_norm


user_teksts = input('ievadiet tekstu: ')

text_star = zvaigzne(user_text=user_teksts)

print(text_star)

user_letter = input('ievadiet burtu: ')

index_of_letter = index_burti(user_teksts, user_letter)

norm_text = return_burti(text_star, index_of_letter, user_letter)

print(norm_text)

while "*" in norm_text:
    user_letter = input('ievadiet burtu: ')
    index_of_letter = index_burti(user_teksts, user_letter)
    norm_text = return_burti(norm_text, index_of_letter, user_letter)
    print(norm_text)
