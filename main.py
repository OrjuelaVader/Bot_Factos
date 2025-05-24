import discord
from discord.ext import commands
import requests
import pyttsx3
from googletrans import Translator

intents = discord.Intents.default()
intents.message_content = True  # Activar lectura de mensajes

bot = commands.Bot(command_prefix="!", intents=intents)

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(text)
    engine.runAndWait()

translator = Translator()

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def hola(ctx):
    await ctx.send("¡Hola! Soy tu bot de prueba.")

@bot.command()
async def fact(ctx):
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        hecho = data["text"]
        traduccion = await translator.translate(hecho, dest="es")
        await ctx.send(f"Dato curioso: {traduccion.text}")
        speak(traduccion.text)
    else:
        return "No se pudo obtener un dato curioso"

bot.run("TOKEN")
