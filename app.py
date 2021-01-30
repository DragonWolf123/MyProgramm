import asyncio
from asyncio import sleep
import os
import progressbar
import time
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter.ttk import Frame
from tkinter import scrolledtext
from tkinter import ttk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label
import random
from typing import Collection
import flask
from requests import get
from threading import Thread
from PIL import Image, ImageDraw, ImageFont, ImageTk
import sys
from sys import argv
import pyttsx3 as pt
from gtts import gTTS
from tqdm import tqdm as bar
import pynput
from pynput.keyboard import Key, Listener
import pyglet
import youtube_dl
import platform

nameacc = 'USER'

root = Tk()
root.geometry("750x750")
root.resizable(width = False, height = False)
root.title(f'Programm By DragonWolf')
root.wm_attributes( '-alpha', 0.6)
root[ 'bg' ] = '#000000'

def fullsbindon(event):
    root.attributes('-fullscreen', True)
    print(f'{ nameacc } Вы включили полноэкранный режим. Чтобы выйти из него нажмите F12')

def fullsbindoff(event):
    root.attributes('-fullscreen', False)
    print(f'{ nameacc } Вы выключили полноэкранный режим. Чтобы в него войти нажмите F11')

root.bind("<F11>", fullsbindon)
root.bind("<F12>", fullsbindoff)

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def open_file():
    fd.askopenfilename()

def save_file():
    fd.asksaveasfilename()

def creditsprog():
    print(f'Создавал DragonWolf')

def contact():
    print(f'Связатся со мной можно по дискорду: DragonWolf#1712')

def message():
    messagebox.showwarning( 'Инфо о программе', 'Создавал DragonWolf. Программа была написана на чистом питоне Python 3.8.5' )

def plustext():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Склеивание текста" из-за неправильного ключа "key"')
    else:
        print(f'---------Склеивание текста--By DragonWolf------')
        cley1 = input(f'Введите значение 1:')
        cley2 = input(f'Введите значение 2:')
        print(f'Ответ: { cley1 + cley2 }')

def editscale():
    root.resizable(width = True, height = True)

def editscale2():
    root.resizable(width = False, height = False)

def editscalestatic():
    scales1 = input(f'Введите 1 значение по ширине:')
    scales2 = input(f'Введите 2 значение по высоте:')
    messagebox.showwarning( 'Внимание', 'После нажатия Ok изменится размер приложения' )
    root.geometry(f'{scales1}x{scales2}')

def console():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Консоль" из-за неправильного ключа "key"')
    else:
        command = input(f'/')
        if command == 'help':
            print(f'Команды:')
            print(f'/help - Эта команда')
            print(f'/exitconsole - Выйти из консоли')
            print(f'/exitapi - Выйти из программы')
            print(f'/who - Кто в данный момент пользуется программой')
            print(f'------------------------------')

        if command == 'exitconsole':
            print(f'Вы вышли из консоли')

        if command == 'exitapi':
            exit1 = input(f'Выйти из программы? [yes or no]:')
            if exit1 == 'yes':
                sys.exit()

            if exit1 == 'no':
                print(f'Вы не выходите из программы')

        if command == 'who':
            print(f'Вы вошли как: { nameacc }')

def seticon():
    iconfile = fd.askopenfilename()
    root.iconbitmap(iconfile)

def setopacity():
    opacity = input(f'Введите прозрачность:')
    root.wm_attributes( '-alpha', opacity)

def setbg():
    bgtype = input(f'Введите тип # или ничего:')
    bgcolor = input(f'Введите цвет: { bgtype }')
    textm.configure(bg = f'{ bgtype }{ bgcolor }')
    textm1.configure(bg = f'{ bgtype }{ bgcolor }')
    textm2.configure(bg = f'{ bgtype }{ bgcolor }')
    root[ 'bg' ] = f'{ bgtype }{ bgcolor }'

def passgenerate():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Генератор паролей" из-за неправильного ключа "key"')
    else:
        number = int( input( 'Кол-во паролей: ' ) )
        lenght = int( input( 'Длина строки: ' ) )

        if number > 1000:
            real = messagebox.askyesno('Password Generator', 'Вы выбрали 1000 и больше паролей которые будут генерироватся. Возможно файл не сможет открытся! Вы хотите продолжить?')
            if real == 'True':
                pass
            if real == 'False':
                passgenerate

        if lenght > 1000:
            real2 = messagebox.askyesno('Password Generator', 'Вы выбрали 1000 и больше длину паролей которые будут генерироватся. Возможно файл не сможет открытся! Вы хотите продолжить?')
            if real2 == 'True':
                pass
            if real2 == 'False':
                passgenerate
 
        for x in range( number ):
            password = ''
 
        for i in range( lenght ):
            password += random.choice( chars )
 
            file = open( 'password.txt', 'a' )
            file.write( '\n' + password )
            file.close()

            print(f'Пароль был сгенерирован. Пароль: { password }')

def infinitygenerate():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Бесконечная генерация" из-за неправильного ключа "key"')
    else:
        waitime = input(f'Введите задержку: ')
        filein = open( 'infinity.txt', 'a' )
        while True:
            filein.write( '\nInfinity Generating.' )
            print(f'Infinity Generating.')
            asyncio.sleep(waitime)
            filein.write( '\nInfinity Generating..' )
            print(f'Infinity Generating..')
            asyncio.sleep(waitime)
            filein.write( '\nInfinity Generating...' )
            print(f'Infinity Generating...')
            asyncio.sleep(waitime)

def texterror():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно вывести сообщение из-за неправильного ключа "key"')
    else:
        textapi = input(f'Введите заголовок сообщения:')
        textapi2 = input(f'Введите текст сообщения:')
        messagebox.showerror(f'{textapi}', f'{textapi2}')

def textwarning():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно вывести сообщения из-за неправильного ключа "key"')
    else:
        textapiwar = input(f'Введите заголовок сообщения:')
        textapiwar2 = input(f'Введите текст сообщения:')
        messagebox.showwarning(f'{textapiwar}', f'{textapiwar2}')

def textinfo():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно вывести сообщения из-за неправильного ключа "key"')
    else:
        textapiinfo = input(f'Введите заголовок сообщения:')
        textapiinfo2 = input(f'Введите текст сообщения:')
        messagebox.showinfo(f'{textapiinfo}', f'{textapiinfo2}')

def editinfobutton():
    bgtype2 = input(f'Введите тип # или ничего:')
    bgcolor2 = input(f'Введите цвет: {bgtype2}')
    fgcolor2 = input(f'Введите цвет текста: {bgtype2}')
    infobutton.configure(bg = f'{ bgtype2 }{ bgcolor2 }', fg = f'{ bgtype2 }{ fgcolor2 }')

def edittextm():
    bgtype3 = input(f'Введите тип # или ничего:')
    bgcolor3 = input(f'Введите цвет: {bgtype3}')
    fgcolor3 = input(f'Введите цвет текста: {bgtype3}')
    textm.configure(bg = f'{ bgtype3 }{ bgcolor3 }', fg = f'{ bgtype3 }{ fgcolor3 }')

def programmcrasher():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Stress test" из-за неправильного ключа "key"')
    else:
        while True:
        	print(f'Запущен Stress test!')
        	root[ 'bg' ] = '#113355'
        	root.wm_attributes('-toolwindow', True)
        	print(f'Запущен Stress test!!')
        	root[ 'bg' ] = '#553311'
        	root.wm_attributes('-toolwindow', False)
        	root[ 'bg' ] = '#551133'
        	print(f'Запущен Stress test!!!')

def exitapi():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Выйти из программы" из-за неправильного ключа "key"')
    else:
        messagebox.showwarning('Exit Api', 'После нажатия ок вы выйдете из программы')
        sys.exit(1)

def textread():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Прочитать файл" из-за неправильного ключа "key"')
    else:
        fileread1 = fd.askopenfilename()
        print(f'Начинается чтение файла...')
        print(f'-------------------------------')
        with open(f'{fileread1}', 'r') as f:
            text = f.read()
            print(text)
            print(f'-------------------------------')

def fileremover():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Удалить файл" из-за неправильного ключа "key"')
    else:
        fileinput = fd.askopenfilename()
        messagebox.showwarning('File Remover', 'После нажатия ок файл будет удалён')
        os.remove(fileinput)
        messagebox.showwarning('File Remover', 'Файл был удалён')

def filerenamer():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Перейменовать файл" из-за неправильного ключа "key"')
    else:
        oldname = fd.askopenfilename()
        newname = input(f'Введите новое название файла { oldname }: ')
        os.rename(oldname, newname)
        messagebox.showwarning(f'File Renamer', f'Файл { oldname } был перейменован на { newname }')

def filewhiter():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Записать в файл" из-за неправильного ключа "key"')
    else:
        filename = fd.askopenfilename()
        textforfile = input(f'Введите текст который хотите записать в файл:')
        filename2 = open(f'{ filename }', 'a', encoding = 'utf-8')
        filename2.write(f'{textforfile}\n')

def runsys():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Выполнить команду" из-за неправильного ключа "key"')
    else:
        commandsys = input(f'{ os.getcwd() }>')
        os.system( commandsys )

def checkfolder():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Просмотр файлов в папке" из-за неправильного ключа "key"')
    else:
        pathdir = input(f'Введите путь к папке: ')
        rescf = os.listdir(path = f'{ pathdir }')
        print(f'{ rescf }')

def checkperms():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Проверить права" из-за неправильного ключа "key"')
    else:
        print(f'Это программа позволяет проверить есть ли у вас доступ к файлу или нет')
        checkpermf = fd.askopenfilename()
        print(f'Флаги: os.F_OK - объект существует, os.R_OK - доступен на чтение, os.W_OK - доступен на запись, os.X_OK - доступен на исполнение.')
        cf1 = os.access(checkpermf, 1)
        cf2 = os.access(checkpermf, 2)
        cf3 = os.access(checkpermf, 3)
        cf4 = os.access(checkpermf, 4)
        print(f'Флаг os.F_OK: { cf1 }')
        print(f'Флаг os.R_OK: { cf2 }')
        print(f'Флаг os.W_OK: { cf3 }')
        print(f'Флаг os.X_OK: { cf4 }')

def checkdir():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Где находится программа?" из-за неправильного ключа "key"')
    else:
        osnamey = os.getcwd()
        print(f'Программа находится по следуещему расположению: { osnamey }')

def checkprocessid():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "ID Процесса программы" из-за неправильного ключа "key"')
    else:
        apiprocessid = os.getpid()
        print(f'ID процесса программы: { apiprocessid }')

def editgetbutton():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно изменить элемент под ID: getbutton из-за неправильного ключа "key"')
    else:
        type10 = input(f'Введите # или ничего:')
        bgcolorget10 = input(f'Введите цвет: {type10}')
        fgcolorget10 = input(f'Введите цвет текста: {type10}')
        getbutton.configure(bg = f'{ type10 }{ bgcolorget10 }', fg = f'{ type10 }{ fgcolorget10 }')

def editextm1():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно изменить элемент под ID: textm1 из-за неправильного ключа "key"')
    else:
        type11 = input(f'Введите # или ничего:')
        bgcolorget11 = input(f'Введите цвет: {type11}')
        fgcolorget11 = input(f'Введите цвет текста: {type11}')
        textm1.configure(bg = f'{ type11 }{ bgcolorget11 }', fg = f'{ type11 }{ fgcolorget11 }')

def editextm2():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно изменить элемент под ID: textm2 из-за неправильного ключа "key"')
    else:
        type12 = input(f'Введите # или ничего:')
        bgcolorget12 = input(f'Введите цвет: {type12}')
        fgcolorget12 = input(f'Введите цвет текста: {type12}')
        textm2.configure(bg = f'{ type12 }{ bgcolorget12 }', fg = f'{ type12 }{ fgcolorget12 }')

def playsound():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Воспроизвести музыку" из-за неправильного ключа "key"')
    else:
        soundfile = fd.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")))
        sound = pyglet.media.load(f'{ soundfile }', streaming = False)
        print(f'Внимание: во время использования программы когда она воиспроизводит звуковой файл а именно { soundfile }, могут быть проблемы...')
        sound.play()
        pyglet.app.run()

def setoverrideredirect1():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Включить границу окна" из-за неправильного ключа "key"')
    else:
        root.overrideredirect(1)

def setoverrideredirect0():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Выключить границу окна" из-за неправильного ключа "key"')
    else:
        root.overrideredirect(0)

def ytdownloader():
    if nameacc == 'TEMPUSER':
        while True:
            messagebox.showerror(f'Ошибка реестра', f'Невозможно запустить "Скачать музыку с YouTube" из-за неправильного ключа "key"')
    else:
        yturl = input(f'URL: ')
    
        ydl_opts = {
            'format' : 'bestaudio/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '128'
            }],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([yturl])
            messagebox.showwarning(f'YT Downloader by DragonWolf', f'Была скачана музыка по URL: { yturl }')

        ydl_optst = {
            'format' : 'bestvideo/best',
            'postprocessors' : [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '128'
            }],
        }

        with youtube_dl.YoutubeDL(ydl_optst) as ydlt:
            ydlt.download([yturl])
            messagebox.showwarning(f'YT Downloader by DragonWolf', f'Было скачано видео по URL: { yturl }')

def fullson():
    root.attributes('-fullscreen', True)

def fullsoff():
    root.attributes('-fullscreen', False)

def logoutwin():
	os.system('logout')

def toolswon():
	root.wm_attributes('-toolwindow', True)

def toolswoff():
	root.wm_attributes('-toolwindow', False)

def create_service():
	os.system('sc \api create fwapis description="Service api for Programm By DragonWolf" binpath = "D:\"')

def remove_service():
	os.system('sc delete fwapis')

mainmenu = Menu(root)
root.config(menu = mainmenu)

filemenu = Menu(mainmenu, tearoff = 0)
settings = Menu(mainmenu, tearoff = 0)
helpmenu = Menu(mainmenu, tearoff = 0)
programmmenu = Menu(mainmenu, tearoff = 0)
messagesapi = Menu(mainmenu, tearoff = 0)
elements = Menu(mainmenu, tearoff = 0)
filemanager = Menu(mainmenu, tearoff = 0)
sysmenu = Menu(mainmenu, tearoff = 0)

filemenu.add_command(label = "--------------------------Файл------------------------", activebackground = 'black')
filemenu.add_command(label = "Открыть", command = open_file, activebackground = 'black')
filemenu.add_command(label = "Сохранить как", command = save_file, activebackground = 'black')
filemenu.add_command(label = "-------------------------------------------------------", activebackground = 'black')

settings.add_command(label = "-----------------Основные настройки----------------", activebackground = 'black')
settings.add_command(label = "Включить режим изменения размера", command = editscale, activebackground = 'black')
settings.add_command(label = "Выключить режим изменения размера", command = editscale2, activebackground = 'black')
settings.add_command(label = "Изменить статичный размер", command = editscalestatic, activebackground = 'black')
settings.add_command(label = "Изменить прозрачность", command = setopacity, activebackground = 'black')
settings.add_command(label = "Изменить иконку", command = seticon, activebackground = 'black')
settings.add_command(label = "Изменить цвет фона", command = setbg, activebackground = 'black')
settings.add_command(label = "Включить границу окна", command = setoverrideredirect0, activebackground = 'black')
settings.add_command(label = "Выключить границу окна", command = setoverrideredirect1, activebackground = 'black')
settings.add_command(label = "Включить полноэкранный режим", command = fullson, activebackground = 'black')
settings.add_command(label = "Выключить полноэкранный режим", command = fullsoff, activebackground = 'black')
settings.add_command(label = "Включить режим инструментного окна", command = toolswon, activebackground = 'black')
settings.add_command(label = "Выключить режим инструментного окна", command = toolswoff, activebackground = 'black')
settings.add_command(label = "--------------------------------------------------------", activebackground = 'black')

helpmenu.add_command(label = "---------Помощь по программе и инфо----------", activebackground = 'black')
helpmenu.add_command(label = "Кто создавал?", command = creditsprog, activebackground = 'black')
helpmenu.add_command(label = "Связатся по дискорду", command = contact, activebackground = 'black')
helpmenu.add_command(label = "Инфо о программе", command = message, activebackground = 'black')
helpmenu.add_command(label = "-----------------------------------------------------", activebackground = 'black')

programmmenu.add_command(label = "-----------------Программы-----------------", activebackground = 'black')
programmmenu.add_command(label = "Склеивание текста", command = plustext, activebackground = 'black')
programmmenu.add_command(label = "Консоль", command = console, activebackground = 'black')
programmmenu.add_command(label = "Генератор паролей", command = passgenerate, activebackground = 'black')
programmmenu.add_command(label = "Проверка компютера под нагрузкой", command = programmcrasher, activebackground = 'black')
programmmenu.add_command(label = "Выйти из программы", command = exitapi, activebackground = 'black')
programmmenu.add_separator()
programmmenu.add_cascade(label = "Файловый менеджер", menu = filemanager, activebackground = 'black')
programmmenu.add_separator()
programmmenu.add_command(label = "Выполнить команду", command = runsys, activebackground = 'black')
programmmenu.add_command(label = "Просмотр файлов в папке", command = checkfolder, activebackground = 'black')
programmmenu.add_command(label = "Проверить права", command = checkperms, activebackground = 'black')
programmmenu.add_command(label = "Где находится программа?", command = checkdir, activebackground = 'black')
programmmenu.add_command(label = "ID Процесса программы", command = checkprocessid, activebackground = 'black')
programmmenu.add_command(label = "Бесконечная генерация", command = infinitygenerate, activebackground = 'black')
programmmenu.add_command(label = "Воспроизвести музыку", command = playsound, activebackground = 'black')
programmmenu.add_command(label = "Скачать аудио с YouTube", command = ytdownloader, activebackground = 'black')
programmmenu.add_command(label = "------------------------------------------------", activebackground = 'black')

messagesapi.add_command(label = "----------------------Сообщения-----------------", activebackground = 'black')
messagesapi.add_command(label = "Вывести сообщение в ERROR", command = texterror, activebackground = 'black')
messagesapi.add_command(label = "Вывести сообщение в WARNING", command = textwarning, activebackground = 'black')
messagesapi.add_command(label = "Вывести сообщение в INFO", command = textinfo, activebackground = 'black')
messagesapi.add_command(label = "----------------------------------------------------", activebackground = 'black')

elements.add_command(label = "-------------------EDIT ELEMENTS API----------------", activebackground = 'black')
elements.add_command(label = "Изменить обьект с ID: textm", command = edittextm, activebackground = 'black')
elements.add_command(label = "Изменить обьект с ID: infobutton", command = editinfobutton, activebackground = 'black')
elements.add_command(label = "Изменить обьект с ID: textm1", command = editextm1, activebackground = 'black')
elements.add_command(label = "Изменить обьект с ID: textm2", command = editextm2, activebackground = 'black')
elements.add_command(label = "--------------------------------------------------------", activebackground = 'black')

filemanager.add_command(label = "--------------Файловый менеджер----------------", activebackground = 'black')
filemanager.add_command(label = "Прочитать файл", command = textread, activebackground = 'black')
filemanager.add_command(label = "Удалить файл", command = fileremover, activebackground = 'black')
filemanager.add_command(label = "Перейменовать файл", command = filerenamer, activebackground = 'black')
filemanager.add_command(label = "Записать в файл", command = filewhiter, activebackground = 'black')
filemanager.add_command(label = "------------------------------------------------------", activebackground = 'black')

sysmenu.add_command(label = "-------------------Меню Системы---------------------", activebackground = 'black')
sysmenu.add_command(label = "Создать службу программы", command = create_service, activebackground = 'black')
sysmenu.add_command(label = "Удалить службу программы", command = remove_service, activebackground = 'black')
sysmenu.add_command(label = "----------------------------------------------------", activebackground = 'black')

mainmenu.add_cascade(label = "Файл", menu = filemenu)
mainmenu.add_cascade(label = "Настройки", menu = settings)
mainmenu.add_cascade(label = "Помощь", menu = helpmenu)
mainmenu.add_cascade(label = "Программы", menu = programmmenu)
mainmenu.add_cascade(label = "Сообщения", menu = messagesapi)
mainmenu.add_cascade(label = "Элементы", menu = elements)
mainmenu.add_cascade(label = "Система", menu = sysmenu)

textm = Label(text = f'Добро пожаловать в мою программу на питоне', background = 'black', foreground = 'white')
textm.grid(column=0, row=0)

apiprocessid2 = os.getpid()
textm1 = Label(text = f'ID процесса: { apiprocessid2 }. OS: { platform.system() }', background = 'black', foreground = 'white')
textm1.grid(column=0, row=1)

infobutton = Button(text="Инфо о программе", command = message, bg = 'black', fg = 'white', activebackground = 'green')  
infobutton.grid(column=0, row=3)

root.mainloop()
