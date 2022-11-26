
def methods(xi,N):

    g = 6.5
    massive_end = [N]
    for n in range(N):
        massive_end=g*xi
        xi=massive_end
        print(massive_end)

def test_1(self):
    pass


def test_2(self):
    pass

def main():
    being_xi = float(input('Введите значение: '))
    N = int(input('Введите значение: '))
    methods(being_xi,N)


if __name__=='__main__':
    main()