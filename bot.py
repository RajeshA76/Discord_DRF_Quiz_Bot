import discord 
import requests
import json
import asyncio

client = discord.Client() # Building conneciton to discord

def get_question():
	qs = ''
	id = 1
	answer = 0
	response = requests.get("http://127.0.0.1:8000/api/random")
	json_data = json.loads(response.text)
	qs += "Question: \n"
	qs += json_data[0]['title'] + "\n"

	for item in json_data[0]['answer']:
		qs += str(id) + ". " + item['answer'] + "\n"

		if item['is_correct']:
    			answer = id


		id += 1

	return(qs,answer)





#Bot works on events

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('hello') or message.content.startswith('hi'):
		await message.channel.send("hello, i am a bot")


	if message.content.startswith('$question'):
    		
		q,a = get_question()
		await message.channel.send(q)

		def check(m):
			return m.author == message.author and m.content.isdigit()

		try:
			guess = await client.wait_for('message',check=check,timeout=10.0)
		except asyncio.TimeoutError:
			return await message.channel.send("Sorry, You took too long")

		if int(guess.content) == a:
				await message.channel.send('you are right')
		else:
				await message.channel.send('oops , that is not right')

client.run('ODUwMzY5MDUzNjEyMzEwNTM5.YLot5Q.raVGl7QEsADeM62AUeGuqxB_1B8')

