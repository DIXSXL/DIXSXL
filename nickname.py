import pystyle
import colorama
from pystyle import Colors

nickname = input(pystyle.Colorate.Horizontal(Colors.blue_to_white, "введите ник: "))

report = pystyle.Colorate.Horizontal(Colors.blue_to_white, f"""
        отчет по {nickname}
├ https://www.instagram.com/{nickname}
├ https://www.tiktok.com/@{nickname}
├ https://twitter.com/{nickname}
├ https://www.facebook.com/{nickname}
├ https://www.youtube.com/@{nickname}
└ https://t.me/{nickname}
""")

print(report)
