# This bot makes use of the GroupAPI which can be found at https://github.com/rhgrant10/Groupy.
# Access token must be placed in user's home directory in a file named ".group.key"

import groupy, pyrebase
from groupy import Group, Bot

groups = Group.list()
bots = Bot.list()

# Check to see if WTF@CU group is present, create one if needed
foundGroup = 0;

group_name = "WTF@CU Weekly Digest"
group_description = "Receive your weekly digest of WTF@CU postings from your very own WTFbot!"
group_avatar = "https://files.slack.com/files-pri/T02NNV20J-F2QHH6C3V/logo.png"
group_share = "true"

for group in groups:
	if group.name == group_name:
		wtfcu_group = group
		foundGroup = 1;
		print("found group")

if foundGroup == 0:
	wtfcu_group = Group.create(group_name, group_description, group_avatar, group_share)
	foundGroup = 1;
	print("created group")

# Check to see if WTFbot is present, create one if needed
foundBot = 0;

bot_name = "WTFbot"
bot_avatar = "http://m.memegen.com/rexzsc.jpg"
bot_welcome = "Thanks for using WTF@CU! Here, you will receive a weekly digest of the latest and greatest postings that have been made by students across Columbia. Every week, we will curate of the top WTFs on the website. See you around! :)"

for bot in bots:
	if bot.name == "WTFbot":
		wtfcu_bot = bot;
		foundBot = 1;
		print("found bot")

if foundBot == 0:
	wtfcu_bot = Bot.create(bot_name, wtfcu_group, bot_avatar)
	wtfcu_bot.post(bot_welcome)
	foundBot = 1
	print("created bot")

# Back end statistics go here, results tabulated in string:

results = "[results go here]"

# Post results to GroupMe chat

wtfcu_bot.post(results)


