import random
import time


def calculate_score():
    if (
        card := random.choice(
            ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        )
    ) in ["J", "Q", "K"]:
        card = 10
    elif card == "A":
        card = 11
    else:
        card = int(card)

    return random.randint(1, 6) + card


def play_game():
    return calculate_score()


def simulate_games(n):
    scores = []
    for _ in range(n):
        scores.append(play_game())
    return scores


if __name__ == "__main__":
    start_time = time.perf_counter()
    scores = simulate_games(1000000)
    end_time = time.perf_counter()
    print(f"Simulation took {end_time - start_time} seconds")
