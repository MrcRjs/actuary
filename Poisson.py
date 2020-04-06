EULER = 2.7182818284590452353602874713527

def poisson(lambada, k):
    if(k <= 0):
        return pow(EULER, -lambada)
    else:
        res = (lambada/k * poisson(lambada, k-1))
        # print('PKM(' + str(k) + ') = ', res)
        return res

def poissonmod(lambada, k, p0m):
    if (k == 0):
        return pow(EULER, -lambada)
    else:
        # entonces (1-p0m)/(1 - e elevado a menos lambda)*(poisson k)
        return ((1 - p0m)/(1 - pow(EULER, -lambada))) * poisson(lambada, k)

if __name__ == "__main__":
    l = 1
    k = 2

    resultadoPoisson = poisson(l, k)
    resultadoPoissonMod = poissonmod(l, k, .5)
    resultadoPoissonZero = poissonmod(l, k, 0)

    print('\n\n--------------------------------\n')
    
    print('k = ', k)
    print('λ = ', l)
    print('PKM(' + str(k)  + ") = ", resultadoPoisson)
    print('p0m = ', .5)
    print('PKM(' + str(k)  + ") = ", resultadoPoissonMod)
    print('p0m = ', 0)
    print('PKM(' + str(k)  + ") = ", resultadoPoissonZero)

    print('\n--------------------------------\n')
