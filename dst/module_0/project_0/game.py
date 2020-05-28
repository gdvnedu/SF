def game_core_v3(number):
    '''Начинаем угадывать с середины отрезка. Далее ограничиваем отрезок поиска медианой списка чисел
    между максимальным и минимальным значением. Для начала поиска минимум = 1, максимум = 100, медиана 50'''
    count = 1
    predict = 50
    minimum = 1
    maximum = 100
    while number != predict:
        count+=1
        if number > predict:
            minimum = predict
            predict = (maximum + minimum + 1) // 2
        else:
            maximum = predict
            predict = (maximum + minimum) // 2
    return count


print(game_core_v3(10))