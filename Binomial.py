def binomial(m, q, k):
    if(k <= 0):
        return pow(1 - q, m)
    else:
        res = (((m - k + 1) * q) / (k * 1 - q)) * binomial(m, q, k - 1)
        print('PKM(' + str(k) + ') = ', res)
        return res

def binomialMod(m, q, k, p0m):
    if (k == 0):
        return pow(1 - q, m)
    else:
        return ((1 - p0m)/(1 - binomial(m, q, 0))) * binomial(m, q, k)

if __name__ == "__main__":
    
    A = -1
    B = 5
    K = 1
    P0M = 0.5

    Q = -A / (1 - A)
    M = (B * (1 - Q)) / Q -1 

    resultadoBinomial = binomial(M, Q, K)
    resultadoBinomialMod = binomialMod(M, Q, K, P0M)
    resultadoBinomialZero = binomialMod(M, Q, K, 0)

    print('\n\n--------------------------------\n')
    print('A = ', A)
    print('B = ', B)
    print('Q = ', Q)
    print('M = ', M)
    print('PKM(' + str(K)  + ") = ", resultadoBinomial)
    print('P0M = ', P0M)
    print('PKM(' + str(K)  + ") = ", resultadoBinomialMod)
    print('P0M = ', 0)
    print('PKM(' + str(K)  + ") = ", resultadoBinomialZero)

    print('\n--------------------------------\n')
