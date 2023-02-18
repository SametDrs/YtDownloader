from os import mkdir, getlogin
from win32com.client import Dispatch
from win32ui import MessageBox
from requests import get
try:
    mkdir("C:/SD")
except FileExistsError:
    pass
try:
    mkdir("C:/SD/YtDownloader")
except FileExistsError:
    pass
try:
    MessageBox("YouTube Downloader yükleniyor...", "YouTube Downloader", 0)
    print("YouTube Downloader yükleniyor...")
    print("Dosyalar indiriliyor...")
    print("İndiriliyor: main.exe")
    r = get("https://sametdrs.me/pages/api/YtDownloader/main.exe")
    with open("C:/SD/YtDownloader/main.exe", "wb") as f:
        f.write(r.content)
    print("İndirildi: main.exe")
    print("İndiriliyor: interface.ui")
    r = get("https://sametdrs.me/pages/api/YtDownloader/interface.ui")
    with open("C:/SD/YtDownloader/interface.ui", "wb") as f:
        f.write(r.content)
    print("İndirildi: interface.ui")
    print("İndiriliyor: YtDownloader.ico")
    r = get("https://sametdrs.me/pages/api/YtDownloader/YtDownloader.ico")
    with open("C:/SD/YtDownloader/YtDownloader.ico", "wb") as f:
        f.write(r.content)
    print("İndirildi: YtDownloader.ico")
except Exception:
    print("Dosyalar indirilirken bir hata oluştu!")
try:
    print("Kısayol oluşturuluyor...")
    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(
        f"C:/Users/{getlogin()}/Desktop/YouTube Downloader.lnk")
    shortcut.Targetpath = "C:/SD/YtDownloader/main.exe"
    shortcut.iconlocation = "C:/SD/YtDownloader/YtDownloader.ico"
    shortcut.save()
    print("Kısayol oluşturuldu!")
except Exception:
    print("Kısayol oluşturulurken bir hata oluştu!")
MessageBox("YouTube Downloader başarıyla yüklendi!", "YouTube Downloader", 0)