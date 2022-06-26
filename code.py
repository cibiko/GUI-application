from tkinter import *
from speedtest import Speedtest


def test():
    download = Speedtest().download()
    upload = Speedtest().upload()
    download_speed = round(download / (10**6), 2)
    upload_speed = round(upload / (10**6), 2)

    download_label.config(text="Скорость Загрузки:\n-" + str(download_speed) + "MbPs")
    upload_label.config(text="Скорость Отдачи:\n-" + str(upload_speed) + "MbPs")

#p.s если долго будет загружать ничего страшного, просто идет анализ, через несколько секунд все подгрузит
root = Tk()

root.title("spedtest")
root.geometry("300x400")

button = Button(root, text="Нажмите чтоб начать ", font=40, command=test)
button.pack(side=BOTTOM, pady=40)


download_label = Label(root, text="Скорость Загрузки:\n-", font=35)
download_label.pack(pady=(50, 0))

upload_label = Label(root, text="Скорость Отдачи:\n-", font=35)
upload_label.pack(pady=(10, 0))

root.mainloop()