from robomaster import Robot

bot = Robot()
bot.connect()

print(bot.battery())
m = bot.move(0.2, -0.1)
print(m)

bot.disconnect()