import discord
import asyncio
from discord.ui import View

# ==================================================
# QUESTIONS
# ==================================================
QUESTIONS = [
    *[{"question": q, "options": o, "dimension": ("E","I")} for q,o in [
        ("Di acara sosial, kamu biasanya?", {"A":"Aktif","B":"Netral","C":"Diam"}),
        ("Mengisi energi dengan?", {"A":"Orang","B":"Keduanya","C":"Sendiri"}),
        ("Kerja kelompok?", {"A":"Diskusi","B":"Campuran","C":"Mandiri"}),
        ("Mulai obrolan?", {"A":"Sering","B":"Kadang","C":"Jarang"}),
        ("Bersosialisasi itu?", {"A":"Seru","B":"Biasa","C":"Capek"}),
        ("Lingkar teman?", {"A":"Banyak","B":"Sedang","C":"Sedikit"}),
        ("Di tempat baru?", {"A":"Langsung akrab","B":"Adaptasi","C":"Mengamati"}),
        ("Pusat perhatian?", {"A":"Nyaman","B":"Netral","C":"Tidak"}),
        ("Ngobrol lama?", {"A":"Betah","B":"Tergantung","C":"Cepat lelah"}),
        ("Hangout?", {"A":"Sering","B":"Kadang","C":"Jarang"}),
    ]],
    *[{"question": q, "options": o, "dimension": ("S","N")} for q,o in [
        ("Fokus ke?", {"A":"Fakta","B":"Campuran","C":"Ide"}),
        ("Belajar suka?", {"A":"Contoh","B":"Keduanya","C":"Teori"}),
        ("Percaya karena?", {"A":"Pengalaman","B":"Seimbang","C":"Intuisi"}),
        ("Cerita menarik?", {"A":"Detail","B":"Campuran","C":"Makna"}),
        ("Masalah diselesaikan dengan?", {"A":"Praktis","B":"Campuran","C":"Inovatif"}),
        ("Mengingat sesuatu?", {"A":"Detail","B":"Keduanya","C":"Gambaran"}),
        ("Ide favorit?", {"A":"Realistis","B":"Fleksibel","C":"Kreatif"}),
        ("Instruksi?", {"A":"Rinci","B":"Campuran","C":"Garis besar"}),
        ("Menilai dari?", {"A":"Fakta","B":"Netral","C":"Makna"}),
        ("Perubahan itu?", {"A":"Risiko","B":"Netral","C":"Peluang"}),
    ]],
    *[{"question": q, "options": o, "dimension": ("T","F")} for q,o in [
        ("Ambil keputusan pakai?", {"A":"Logika","B":"Campuran","C":"Perasaan"}),
        ("Saat konflik?", {"A":"Solusi","B":"Netral","C":"Empati"}),
        ("Menilai orang?", {"A":"Objektif","B":"Seimbang","C":"Perasaan"}),
        ("Dikritik suka?", {"A":"Langsung","B":"Biasa","C":"Lembut"}),
        ("Menghargai?", {"A":"Keadilan","B":"Campuran","C":"Empati"}),
        ("Debat?", {"A":"Seru","B":"Kadang","C":"Hindari"}),
        ("Keputusan ideal?", {"A":"Rasional","B":"Campuran","C":"Nyaman"}),
        ("Nilai kerja?", {"A":"Hasil","B":"Proses","C":"Relasi"}),
        ("Keputusan baik?", {"A":"Objektif","B":"Adaptif","C":"Manusiawi"}),
        ("Sifatmu?", {"A":"Tegas","B":"Seimbang","C":"Pengertian"}),
    ]],
    *[{"question": q, "options": o, "dimension": ("J","P")} for q,o in [
        ("Gaya hidup?", {"A":"Terencana","B":"Campuran","C":"Fleksibel"}),
        ("Deadline?", {"A":"Tepat","B":"Tergantung","C":"Santai"}),
        ("Jadwal?", {"A":"Rapi","B":"Semi","C":"Bebas"}),
        ("Cara kerja?", {"A":"List","B":"Kadang","C":"Spontan"}),
        ("Perubahan?", {"A":"Tidak nyaman","B":"Netral","C":"Santai"}),
        ("Selesaikan tugas?", {"A":"Cepat","B":"Bertahap","C":"Mengalir"}),
        ("Tenang jika?", {"A":"Terencana","B":"Seimbang","C":"Bebas"}),
        ("Soal waktu?", {"A":"Tepat","B":"Tergantung","C":"Fleksibel"}),
        ("Keteraturan?", {"A":"Penting","B":"Situasional","C":"Membatasi"}),
        ("Hidup ideal?", {"A":"Terstruktur","B":"Adaptif","C":"Spontan"}),
    ]]
]

# ==================================================
# DESKRIPSI MBTI (3 KATA)
# ==================================================
MBTI_INFO = {
    "INTJ":"Strategis, mandiri, visioner",
    "INTP":"Analitis, logis, konseptual",
    "INFJ":"Idealis, reflektif, bermakna",
    "INFP":"Empatik, kreatif, berprinsip",
    "ENTJ":"Tegas, visioner, pemimpin",
    "ENTP":"Inovatif, lincah, kreatif",
    "ENFJ":"Inspiratif, peduli, sosial",
    "ENFP":"Antusias, imajinatif, hangat",
    "ISTJ":"Terstruktur, disiplin, konsisten",
    "ISFJ":"Setia, suportif, teliti",
    "ISTP":"Praktis, logis, tenang",
    "ISFP":"Tenang, sensitif, artistik",
    "ESTJ":"Terorganisir, tegas, efektif",
    "ESFJ":"Sosial, kooperatif, peduli",
    "ESTP":"Spontan, berani, adaptif",
    "ESFP":"Ceria, ramah, ekspresif"
}

# ==================================================
user_sessions = {}

def start_quiz(uid):
    user_sessions[uid] = {
        "step": "name",
        "index": 0,
        "score": {k: 0 for k in "EISNTFJP"}
    }

def calculate_mbti(score):
    return (
        ("E" if score["E"] >= score["I"] else "I") +
        ("S" if score["S"] >= score["N"] else "N") +
        ("T" if score["T"] >= score["F"] else "F") +
        ("J" if score["J"] >= score["P"] else "P")
    )

def format_question(q, i, total):
    embed = discord.Embed(
        title="🧠 MBTI Quiz",
        description=f"Soal {i+1}/{total}\n\n{q['question']}",
        color=discord.Color.blurple()
    )
    for k, v in q["options"].items():
        embed.add_field(name=k, value=v, inline=False)
    return embed

class QuizView(View):
    def __init__(self, uid):
        super().__init__(timeout=600)
        self.uid = uid

    async def answer(self, interaction, choice):
        await interaction.response.defer()

        if interaction.user.id != self.uid:
            return await interaction.followup.send(
                "❌ Bukan kuis kamu.", ephemeral=True
            )

        s = user_sessions[self.uid]
        q = QUESTIONS[s["index"]]
        a, b = q["dimension"]

        if choice == "A":
            s["score"][a] += 1
        elif choice == "C":
            s["score"][b] += 1

        s["index"] += 1

        if s["index"] >= len(QUESTIONS):
            await interaction.edit_original_response(
                embed=discord.Embed(
                    title="🧠 Psychology Bot",
                    description="🤔 **Bot is thinking your MBTI...**",
                    color=discord.Color.orange()
                ),
                view=None
            )

            await asyncio.sleep(10)

            mbti = calculate_mbti(s["score"])
            desc = MBTI_INFO.get(mbti, "")

            embed = discord.Embed(
                title="🧠 Hasil Tes MBTI",
                color=discord.Color.green()
            )
            embed.add_field(name="Nama", value=s["name"], inline=False)
            embed.add_field(name="Usia", value=s["age"], inline=False)
            embed.add_field(name="MBTI", value=mbti, inline=False)
            embed.add_field(name="", value=f"*{desc}*", inline=False)
            embed.add_field(
                name="",
                value="Terima kasih telah mengunjungi bot kami.\nSemoga hasil ini bermanfaat ✨",
                inline=False
            )

            user_sessions.pop(self.uid)
            return await interaction.edit_original_response(embed=embed)

        await interaction.edit_original_response(
            embed=format_question(
                QUESTIONS[s["index"]],
                s["index"],
                len(QUESTIONS)
            ),
            view=QuizView(self.uid)
        )

    @discord.ui.button(label="A", style=discord.ButtonStyle.primary)
    async def a(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.answer(interaction, "A")

    @discord.ui.button(label="B", style=discord.ButtonStyle.secondary)
    async def b(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.answer(interaction, "B")

    @discord.ui.button(label="C", style=discord.ButtonStyle.success)
    async def c(self, interaction: discord.Interaction, button: discord.ui.Button):
        await self.answer(interaction, "C")
