import argparse

def hallo(name, alter):
    print(f"{name} ist {alter} Jahre")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str)
    parser.add_argument("alter", type=str)
    args = parser.parse_args()
    hallo(args.name, args.alter)