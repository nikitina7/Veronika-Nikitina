import random

def hodi(razmer_pole, ss, vistrel):
    vistrel_vert = int(input('выбери ход  вертикально:(0-' + str(razmer_pole - 1) + '):'))
    vistrel_goriz = int(input('выберите ход гориззонтально:(0-' + str(razmer_pole - 1 ) + '):'))
    if pole[vistrel_goriz][vistrel_vert] == 0:
        pole[vistrel_goriz][vistrel_vert] = 2
        vistrel -= 1
    elif pole[vistrel_goriz][vistrel_vert] == 1:
        pole[vistrel_goriz][vistrel_vert] = 3
        ss -= 1
        vistrel -= 1
    return
def razmer_more(razmer_pole):
    for sea in range(razmer_pole):
        more = [0] * razmer_pole
        pole.append(more)
        list.append(sea)

def korabliki(ss, razmer_pole, pole):        
    while ss < razmer_pole // 2:
        korablik_list = random.randrange(0, razmer_pole)
        korabli = random.randrange(0, razmer_pole)
        if pole[korablik_list][korabli] == 0:
            pole[korablik_list][korabli] = 1
            ss += 1
        else:
            pole[korablik_list][korabli] = 1


pole = [

]

list = [

]
razmer_pole = 10



ss = 0
razmer_korabl = random.randint(0, razmer_pole // 2)

vistrel = razmer_pole * razmer_pole // 2
while True:
    for index, row in enumerate(pole):
        print(index, end='')
        for element in row:
            if element == 0 or element == 1:
                print('💙', end='')
            elif element == 2:
                print('🤍', end='')
            elif element == 3:
                print('💥', end='')
        print('')
    print('здесь есть', str(ss), 'корабли')
    print('у тебя осталось', str(vistrel), 'выстрелов')
    if ss == 0:
        print('все корабли утопились. ты победил')
        break
    if vistrel == 0:
        print('корабли ещё есть, но у тебя не осталось выстрелов')
        for index, row in enumerate(pole):
            print(index, end='')
            for element in row:
                if element == 0 or element == 1:
                    print('💙', end='')
                elif element == 1:
                    print('🤎', end='')
                elif element == 2:
                    print('🤍', end='')
                elif element == 3:
                    print('💥', end='')
            print('')
    break

hodi_def = hodi(razmer_pole=razmer_pole, ss=ss, vistrel=vistrel)
while vistrel > 0:
    print(hodi_def)
    break