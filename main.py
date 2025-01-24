import requests, telebot, random
from telebot import types
import json
import os
import logging
import sys
from telebot import types
from bin import bin, bincc
from sk import check_sk
from gen import gg
from gemini import gem
from ip import ip
from yt import yt
from fb import fb
from igd import igd
from tik import tik
from pinterest import pi
from waifu import waifu
from nwaifu import nwaifu
from ig import igg
from cchk import cchk
from proxyall import *
from random_user import geninfo
from mchk import new_func, get_response_mchk
import time
from pymongo import MongoClient

# Initialize the bot with your token
tok = "7825415593:AAEE4vR-vGj-vzsb_6fjBIl9vV78ZozPBes"
bot = telebot.TeleBot(tok)
admin_username = "@rabbisudo"
admin_id = [6355601354, 7679832065]  # Add as many IDs as you want

# Construct the MongoDB URI
MONGO_URI = "mongodb+srv://yoogovip:Hpren5jvF_NaGYa@cluster0.qa6a4.mongodb.net"

# Connect to MongoDB
try:
    client = MongoClient(MONGO_URI)
    print("Connected to MongoDB!")
    # Test connection by listing databases
    print(client.list_database_names())
except Exception as e:
    print("Failed to connect to MongoDB:", e)


client = MongoClient(MONGO_URI)
db = client["yoo_go"]  # Replace "yoo_go" with your desired database name
users_collection = db["registered_users"]  # Replace "registered_users" with your desired collection name

# Check if a user is already registered
def is_user_registered(user_id):
    return users_collection.find_one({"user_id": user_id}) is not None

# Save a new registered user to MongoDB
def save_user_to_db(user_id, full_name, username):
    users_collection.insert_one({
        "user_id": user_id,
        "full_name": full_name,
        "username": username
    })

def get_all_registered_users():
    try:
        # Query the database to fetch all user documents
        users = users_collection.find({}, {"user_id": 1, "_id": 0})  # Project only `user_id`
        
        # Extract user_id values into a list
        user_ids = [user['user_id'] for user in users]
        
        return user_ids
    except Exception as e:
        print(f"Error fetching user IDs: {e}")
        return []

@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    user_id = message.from_user.id
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="ADMIN", url="tg://user?id=6355601354")
    b2 = types.InlineKeyboardButton(text="COMMUNITY", url="https://t.me/addlist/fwmfH3MsckZkNGE1")
    key.row_width = 2
    key.add(b1, b2)
    bot.delete_message(message.chat.id, message.message_id)
    for new_member in message.new_chat_members:
        bot.send_photo(
            message.chat.id,
            photo="https://i.ibb.co.com/cr06rBz/5939624176627332725-121.jpg",
            caption=f"""<strong><b>み​ <a href=\"https://telegram.dog/YooGoXBot\">YooGo↯</a> ⌁ Welcome</b>\n
Hey <a href=\"tg://user?id={user_id}\">{new_member.first_name}</a>!\nWelcome To Our Group ❤️\n
Please Follow Some Rules :\n1. Don't Send Unwanted Links To Here.\n2. Don't Spam.\n3. Promo Of Your Channel is Prohibited.\n
↯ Press /cmds To Know My Features.\n</strong>""",
            parse_mode="html",
            reply_markup=key,
        )

@bot.message_handler(content_types=['left_chat_member'])
def delete_left_member_message(message):
    bot.delete_message(message.chat.id, message.message_id)

# Command handler for '/start'
@bot.message_handler(commands=["start"])
def run(message):
    user_id = message.from_user.id
    if message.text.lower() == "/start register":
        register_user(message)
    else:
        if is_user_registered(user_id):
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="MY PROFILE", callback_data="my_profile")
            b2 = types.InlineKeyboardButton(text="ABOUT", callback_data="about")
            b3 = types.InlineKeyboardButton(text="JOIN OUR COMMUNITY", url="https://telegram.dog/YooGoX")
            key.row_width = 2
            key.add(b1, b2, b3)

            bot.send_photo(
                chat_id=message.chat.id,
                photo="https://i.ibb.co.com/WFcfb6Q/download.jpg",  # Replace with the actual photo URL or file ID
                caption=f"<strong>Hi, {message.from_user.first_name}!\nI'm <a href='https://telegram.dog/YooGoXBot'>YooGo↯</a>. A Multi-Functional Bot With Many Tools and Checker Gateways.\nPress /cmds To Know My Features</strong>", 
                parse_mode="HTML", 
                reply_markup=key,
                reply_to_message_id=message.message_id
            )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
                reply_to_message_id=message.message_id
            )

# Command handler for registration
@bot.message_handler(commands=["register"])
def register_user(message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username if message.from_user.username else "Not Set"
    channel_id = "-1002399084572"  # Replace with your channel's username or ID

    if not is_user_registered(user_id):
        save_user_to_db(user_id, full_name, username) 
        
        # Notify the user of successful registration
        bot.send_message(
            message.chat.id,
            text=f"""<strong><b>み​ <a href=\"https://telegram.dog/YooGoXBot\">YooGo↯</a> ⌁ Registration Successful</b>\n
↯ 𝖭𝖺𝗆𝖾 ⌁ <code>{full_name}</code>\n↯ 𝖴𝗌𝖾𝗋 𝖨𝖣 ⌁ <code>{user_id}</code>\n↯ To view my all services click /cmds\n</strong>""",
            parse_mode="html",
            disable_web_page_preview=True,
        )

        # Send a message to the channel about the new registration
        bot.send_message(
            channel_id,
            text=f"""<b>🎉 New User Registration Notification!</b>\n
<b>↯ 𝖭𝖺𝗆𝖾 ⌁</b> {full_name}\n<b>↯ 𝖴𝗌𝖾𝗋 Name ⌁</b> @{username}\n<b>↯ 𝖴𝗌𝖾𝗋 𝖨𝖣 ⌁</b> {user_id}\n<b>↯ Profile Link ⌁ <a href=\"tg://user?id={user_id}\">Click Here</a></b>\n""",
            parse_mode="html",
        )
    else:
        key = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(text="BOI CHANNEL", url="https://telegram.dog/YooGoX")
        b2 = types.InlineKeyboardButton(text="BOI GROUP", url="https://telegram.dog/YooGoX")
        key.row_width = 2
        key.add(b1, b2)
        
        bot.send_photo(
            message.chat.id,
            photo="https://i.ibb.co.com/v4KT4yW/wallpaper-mania-com-High-resolution-wallpaper-background-ID-77700067088.webp",
            caption=f"""<strong><b>み​ <a href=\"https://telegram.dog/YooGoXBot\">YooGo↯</a> ⌁ 𝖠𝗅𝗋𝖾𝖺𝖽𝗒 𝖱𝖾𝗀𝗂𝗌𝗍𝖾𝗋𝖾𝖽</b>\n
↯ 𝖭𝖺𝗆𝖾 ⌁ <code>{full_name}</code>\n↯ 𝖴𝗌𝖾𝗋 𝖨𝖣 ⌁ <code>{user_id}</code>\n↯ Profile Link ⌁ <a href=\"tg://user?id={user_id}\">Click Here</a>\n↯ To view my all services click /cmds\n</strong>""",
            parse_mode="html",
            reply_markup=key,
            reply_to_message_id=message.message_id
        )

@bot.message_handler(commands=['admin'])
def show_admin_commands(message):
    user_id = message.from_user.id

    if user_id not in admin_id:
        # If the user is not an admin, send an error message
        bot.reply_to(message, "You are not authorized to use this command.")
    else:
        # If the user is an admin, send the broadcast message
        bot.reply_to(
            message,
            text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Admin</b>\n
〆 Broadcast Message
↯ Command ⌁ <code>/broadcast</code>
↯ Status ⌁ Active\n
〆 Showing Error Message
↯ Command ⌁ <code>/geterror</code>
↯ Status ⌁ Active\n
〆 Restart the bot
↯ Command ⌁ <code>/restart</code>
↯ Status ⌁ Active\n
</strong>""",
            parse_mode="html",
            disable_web_page_preview=True,  # Disable the link preview
        )

# Configure logging to write errors and messages to a file
log_file = "bot_errors.log"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()  # Optional: to also log to console
    ]
)

# Example of logging an error (use in your try-except blocks as needed)
def log_error(message):
    logging.error(message)

# Define the /geterror command
@bot.message_handler(commands=["geterror"])
def send_error_log(message):
    user_id = message.from_user.id
    if user_id in admin_id:
        if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
            with open(log_file, "rb") as file:
                bot.send_document(
                    chat_id=message.chat.id,
                    document=file,
                    caption="Here are the recent error logs.",
                    reply_to_message_id=message.message_id
                )
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text="The log file is empty or does not exist.",
                reply_to_message_id=message.message_id
            )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="You are not authorized to use this command.",
            reply_to_message_id=message.message_id
        )


@bot.message_handler(commands=["restart"])
def restart_bot(message):
    user_id = message.from_user.id
    if user_id in admin_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Restarting the bot...",
            reply_to_message_id=message.message_id
        )
        logging.info("Bot is restarting upon admin request.")
        
        # Restart the bot
        os.execv(sys.executable, ['python'] + sys.argv)
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="You are not authorized to use this command.",
            reply_to_message_id=message.message_id
        )


@bot.message_handler(commands=['broadcast'])
def broadcast(message):
    user_id = message.from_user.id
    if user_id not in admin_id:
        bot.reply_to(message, "You are not authorized to use this command.", reply_to_message_id=message.message_id)
        return

    # Check if the message is a reply to another message
    if not message.reply_to_message:
        bot.reply_to(message, "Please reply to a message to broadcast it.", reply_to_message_id=message.message_id)
        return

    # Get all registered user IDs
    user_ids = get_all_registered_users()

    successful = 0
    blocked = 0
    deleted = 0
    failed = 0

    for user_id in user_ids:
        try:
            # Forward the replied message to each user
            bot.forward_message(chat_id=user_id, from_chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
            successful += 1
        except telebot.apihelper.ApiTelegramException as e:
            if "blocked" in str(e).lower():
                blocked += 1
            elif "chat not found" in str(e).lower():
                deleted += 1
            else:
                failed += 1

    # Reply with the broadcast status
    bot.reply_to(
        message,
        f"*Broadcast Status Updated!*\n"
        f"*Successful* = {successful} Users\n"
        f"*Blocked* = {blocked} Users\n"
        f"*Deleted* = {deleted} Users\n"
        f"*Failed* = {failed} Users",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['static'])
def send_user_count(message):
    # Check if the user is an admin
    if message.from_user.id not in admin_id:
        bot.send_message(message.chat.id, "You do not have permission to access this command.")
        return
    
    try:
        # Count the number of registered users
        total_users = users_collection.count_documents({})
        
        # Send the total number of users to the admin
        bot.reply_to(
            message,
            text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Stactic</b>\n
Total registered users: {total_users}
↯ DevBy ⌁ {admin_username}
</strong>""",parse_mode="html",disable_web_page_preview=True,)
    except Exception as e:
        # Handle any errors that might occur while accessing the database
        bot.send_message(message.chat.id, "An error occurred while fetching the user count.")
        print(f"Error fetching user count: {e}")



# ADMIN==========
@bot.message_handler(func=lambda m: True)
def mess(message):
    user_id = message.from_user.id
    user = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    text = message.text

    # all command
    if "/cmds" in text:
        if is_user_registered(user_id):
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="GATEWAY", callback_data="gateway")
            b2 = types.InlineKeyboardButton(text="TOOLS", callback_data="tools")
            b3 = types.InlineKeyboardButton(text="HELPER", callback_data="helper")
            b4 = types.InlineKeyboardButton(text="EXIT", callback_data="exit")
            
            # Set the number of buttons in each row to 2
            key.row_width = 2
            key.add(b1, b2,b3,b4)  # Add both buttons to the row
            # Set the number of buttons in each row to 2
            bot.reply_to(
                    message,
                    text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Commands</b>\n
Yoo Go↯ 𝖧𝖺𝗌 𝗉𝗅𝖾𝗇𝗍𝗒 𝗈𝖿 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌. 𝖶𝖾 𝖧𝖺𝗏𝖾 𝖠𝗎𝗍𝗁 𝖦𝖺𝗍𝖾𝗌, 𝖢𝗁𝖺𝗋𝗀𝖾 𝖦𝖺𝗍𝖾𝗌, 𝖳𝗈𝗈𝗅𝗌, 𝖠𝗇𝖽 𝖮𝗍𝗁𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌.\n
𝖢𝗅𝗂𝖼𝗄 𝖤𝖺𝖼𝗁 𝗈𝖿 𝖳𝗁𝖾𝗆 𝖡𝖾𝗅𝗈𝗐 𝗍𝗈 𝖪𝗇𝗈𝗐 𝖳𝗁𝖾𝗆 𝖡𝖾𝗍𝗍𝖾𝗋.\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>""",
                parse_mode="html",
                disable_web_page_preview=True,
                reply_markup=key,
            )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )
        
    if ".info" in text or "/info" in text:
        if is_user_registered(user_id):
            bot.reply_to(
                message,
                parse_mode="html",disable_web_page_preview=True,
                text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ INFORMATION</b>\n
↯ ID ⌁ <code>{user_id}</code>
↯ Name ⌁ <code>{full_name}</code>
↯ Username ⌁ <code>{user}</code>\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
            )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )

    if ".id" in text or "/id" in text:
        if is_user_registered(user_id):
            bot.reply_to(
                message,
                parse_mode="html",disable_web_page_preview=True,
                text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ INFORMATION</b>\n
↯ User ID ⌁ <code>{user_id}</code>
↯ Chat ID ⌁ <code>{chat_id}</code>\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
            )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )
    
    if "/gay" in text:
        if is_user_registered(user_id):
            gay_percentage = random.randint(1, 100)
            bot.reply_to(
                message,
                parse_mode="html",disable_web_page_preview=True,
            text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Fun Commands</b>\n
↯ You will be happy to know that you are {gay_percentage}% gay. 😀😀\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
            )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )
    
    if "/ping" in text:
        # Measure time to respond in milliseconds
        start_time = time.time()  # Record the time at the start
        
        # Your bot's response message
        user = message.from_user.username  # Get the username of the user who sent the message
        ping_time = round((time.time() - start_time) * 1000, 3)  # Convert to milliseconds
        if is_user_registered(user_id):
        # Respond with a formatted HTML message
            bot.reply_to(
                message,
                parse_mode="html", 
                disable_web_page_preview=True,
                text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Ping</b>\n
↯ 𝖡𝗈𝗍 𝖲𝗍𝖺𝗍𝗎𝗌 ⌁ Running
↯ Time ⌁ {ping_time}ms\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
        )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )

            
    if "/socks4" == text:
        se = socks4()
        se_cleaned = "\n".join([line for line in se.splitlines() if line.strip()])  # Remove empty lines
        with open("socks4.txt", "w") as f:
            f.write(se_cleaned)

        with open("socks4.txt", "r") as f:
            lines = f.readlines()
            socks_count = len(lines)
        
        with open("socks4.txt", "r") as jgs:
            bot.send_document(
                message.chat.id,
                jgs,
                caption=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Socks4</b>\n\n↯ Type ⌁ socks4\n↯ Count ⌁ {socks_count}\n\n↯ ReqBy ⌁ @{user}\n↯ DevBy ⌁ {admin_username}</strong>""",
                parse_mode="html",
                reply_to_message_id=message.message_id
            )

    if "/socks5" == text:
        se = socks5()
        js = open("socks5.txt", "w").write(se)
        jgs = open("socks5.txt", "r")
        bot.send_document(
            message.chat.id,
            jgs,
            caption=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Socks5</b>\n\n↯ Type ⌁ socks4\n↯ Count ⌁ {socks_count}\n\n↯ ReqBy ⌁ @{user}\n↯ DevBy ⌁ {admin_username}</strong>""",
            parse_mode="html",
            reply_to_message_id=message.message_id
        )
    if "/https" == text:
        se = https()
        js = open("Https.txt", "w").write(se)
        jgs = open("Https.txt", "r")
        bot.send_document(
            message.chat.id,
            jgs,
            caption=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ https</b>\n\n↯ Type ⌁ socks4\n↯ Count ⌁ {socks_count}\n\n↯ ReqBy ⌁ @{user}\n↯ DevBy ⌁ {admin_username}</strong>""",
            parse_mode="html",
            reply_to_message_id=message.message_id
        )
    if "/http" == text:
        se = http()
        js = open("Http.txt", "w").write(se)
        jgs = open("Http.txt", "r")
        bot.send_document(
            message.chat.id,
            jgs,
            caption=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ http</b>\n\n↯ Type ⌁ socks4\n↯ Count ⌁ {socks_count}\n\n↯ ReqBy ⌁ @{user}\n↯ DevBy ⌁ {admin_username}</strong>""",
            parse_mode="html",
            reply_to_message_id=message.message_id
        )

    if "/status" in text:
        if is_user_registered(user_id):
            bot.reply_to(
                message,
                text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Status</b>\n
↯ Status ⌁ Active\n
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ {admin_username}</b></strong>""",
            parse_mode="html",disable_web_page_preview=True
        )
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )

    if "/sk" in text or ".sk" in text:
        try:
            sk = text.split(" ")[1]
            send = check_sk(sk, user, id)
            bot.reply_to(message, send, parse_mode="html")
        except:
            bot.reply_to(message, "<strong>Sk Error Format</strong>", parse_mode="html")
            pass

    if "/bin" in text or ".bin" in text:
        if is_user_registered(user_id):
            try:
                # Send a loading message
                loading_msg = bot.reply_to(message, "Processing your request... ⏳", parse_mode="html", disable_web_page_preview=True)

                bi = text.split(" ")[1]

                # Validate the BIN input
                if len(bi) < 6 or len(bi) > 15:  # Adjusting the upper limit to a reasonable size for a BIN
                    bot.edit_message_text("<strong>🚫 Incorrect input. Enter a 6-digit BIN number.</strong>", 
                                        chat_id=message.chat.id, 
                                        message_id=loading_msg.message_id, 
                                        parse_mode="html", 
                                        disable_web_page_preview=True)
                else:
                    send = bin(bi, id, user)
                    bot.edit_message_text(send, 
                                        chat_id=message.chat.id, 
                                        message_id=loading_msg.message_id, 
                                        parse_mode="html", 
                                        disable_web_page_preview=True)
            except Exception as e:
                # Catching any exceptions and showing an error message
                bot.edit_message_text("<strong>🚨 An error occurred while processing your request. Please try again later.</strong>", 
                                    chat_id=message.chat.id, 
                                    message_id=loading_msg.message_id, 
                                    parse_mode="html", 
                                    disable_web_page_preview=True)
                print(f"Error: {e}")
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )


    elif "/gen" in text or ".gen" in text:
        if is_user_registered(user_id):
            try:
                # Send a loading message
                loading_msg = bot.reply_to(message, "Processing your request... ⏳", parse_mode="html", disable_web_page_preview=True)
                
                # Split the text and get the argument after the command
                m = text.split(" ")[1]
                
                # Check if m is empty or just whitespace
                if not m.strip():
                    bot.edit_message_text("Your Bin Is Empty.", chat_id=message.chat.id, message_id=loading_msg.message_id, parse_mode="html", disable_web_page_preview=True)
                else:
                    # Proceed with the function if m is not empty
                    send = gg(m, user, id)
                    bot.edit_message_text(send, chat_id=message.chat.id, message_id=loading_msg.message_id, parse_mode="html", disable_web_page_preview=True)
            
            except IndexError:
                # In case the input is missing entirely (IndexError will occur if there's no argument after the command)
                bot.edit_message_text("Your Bin Is Empty", chat_id=message.chat.id, message_id=loading_msg.message_id, parse_mode="html", disable_web_page_preview=True)
            
            except Exception as e:
                # Catch any other exceptions and print them for debugging
                bot.edit_message_text("An error occurred. Please try again later.", chat_id=message.chat.id, message_id=loading_msg.message_id, parse_mode="html", disable_web_page_preview=True)
                print(f"Error: {e}")
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )





    elif "/ip" in text:
        if is_user_registered(user_id):
            try:
                ip_address = text.split(" ")[1] if len(text.split()) > 1 else ""
                # Check if the ip is empty
                if not ip_address:
                    bot.reply_to(message, "<strong>Please provide a ip address after '/ip'.</strong>", parse_mode="html", disable_web_page_preview=True)
                else:
                    send = ip(ip_address, id, user)
                    bot.reply_to(message, send, parse_mode="html", disable_web_page_preview=True)
            except:
                pass
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )
    
    if "/waifu" in text:
        send = waifu(chat_id, user,admin_username)
        if is_user_registered(user_id):
            bot.send_photo(chat_id, send['image_url'], caption=send['caption'], parse_mode="HTML",reply_to_message_id=message.message_id)
            pass
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
                reply_to_message_id=message.message_id
            )

    if "/nwaifu" in text:
        allowed_ids = [6355601354, 7679832065]  # Add as many IDs as you want
        if is_user_registered(user_id):
            if user_id in allowed_ids:
                send = nwaifu(chat_id, user, admin_username)
                bot.send_photo(chat_id, send['image_url'], caption=send['caption'], parse_mode="HTML",reply_to_message_id=message.message_id)
            else:
                bot.reply_to(
                    message, f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Random Nswf Waifu</b>\n
↯ You are not an admin in YooGo↯\n
<b>↯ ReqBy ⌁ @{user}</b>
<b>↯ DevBy ⌁ {admin_username}</b>
</strong>""", parse_mode="html", disable_web_page_preview=True
                )
            pass
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )

    if "/pi" in text:
        if is_user_registered(user_id):
            try:
                pi_link = text.split(" ")[1] if len(text.split()) > 1 else ""
                # Check if the link is empty
                if not pi_link:
                    bot.reply_to(message, "<strong>Please provide a link after '/pi'.</strong>", parse_mode="html", disable_web_page_preview=True)
                else:
                    # Send loading message
                    loading_message = bot.send_message(chat_id, "<strong>Processing your request...</strong>", parse_mode="html")
                    send = pi(pi_link, admin_username, user)
                    bot.delete_message(chat_id, loading_message.message_id)
                    bot.send_photo(chat_id, send['image_url'], caption=send['caption'], parse_mode="HTML",reply_to_message_id=message.message_id)

            except Exception as e:
                # Handle any exceptions
                print(str(e))
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )
                
    if "/yt" in text:
        user_id = message.from_user.id
        text = message.text

        if is_user_registered(user_id):
            try:
                yt_link = text.split(" ")[1] if len(text.split()) > 1 else ""
                if not yt_link:
                    bot.reply_to(message, "<strong>Please provide a link after '/yt'.</strong>", parse_mode="html", disable_web_page_preview=True)
                else:
                    search_message = bot.reply_to(message, "Searching the video...", parse_mode="html")

                    video_url, video_title = yt(yt_link)

                    if video_url:
                        download_message = bot.edit_message_text("Downloading the video...", chat_id=search_message.chat.id, message_id=search_message.message_id)

                        upload_message = bot.edit_message_text("Uploading the video...", chat_id=search_message.chat.id, message_id=download_message.message_id)
                        caption = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Youtube Downloader</b>\n
↯ Video Title ⌁ <code>{video_title}</code>\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
                        bot.delete_message(upload_message.chat.id, upload_message.message_id)
                        bot.send_video(
                            message.chat.id, 
                            video_url, 
                            caption=caption, 
                            parse_mode="html",
                            reply_to_message_id=message.message_id 
                        )
                    else:
                        bot.delete_message(search_message.chat.id, search_message.message_id)
                        bot.reply_to(message, "<strong>Sorry, the video could not be found.</strong>", parse_mode="html")

            except Exception as e:
                bot.delete_message(search_message.chat.id, search_message.message_id)
                bot.reply_to(message, "<strong>There was an error processing your request.</strong>", parse_mode="html")
                print(e)
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",
                reply_markup=key,
            )
                 
    if "/fb" in text:
        user_id = message.from_user.id
        text = message.text

        if is_user_registered(user_id):
            try:
                fb_link = text.split(" ")[1] if len(text.split()) > 1 else ""
                if not fb_link:
                    bot.reply_to(message, "<strong>Please provide a link after '/fb'.</strong>", parse_mode="html", disable_web_page_preview=True)
                else:
                    search_message = bot.reply_to(message, "Searching the video...", parse_mode="html")

                    video_url = fb(fb_link)

                    if video_url:
                        download_message = bot.edit_message_text("Downloading the video...", chat_id=search_message.chat.id, message_id=search_message.message_id)

                        upload_message = bot.edit_message_text("Uploading the video...", chat_id=search_message.chat.id, message_id=download_message.message_id)
                        caption = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Facebook Downloader</b>\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
                        bot.delete_message(upload_message.chat.id, upload_message.message_id)
                        bot.send_video(
                            message.chat.id, 
                            video_url, 
                            caption=caption, 
                            parse_mode="html",
                            reply_to_message_id=message.message_id
                        )
                    else:
                        bot.delete_message(search_message.chat.id, search_message.message_id)
                        bot.reply_to(message, "<strong>Sorry, the video could not be found.</strong>", parse_mode="html")

            except Exception as e:
                bot.delete_message(search_message.chat.id, search_message.message_id)
                bot.reply_to(message, "<strong>There was an error processing your request.</strong>", parse_mode="html")
                print(e)
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",
                reply_markup=key,
            )

                
    if "/tik" in text:
        user_id = message.from_user.id
        text = message.text

        if is_user_registered(user_id):
            try:
                tik_link = text.split(" ")[1] if len(text.split()) > 1 else ""
                if not tik_link:
                    bot.reply_to(message, "<strong>Please provide a link after '/tik'.</strong>", parse_mode="html", disable_web_page_preview=True)
                else:
                    search_message = bot.reply_to(message, "Searching the video...", parse_mode="html")

                    video_url = tik(tik_link)

                    if video_url:
                        download_message = bot.edit_message_text("Downloading the video...", chat_id=search_message.chat.id, message_id=search_message.message_id)

                        upload_message = bot.edit_message_text("Uploading the video...", chat_id=search_message.chat.id, message_id=download_message.message_id)
                        caption = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Tiktok Downloader</b>\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
                        bot.delete_message(upload_message.chat.id, upload_message.message_id)
                        bot.send_video(
                            message.chat.id, 
                            video_url, 
                            caption=caption, 
                            parse_mode="html",
                            reply_to_message_id=message.message_id
                        )
                    else:
                        bot.delete_message(search_message.chat.id, search_message.message_id)
                        bot.reply_to(message, "<strong>Sorry, the video could not be found.</strong>", parse_mode="html")

            except Exception as e:
                bot.delete_message(search_message.chat.id, search_message.message_id)
                bot.reply_to(message, "<strong>There was an error processing your request.</strong>", parse_mode="html")
                print(e)
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",
                reply_markup=key,
            )

                
    if "/igd" in text:
        user_id = message.from_user.id
        text = message.text

        if is_user_registered(user_id):
            try:
                in_link = text.split(" ")[1] if len(text.split()) > 1 else ""
                if not in_link:
                    bot.reply_to(message, "<strong>Please provide a link after '/igd'.</strong>", parse_mode="html", disable_web_page_preview=True)
                else:
                    search_message = bot.reply_to(message, "Searching the video...", parse_mode="html")

                    video_url = igd(in_link, message.from_user.username, message.from_user.id)

                    if video_url:
                        download_message = bot.edit_message_text("Downloading the video...", chat_id=search_message.chat.id, message_id=search_message.message_id)

                        upload_message = bot.edit_message_text("Uploading the video...", chat_id=search_message.chat.id, message_id=download_message.message_id)
                        caption = f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Instagram Downloader</b>\n
↯ ReqBy ⌁ @{user}
↯ DevBy ⌁ {admin_username}
</strong>"""
                        bot.delete_message(upload_message.chat.id, upload_message.message_id)
                        bot.send_video(
                            message.chat.id, 
                            video_url, 
                            caption=caption, 
                            parse_mode="html"
                        )
                    else:
                        bot.delete_message(search_message.chat.id, search_message.message_id)
                        bot.reply_to(message, "<strong>Sorry, the video could not be found.</strong>", parse_mode="html")

            except Exception as e:
                bot.delete_message(search_message.chat.id, search_message.message_id)
                bot.reply_to(message, "<strong>There was an error processing your request.</strong>", parse_mode="html")
                print(e)
        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.send_message(
                message.chat.id,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",
                reply_markup=key,
            )


    elif "/ig" in text or "/infoig" in text:
        loading_msg = bot.reply_to(message, "Processing your request... ⏳", parse_mode="html", disable_web_page_preview=True)
        usernameig = text.split(" ")[1]
        send = igg(usernameig, user,admin_username)
        bot.edit_message_text(send, chat_id=message.chat.id, message_id=loading_msg.message_id, parse_mode="html", disable_web_page_preview=True)

    elif "/cch" in text or "/cch" in text:
        card = text.split(" ")[1]
        print(card)
        try:
            chh = cchk(card, id, user)
            bininfo = bincc(card, id, user)
            bot.reply_to(
                message,
                f"""
			<strong>
			INPUT: <code>{card}</code>
			Reponse: <code> {chh} </code>	
			Gateway: Stripe Auth  (CH){bininfo}
			</strong>
			""",
                parse_mode="html",
            )
        except:
            bot.reply_to(
                message, "<strong>Error Try Again 30ś</strong>", parse_mode="html"
            )

    elif "/fake" in text or "/fakeinfo" in text:
        if is_user_registered(user_id):
            try:
                loading_message = bot.reply_to(message, "<strong>Processing your request...</strong>", parse_mode="html")
                country_code = text.split(" ")[1] if len(text.split(" ")) > 1 else ""
                valid_country_codes = ["AU", "BR", "CA", "CH", "DE", "DK", "ES", "FI", "FR", "GB", "IE", "IN", "IR", "MX", "NL", "NO", "NZ", "RS", "TR", "UA", "US"]
                country_code = country_code.upper() if country_code else ""
                if not country_code or country_code not in valid_country_codes:
                    country_code = "US"
                send = geninfo(id, user, country_code, admin_username)
                bot.edit_message_text(chat_id=message.chat.id, message_id=loading_message.message_id, text=send, parse_mode="html", disable_web_page_preview=True)
            except Exception as e:
                bot.reply_to(message, "<strong>Error Try Again in 30s</strong>", parse_mode="html")
                print(f"Error: {e}")

        else:
            key = types.InlineKeyboardMarkup()
            b1 = types.InlineKeyboardButton(text="REGISTER", url="https://t.me/YooGoXbot?start=register")
            key.add(b1)
            bot.reply_to(
                message,
                text=f"<strong>You are an Unregistered User.\n\nClick Below Register Button to Register.</strong>",
                parse_mode="HTML",  # Enable HTML parsing to support <a> tags
                reply_markup=key,
            )

    elif "/chfree" in text or "/chfree" in text:
        card = text.split(" ")[1]
        bininfo = bincc(card, id, user)
        for i in range(1):
            cc = card.split("|")[0]
            exp = card.split("|")[1]
            try:
                exy = card.split("|")[2].split("0")[1]
            except:
                exy = card.split("|")[2]
            ccv = card.split("|")[3]
            getresonse = new_func(cc, ccv, exp, exy)
            ms1 = get_response_mchk(getresonse)
            try:
                mess = str(ms1[0]).split("-")[1]
            except:
                mess = ms1[0]
            logo = ms1[1]
            code = ms1[2]
            bot.reply_to(
                message,
                f"""
			<strong>
			INPUT: <code>{card}</code>
			Charging Card $Auth
			Result Charge:<code>{logo}</code>
			Reponse: <code> {mess} </code>
			Reponse Code: <code> {code} </code>	
			Gateway: STRIPE Gateway v1 (CH){bininfo}
			</strong>
			""",
                parse_mode="html",
            )

    else:
        pass


@bot.callback_query_handler(func=lambda call: True)
def qery(call):
    user = call.from_user.username
    first_name = call.from_user.first_name
    last_name = call.from_user.last_name
    full_name = call.from_user.full_name
    id = call.from_user.id
    
    # Check if the user who pressed the button is the one who sent the message
    if call.message.reply_to_message:  # Check if it's a reply to a message
        original_sender_id = call.message.reply_to_message.from_user.id
        if call.from_user.id != original_sender_id:
            # If the user is not the original sender, show an alert
            bot.answer_callback_query(
                callback_query_id=call.id,
                text="kid, you can't control this menu",
                show_alert=True  # Show an alert to the user
            )
            return  # Stop further processing of the callback

    # Process button clicks as usual
    if call.data == "my_profile":
        profile(call.message, user, first_name, id)
    elif call.data == "about":
        about(call.message)
    elif call.data == "home":
        home(call.message, first_name)
    elif call.data == "exit":
        exit(call.message)

    # Other commands
    elif call.data == "tools":
        tools(call.message)   
    elif call.data == "bining_tools":
        bining_tools(call.message)
    elif call.data == "ai_tools":
        ai_tools(call.message)
    elif call.data == "back":
        back(call.message)
    elif call.data == "helper":
        helper(call.message)
    elif call.data == "bot_helper":
        bot_helper(call.message)
    elif call.data == "self_helper":
        self_helper(call.message)
    elif call.data == "others_tool":
        others_tool(call.message)
    elif call.data == "gateway":
        gateway(call.message)

   
def profile(message,user, first_name,id):
    key = types.InlineKeyboardMarkup()
    b3 = types.InlineKeyboardButton(text="BACK", callback_data="home")
    key.row_width = 2
    key.add(b3)
    bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message.message_id,
            caption=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ INFORMATION</b>\n
↯ ID                   ⌁ <code>{id}</code>
↯ Name            ⌁ <code>{first_name}</code>
↯ Username    ⌁ <code>{user}</code>
↯ Profile Link  ⌁ <a href="tg://user?id={id}">Click Here</a>\n
↯ DevBy           ⌁ {admin_username}</strong>""",
        parse_mode="html",  # Ensure HTML parsing mode is enabled
        reply_markup=key,
        )
    
def about(message):
    key = types.InlineKeyboardMarkup()
    b3 = types.InlineKeyboardButton(text="BACK", callback_data="home")
    key.row_width = 2
    key.add(b3)
    bot.edit_message_caption(
            chat_id=message.chat.id,
            message_id=message.message_id,
            caption=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ BreakDown!</b>\n
↯ Language     ⌁ Python
↯ Version         ⌁ Beta Testing
↯ Hosting         ⌁ LOCALHOST
↯ Developer     ⌁ {admin_username}
↯ Updated        ⌁ 14/12/2024\n
〆 Our Community 
↯ DevBy             ⌁ {admin_username}
↯ Channel         ⌁ @YooGoX
↯ Checker Bot  ⌁ @YooGoXbot\n
Send feeback/report to {admin_username}</strong>""",
            parse_mode="html",
            reply_markup=key,
        )

def home(message,first_name):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="MY PROFILE", callback_data="my_profile")
    b2 = types.InlineKeyboardButton(text="ABOUT", callback_data="about")
    b3 = types.InlineKeyboardButton(text="JOIN OUR COMMINITY", url="https://telegram.dog/YooGoX")
    
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1, b2,b3)  # Add both buttons to the row
    bot.edit_message_caption(
        chat_id=message.chat.id,
        message_id=message.message_id,
        caption=f"""<strong>Hi, {first_name}!\nI'm <a href='https://telegram.dog/YooGoXBot'>YooGo↯</a>. A Multi-Functional Bot With Many Tools and Checker Gateways.\nPress /cmds To Know My Features.
        </strong>""",
        parse_mode="html",
        reply_markup=key,
    )

def exit(message):
    bot.delete_message(
        chat_id=message.chat.id,
        message_id=message.message_id,
    )
  
# tooolss
def tools(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Bining", callback_data="bining_tools")
    b2 = types.InlineKeyboardButton(text="Ai Tools", callback_data="ai_tools")
    b3 = types.InlineKeyboardButton(text="Others Tools", callback_data="others_tool")
    b4 = types.InlineKeyboardButton(text="Back", callback_data="back")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1, b2,b3,b4)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Tools</b>\n
𝖢𝗅𝗂𝖼𝗄 𝗈𝗇 𝖾𝖺𝖼𝗁 𝗈𝗇𝖾 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗀𝖾𝗍 𝗍𝗈 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾𝗆 𝖻𝖾𝗍𝗍𝖾𝗋.</strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )
# tooolss
def bining_tools(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Ai Tools", callback_data="ai_tools")
    b2 = types.InlineKeyboardButton(text="Others Tools", callback_data="others_tool")
    b3 = types.InlineKeyboardButton(text="Back", callback_data="tools")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1, b2,b3)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Bining Tools</b>\n
〆 BIN Chacker
↯ Command ⌁ <code>/bin bin_number</code>
↯ Example ⌁ <code>/bin 412236</code>
↯ Status ⌁ Active\n
〆 Card Generator
↯ Command ⌁ <code>/gen bin</code>
↯ Example ⌁ <code>/gen 412236</code>
↯ Status ⌁ Active\n
〆 Fake Info & Address
↯ Command ⌁ <code>/fake country_code</code>
↯ Example ⌁ <code>/fake us</code>
↯ Status ⌁ Active\n
        </strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )

def ai_tools(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Bining", callback_data="bining_tools")
    b2 = types.InlineKeyboardButton(text="Others Tools", callback_data="others_tool")
    b3 = types.InlineKeyboardButton(text="Back", callback_data="tools")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1, b2,b3)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Ai Tools</b>\n
〆 CHATGPT
↯ Command ⌁ <code>/gpt your_prompt</code>
↯ Example ⌁ <code>/gpt how to write "hello world!" in python</code>
↯ Status ⌁ Coming Soon....\n
〆 Gemini.Ai
↯ Command ⌁ <code>/gem your_prompt</code>
↯ Example ⌁ <code>/gem how to write "hello world!" in node.js</code>
↯ Status ⌁ Active\n
〆 𝖳𝖾𝗑𝗍 𝗍𝗈 Voice
↯ Command ⌁ <code>/voice your_text</code>
↯ Example ⌁ <code>/voice hello world!</code>
↯ Status ⌁ Coming Soon....\n
        </strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )

def others_tool(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Ai Tools", callback_data="ai_tools")
    b2 = types.InlineKeyboardButton(text="Bining", callback_data="bining_tools")
    b3 = types.InlineKeyboardButton(text="Back", callback_data="tools")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1,b2,b3)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Other Tools</b>\n
〆 IP Information
↯ Command ⌁ <code>/ip</code>
↯ Status ⌁ Active\n
〆 Random Anime Waifu
↯ Command ⌁ <code>/waifu</code>
↯ Status ⌁ Active\n
〆 Pinterest Downloader
↯ Command ⌁ <code>/pi</code>
↯ Status ⌁ Active\n
〆 Youtube Downloader
↯ Command ⌁ <code>/yt</code>
↯ Status ⌁ Active\n
〆 Facebbok Downloader
↯ Command ⌁ <code>/fb</code>
↯ Status ⌁ Active\n
〆 Instagram Downloader
↯ Command ⌁ <code>/igd</code>
↯ Status ⌁ Active\n
〆 Tiktok Downloader
↯ Command ⌁ <code>/tik</code>
↯ Status ⌁ Active\n
Stay tuned! Many more tools and features are coming soon to enhance your experience. Exciting updates ahead!
        </strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )


def helper(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Bot Helper", callback_data="bot_helper")
    b2 = types.InlineKeyboardButton(text="Self Helper", callback_data="self_helper")
    b3 = types.InlineKeyboardButton(text="Back", callback_data="back")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1, b2,b3)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Helper</b>\n
𝖢𝗅𝗂𝖼𝗄 𝗈𝗇 𝖾𝖺𝖼𝗁 𝗈𝗇𝖾 𝖻𝖾𝗅𝗈𝗐 𝗍𝗈 𝗀𝖾𝗍 𝗍𝗈 𝗄𝗇𝗈𝗐 𝗍𝗁𝖾𝗆 𝖻𝖾𝗍𝗍𝖾𝗋.
        </strong>""",    
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )

def bot_helper(message):
    key = types.InlineKeyboardMarkup()
    b2 = types.InlineKeyboardButton(text="Back", callback_data="helper")
    # Set the number of buttons in each row to 2
    key.row_width = 1
    key.add(b2)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Bot Helper</b>\n
〆 Start YooGo↯
↯ Command ⌁ <code>/start@YooGoXbot</code>
↯ Status ⌁ Active\n
〆 User ID
↯ Command ⌁ <code>/id</code>
↯ Status ⌁ Active\n
〆 User Info
↯ Command ⌁ <code>/info</code>
↯ Status ⌁ Active\n
〆 𝖢𝗁𝖾𝖼𝗄 YooGo↯ Status
↯ Command ⌁ <code>/status</code>
↯ Status ⌁ Active\n
〆 𝖢𝗁𝖾𝖼𝗄 𝖸𝗈𝗎𝗋 𝖦𝖺𝗒 𝖲𝖼𝗈𝗋𝖾
↯ Command ⌁ <code>/gay</code>
↯ Status ⌁ Active\n
        </strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )

def self_helper(message):
    key = types.InlineKeyboardMarkup()
    b2 = types.InlineKeyboardButton(text="Back", callback_data="helper")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b2)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Self Helper</b>\n
〆 Status ⌁ Coming Soon....
        </strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )

def gateway(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="Back", callback_data="back")
    # Set the number of buttons in each row to 2
    key.row_width = 1
    key.add(b1)  # Add both buttons to the row
    bot.edit_message_text(
        chat_id=message.chat.id,
        message_id=message.message_id,
        text=f"""<strong><b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Gateway</b>\n
〆 Status ⌁ Coming Soon....
        </strong>""",
        parse_mode="html",
        reply_markup=key,
        disable_web_page_preview=True,  # Disable the link preview
    )

def back(message):
    key = types.InlineKeyboardMarkup()
    b1 = types.InlineKeyboardButton(text="GATEWAY", callback_data="gateway")
    b2 = types.InlineKeyboardButton(text="TOOLS", callback_data="tools")
    b3 = types.InlineKeyboardButton(text="HELPER", callback_data="helper")
    b4 = types.InlineKeyboardButton(text="EXIT", callback_data="exit")
    # Set the number of buttons in each row to 2
    key.row_width = 2
    key.add(b1, b2,b3,b4)  # Add both buttons to the row
    # Set the number of buttons in each row to 2
    # user = message.chat.username
    bot.edit_message_text(
                chat_id=message.chat.id,
                message_id=message.message_id,
                text=f"""<strong>
<b>み​ <a href="https://telegram.dog/YooGoXBot">YooGo↯</a> ⌁ Commands</b>\n
Yoo Go↯ 𝖧𝖺𝗌 𝗉𝗅𝖾𝗇𝗍𝗒 𝗈𝖿 𝖢𝗈𝗆𝗆𝖺𝗇𝖽𝗌. 𝖶𝖾 𝖧𝖺𝗏𝖾 𝖠𝗎𝗍𝗁 𝖦𝖺𝗍𝖾𝗌, 𝖢𝗁𝖺𝗋𝗀𝖾 𝖦𝖺𝗍𝖾𝗌, 𝖳𝗈𝗈𝗅𝗌, 𝖠𝗇𝖽 𝖮𝗍𝗁𝖾𝗋 𝖳𝗁𝗂𝗇𝗀𝗌.\n
𝖢𝗅𝗂𝖼𝗄 𝖤𝖺𝖼𝗁 𝗈𝖿 𝖳𝗁𝖾𝗆 𝖡𝖾𝗅𝗈𝗐 𝗍𝗈 𝖪𝗇𝗈𝗐 𝖳𝗁𝖾𝗆 𝖡𝖾𝗍𝗍𝖾𝗋.\n
↯ DevBy ⌁ {admin_username}
</strong>""",
                parse_mode="html",disable_web_page_preview=True,  reply_markup=key,
            )
    
bot.polling(True)