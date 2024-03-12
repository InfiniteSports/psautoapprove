from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "2238786"))
    API_HASH = getenv("API_HASH", "e449d6cc630583d0b415b286eedb9192")
    BOT_TOKEN = getenv("BOT_TOKEN", "6900717691:AAHTC2hKMhNjEJqEKUIbsE-VkdnGB6a5dMA")
    SUDO = list(map(int, getenv("SUDO", "950958796 5003133371").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Auto:Auto@cluster0.xnmdjg4.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
