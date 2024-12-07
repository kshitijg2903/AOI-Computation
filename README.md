This repository contains the codebase for simulating and analyzing the Age of Information (AoI) in status update systems. The simulation evaluates three distinct packet management policies in a single-server queueing model to measure their impact on AoI. This repository is a part of the research project aimed at understanding and optimizing AoI in real-time communication systems.

Features
Simulation of AoI: Models the evolution of AoI over time for three packet management policies:
Policy 1: Discard packets when the server is busy.
Policy 2: Allow one packet in the queue, discard excess packets.
Policy 3: Replace queued packets with newer arrivals.

Comparison Metrics:
Average AoI: Mean value of AoI across the simulation period.
Peak AoI: Maximum AoI observed during the simulation.

Visualization:
AoI evolution over time for each policy.
Bar plots comparing average and peak AoI across policies.

You can modify the following parameters in the aoi_simulation.py file:

Arrival Rate (𝜆 
λ): Adjust lambda_rate to change the rate of packet arrivals.
Service Rate (
𝜇
μ): Adjust mu_rate to change the server's processing rate.
Simulation Time: Set total_time to control the duration of the simulation.

Output -

AoI Evolution Plot:
Visualizes how AoI changes over time for the three policies.
Bar Chart Comparison:
Compares the average and peak AoI across the policies.
