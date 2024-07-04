import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"

print("Tossing a coin...")
results = [toss_coin() for _ in range(3)]
heads_count = results.count("Heads")
tails_count = results.count("Tails")

for i, result in enumerate(results, 1):
    print(f"Round {i}: {result}")

print(f"Heads: {heads_count}, Tails: {tails_count}")
