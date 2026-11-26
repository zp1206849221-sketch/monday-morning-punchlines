import os

LINE = "Friday me booked Monday me a 7 a.m. spin class. Monday me showed up only to identify the traitor."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
