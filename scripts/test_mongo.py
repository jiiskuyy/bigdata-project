from pymongo import MongoClient
uri = "mongodb+srv://hifzi_db_user:Hifzi12345_@cluster0.dkkxzin.mongodb.net/?appName=Cluster0"
try:
    client = MongoClient(uri)
    print("Koneksi berhasil!")
    print(client.list_database_names())
except Exception as e:
    print("Koneksi gagal:", e)