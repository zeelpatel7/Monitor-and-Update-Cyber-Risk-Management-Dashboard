import random

# Define the range for cost
min_count = 5000  # 5 thousand
max_count = 300000  # 3 hundred thousand

regions = ["North America", "Latin America", "Europe", "Asia", "Africa", "Oceania"]

# Randomly generate count for each combination of count of companies and region
data = []
for region in regions:
    count = random.randint(min_count, max_count)
    data.append((region, count))

# Display the generated data
for entry in data:
    print(entry)
    