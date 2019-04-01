import time
import random
import datetime
import telepot
from telepot.loop import MessageLoop

def handle(msg):
  chat_id = msg['chat']['id']
  command = msg['text']

print 'Command received: %s' % command

if command == '/about':
  bot.sendMessage(chat_id, 'Hi, I\'m Jalal.pro')
elif command == '/random':
  bot.sendMessage(chat_id, random.randint(0,9))
elif command == '/time':
  bot.sendMessage(chat_id, str(datetime.datetime.now()))

bot = telepot.Bot('Insert your Bot Token here')

MessageLoop(bot, handle).run_as_thread()
print 'Bot ready!'

while 1:
  time.sleep(10)
