import numpy as np
import matplotlib.pyplot as plt

#define a function to calculate the changing
beta=0.3
gamma=0.05
def sir_model(N_infected, N_susceptible, N_recovered, beta, gamma, time_steps):
    N_total = N_infected + N_susceptible + N_recovered
    infected_number_info = [N_infected]

    for time_points in range(time_steps):
        infection_proportion = N_infected / N_total
        infection_rate = beta * infection_proportion
        recovery_rate = gamma

        new_infections = np.random.choice([True, False], size=N_susceptible, p=[infection_rate, 1 - infection_rate])
        N_infected += np.sum(new_infections)
        N_susceptible -= np.sum(new_infections)

        new_recoveries = np.random.choice([True, False], size=N_infected, p=[recovery_rate, 1 - recovery_rate])
        N_recovered += np.sum(new_recoveries)
        N_infected -= np.sum(new_recoveries)

        infected_number_info.append(N_infected)

    return infected_number_info

# 0%
infected_number_info_0 = sir_model(1, 7999, 2000, beta, gamma, 1000)

# 10%
infected_number_info_10 = sir_model(1, 7199, 2800, beta, gamma, 1000)

# 20%
infected_number_info_20 = sir_model(1, 7999, 2000, beta, gamma, 1000)

# 30%
infected_number_info_30 = sir_model(1, 6999, 3000, beta, gamma, 1000)

# 40%
infected_number_info_40 = sir_model(1, 5999, 4000, beta, gamma, 1000)

# 50%
infected_number_info_50 = sir_model(1, 4999, 5000, beta, gamma, 1000)

# 60%
infected_number_info_60 = sir_model(1, 3999, 6000, beta, gamma, 1000)

# 70%
infected_number_info_70 = sir_model(1, 2999, 7000, beta, gamma, 1000)

# 80%
infected_number_info_80 = sir_model(1, 1999, 8000, beta, gamma, 1000)

# 90%
infected_number_info_90 = sir_model(1, 999, 9000, beta, gamma, 1000)

# 100%
infected_number_info_100 = sir_model(1, 0, 9999, beta, gamma, 1000)

plt.plot(infected_number_info_0, label='0%')
plt.plot(infected_number_info_10, label='10%')
plt.plot(infected_number_info_20, label='20%')
plt.plot(infected_number_info_30, label='30%')
plt.plot(infected_number_info_40, label='40%')
plt.plot(infected_number_info_50, label='50%')
plt.plot(infected_number_info_60, label='60%')
plt.plot(infected_number_info_70, label='70%')
plt.plot(infected_number_info_80, label='80%')
plt.plot(infected_number_info_90, label='90%')
plt.plot(infected_number_info_100, label='100%')
plt.title("SIR Model with different vaccination rates")
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.legend()
plt.show()