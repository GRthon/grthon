from time import sleep
from os import system, path

PANDA = "JMTHON USERBOT DEPLOY"


def clear():
    system("clear")

def jmthon():
    print(f"NOW PUT YOUR VARS CORRECTLY")
    with open(".env", "a") as file:
        for var in ["ALIVE_AME", "APP_ID", "API_HASH", "STRING_SESSION", "DATABASE_URL", "TG_BOT_TOKEN", "TZ"]:
            inpr = input(f"Enter {var}\n- ")
            file.write(f"{var}={inpr}\n")
    print("* Created '.env' file successfully *")
    sleep(0.1)
    system("screen -S jmthon")
    system("python3 -m sbb_b")
