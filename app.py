# monte carlo simulation of 100 prisoners problem to predict the output of the random process of the prisoners
# Each prisoner first opens the drawer labeled with the number of the prisoner, then draws a random number 
# if the drawer contains his number, he is free, otherwise he is caught
# otherwise, the drawer contains the number of another prisioner and he opens the drawer labeled with that number
# the process is repeated until all prisoners are free or he finds the number of the last prisoner in the drawer or has opened 50 drawers. 
# the probability of being caught is calculated and the probability of being free is calculated

import random
# monte carlo simulation of 100 prisoners problem to predict the output of the random process of the prisoners
def monte_carlo_simulation(prisoners):
    prisoners_free = 0
    prisoners_caught = 0
    for i in range(100):
        prisoners_free_i, prisoners_caught_i = prisoner_simulation(prisoners)
        prisoners_free += prisoners_free_i
        prisoners_caught += prisoners_caught_i
    return prisoners_free / 100, prisoners_caught / 100

# Each prisoner first opens the drawer labeled with the number of the prisoner, then draws a random number 
# if the drawer contains his number, he is free, otherwise he is caught
def prisoner_simulation(prisoners):
    prisoners_free = 0
    prisoners_caught = 0
    for prisoner in prisoners:
        drawer = random.randint(1, 100)
        if prisoner == drawer:
            prisoners_free += 1
        else:
            prisoners_caught += 1
    return prisoners_free, prisoners_caught


# if the drawer contains his number, he is free, otherwise he is caught
def prisoner_simulation_2(prisoners):
    prisoners_free = 0
    prisoners_caught = 0
    for prisoner in prisoners:
        drawer = random.randint(1, 100)
        if prisoner == drawer:
            prisoners_free += 1
        else:
            prisoners_caught += 1
    else:
        # otherwise, the drawer contains the number of another prisioner and he opens the drawer labeled with that number
        drawer = random.randint(1, 100)
        prisoners_free, prisoners_caught = prisoner_simulation_2(prisoners) # recursive call
    return prisoners_free, prisoners_caught

# the probability of being caught is calculated and the probability of being free is calculated
def prisoner_caught_probability(prisoners):
    prisoners_free, prisoners_caught = prisoner_simulation(prisoners)
    return prisoners_caught / 100 

# main function
if __name__ == "__main__":
    prisoners = [random.randint(1, 100) for i in range(100)]
    prisoners_free, prisoners_caught = monte_carlo_simulation(prisoners)
    print("The probability of being caught is:", prisoners_caught)
    print("The probability of being free is:", prisoners_free)
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    print("The probability of being free is:", 1 - prisoner_caught_probability(prisoners))
    print("The probability of being caught is:", prisoner_caught_probability(prisoners))
    