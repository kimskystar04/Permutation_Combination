import itertools
import copy
import time


def fac(n):
    if n <= 1:
        return 1
    return n * fac(n - 1)


def pmt(n, r):
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result


def cbn(n, r):
    result = pmt(n, r)

    for i in range(r, 1, -1):
        result //= i
    return result


def drawfac(n):
    print()
    print(str(n) + "! 의 값은 ", end="")
    for i in range(n, 1, -1):
        print(str(i) + " X ", end="")
    print('1 이므로,  ' + str(fac(n)) + " 이다!")


def drawpmt(data, r):
    full_length = pmt(len(data), r) * 4
    bigdata = [[] for _ in range(r + 1)]
    tmp = copy.deepcopy(data)
    bigdata[1].append(tmp)
    count = 1

    while count < r:
        for i in bigdata[count]:
            for k in range(len(i)):
                temp = copy.deepcopy(i)
                temp.pop(k)
                bigdata[count + 1].append(temp)
        count += 1

    raw = [len(data)]
    for t in range(r - 1):
        raw.append(raw[-1] * (len(data) - t - 1))
    former_temp = 0
    now = len(data) - 1
    for i in bigdata[1:]:
        temp = []
        for j in i:
            temp += j

        if len(temp) != raw[0]:
            lt = len(temp)
            if len(temp) == former_temp:
                for k in temp:
                    print(" " * ((full_length // len(temp)) // 2 - 1) + "|" + " " * ((full_length // len(temp)) // 2),
                          end="")

            else:
                while lt > 0:
                    print(" " * ((full_length // len(temp)) // 2 - 1) + " " + "-" * ((full_length // len(temp)) // 2),
                          end="")
                    lt -= 1
                    for s in range(now - 2):
                        print(
                            "-" * ((full_length // len(temp)) // 2 - 1) + "-" + "-" * ((full_length // len(temp)) // 2),
                            end="")
                        lt -= 1
                    print("-" * ((full_length // len(temp)) // 2 - 1) + " " + " " * ((full_length // len(temp)) // 2),
                          end="")
                    lt -= 1
                now -= 1
        print()

        if len(temp) != raw[0]:
            for k in temp:
                print(" " * ((full_length // len(temp)) // 2 - 1) + "|" + " " * ((full_length // len(temp)) // 2),
                      end="")
        print()
        for k in temp:
            print(" " * ((full_length // len(temp)) // 2 - 1) + str(k) + " " * ((full_length // len(temp)) // 2),
                  end="")
        print()
        # 여기 있는 time.sleep가 한 줄씩 텀을 두고 쉬어가게 해주는 것.  괄호 안의 숫자를 10으로 하면 10초간격으로 한 줄 씩 나옴.
        time.sleep(1.5)
        if len(temp) != pmt(len(data), r):
            for k in temp:
                print(" " * ((full_length // len(temp)) // 2 - 1) + "|" + " " * ((full_length // len(temp)) // 2),
                      end="")
        print()
        print()
        former_temp = len(temp)

    print(
        str(len(data)) + " P " + str(r) + " 의 모든 경우 위와 같고, 총 갯수는 " + str(pmt(len(data), r)) + " 입니다! by 김민규-평촌고1Coding")


def drawcbn(data, r):
    print()
    result = list(itertools.combinations(data, r))
    for i in result:
        print(i)
    print()
    print(
        str(len(data)) + " C " + str(r) + " 의 모든 쌍은 위와 같고, 총 갯수는 " + str(cbn(len(data), r)) + " 입니다! by 김민규-평촌고1Coding")


# 일단 먼저, 팩토리얼, 순열, 조합의 "갯수"만을 출력해주는 것

# 1. 팩토리얼
# print(fac(n))

# 2. 순열
# print(pmt(n,r))

# 3. 조합
# print(cbn(n,r))

# 팩토리얼, 순열, 조합이 어떤 과정에 의해 위와 같은 값들이 나왔는지

# 1. 팩토리얼
# drawfac(n)

# 2. 순열
# drawpmt([n],r)

# 3.조합
# drawcbn([n],r)

drawpmt(["김민규","김성우","이미나","권추자","이재욱"],5)
