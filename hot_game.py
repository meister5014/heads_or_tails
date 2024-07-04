import random

def toss_coin():
    return "Heads" if random.choice([True, False]) else "Tails"
    
name = input("Who are you?\n> ")
print(f"Hello, {name}!")

print("Tossing a coin...")
results = [toss_coin() for _ in range(3)]
    
for i, result in enumerate(results, 1):
    print(f"Round {i}: {result}")

heads_count = results.count("Heads")
tails_count = results.count("Tails")
print(f"Heads: {heads_count}, Tails: {tails_count}")
