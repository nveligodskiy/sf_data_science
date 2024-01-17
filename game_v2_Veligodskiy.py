import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    predict = np.random.randint(1, 101)
    #I choose human logic when we guess certain number, so when we need to guess something we input number,
    #in depence if it is big or small we try to decrease or increase it in two times
    if predict>number:
        number=int(number*2)
    else:
        number=int(number/2)
    #then after we doubled number we need act more carefully and perfrom summm or deduction with less amount in each stage of iteration
    if predict>number:
        number+=12
    else:
        number=number-12

    if predict>number:
        number+=7
    else:
        number=number-7
    
    if predict>number:
        number+=3
    else:
        number=number-3
    
    while number!=predict:
        count+=1            
        if number >= predict:
            predict += 1
        elif number < predict:
            predict -= 1
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")