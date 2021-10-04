import discord
from discord.ext import commands
import os
import requests
from twilio.rest import Client
import mysql.connector
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!",intents=intents)
token = ""
#this intiliazes it ! starts
#need to get peoples ids
#mysql connector
# and set the environment variables. See http://twil.io/secure
account_sid = ''
auth_token = ''
phone = Client(account_sid, auth_token)



mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="!",
    database="youtube"
)

mycursor = mydb.cursor(buffered=True)

@client.event
async def on_ready():
        print("Bot is live")
        location = client.get_channel(804587851680972831)
        await location.send("Lets see if I work this time")
        
        
@client.command()
async def give (ctx,user,points):
    logs = client.get_channel('')
    
    if ctx.message.author.id == '' or ctx.message.author.id == '' or  ctx.message.author.id == '' or ctx.message.author.id == '' or ctx.message.author.id == '':
        sql = f"UPDATE discord SET points = points + {points} WHERE discordid = '{user}'"
        mycursor.execute(sql)
        mydb.commit()
        await logs.send(f"<@{ctx.message.author.id}> Just gave <@{user}> {points} points")
        
        
@client.command()
async def down(ctx):
	person = f"<@{ctx.message.author.id}>"
	alert = client.get_channel('')
	await alert.send("Tech support has been pinged bot will be fixed shortly")
	message = phone.messages.create(
                              body=f'Discord bot has been reported offline ',
                              from_='',
                              to=''
                          )
@client.command()
async def joke (ctx):
    url = 'https://evilinsult.com/generate_insult.php?lang=en&type=json'
    r = requests.get(url)
    dict = r.json()
    await ctx.send(dict['insult'])


@client.command()
async def take (ctx,user,points):
    logs = client.get_channel('')
    
    if ctx.message.author.id == '' or ctx.message.author.id == '' or ctx.message.author.id == '' or  ctx.message.author.id == '' or ctx.message.author.id == '' :
        sql = f"UPDATE discord SET points = points - {points} WHERE discordid = '{user}'"
        mycursor.execute(sql)
        mydb.commit()
        await logs.send(f"<@{ctx.message.author.id}> Just took <@{user}> {points} points")

@client.command()
async def helpme(ctx):
    place = client.get_channel('')
    embed=discord.Embed()
    embed.add_field(name="!top", value="shows how many points a user has", inline=False)
    embed.add_field(name="!help", value="shows help", inline=False)
    embed.add_field(name="!post", value="""!post <url> <length> <platform>
!post https://www.youtube.com/watch?v=SrUqDOjSjhE&t=78s 4:01 Youtube
""", inline=True)
    await place.send(embed=embed)



@client.command()
async def post(ctx,video,length,platform):
 
    engage = client.get_channel('')
    youtube = client.get_channel('')
    sql = f"SELECT * FROM discord WHERE discordid = '{ctx.message.author.id}'"
    rows = mycursor.execute(sql)
    mydb.commit()
    if video is None or length is None or platform is None:
        await youtube.send("You are missing a variable make sure your command looks something like this ```!post <videourl> <length> <platform>```")
    else:


        if mycursor.rowcount == 0:
            sql = f"INSERT INTO discord (id,discordid,points) VALUES (NULL,'{ctx.message.author.id}','{0}')"
            mycursor.execute(sql)
            mydb.commit()
            await engage.send("Sorry you dont have enough credits go to #youtube-engage and watch some videos for points (dont forget to react)")
        else:
            sql = f"SELECT * FROM discord WHERE discordid = '{ctx.message.author.id}'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            for row in result:
                if row[2] < 5:
                    await engage.send(f"Sorry you dont have enough credits (you need 5 points you have {row[2]} )go to #youtube-engage and watch some videos for points (dont forget to react)")
                else:
                    #added = await youtube.send(f'this is your video {video}!')
                    embed=discord.Embed(title="Content Match", description="Please be honest and respect each other", color=0xff0000)
                    embed.set_thumbnail(url=ctx.author.avatar_url)
                    embed.set_author(name=ctx.message.author.name)
                    embed.add_field(name="Platform", value=platform, inline=False)
                    embed.add_field(name="Length Of Content" , value=length, inline=True)
                    embed.add_field(name="Content", value=video, inline=False)
                    embed.set_footer(text="Watch 60% Of Total Video Content. Like Comment And Show Proof In #show-proof")
                    await youtube.send(embed=embed)
                    added = await youtube.send(video)
                    
                    emoji = "👍"
                    await added.add_reaction(emoji)
                    sql = f"UPDATE discord SET points = {row[2]} - 5 WHERE discordid ='{ctx.message.author.id}'"
                # print (sql)
                    mycursor.execute(sql)
                    mydb.commit()
                    foursql = f"INSERT INTO post (id,videourl,discordid,timedelete) VALUES (NULL,'{video}','{ctx.message.author.id}',CURRENT_TIMESTAMP)"
                    mycursor.execute(foursql)
                    mydb.commit()
                    #print (foursql)
                    #print (sql)

@client.command()
async def massdm(ctx, *, message):
  await ctx.message.delete()
  if ctx.message.author.id == '':
    for user in ctx.guild.members:
        try:
         await user.send(message)
         print(f"Successfully DMed users!")
        except:
         print(f"Unsuccessfully DMed users, try again later.")



#for loop
@client.command()
async def all(ctx):
    engage = client.get_channel('')
    for member in ctx.guild.members:
        sql = f"SELECT * FROM discord WHERE discordid = '{member.id}'"
        #print (sql)
        rows = mycursor.execute(sql)
       # print (mycursor.rowcount)
        if mycursor.rowcount == 0:
            sql= f"INSERT INTO discord (id,discordid,points) VALUES (NULL,'{member.id}','{0}')"
            #print (sql)
            mycursor.execute(sql)
            mydb.commit()
        else:
            pass
        #await engage.send(f"Hey {member.id}")

    #await engage.send(f"Hey {member}")


@client.command()
async def top(ctx):
    engage = client.get_channel('')

    sql = f"SELECT * FROM discord WHERE discordid = '{ctx.message.author.id}'"

    mycursor.execute(sql)

    result = mycursor.fetchall()
 
    for row in result:

        embed=discord.Embed(title="Content Match Account Info", description="Please be honest and respect each other", color=0xff0000)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.set_author(name=ctx.message.author.name)
        embed.add_field(name="Points", value=f"{row[2]}", inline=False)
        embed.add_field(name="Level" , value=f"{row[3]}", inline=True)
        embed.add_field(name="Current XP", value=f"{row[4]}", inline=False)
        await engage.send(embed=embed)
        mydb.commit()


   


#825188439099965480
@client.event
async def on_raw_reaction_add(payload):
    engage = client.get_channel('')
    logs = client.get_channel('')
    #print (payload.emoji.name)



#   await engage.send(f'hello <@{payload.user_id}> this is {payload.emoji}')
    if payload.emoji.name == "👍":
        #print ("smoled")
        await logs.send(f"<@{payload.user_id}> Just liked a video ")
        rows = mycursor.execute(f"SELECT * FROM discord WHERE discordid = '{payload.user_id}'")
        #print (mycursor.rowcount)
        if mycursor.rowcount == 0:


            sql = f"INSERT INTO discord (id,discordid,points) VALUES (NULL,'{payload.user_id}','1')"
            #print (sql)

            mycursor.execute(sql)
            mydb.commit()
        else:
            sql = f"UPDATE discord SET points = points + 1 WHERE discordid = '{payload.user_id}'"
            #print (sql)
            mycursor.execute(sql)
            mydb.commit()



#@client.event
#async def on_message(message):
#    if len(message.content) > 0:
#        sql = f"UPDATE discord SET xp = xp + 1 WHERE discordid = '{message.author.id}'"
#        mycursor.execute(sql)
 #   else:
 #       pass
 #   
 #   await client.process_commands(message)


@client.event
async def on_raw_reaction_remove(payload):
    logs = client.get_channel('')
    if payload.emoji.name == "👍":
    
        await logs.send(f"<@{payload.user_id}> Just disliked a video ")
        sql = f"UPDATE discord SET points = points - 1 WHERE discordid = '{payload.user_id}'"
        #print (sql)
        mycursor.execute(sql)
        mydb.commit()

@client.event

async def on_member_join(member):
    msg = """Welcome to Contentmatch !!!! https://giphy.com/embed/fU4elxKlRsulB4Jy7w if your a youtuber twitch streamer or
     whoever trying to get engagement your in the right place!!! My name is Jeff and i am a dev... This entire discord is easy to use and can broken down into simple steps
     Please Watch This Video This Will Explain Everything
     https://www.youtube.com/watch?v=SrUqDOjSjhE&t=78s
     """
    print (member.id)
    await member.send(msg)
    logs = client.get_channel('')
    sql = f"INSERT INTO discord (id,discordid,points) VALUES (NULL,'{member.id}','0')"

    welcome = client.get_channel('')
    use= "#"
    await logs.send(f"<@{member.id}> Welcome to ContentMatch a place to grow your channel and help each other for a quickstart go to **{use}how-to-use** If you have any questions hit <@342738297270960128>  up  ")


    #print (sql)

    mycursor.execute(sql)
    #print ("joined")
    mydb.commit()

@client.event

async def on_member_remove(member):
    sql = f"DELETE FROM discord WHERE discordid= '{member.id}'"
    #print (sql)
    mycursor.execute(sql)
    #print ("left")
    mydb.commit()

client.run(token)



