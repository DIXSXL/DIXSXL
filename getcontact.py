import csv

search_word = input("введите номер: ")

with open("getcontact.csv", "r") as f:
    reader = csv.reader(f)

 
    for row in reader:
        if search_word in row:
       
            found_line = ",".join(row)

         
            print(f"""
отчет по {search_word}
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┣ {found_line}
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
            break
    else:
        
        print(f"по запросу {search_word} ничего не найдено")
