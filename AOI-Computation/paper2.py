import numpy as np
import matplotlib.pyplot as plt

def simulate_aoi_policy1(lambda_rate, mu_rate, total_time):
    time = 0
    aois = []
    time_steps = []
    last_update_time = 0

    while time < total_time:
        interarrival_time = np.random.exponential(1 / lambda_rate)
        service_time = np.random.exponential(1 / mu_rate)
        time += interarrival_time
        
        if time >= last_update_time + service_time:
            aois.append(time - last_update_time)
            time_steps.append(time)
            last_update_time = time + service_time

    return aois, time_steps

def simulate_aoi_policy2(lambda_rate, mu_rate, total_time):
    time = 0
    aois = []
    time_steps = []
    last_update_time = 0
    queue_occupied = False

    while time < total_time:
        interarrival_time = np.random.exponential(1 / lambda_rate)
        service_time = np.random.exponential(1 / mu_rate)
        time += interarrival_time

        if time >= last_update_time + service_time:
            aois.append(time - last_update_time)
            time_steps.append(time)
            last_update_time = time + service_time
            queue_occupied = False
        elif not queue_occupied:
            queue_occupied = True
            last_update_time += service_time

    return aois, time_steps

def simulate_aoi_policy3(lambda_rate, mu_rate, total_time):
    time = 0
    aois = []
    time_steps = []
    last_update_time = 0
    queued_packet_arrival = None

    while time < total_time:
        interarrival_time = np.random.exponential(1 / lambda_rate)
        service_time = np.random.exponential(1 / mu_rate)
        time += interarrival_time

        if time >= last_update_time + service_time:
            if queued_packet_arrival is not None:
                aois.append(time - queued_packet_arrival)
                time_steps.append(time)
                last_update_time = time + service_time
                queued_packet_arrival = None
        else:
            queued_packet_arrival = time

    return aois, time_steps


lambda_rate = 1.0  # Arrival rate
mu_rate = 1.5      # Service rate
total_time = 1000  # Simulation time

aois_policy1, time_steps_policy1 = simulate_aoi_policy1(lambda_rate, mu_rate, total_time)
aois_policy2, time_steps_policy2 = simulate_aoi_policy2(lambda_rate, mu_rate, total_time)
aois_policy3, time_steps_policy3 = simulate_aoi_policy3(lambda_rate, mu_rate, total_time)

plt.figure(figsize=(12, 6))
plt.plot(time_steps_policy1, aois_policy1, label="Policy 1: Discard Busy Packets")
plt.plot(time_steps_policy2, aois_policy2, label="Policy 2: Allow One Packet")
plt.plot(time_steps_policy3, aois_policy3, label="Policy 3: Replace Packets")
plt.xlabel("Time")
plt.ylabel("Age of Information (AoI)")
plt.title("AoI Evolution Over Time")
plt.legend()
plt.grid()
plt.show()

avg_aoi1, peak_aoi1 = np.mean(aois_policy1), max(aois_policy1)
avg_aoi2, peak_aoi2 = np.mean(aois_policy2), max(aois_policy2)
avg_aoi3, peak_aoi3 = np.mean(aois_policy3), max(aois_policy3)

policies = ["Policy 1", "Policy 2", "Policy 3"]
avg_aois = [avg_aoi1, avg_aoi2, avg_aoi3]
peak_aois = [peak_aoi1, peak_aoi2, peak_aoi3]

x = np.arange(len(policies))
width = 0.35

plt.figure(figsize=(12, 6))
plt.bar(x - width/2, avg_aois, width, label="Average AoI")
plt.bar(x + width/2, peak_aois, width, label="Peak AoI")
plt.xlabel("Policies")
plt.ylabel("AoI")
plt.title("Comparison of Average and Peak AoI Across Policies")
plt.xticks(x, policies)
plt.legend()
plt.grid(axis="y")
plt.show()