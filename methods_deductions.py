import time
import functools

class Deductions:

    massive_end = []
    testing_massive = []
    main_massive=[]
    massive_check=[0.0016, 0.211,0.584,1.06,1.61,2.20,2.83,3.49,4.17,4.86,5.6,6.3,7.0,7.8,8.5,9.3,10.1,10.9,11.7,12.4]

    @classmethod
    def get_massive(cls):
        return Deductions.massive_end

    def D(self,xi):
        return float(xi)-int(xi)

    def methods(self, xi, N):
        deductions = Deductions()
        g = 6.5
        xi_l=xi
        deductions.massive_end = []

        for n in range(N):

            xi_n=deductions.D(xi_l)*(g*xi)
            deductions.massive_end.append(xi_n)
            xi_l=deductions.massive_end[n]
            print('Итерация: ',n,', результат:',xi_n)
            
        return deductions.massive_end

    def uniformity(self,xi,N):
        deductions=Deductions()
        xi_l = xi
        g = 6.5
        deductions.main_massive=[]

        for j in range(N):
            xi_n = deductions.D(xi_l) * (g * xi)
            deductions.testing_massive.append(xi_n)
            xi_l = deductions.testing_massive[j]
            p=xi_n-xi
            X=(deductions.testing_massive[j]-(p*N))**2/(p*N)
            deductions.main_massive.append(X)

        sumMassive=sum(deductions.main_massive)
        print('Значение Хи_квадрат:',sumMassive)
        if functools.reduce(lambda x, y: x and y, map(lambda p, q: p == q, deductions.testing_massive, deductions.massive_check), True):
            print("Тест на равномерность прошел успешно")
        else:
            print("Тест на равномерность не прошел успешно")

        return  sumMassive

def main():

    N = 50
    xi=0.25
    deductions=Deductions()
    print('\nТестирование программы запущено')
    deductions.methods(xi, N)
    print('\nПервый тест:')
    deductions.uniformity(xi,N)
    print('\nТестированние программы завершено!')

if __name__=='__main__':
    main()