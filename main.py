import time

from src.selenium import BotInterface

bot = BotInterface()
bot.get_to_third_step()

# checks for empty slots every 10 seconds
while True:
    bot.check_for_appointment()
    time.sleep(10)
    print("Checking again in 10 seconds ...")
