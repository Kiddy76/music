from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/272f50a40834f0f010847.jpg")
START_IMG = getenv("START_IMG", "https://telegra.ph/file/508b873f80d0d7aff15a0.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/LagXd_botsup")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_mhe")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1687940446").split()))


FAILED = "https://telegra.ph/file/a0bfebaf76e3161864019.jpg"
