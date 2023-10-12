import numpy as np

# Define a range of expected radon levels (in picocuries per liter)
min_radon = 0
max_radon = 150  # Typical indoor radon levels

# Generate random data for geopathic stress related to radon levels
num_samples = 100  # You can adjust this number as needed
radon_data = np.random.uniform(min_radon, max_radon, num_samples)
