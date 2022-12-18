import time

class Deductions:

    massive_end = []
    testing_massive = []
    test_massive=[]

    @classmethod
    def get_massive(cls):
        return Deductions.massive_end

    def D(self,xi):
        return float(xi)-int(xi)

    def methods(self, xi, N):
        deductions = Deductions()
        g = 6.5
        xi_l=xi

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
        B=0.9
        for j in range(N):
            xi_n = deductions.D(xi_l) * (g * xi)
            deductions.testing_massive.append(xi_n)
            xi_l = deductions.testing_massive[j]
            p=xi_n-xi
            X=(B-(p*N))**2/(p*N)
            deductions.test_massive.append(X)

            print('Итерация: ', j, ', результат:', X)

        return  deductions.test_massive




def main():

    N = 50
    xi=0.25
    deductions=Deductions()
    print('\nТестирование программы запущено')
    print('\nПервый тест:')
    deductions.uniformity(xi,N)
    print('\nТестированние программы завершено!')

if __name__=='__main__':
    main()