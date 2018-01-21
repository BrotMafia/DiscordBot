import asyncio
import discord
import bla
import commands

players = {}
d = discord.Client()
bananenbrot = "277083383425794058"
vollkornbrot = "360859154249678858"
admins = ["277083383425794058", "360859154249678858"]


@d.event
async def on_ready():
    print('Logged in as')
    print(d.user.name)
    print(d.user.id)
    print('------')
    await d.change_presence(game=discord.Game(name='Bester Discord der Welt'))

#=======================================================================================================================
#================================================Nachrichten Fukntion===================================================
#=======================================================================================================================

@d.event
async def on_message(message):
    # ======================================================================================================Test command
    if message.content.startswith(bla.prefix + commands.test):
        counter = 0
        tmp = await d.send_message(message.channel, 'Calculating messages...')
        async for log in d.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await d.edit_message(tmp, 'You have {} messages.'.format(counter))
    # =====================================================================================================Sleep command
    elif message.content.startswith(bla.prefix + commands.sleep):
        await asyncio.sleep(5)
        await d.send_message(message.channel, 'Done sleeping')
    # =======================================================================================================Say Command
    if message.content.startswith(bla.prefix + commands.text):
        try:
            text = message.content[5:]
            await d.send_message(message.channel, text)
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{error}```'.format(error=error))
    # ======================================================================================================Game command
    if message.content.startswith(bla.prefix + commands.game):
        print('geht 1')
        if message.author.id == bananenbrot:
            game = message.content[6:]
            await d.change_presence(game=discord.Game(name=game))
            await  d.send_message(message.channel, 'Ich habe mein Spiel zu ' + game + ' geändert')
        else:
            d.send_message(message.channel, '----------nicht genug rechte----------')

        if message.author.id == vollkornbrot:
            game = message.content[6:]
            await d.change_presence(game=discord.Game(name=game))
            await  d.send_message(message.channel, 'Ich habe mein Spiel zu ' + game + ' geändert')
        else:
            d.send_message(message.channel, '----------nicht genug rechte----------')
    # ===================================================================================================Restart command
    if message.content.startswith(bla.prefix + commands.restart):
        await d.change_presence(game=discord.Game(name='--restart--'))
        d.close()
        print('restart')
    # ======================================================================================================Help command
    if message.content.startswith(bla.prefix + commands.help):
       await d.send_message(message.channel, 'Es gibt die Befehle:\n' )
       await d.send_message(message.channel, ' - ' + bla.descriptionTest + '\n - '+ bla.descriptionText+ '\n - '+bla.descriptionGame+'\n - '+bla.descriptionRestart+'\n - '+bla.descriptionHelp+'\n - '+bla.descriptionBjoern+'\n - '+bla.descriptionSleep)
    # =====================================================================================================bjoen command
    if message.content.startswith(bla.prefix + commands.bjoern):
        if message.author.id == bananenbrot:
            d.send_message(message.channel, 'Hallo Björn')
        if message.author.id == vollkornbrot:
            d.send_message(message.channel, 'Hallo Björn')
    # ======================================================================================================Join command
    if message.content.startswith(bla.prefix + commands.join):
            try:
                channel = message.author.voice.voice_channel
                await d.join_voice_channel(channel)
            except discord.errors.InvalidArgument:
                await d.send_message(message.channel, 'Du musst in einem Channel sein...')
                print('...')
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{error}```'.format(error=error))
    # ===================================================================================================== Quit command
    if message.content.startswith(bla.prefix + commands.quit):
            try:
                voice_client = d.voice_client_in(message.server)
                await  voice_client.disconnect()
            except AttributeError:
                await d.send_message(message.channel, 'Ich bin in keinem Channel...')
            except Exception as fehler:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler1}```'.format(fehler1=fehler))
    # ======================================================================================================Play command
    if message.content.startswith(bla.prefix + commands.music):
        bla.liedURL3 = message.content[6:]
        if message.content[6:].startswith(bla.liedText1):
            try:
                channel = message.author.voice.voice_channel
                voice = await d.join_voice_channel(channel)
                print("join")
                d.send_message(message.channel, "Wird geladen...")
                player = await voice.create_ytdl_player(bla.liedURL1)
                players[message.server.id] = player
                player.start()
                d.send_message(message.channel, "Wurde geladen!")
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
        elif message.content[6:].startswith(bla.liedText2):
            try:
                channel = message.author.voice.voice_channel
                voice = await d.join_voice_channel(channel)
                player = await voice.create_ytdl_player(bla.liedURL2)
                d.send_message(message.channel, "Wird geladen...")
                players[message.server.id] = player
                player.start()
                d.send_message(message.channel, "Wurde geladen!")
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
        elif message.content[6:].startswith(bla.liedText3):
            try:
                channel = message.author.voice.voice_channel
                voice = await d.join_voice_channel(channel)
                player = await voice.create_ytdl_player(bla.liedURL3)
                d.send_message(message.channel, "Wird geladen...")
                players[message.server.id] = player
                player.start()
                d.send_message(message.channel, "Wurde geladen!")
            except:
                pass
        elif message.content[6:].startswith(bla.liedText4):
            try:
                channel = message.author.voice.voice_channel
                voice = await d.join_voice_channel(channel)
                player = await voice.create_ytdl_player(bla.liedURL4)
                d.send_message(message.channel, "Wird geladen...")
                players[message.server.id] = player
                player.start()
                d.send_message(message.channel, "Wurde geladen!")
            except:
                pass
        elif message.content[6:].startswith(bla.liedText5):
            try:
                channel = message.author.voice.voice_channel
                voice = await d.join_voice_channel(channel)
                player = await voice.create_ytdl_player(bla.liedURL5)
                d.send_message(message.channel, "Wird geladen...")
                players[message.server.id] = player
                player.start()
                d.send_message(message.channel, "Wurde geladen!")
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
        elif message.content[6:].startswith('loop'):
            print("loop")
            try:
                i = 0
                print("try")
                while i < 4:
                    print("loop")
                    channel = message.author.voice.voice_channel
                    voice = await d.join_voice_channel(channel)
                    player = await voice.create_ytdl_player(bla.lieder[1:4])
                    d.send_message(message.channel, "Wird geladen...")
                    players[message.server.id] = player
                    player.start()
                    d.send_message(message.channel, "Wurde geladen!")
                    i = i +1
            except Exception as error:
                await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    # ======================================================================================================lieder commnd
    if message.content.startswith(bla.prefix + commands.lieder):
        await d.send_message(message.channel, 'Du kannst mit !play + einem der folgenden namen bestimmte lieder auswählen: \n - Dupstep \n - Chillstep \n - Workout\n - Chillout \n - oder einfach plus einen Link ')

    # =====================================================================================================Pause command
    if message.content.startswith(bla.prefix + commands.pause):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    # ====================================================================================================Resume command
    if message.content.startswith(bla.prefix + commands.resume):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
    # ======================================================================================================Kick command
    if message.content.startswith(bla.prefix + commands.kick):
        member = message.content[6:]

        member.User.id

        await d.kick(member)
    # =================================================================================================flüsstern command
    if message.content.startswith(bla.prefix + commands.whisper):
        try:
            text = message.content[6:]
            d.send_message(message.channel, text)
        except Exception as error:
            await d.send_message(message.channel, 'Der Fehler ist: ```{fehler}```'.format(fehler=error))
#=======================================================================================================================
#================================================Member Join Fukntion===================================================
#=======================================================================================================================
@d.event
async def on_member_join(member):
    chennel = bla.channel
    await d.send_message(discord.message.channel, "hi")


d.run(bla.token)


d.embed(discord.colour())

#hallo 