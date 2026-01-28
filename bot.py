import discord
from discord.ext import commands
from config import BOT_TOKEN
from logic import start_quiz, format_question, QuizView, user_sessions, QUESTIONS

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot aktif sebagai {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    uid = message.author.id

    if uid in user_sessions:
        s = user_sessions[uid]

        if s["step"] == "name":
            s["name"] = message.content.strip()
            s["step"] = "age"
            await message.channel.send("📅 Masukkan **usia** kamu:")
            return

        if s["step"] == "age":
            if not message.content.isdigit():
                await message.channel.send("❌ Usia harus angka.")
                return

            s["age"] = int(message.content)
            s["step"] = "quiz"

            await message.channel.send(
                embed=format_question(QUESTIONS[0], 0, len(QUESTIONS)),
                view=QuizView(uid)
            )
            return

    await bot.process_commands(message)

@bot.command()
async def quiz(ctx):
    start_quiz(ctx.author.id)
    await ctx.send("👤 Silakan masukkan **NAMA** kamu:")

@bot.command()
async def start(ctx):
    await ctx.send(
        "🧠 **Psychology Bot**\n\n"
        "Gunakan `!quiz` untuk memulai tes MBTI.\n"
        "Kamu akan diminta **nama**, **usia**, lalu menjawab soal.\n\n"
        "Hasil bersifat edukatif & reflektif 🌱"
    )

bot.run(BOT_TOKEN)
