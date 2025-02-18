# Activity Tracker

## A stupid little project I made to make me feel bad to see every time I open Google Calendar that I'm procrastinating 

This uses multiple libraries, such as :
- discord.py
- datetime
- Google Calendar Simple API (gcsa)
- pysondb
- dotenv

All libraries are in requirements.txt

## How to install

### As always, you're more than advised to know what this code does / know Python

To install, you must :

1. Clone / Download this repository on your computer
2. Must have at least [Python 3.13.2](https://www.python.org/downloads/release/python-3132/), as it was written in this version.
3. Install the libraries with `pip install -r requirements.txt` (Note that you may have to add `py -m`, `py3 -m`, `python -m` or `python3 -m` in front of the 1st command for it to work)
4. Create a file called ".env"
5. You're gonna need Google API Services credentials, you may create them [here](https://google-calendar-simple-api.readthedocs.io/en/latest/getting_started.html#getting-started). But I'm giving you a quick rundown :
    1. Click [here](https://console.cloud.google.com/projectcreate) to create a project (You will need to create a Google Cloud account)
    2. Go to [this page](https://cloud.google.com/integration-connectors/docs/connectors/gsc_google_calendar/configure) and follow the instructions (It is the only time I'm going to ask you to read the official website, it's just way too long to explain it here)
    3. Once you've created it, you will need to configure the [Branding](https://console.cloud.google.com/auth/branding)
    4. After that, you want to create a [Client](https://console.cloud.google.com/auth/clients)
        1. Choose "Web application"
        2. Give it a name
        3. Do not add any URI for JavaScript or redirects.
        4. Click "Create"
    5. Then click on the down arrow on the far right to download the Json file, a window will pop up, click on "DOWNLOAD JSON" and rename it "credentials.json"
    6. After renaming the file, click on "Data Access" on the left and "ADD OR REMOVE SCOPES"
        - If you've done everything correctly, you should have a bunch of links like "...auth/calendar"
    7. Check the following scopes:
        - .../auth/calendar (See, edit, share, and permanently delete all the calendars you can access using Google Calendar)
        - .../auth/calendar.app.created (Make secondary Google calendars, and see, create, change, and delete events on them)
        - Click "Update"
    8. Place your "credentials.json" file in a folder called "credentials"
6. On Google Calendar, create or click on the 3 dots next to the calendar name, and click on "Settings and sharing"
7. Scroll down to "Integrate calendar", find "Calendar ID" and copy the whole text that looks like an email adress. Paste in in ".env" such as `CALENDAR_ID = <your calendar id>`
8. You will also need a Discord bot :
    1. Create a [New Application](https://discord.com/developers/applications)
    2. In the "Bot" tab, click on "Reset Token" to generate one. PLEASE COPY IT AND SAVE IT IN THE ".env" FILE LIKE THIS `TOKEN = <the token you just copied>`. DO NOT GIVE IT TO ANYBODY OR PEOPLE WILL HAVE ACCESS TO YOUR BOT.
    3. Then click on the "OAuth2" tab (right above the "Bot" tab)
        - Select "bot"
    4. A new category just appeared under. Select the following scopes:
        1. Under "General Permissions", check :
            - "View Channels"
            - (Yes, this bot **DOES NOT NEED** the "Administrator" permission, shocking right?)
        2. Under "Text Permissions", check :
            - "Send Messages"
            - "Read Message History"
            - "Add Reactions"
    5. Now go at the bottom of the page, and click "Copy" next to the URL, and paste it in a new tab. (You will need to add the bot to a discord server to see him and DM him.)
9. Congrats, you now have everything ready! You can now start `main.py` and DM your bot!