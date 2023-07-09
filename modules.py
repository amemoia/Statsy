import os
import sys
import dotenv
import discord
import subprocess
from datetime import datetime

class Tools():
    def token(self):
        """Either returns a bot's token from .env or creates the file."""
        if not os.path.isfile('.env'):
            content = "TOKEN="
            ans = input("Please paste your bot's token and hit enter. \n")
            with open('.env', 'w') as env:
                env.write(content+ans)
        with open('.env', "r+") as env:
            dotenv.load_dotenv()
            return str(os.getenv("TOKEN"))
    
    def timestamp(self):
        """Returns a pre-formatted timestamp."""
        dt = datetime.now()
        ts = dt.strftime("%H:%M:%S")
        return ts
    
    def console(self, msg: str, msg_type: str = "normal"):
        """Formats a message and prints it to the console with a timestamp. Accepts types normal or warn."""
        c = {
            "normal" : "#",
            "warn" : "!"
        }
        print(f"{self.timestamp()}    {c[msg_type]}{c[msg_type]}{c[msg_type]}    {msg}")

    def embed(self, bot, title: str, desc: str, color: str = "normal"):
        colors = {
            "normal" : discord.Color.blurple(),
            "error": discord.Color.red(),
            "warn" : discord.Color.orange()
        }
        ts = datetime.utcnow()
        embed = discord.Embed(title=title, description=desc, color=colors[color], timestamp=ts)
        embed.set_footer(icon_url=bot.user.avatar.url, text=bot.user.display_name)
        return embed

class Updater():
    def check(self):
        """Checks the current and most recent shortened commit hash. Requires git to be installed to PATH.
        Returns 0 if up to date, 1 if outdated, 2 if version is unknown, 3 if git is not installed."""
        fatal = "fatal:"
        behind = "Your branch is behind"
        # git log --pretty=format"%h" -1
        # i must have been on crack whenever i wrote this but it works and thats what matters
        try:
            commit = subprocess.run(args=['git', 'log', '--pretty=' 'format:' '"%h"', '-1'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            return 3
        if fatal in commit.stdout or fatal in commit.stderr or commit.returncode != 0:
            return 2
        else:
            version = str(commit.stdout)
            # check if out of date
            subprocess.run(args=['git', 'remote', 'update'])
            status = subprocess.run(args=['git', 'status'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if behind in status.stdout:
                return 1
            else:
                return 0
            
    def pull(self):
        """Pulls commits from the bot's repository. Requires Git to be installed to PATH."""
        update = subprocess.run(args=['git', 'pull'], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if update.returncode != 0:
            tools.console("Update failed! Don't try to update if you modified the bot's code.", "warn")
        return update.returncode

    def restart(self, time: int):
        tools.console(f'Restarting in {str(time)} seconds.', "warn")
        time.sleep(time)
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

tools = Tools()
updater = Updater()