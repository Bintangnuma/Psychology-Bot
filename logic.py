import discord
from discord.ui import View, Button

# ==================================================
# QUESTIONS (40 MBTI QUESTIONS)
# ==================================================

QUESTIONS = [
    # E vs I
    *[
        {"question": q, "options": o, "dimension": ("E", "I")}
        for q, o in [
            ("Di acara sosial, kamu biasanya?", {"A": "Aktif berbicara", "B": "Tergantung situasi", "C": "Lebih banyak diam"}),
            ("Kamu mengisi energi dengan?", {"A": "Bertemu orang", "B": "Keduanya", "C": "Waktu sendiri"}),
            ("Saat bekerja kelompok?", {"A": "Diskusi langsung", "B": "Campuran", "C": "Kerja mandiri"}),
            ("Lebih nyaman komunikasi lewat?", {"A": "Voice", "B": "Bebas", "C": "Chat"}),
            ("Setelah hari melelahkan?", {"A": "Hang out", "B": "Netral", "C": "Menyendiri"}),
            ("Memulai obrolan?", {"A": "Sering", "B": "Kadang", "C": "Jarang"}),
            ("Lingkar pertemanan?", {"A": "Banyak", "B": "Seimbang", "C": "Sedikit tapi dekat"}),
            ("Di tempat baru?", {"A": "Cepat berbaur", "B": "Adaptasi", "C": "Mengamati dulu"}),
            ("Nyaman jadi pusat perhatian?", {"A": "Ya", "B": "Tergantung", "C": "Tidak"}),
            ("Bersosialisasi itu?", {"A": "Menyenangkan", "B": "Netral", "C": "Melelahkan"}),
        ]
    ],

    # S vs N
    *[
        {"question": q, "options": o, "dimension": ("S", "N")}
        for q, o in [
            ("Lebih fokus pada?", {"A": "Fakta", "B": "Keduanya", "C": "Ide"}),
            ("Saat belajar?", {"A": "Contoh nyata", "B": "Campuran", "C": "Konsep"}),
            ("Lebih percaya?", {"A": "Pengalaman", "B": "Seimbang", "C": "Insting"}),
            ("Dalam cerita?", {"A": "Detail", "B": "Keduanya", "C": "Makna"}),
            ("Menyelesaikan masalah?", {"A": "Praktis", "B": "Campuran", "C": "Cara baru"}),
            ("Lebih mudah mengingat?", {"A": "Detail", "B": "Keduanya", "C": "Gambaran besar"}),
            ("Ide favorit?", {"A": "Realistis", "B": "Fleksibel", "C": "Inovatif"}),
            ("Diberi instruksi?", {"A": "Langsung", "B": "Bebas", "C": "Garis besar"}),
            ("Menilai sesuatu dari?", {"A": "Fakta", "B": "Seimbang", "C": "Makna"}),
            ("Perubahan itu?", {"A": "Risiko", "B": "Tergantung", "C": "Peluang"}),
        ]
    ],

    # T vs F
    *[
        {"question": q, "options": o, "dimension": ("T", "F")}
        for q, o in [
            ("Mengambil keputusan?", {"A": "Logika", "B": "Seimbang", "C": "Perasaan"}),
            ("Saat konflik?", {"A": "Solusi", "B": "Netral", "C": "Perasaan"}),
            ("Menilai dari?", {"A": "Benar/salah", "B": "Keduanya", "C": "Dampak"}),
            ("Suka kritik?", {"A": "Langsung", "B": "Biasa", "C": "Lembut"}),
            ("Menghargai?", {"A": "Keadilan", "B": "Seimbang", "C": "Empati"}),
            ("Saat debat?", {"A": "Argumen", "B": "Fleksibel", "C": "Hindari"}),
            ("Keputusan ideal?", {"A": "Rasional", "B": "Campuran", "C": "Semua nyaman"}),
            ("Menilai kerja?", {"A": "Hasil", "B": "Proses", "C": "Hubungan"}),
            ("Keputusan baik itu?", {"A": "Objektif", "B": "Adaptif", "C": "Manusiawi"}),
            ("Kamu cenderung?", {"A": "Tegas", "B": "Seimbang", "C": "Pengertian"}),
        ]
    ],

    # J vs P
    *[
        {"question": q, "options": o, "dimension": ("J", "P")}
        for q, o in [
            ("Lebih suka?", {"A": "Terencana", "B": "Campuran", "C": "Fleksibel"}),
            ("Deadline?", {"A": "Tepat", "B": "Tergantung", "C": "Fleksibel"}),
            ("Jadwal harian?", {"A": "Rapi", "B": "Semi", "C": "Bebas"}),
            ("Cara kerja?", {"A": "To-do list", "B": "Kadang", "C": "Spontan"}),
            ("Ada perubahan?", {"A": "Tidak nyaman", "B": "Netral", "C": "Santai"}),
            ("Selesaikan tugas?", {"A": "Cepat", "B": "Bertahap", "C": "Mengalir"}),
            ("Tenang jika?", {"A": "Terencana", "B": "Seimbang", "C": "Bebas"}),
            ("Soal waktu?", {"A": "Tepat", "B": "Tergantung", "C": "Fleksibel"}),
            ("Keteraturan?", {"A": "Penting", "B": "Situasional", "C": "Membatasi"}),
            ("Gaya hidup?", {"A": "Terstruktur", "B": "Adaptif", "C": "Spontan"}),
        ]
    ],
]

# ==================================================
# MBTI DESCRIPTIONS
# ==================================================

MBTI_INFO = {
    "INTJ ✅": "Ini artinya, Kamu tipe orang yang pemikir strategis, mandiri, dan visioner.",
    "INTP ✅": "Ini artinya, kamu tipe orang yang analitis, logis, dan pencari konsep.",
    "INFJ ✅": "Ini artinya kamu tipe orang yang idealis, reflektif, dan penuh makna.",
    "INFP ✅": "Ini artinya kamu tipe orang yang empatik, kreatif, dan berpegang nilai.",
    "ENTJ ✅": "Ini artinya kamu tipe orang yang pemimpin tegas dan visioner.",
    "ENTP ✅": "Ini artinya kamu tipe orang yang inovatif, debat aktif, dan kreatif.",
    "ENFJ ✅": "Ini artinya kamu tipe orang yang inspiratif dan peduli orang lain.",
    "ENFP ✅": "Ini artinya kamu tipe orang yang antusias, imajinatif, dan bebas.",
    "ISTJ ✅": "Ini artinya kamu tipe orang yang terstruktur, disiplin, dan dapat diandalkan.",
    "ISFJ ✅": "Ini artinya kamu tipe orang yang setia, teliti, dan suportif.",
    "ISTP ✅": "Ini artinya kamu tipe orang yang praktis, logis, dan mandiri.",
    "ISFP ✅": "Ini artinya kamu tipe orang yang tenang, sensitif, dan artistik.",
    "ESTJ ✅": "Ini artinya kamu tipe orang yang terorganisir dan pemimpin alami.",
    "ESFJ ✅": "Ini artinya kamu tipe orang yang sosial, peduli, dan kooperatif.",
    "ESTP ✅": "Ini artinya kamu tipe orang yang spontan, cepat tanggap, dan berani.",
    "ESFP ✅": "Ini artinya kamu tipe orang yang ceria, ramah, dan menikmati hidup."
}

# ==================================================
# SESSION
# ==================================================

user_sessions = {}

def start_quiz(user_id: int):
    user_sessions[user_id] = {
        "index": 0,
        "score": {k: 0 for k in "EISNTFJP"}
    }

def calculate_mbti(score: dict) -> str:
    return (
        ("E" if score["E"] >= score["I"] else "I") +
        ("S" if score["S"] >= score["N"] else "N") +
        ("T" if score["T"] >= score["F"] else "F") +
        ("J" if score["J"] >= score["P"] else "P")
    )

# ==================================================
# EMBED
# ==================================================

def format_question(question, index, total):
    embed = discord.Embed(
        title="🧠 Psychology Bot — MBTI Quiz",
        description=f"**Soal {index+1}/{total}**\n\n{question['question']}",
        color=discord.Color.blurple()
    )
    embed.add_field(name="A️", value=question["options"]["A"], inline=False)
    embed.add_field(name="B️", value=question["options"]["B"], inline=False)
    embed.add_field(name="C️", value=question["options"]["C"], inline=False)
    embed.set_footer(text="Pilih jawaban dengan tombol di bawah ⬇️")
    return embed

# ==================================================
# VIEW
# ==================================================

class QuizView(View):
    def __init__(self, user_id: int):
        super().__init__(timeout=180)
        self.user_id = user_id

    async def handle(self, interaction, choice):
        if interaction.user.id != self.user_id:
            return await interaction.response.send_message("❌ Ini bukan kuis kamu.", ephemeral=True)

        session = user_sessions[self.user_id]
        question = QUESTIONS[session["index"]]
        left, right = question["dimension"]

        if choice == "A":
            session["score"][left] += 1
        elif choice == "C":
            session["score"][right] += 1

        session["index"] += 1

        if session["index"] >= len(QUESTIONS):
            mbti = calculate_mbti(session["score"])
            desc = MBTI_INFO.get(mbti, "Deskripsi belum tersedia.")
            user_sessions.pop(self.user_id)

            embed = discord.Embed(
                title=f"🧠 Hasil MBTI Kamu: {mbti}",
                description=desc,
                color=0x2ECC71
            )
            return await interaction.response.edit_message(embed=embed, view=None)

        await interaction.response.edit_message(
            embed=format_question(
                QUESTIONS[session["index"]],
                session["index"],
                len(QUESTIONS)
            ),
            view=QuizView(self.user_id)
        )

    @discord.ui.button(label="A️", style=discord.ButtonStyle.primary)
    async def a(self, interaction, button):
        await self.handle(interaction, "A")

    @discord.ui.button(label="B️", style=discord.ButtonStyle.secondary)
    async def b(self, interaction, button):
        await self.handle(interaction, "B")

    @discord.ui.button(label="C️", style=discord.ButtonStyle.success)
    async def c(self, interaction, button):
        await self.handle(interaction, "C")

