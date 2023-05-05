import shutil
import os
from docx import Document
import win32com.client as win32
import sqlite3
import datetime
import subprocess
import sys
from PyQt6.QtWidgets import QMessageBox
import re
def List_dish(category):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    category = 'первые блюда'
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=?", (category,))
    results = cursor.fetchall()
    conn.close()
    return results
def Dish(id):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    id = '3'
    cursor.execute("SELECT * FROM Dish_table WHERE Id_dish=?", (id))
    results = cursor.fetchone()
    conn.close()
    return results
#РАботает
def Sertifikat(name):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM state")
    results = cursor.fetchone()
    conn.close()
    rang=results[1]
    kolvo_b=results[0]
    date = str(datetime.date.today())

    template = "СертификатШаблон.docx"
    new_document = "Сертификат.docx"
    template_copy = "СертификатШаблон_copy.docx"

    # создаем копию оригинального документа
    shutil.copy(template, template_copy)

    # открываем копию в качестве шаблона
    doc = Document(template_copy)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if 'ИМЯ ФАМИЛИЯ' in run.text:
                run.text = run.text.replace('ИМЯ ФАМИЛИЯ', name)
            elif '1' in run.text:
                run.text = run.text.replace('1', str(rang))
            elif '9' in run.text:
                run.text = run.text.replace('9', str(kolvo_b))
            elif 'Дата' in run.text:
                run.text = run.text.replace('Дата', date)

    # сохраняем созданный документ
    doc.save(new_document)

    # удаляем копию шаблона
    os.remove(template_copy)
     
    os.startfile(new_document)
#РАботает
def Dobav_rezept(name,kategory,discription,product,level):
    product = re.sub(r"\s+", " ",product).strip()
    product = product.split(", ") # разбить строку на список по запятой
    product.sort() # сортировать список
    product = ", ".join(product)
    product = product.lower()
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Dish_table (Name_dish,Name_category,Description_dish,Grocery_list, Level_dish,Favorite,Done) VALUES (?, ?, ?, ?, ?,?,?)", 
                   (name, kategory, discription,product,level,"0","0"))
    conn.commit()
    conn.close()
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Запись добавлена")

    msg.exec()

#РАботает
def go_to_new_file(filename):
    # Запустить новый файл в новом процессе
    os.execl(sys.executable, sys.executable, filename)

    # Закрыть текущий файл
    sys.exit()
#РАботает
def go_to_podbor(filename,product):
    product = re.sub(r"\s+", " ",product).strip()
    product = product.split(", ") # разбить строку на список по запятой
    product.sort() # сортировать список
    product = ", ".join(product)
    product = product.lower()
    subprocess.run(["python", filename, product])

    sys.exit()
#РАботает
def vabor_category(kategory,param):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=? AND Grocery_list LIKE ?", (kategory, f"%{param}%"))
    results = cursor.fetchall()
    conn.close()
    return results
def vabor_category_delete_dish(kategory,):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=?", (kategory,))
    results = cursor.fetchall()
    conn.close()
    return results
def delete_dish(name_dish):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Dish_table WHERE Name_dish=?", (name_dish,))
    conn.commit() # you need to commit the changes to the database
    conn.close()
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Запись удалена")

    msg.exec()

#РАботает
def vivod_recipe(name_dish):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_dish=?", (name_dish,))
    results = cursor.fetchone()
    conn.close()
    return results

def vabor_category_izbrannoe(kategory):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Dish_table WHERE Name_category=? AND Favorite=1 ", (kategory,))
    results = cursor.fetchall()
    conn.close()
    return results

def update_dish(dish_id, name, category, description, grocery_list, level):
    grocery_list = re.sub(r"\s+", " ",grocery_list).strip()
    grocery_list = grocery_list.split(", ") # разбить строку на список по запятой
    grocery_list.sort() # сортировать список
    grocery_list = ", ".join(grocery_list)
    grocery_list = grocery_list.lower()
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Dish_table SET Name_dish = ?, Name_category = ?, Description_dish = ?, Grocery_list = ?, Level_dish = ?, Favorite = ?, Done = ? WHERE Id_dish = ?",
                   (name, category, description, grocery_list, level, "0", "0", dish_id))
    conn.commit()
    conn.close()
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Запись изменена")

    msg.exec()

def radioButton_cheked(name_dish,level):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Dish_table SET Done = ? WHERE Name_dish = ?",
                ("1",name_dish))
    conn.commit()
    conn.close()
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM state ")
    results = cursor.fetchone()
    conn.close()
    Kol_vo_dish=results[0]
    Rang=results[1]
    exp=results[2]
    need_exp=results[3]
    Kol_vo_dish+=1
    exp+=int(level)
    if exp>=need_exp:
        Rang+=1
        need_exp+=10
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE state SET Kol_vo_dish=?, Rang=?,exp=?,need_exp=?",
                (Kol_vo_dish,Rang,exp,need_exp))
    conn.commit()
    conn.close()
def add_favorite(name_dish):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Dish_table SET Favorite = ? WHERE Name_dish = ?",
                ("1",name_dish))
    conn.commit()
    conn.close()
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Рецепт добавлен в избранное")

    msg.exec()
def delete_izbrannoe(name_dish):
    conn = sqlite3.connect('Recipe_book.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Dish_table SET Favorite = ? WHERE Name_dish = ?",
                ("0",name_dish))
    conn.commit()
    conn.close()
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText("Рецепт удален из избранного")

    msg.exec()