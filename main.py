from Poisson import poisson
from Poisson import poissonmod
from Binomial import binomial
from Binomial import binomialMod
# from BinomialNegativa import binomialNegativa
# from BinomialNegativa import binomialNegativaMod

if __name__ == "__main__":
    l = 0
    k = 0
    p0m = 0
    beta = 0
    r = 0 
    m = 0
    q = 0

    TIPO = ""
 
    A = 0
    B = 0

    print("Ingresa A: ")
    A = float(input())
    print("Ingresa B: ")
    B = float(input())

    while True:
        print("Ingresa K:")
        k = int(input())
        if(k >= 0):
            break

    while True:
        print("Ingresa P0M: (NA para omitir)")
        p0minput = input()
        if p0minput == 'NA' or p0minput == 'na':
            p0m = 'NA'
            break
        p0m = float(p0minput)
        if(p0m >= 0 and p0m < 1):
            break


    # Seleccionar distribucion
    if (A < 0 and B > 0):
        # Binomial
        TIPO = "Binomial"
        pass

    elif (A != 0 and B == 0):
        # Geometrica
        TIPO = "Geometrica"
        pass

    elif (A == 0 and B != 0):
        # Poisson
        TIPO = "Poisson"
        pass
    else:
        # Binomial Negativa
        TIPO = "Binomial Negativa"
        pass


    if(TIPO == "Poisson"):
        l = B
        resultado = 0
        esperanza = l
        varianza = l
        if(p0m == 'NA'):
            TIPO = 'Poisson'
            resultado = poisson(l, k)
        else:
            esperanzaGral = l
            varianzaGral = l
            if(p0m == 0):
                TIPO = 'Poisson Zero Truncada'
                resultado = poissonmod(l, k, 0)
                esperanza = l / (1 - poisson(l, 0))
                segundomomento = varianzaGral + pow(esperanzaGral, 2)
                segundomomenotrun = segundomomento / (1 - poisson(l, 0))
                varianza = segundomomenotrun - pow( esperanza , 2 )

            else:
                TIPO = 'Poisson Zero Mod'
                resultado = poissonmod(l, k, p0m)
                esperanza = ((1 - p0m) / (1 - poisson(l, 0))) * esperanzaGral
                segundomomento = varianzaGral + pow(esperanzaGral, 2)
                segundomomentomod = ((1-p0m)/(1 - poisson(l,0))) * segundomomento
                varianza = segundomomentomod - pow(esperanza, 2) 

        print('\n\n----------------'+TIPO+'----------------\n')

        print('λ = ', l)
        print('k = ', k)
        if(TIPO != 'Poisson'):
            print('P0M = ', p0m)
        print('Esp[N] = ', esperanza)
        print('Var[N] = ', varianza)
        print('PM(' + str(k) +') = ', resultado)

        print('\n------------------------------------------\n')
    
    if(TIPO == "Binomial"):
        q = -A / (1 - A)
        m = (B * (1 - q)) / q - 1
        resultado = 0
        esperanza = m * q
        varianza = m * q * (1 - q)

        if(p0m == 'NA'):
            TIPO = 'Binomial'
            resultado = binomial(m, q, k)
        else:
            esperanzaGral = esperanza
            varianzaGral = varianza

            if(p0m == 0):
                TIPO = 'Binomial Zero Truncada'
                resultado = binomialMod(m, q, k, 0)

                esperanza = esperanzaGral / (1 - binomial(m, q, 0))
                segundomomento = varianzaGral + pow(esperanzaGral, 2)
                segundomomenotrun = segundomomento / (1 - binomial(m, q, 0))
                varianza = segundomomenotrun - pow(esperanza , 2 )
            else:
                TIPO = 'Binomial Zero Mod'
                resultado = binomialMod(m, q, k, p0m)

                esperanza = ((1 - p0m) / (1 - binomial(m, q, 0))) * esperanzaGral
                segundomomento = varianzaGral + pow(esperanzaGral, 2)
                segundomomentomod = ((1-p0m)/(1 - binomial(m, q, 0))) * segundomomento
                varianza = segundomomentomod - pow(esperanza, 2)

        print('\n\n----------------'+TIPO+'----------------\n')

        print('M = ', m)
        print('Q = ', q)
        print('k = ', k)
        if(TIPO != 'Poisson'):
            print('P0M = ', p0m)
        print('Esp[N] = ', esperanza)
        print('Var[N] = ', varianza)
        print('PM(' + str(k) +') = ', resultado)

        print('\n------------------------------------------\n')
