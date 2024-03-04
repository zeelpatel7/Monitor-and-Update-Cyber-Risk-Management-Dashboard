import random

# Define the range for cost
min_cost = 50000000  # 50 million
max_cost = 3000000000  # 3 billion

# Define the years and sectors
years = list(range(2005, 2025))
sectors = ["Healthcare", "Financial Services", "Retail and E-Commerce", "Technology", "Government and Public Sector"]

# Randomly generate costs for each combination of year and sector
data = []
for year in years:
    for sector in sectors:
        cost = random.randint(min_cost, max_cost)
        data.append((year, sector, cost))

# Display the generated data
for entry in data:
    print(entry)
    