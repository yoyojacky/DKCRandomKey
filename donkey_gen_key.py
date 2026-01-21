import os 
import binascii
import pandas as pd


def generate_random_code(length=12):
    random_bytes = os.urandom(length // 2)
    random_code = binascii.hexlify(random_bytes).decode('utf-8')
    return random_code[:length]


def generate_dk_key():
    random_code = generate_random_code()
    dk_key = f"DK-Key-{random_code}"
    return dk_key 


def generate_keys(num_keys=30):
    keys = [generate_dk_key() for _ in range(num_keys)]
    return keys


def save_to_excel(keys, filename="Donkey_Discount_Keys.xlsx"):
    df = pd.DataFrame(keys, columns=["Donkey Discount Key"])
    df.to_excel(filename, index=False)
    print(f"Keys saved to {filename}")


if __name__ == "__main__":
    keys = generate_keys(30)
    save_to_excel(keys)

