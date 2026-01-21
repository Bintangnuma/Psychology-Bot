import discord
from discord.ext import commands

from config import BOT_TOKEN
from logic import (
    start_quiz,
    calculate_mbti,
    format_question,
    QuizView,
    user_sessions,
    QUESTIONS
)

# =========================
# BOT SETUP
# =========================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

# =========================
# EVENTS
# =========================

@bot.event
async def on_ready():
    print(f"✅ Psychology Bot aktif sebagai {bot.user}")

# =========================
# COMMANDS
# =========================

@bot.command()
async def quiz(ctx):
    start_quiz(ctx.author.id)

    session = user_sessions[ctx.author.id]
    question = QUESTIONS[session["index"]]

    await ctx.send(
        embed=format_question(
            question,
            session["index"],
            len(QUESTIONS)
        ),
        view=QuizView(ctx.author.id)
    )

@bot.command()
async def start(ctx):
    embed = discord.Embed(
        title="🧠 Psychology Bot",
        description="Bot kuis interaktif untuk mengenali kecenderungan MBTI kamu.",
        color=0x5865F2
    )

    embed.add_field(
        name="▶️ !quiz",
        value="Memulai kuis MBTI (40 soal)",
        inline=False
    )

    embed.add_field(
        name="ℹ️ Catatan",
        value=(
            "Hasil kuis ini **bukan diagnosis psikologis**.\n"
            "Digunakan untuk edukasi dan refleksi diri."
        ),
        inline=False
    )

    embed.set_footer(text="Psychology Bot • Educational Purpose")

    await ctx.send(embed=embed)

# =========================
# RUN BOT
# =========================

bot.run(BOT_TOKEN)
