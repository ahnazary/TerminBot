import time

from src.selenium import BotInterface

bot = BotInterface()

# checks for empty slots every 5 minutes
while True:
    bot.get_to_third_step()
    time.sleep(300)
    print("Checking again in 5 minutes...")
