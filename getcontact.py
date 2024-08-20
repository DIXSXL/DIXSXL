import requests
from bs4 import BeautifulSoup

def find_word_on_page(word):
    url = "https://sites.google.com/view/dbgetcontact"
    response = requests.get(url)

    if response.status_code != 200:
        print(pystyle.Colorate.Horizontal(Colors.blue_to_white, "ошибка при доступе к базе"))
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    found = False
    for line in soup.stripped_strings:
        if word in line:
            print(pystyle.Colorate.Horizontal(Colors.blue_to_white, f"отчет по {word}\n\n{line}"))
            found = True
            break

    if not found:
        print("ничего не найдено.")

if __name__ == "__main__":
    user_input = input(pystyle.Colorate.Horizontal(Colors.blue_to_white, "введите номер телефона: "))
    find_word_on_page(user_input)
