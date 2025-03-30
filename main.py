import os
import discord
from gcsa.google_calendar import GoogleCalendar
from gcsa.event import Event
from datetime import datetime
from pysondb import db
from dotenv import load_dotenv

load_dotenv()

def to_datetime(timestamp:float) -> datetime:
    return datetime.fromtimestamp(timestamp)

def to_timestamp(time:datetime) -> float:
    return datetime.timestamp(time)

def formated_time(time:datetime) -> str:
    return time.strftime("%d/%m/%Y, %H:%M:%S")

tasks = db.getDb('tasks.json')

TOKEN = os.getenv('TOKEN')
CALENDAR_ID = os.getenv('CALENDAR_ID')

intents = discord.Intents.default()
intents.guild_messages = True

client = discord.Client(intents=intents)

calendar = GoogleCalendar(default_calendar=CALENDAR_ID, credentials_path='./credentials/credentials.json')

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    message_content:str = message.content.lower()

    if message_content.startswith('start'):
        task_name = message.content[6:]
        for event in tasks.getAll():
            if event["name"] == task_name:
                await message.add_reaction('❌')
                await message.channel.send(f'A task with the name "**{task_name}**" has already been started. Please choose another name for it.')
                return
        tasks.add({"name":message.content[6:],"start":to_timestamp(datetime.now()), "end":None})
        print(f"Started task {task_name} at {formated_time(datetime.now())}")
        await message.add_reaction('✅')
        await message.channel.send(f'Starting "{task_name}".')

    elif message_content.startswith('end'):
        task_name = message.content[4:]
        for event in tasks.getAll():
            if event["name"] == task_name:
                end = datetime.now()
                cal_event = Event(task_name, start=to_datetime(event["start"]), end=end)
                calendar.add_event(cal_event)
                tasks.update({"name":task_name}, {"end":to_timestamp(end)})
                print(f"Ended task {task_name} at {formated_time(end)}")
                await message.add_reaction('✅')
                await message.channel.send(f'"{task_name}" ended.')
                return
        await message.add_reaction('❌')
        await message.channel.send(f'"{task_name}" does not exist.')

    elif message_content == 'get all tasks':
        await message.add_reaction('✅')
        tasks_started = "# Tasks started:\n"
        tasks_finished = "# Last 10 tasks finished:\n"        
        tasks_list = tasks.getAll()
        tasks_list = tasks_list[-10:]
        if len(tasks_list) > 0:
            for event in tasks_list:
                if event['end'] == None:
                    tasks_started += f"- \"{event['name']}\" started at {formated_time(to_datetime(event['start']))} and has not ended yet.\n"
                else:
                    tasks_finished += f"- \"{event['name']}\" started at {formated_time(to_datetime(event['start']))} and ended at {formated_time(to_datetime(event['end']))}\n"
        if tasks_started == "# Tasks started:\n":
            tasks_started += "- No tasks have been started yet."
        if tasks_finished == "# Last 10 tasks finished:\n":
            tasks_finished += "- No tasks have been finished yet."
        await message.channel.send(tasks_started)
        await message.channel.send(tasks_finished)

    elif message_content == 'commands':
        await message.add_reaction('✅')
        await message.channel.send("# Commands:\n- start [task name] --> (starts a task)\n  - [task name] : str --> Name of the task\n- end [task name] --> (ends the task, if it exists)\n  - [task name] : str --> Name of the task\n- get all tasks --> (show all tasks, started & finished (only the last 10))\n- commands --> (shows all commands)")

    else:
        await message.add_reaction('❌')
        await message.channel.send("Invalid command. Type **commands** to see all available commands.")

client.run(TOKEN)