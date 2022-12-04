
# 1.Поиск и замена слов в содержимом текстового файла
file_filling = str((input("fill the file ")).split(" "))
with open ("hw12.txt", "w") as f:
    f.write(file_filling)
search_file_name = input("Enter file name ")
change_word = input("enter change ")
what_to_change = input("what to change ")
def search_file(file, word_find, word_replace):
    with open(file, mode="r") as f:
        li1 = f.readline()
    with open(file, mode="w") as f:
        li1 = li1.replace(word_find,word_replace)
        f.writelines(li1)
search_file(search_file_name,change_word,what_to_change)

# 2. Подсчет количества слов в содержимом текстового файла

def score(file):
    with open(file, mode="r") as f:
        li1 = f.readline()
        li1 = li1.split(" ")
    print(len(li1))
score("hw12.txt")

#3. Вывести слова содержимого файла  в обратном порядке

def revers(file):
    with open(file, mode="r") as f:
        li1 = f.readline()
        li1 = li1.split(",")
        li1 = " ".join(reversed(li1))
        print(li1)
revers("hw12.txt")

# 4. Удаление заданной  по номеру строки из файла
def delate(file):
    li1 = ["Kent" ,"Chester" ,"Winston" ,"Bond"]
    li2 = ["Red" ,"Blue" ,"Green"]
    with open("hw12del.txt", mode="w") as f:
        f.writelines(" ".join(li1)+"\n")
        f.writelines(" ".join(li2))
    with open(file, mode="r") as f:
        li1 = f.readlines()
    with open(file, "w") as f:
        li1.pop(1)
        f.writelines(li1)
delate("hw12del.txt")