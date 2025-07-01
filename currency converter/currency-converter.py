from currency_converter import CurrencyConverter
import tkinter as tk

window = tk.Tk()
window.geometry("500x400")
cur_conv = CurrencyConverter()
#! Process to Convert Currency 
def convert_currency():
    amount = int(enter_amount.get())
    from_curr = enter_currency.get()
    to_curr = to_currency.get()
    data = cur_conv.convert(amount, from_curr, to_curr)
    converted_amount = tk.Label(window, text=data , font="Arial 12 bold").place(x=180, y=325)

#! For Title
title = tk.Label(window, text="Currency Converter", font="Arial 20 bold underline").place(x=120, y=20)
#! Label of Enter amount to convert
amount = tk.Label(window, text="Enter amount to convert:", font="Arial 12 bold").place(x=20, y=100)
#! Enter amount to convert
enter_amount = tk.Entry(window)
#! Label of Currency to convert from
from_currency = tk.Label(window, text="Currency to convert from:", font="Arial 12 bold").place(x=20, y=150)
#! Enter currency 
enter_currency = tk.Entry(window)
#! Label of Currency to convert to
from_currency = tk.Label(window, text="Currency to convert to:", font="Arial 12 bold").place(x=20, y=200)
#! Enter currency in which amount to be converted
to_currency = tk.Entry(window)
#! Button to convert currency
convert = tk.Button(window, text="Convert", font="Arial 12 bold", command=convert_currency).place(x=220, y=250)

enter_amount.place(x=230, y=100, width=200)
enter_currency.place(x=230, y=150, width=200)
to_currency.place(x=230, y=200, width=200)



window.mainloop()