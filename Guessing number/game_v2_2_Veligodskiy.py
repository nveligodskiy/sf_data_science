import numpy as np
def game_core_v5(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    a=range(1,101)#since we need to guess NUMBER in range from 1 till 100 we can just use ordinar range of all possible values 
    mid=len(a)//2 #then we create minimum maximum and middle values with is related to position on list a
    low=0
    high=len(a)
    while a[mid]!=number and low<=high:# and create cykle for binary search among all possible vallues to guess our NUMBER
        count+=1
        if number>a[mid]:
            low=mid+1
        else:
            high=mid-1
        mid=(low+high)//2

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