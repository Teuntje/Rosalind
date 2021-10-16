def calcProbability(k, m, n, population):
    """The probability that two randomly selected mating organisms will
    produce an individual possessing a dominant allele (and thus
    displaying the dominant phenotype)
    """
    #probablity both parents are AA:
    AA = k/population
    
    AaAA = (m/population)*(k/(population-1))
    AaAa = (m/population)*((m-1)/(population-1))*0.75
    Aaaa = (m/population)*(n/(population-1))*0.50
    
    aaaA = (n/population)*(m/(population-1))*0.5
    aaAA = (n/population)*(k/(population-1))
    
    print(AA + AaAA + AaAa + Aaaa + aaaA + aaAA)


if __name__ == "__main__":
    k = 21
    m = 17
    n = 21
    population = k + m + n
    calcProbability(k, m, n, population)
