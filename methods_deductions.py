import time

class Deductions:
    def methods(self,xi, N):

        g = 6.5
        massive_end = []
        for n in range(N):
            xi_end = g * xi
            massive_end.append(xi_end)
            xi = massive_end[n]
            print(massive_end[n])
            time.sleep(0.5)
        print('\nВесь массив:')
        print(massive_end)

    def test_1(self):
        deductions=Deductions()
        xi_0 = 0.0015
        N = 12
        deductions.methods(xi_0, N)

    def test_2(self):
        deductions = Deductions()
        xi_0 = 0.005
        N = 12
        deductions.methods(xi_0, N)

def main():
    deductions=Deductions()
    print('Тестирование программы запущено')
    print('\nПервый тест:')
    deductions.test_1()
    print('\nВторой тест:')
    deductions.test_2()
    print('\nТестированние программы завершено!')


if __name__=='__main__':
    main()