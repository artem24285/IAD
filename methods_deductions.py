import time

class Deductions:

    massive_end = []

    def D(self,xi):
        return xi-int(xi)
    @classmethod
    def get_massive(cls):
        return Deductions.massive_end


    def method(self, xi, N):
        deductions = Deductions()
        g = 6.5
        for n in range(N):
            xi_end = (g * xi)
            Deductions.massive_end.append(xi_end)
            xi = Deductions.massive_end[n]
        #     time.sleep(0.45)
        #     print('Итерация: ',n,', результат: ',Deductions.massive_end[n])
        #     print(deductions.D(xi))
        # print('\nВесь массив:')
        # print( Deductions.massive_end)
        return Deductions.massive_end


    def test_1(self,N):
        deductions=Deductions()
        xi=0.00025
        deductions.method(xi,N)
        print('New massive')
        testing_massive = []
        test_massive=[]
        testing_massive.append(Deductions.massive_end)
        for xi_j in testing_massive:
            for j in xi_j:
                p=xi_j
                print(p)





def main():
    N = int(input('Введите N: '))
    xi=0.25
    deductions=Deductions()
    print('\nТестирование программы запущено')
    print('\nПервый тест:')
    deductions.test_1(N)


    print('\nТестированние программы завершено!')


if __name__=='__main__':
    main()