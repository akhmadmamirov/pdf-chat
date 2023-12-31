## PDF-Chat

Text generation pipeline that enables seamless interaction with any PDF document.

# First Time Setup
<img width="400"  height="235" alt="spice-login" src="https://github.com/akhmadmamirov/pdf-chat/assets/105142060/28bc1ff1-bfe4-4fb9-8bad-e3d94284c488">
<img width="400"  height="235" alt="spice-menu" src="https://github.com/akhmadmamirov/pdf-chat/assets/105142060/de1fb34c-56f0-434c-a5db-0352832f2639">

```
# Create a virtual environment
python -m venv .venv

# On MacOS, WSL, Linux
source .venv/bin/activate

# On Windows
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize the database
flask --app app.web init-db

#Start the terminal with:
inv dev
```
## Required Features

The following **required** functionality is completed:

* Developed text generation pipeline, enabling interaction with any pdf document using OpenAI API and Langchain.

* Allowed streaming responses from LLMs to the user, increasing the overall response rate by 40%.

* Set up the pipeline to self-improve text generation by collecting user feedback on llm, memory and retriever used.


## Video Walkthrough

Here's a walkthrough of implemented features:
* <a href="https://youtu.be/k66s5DFDwTw?feature=shared" target="_blank">Link to the Walkthrough</a>

# Running the app
<img width="400" alt="spice" src="https://github.com/akhmadmamirov/pdf-chat/assets/105142060/b7625d08-406b-442a-a7b2-1a3f0a22685a">
<img width="400" alt="games" src="https://github.com/akhmadmamirov/pdf-chat/assets/105142060/167fff8b-112d-4fd9-ab35-9df260c0982b">

There are three separate processes that need to be running for the app to work: the server, the worker, and Redis.

If you stop any of these processes, you will need to start them back up!

Commands to start each are listed below. If you need to stop them, select the terminal window the process is running in and press Control-C

### To run the Python server

```
inv dev
```

### To run the worker

```
inv devworker
```

### To run Redis

```
redis-server
```
<img width="400" alt="image" src="https://github.com/akhmadmamirov/pdf-chat/assets/105142060/ae7ffdec-3f7a-41df-b03f-24871214b6c9">


### To reset the database

```
flask --app app.web init-db
```

Credits to: Stephen Grider
