from datetime import datetime
import math
class Middle_of_the_squares:
    massive2 = []
    massive2_test = []
    massive2_testMax = []

    def random_generator(initial_number=None):
    #def random_generator(self, initial_number=None):
        #Middle = Middle_of_the_squares()
        if initial_number == None:
            initial_number = _get_initial_number()
            #initial_number = Middle._get_initial_number()

        #if not isinstance(initial_number, int):
            #raise ValueError("Входное значение не является числом!")

        while True:
            Tens=0
            while initial_number%1>0:
                Tens+=1
                initial_number*=10
            initial_number=int(initial_number)
            square_str = str(initial_number ** 2)
            start_index = len(square_str) // 4
            finish_index = start_index + 1 if len(square_str) % 2 else start_index
            #stInd=len(start_index)
            #finInd=len(finish_index)

            #initial_number = initial_number
            initial_number = int(square_str[start_index:-finish_index])
            initial_number = float(initial_number)
            initial_number /= 10**(Tens)
            #print(initial_number)
            yield initial_number



        return deductions.massive_end

    def independence(self, N):
        Middle = Middle_of_the_squares()
        Zb = 2.35
        sumE=0
        sumEi = 0
        sumE2 = 0
        generator = Middle_of_the_squares.random_generator(3485.0625)
        for i, E in (zip(range(N), generator)):
            print("{0}: {1}".format(i, E))
            sumE+=E
            sumEi += E*i
            sumE2 += E**2
            Middle.massive2.append(E)

        p = ((1 / N) * sumEi - (1 / N) * sumE * (N + 1) / 2) / math.sqrt(((1 / N) * sumE2 - ((1 / N) * sumE) ** 2) * (N ** 2 - 1) / 12)
        #p=((1/N)*i*E-(1/N)*E*(N+1)/2)/math.sqrt(((1/N)*E**2-((1/N)*E)**2)*(N**2-1)/12)
        Middle.massive2_test.append(p)
        pMax=Zb*(1-p**2)/math.sqrt(N)
        Middle.massive2_test.append(pMax)
        #Middle.massive2_testMax.append(pMax)


        return Middle.massive2_test



    def _get_initial_number(self):
        now = datetime.now()
        return now.microsecond

    # если происходит запуск модуля, то выведем первые 50 случайных чисел
    def final_numbers(self, k):
        Middle = Middle_of_the_squares()
        generator = Middle_of_the_squares.random_generator(3485.0625)
        for index, number in (zip(range(k), generator)):
            print("{0}: {1}".format(index, number))
            Middle.massive2.append(number)
        return Middle.massive2

    if __name__ == "__main__":
        generator = random_generator(3485.0625)
        for index, number in (zip(range(50), generator)):
            print("{0}: {1}".format(index, number))