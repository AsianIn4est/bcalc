def getfromuser():
    k = [float(i) for i in input().split(" ")]
    return k


def truekef(k):
    p = 1 / k * 100
    p2 = 1/(100 - p)*100
    return round(p2, 1)

def calckef(k):
    return [1/ki*100 for ki in k]


def morj(k):
    s = sum(calckef(k))
    return s - 100 if s > 100 else 0


if __name__ == '__main__':
    print("Привет! Введи кеф. через пробел. Или одно число:")
    while 1:
        try:
            k = getfromuser()
            if len(k) == 1:
                try:
                    t = truekef(k[0])
                    print("Реальный кеф с другой стороны:\t", t)
                except:
                    print("Ты ошибся, будь внимательней!")
            else:
                p = calckef(k)
                print("Вероятности:\t", [str(round(x, 1)) + "%" for x in p])
                print("Маржа:\t", round(morj(k), 1), "%")
        except:
            print("Некорректный ввод!")

