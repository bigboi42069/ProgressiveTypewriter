import random
import string
import time
import sys

total_time = 0.0
delay = 0.01

def progressive_brute_force(target, delay):
    global total_time
    char_set = string.ascii_letters + string.digits + string.punctuation + " "
    result = ["_"] * len(target)
    start_time = time.time()
    try:
        for i in range(len(target)):
            sys.stdout.write("\n")
            while True:
                guess = random.choice(char_set)
                result[i] = guess
                end_time = time.time()
                sys.stdout.write("\033[2K\033[0G")
                sys.stdout.write(f"Generation {i+1}: ")
                sys.stdout.write("".join(result))
                sys.stdout.flush()
                if guess == target[i]:
                    break
                time.sleep(delay)
    except KeyboardInterrupt:
        total_time = end_time - start_time
        raise
    total_time = end_time - start_time
    print(f"\nTime taken: {total_time:.2f} seconds. (Delay: {delay}s)")

def get_float_input(prompt, default):
    while True:
        try:
            value = input(prompt) or default
            return float(value)
        except ValueError:
            print("\033[A\033[K", end='')
            print("\033[A\033[K", end='')
            print("Invalid input. Please enter a valid float.\n")

def main():
    print("CSWC's Progressive Typewriter\n")
    global delay
    try:
        target_string = input("Enter the target string: ")
        if target_string == "":
            print("\033[A\033[K", end='')
            print("\033[A\033[K", end='')
            print("\033[A\033[K", end='')
            main()
        else:
            print()
            delay = get_float_input("Enter the visualization delay in seconds (default: 0.01s): ", 0.01)
            progressive_brute_force(target_string, delay)
    except KeyboardInterrupt:
        print(f"\nProcess interrupted. Time taken: {total_time:.2f} seconds. (Delay: {delay}s)")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()