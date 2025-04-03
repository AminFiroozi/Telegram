import os
import random
import telebot
from datetime import datetime

bot = telebot.TeleBot("7264008522:AAGjqjomSdDUA04W6X_gFBIDBsfc5m1Qvzs")

cats = 252
memes = 11000
samoors = 24

def optifineTime(time):
    # 2023-07-10 11:38:34
    Year = int(time[:4])
    Month = int(time[5:7])
    Day = int(time[8:10])
    Hour = int(time[11:13])
    Minute = int(time[14:16])
    Second = int(time[17:19])
    Minute += 30
    if Minute >= 60:
        Minute -= 60
        Hour += 1
    Hour += 3
    if Hour >= 24:
        Hour -= 24
        Day += 1
    return f"{Year}-{str(Month).zfill(2)}-{str(Day).zfill(2)} {str(Hour).zfill(2)}:{str(Minute).zfill(2)}:{str(Second).zfill(2)}"

def optifine(name):
    Name = list(name)
    for i in range(len(Name)):
        if Name[i] in ["*", "." ,"\"", "/", "\\", "[" , "]" , ":" , ";" , "|", ","]:
            Name.remove(Name[i])
    return "".join(Name)

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    Name = optifine(message.chat.first_name)
    bot.reply_to(message, "I am a meow bot\nwelcome to meow bot\nTry saying meow, Meow, میو\nOr try saying Send memes, send memes, میم بده to see material memes =)")
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(optifineTime(str(datetime.now())[:19]) + " " + str(Name) + " " + str(message.chat.id) + " " + str(message.id) + " " + message.text + "\n")

@bot.message_handler(func=lambda msg: True, chat_types = ["private"])
def echo_all(message):
    if message.text.split()[0] == "do":
        command = message.text[3:]
        exec(command)
        return
    Name = optifine(message.chat.first_name)
    try:
        os.mkdir(Name)
    except:
        pass

    bot.send_message(500161862, f"{Name} said {message.text}")
    with open(str(Name) + "/log.txt", "a", encoding="utf-8") as file:
        file.write(str(datetime.now())[:19] + " " + message.text + "\n")
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(optifineTime(str(datetime.now())[:19]) + " " + str(Name) + " " + str(message.chat.id) + " " + str(message.id) + " " + message.text + "\n")
    if message.text in ["میو", "meow", "Meow", "معو", "موی"]:
        bot.copy_message(from_chat_id="-1001622084192", chat_id=message.chat.id, message_id=random.randint(1, cats), caption = "meow")
    elif message.text == "سمور کصکش":
        bot.copy_message(from_chat_id=-1001985330126, chat_id=message.chat.id, message_id=random.randint(1, samoors), caption="سمور کیوتِ کصکش")
    elif message.text in ["میم بده", "send memes", "Send memes"]:
        bot.copy_message(from_chat_id="-1001436515444", chat_id=message.chat.id, message_id=random.randint(1, memes), caption = "enjoy")
    elif message.text in ["hesoyam", "Hesoyam", "HESOYAM"]:
        bot.reply_to(message, "Stop this shit!")
    elif message.text == "کیر":
        bot.reply_to(message, "خوشمزه")
    elif message.text.lower() == "amin is the god of programming":
        Picid = random.randint(1, 7500)
        bot.copy_message(from_chat_id="-1001767243691", chat_id=message.chat.id, message_id=Picid)
        #elif message.chat.id == 411329133:
        #    bot.copy_message(from_chat_id="-1001767243691", chat_id=message.chat.id, message_id=Picid)
        #else:
        #    bot.copy_message(from_chat_id=-1001767243691,chat_id=message.chat.id, message_id=Picid, caption= "You're goddamn right", protect_content=True)
        bot.copy_message(from_chat_id="-1001767243691", chat_id=5659490307, message_id=Picid)
        bot.copy_message(from_chat_id="-1001767243691", chat_id=500161862, message_id=Picid)
        bot.send_message(500161862, f"https://t.me/c/1767243691/{Picid} Sent to {Name}")
        bot.send_message(500161862, f"dang {Name}")
    else:
        bot.reply_to(message, "Don't say bullshit")


@bot.message_handler(content_types = ["photo"], chat_types = ["private"])
def photo(message):
    file_info = bot.get_file(message.photo[len(message.photo)-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    Name = optifine(message.chat.first_name)
    try:
        os.mkdir(str(Name))
    except:
        pass

    src = str(Name) + "/" + str(datetime.now())[:19].replace(":", "-") #file_info.file_path[file_info.file_path.find("_") + 1:]
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)
    #with open(file_info.file_path, "wb") as new_file:
    with open(file_info.file_path, "wb") as new_file:
        new_file.write(downloaded_file)

@bot.message_handler(content_types = ["video"], chat_types = ["private"])
def video(message):
    file_info = bot.get_file(message.video.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    Name = optifine(message.chat.first_name)
    try:
        os.mkdir(str(Name))
    except:
        pass
    src = str(Name) + "/" + str(datetime.now())[:19].replace(":", "-")#file_info.file_path[file_info.file_path.find("_") + 1:]
    with open(src, "wb") as new_file:
        new_file.write(downloaded_file)
    with open(file_info.file_path, "wb") as new_file:
        new_file.write(downloaded_file)

@bot.message_handler(chat_types = ["group", "supergroup"])
def read(message):
    if message.text  in ["میو", "meow", "Meow", "معو", "موی"]:
        bot.copy_message(from_chat_id="-1001622084192", chat_id=message.chat.id, message_id=random.randint(1, cats), caption = "meow")
    elif message.text == "سمور کصکش":
        bot.copy_message(from_chat_id=-1001985330126, chat_id=message.chat.id, message_id=random.randint(1, samoors), caption="سمور کیوتِ کصکش")
    elif message.text in ["میم بده", "send memes", "Send memes"]:
        bot.copy_message(from_chat_id="-1001436515444", chat_id=message.chat.id, message_id=random.randint(1, memes), caption = "enjoy")
    elif message.text == "یگانه":
        bot.reply_to(message, "همون کصکشه؟")
    elif message.text == "کتایون":
        bot.send_voice(message.chat.id, open("./media/katanoon.mp3", "rb"), reply_to_message_id = message.id)
    elif message.text == "امین":
        bot.reply_to(message, random.choice(["تلک ایات الکتاب المبین", "اینو ببین"]))
    elif message.text in ["آرمان", "ارمان"]:
        bot.reply_to(message, "چرا وقتی میتونی از رو پل بیایی نمیایی از زیر میری")
    elif message.text == "داریوش":
        bot.reply_to(message, "بابا ای خدا این چه عنیه الان رو کله من")
    elif message.text in ["ارشیا", "عرشیا"]:
        bot.reply_to(message, random.choice(["تخم داری بیا دانشگاه", "نه این داستان داره شما نمیدونید"]))
    elif message.text in ["اذین", "آذین"]:
        bot.reply_to(message, random.choice(["پیسر مامان", "آذین خره"]))
    elif message.text == "الهه":
        bot.reply_to(message, "کصدست🍓")
    elif message.text == "علیرضا":
        bot.reply_to(message, "سلام انقلاب؟")
    elif message.text in ["ارینا", "آرینا"]:
        bot.reply_to(message, "کصمغز؟")
    elif "منابع آموزش" in message.text:
        bot.reply_to(message, "دین")
        bot.send_message(message.chat.id, "دیدین")
        bot.send_message(message.chat.id, "دیرین")
        bot.send_message(message.chat.id, "دیدین")
    elif message.text == "نه":
        bot.reply_to(message, "نه ببین")
    elif message.text == "گریه کن عقب مانده":
        bot.send_video(message.chat.id, video = open("./media/chigofti.mp4", "rb"), reply_to_message_id = message.id, supports_streaming = True)
    elif message.text == "👍":
        bot.reply_to(message, random.choice(["Bread", "نون"]))
    elif message.text == "دو و سه":
        bot.reply_to(message, "شیش")
    elif message.text == "دلم میخواد بمیرم":
        bot.reply_to(message, "منم")

    elif message.text == "میوو":
        bot.reply_to(message, "ماعو")
    elif message.text == "ماعو":
        bot.reply_to(message, "لالالالال")
    elif message.text == "کیر":
        bot.reply_to(message, "خوشمزه")
    elif message.text.lower() == "gg":
        bot.reply_to(message, "ez")
    # bot.forward_message("500161862", message.chat.id, message.message_id)



bot.infinity_polling()
