# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 13:50:53 2024

@author: echo
"""
#HK windows
import random
import tkinter as tk
from tkinter import ttk
class WinGUI(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_input_LU = self.__tk_input_ltmiqmpg(self)
        self.tk_input_RU = self.__tk_input_ltmiqp4u(self)
        self.tk_input_LD = self.__tk_input_ltmiqrb5(self)
        self.tk_input_RD = self.__tk_input_ltmiqudd(self)
        self.tk_text_ltmir2qp = self.__tk_text_ltmir2qp(self)
        self.tk_label_ltmispp2 = self.__tk_label_ltmispp2(self)
        self.tk_label_ltmit3x8 = self.__tk_label_ltmit3x8(self)
        self.tk_label_ltmitivo = self.__tk_label_ltmitivo(self)
        self.tk_label_ltmivjis = self.__tk_label_ltmivjis(self)
        self.tk_button_ltmixbaz = self.__tk_button_ltmixbaz(self)
        self.tk_button_Back = self.__tk_button_Back(self)
    def __win(self):
        self.title("HK BUS")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)      
        self.resizable(width=False, height=False)
        
    def __tk_input_ltmiqmpg(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=89, y=69, width=150, height=30)
        return ipt
    def __tk_input_ltmiqp4u(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=359, y=69, width=150, height=30)
        return ipt
    def __tk_input_ltmiqrb5(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=89, y=159, width=149, height=30)
        return ipt
    def __tk_input_ltmiqudd(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=362, y=162, width=148, height=30)
        return ipt
    def __tk_text_ltmir2qp(self,parent):
        text = tk.Text(parent)
        text.place(x=0, y=283, width=600, height=217)
        return text
    def __tk_label_ltmispp2(self,parent):
        label = tk.Label(parent,text="bus",anchor="center", )
        label.place(x=134, y=18, width=50, height=30)
        return label
    def __tk_label_ltmit3x8(self,parent):
        label = tk.Label(parent,text="direction",anchor="center", )
        label.place(x=371, y=19, width=121, height=30)
        return label
    def __tk_label_ltmitivo(self,parent):
        label = tk.Label(parent,text="stop id",anchor="center", )
        label.place(x=133, y=115, width=52, height=30)
        return label
    def __tk_label_ltmivjis(self,parent):
        label = tk.Label(parent,text="bus",anchor="center", )
        label.place(x=413, y=120, width=50, height=30)
        return label
    def __tk_button_ltmixbaz(self,parent):
        btn = tk.Button(parent, text="inqury", takefocus=False, command=self.cause)
        btn.place(x=110, y=224, width=114, height=30)
        return btn
    def __tk_button_Back(self, parent):
        btn = tk.Button(parent, text="Back", takefocus=False, command= self.switch_to_main)
        btn.place(x=364, y=224, width=114, height=30)
        return btn
    def cause(self):
        busroute1 = self.tk_input_LU.get()
        direction = self.tk_input_RU.get()
        idx = self.tk_input_LD.get()
        busroute2 = self.tk_input_RD.get()
        import API as ap
        if busroute1 and direction:  
            try:
                re1 = ap.HK_bus(busroute1,direction)
            except:
                re1 = 'Not a good input for busroute and direction~'
        else:
            re1 = 'None'
        if idx and busroute2:
            try:
                re2 = ap.coming_bus(idx,busroute2)
            except:
                re2 = 'Not a good input for stop_id and busroute~'
        else:
            re2 = 'None'
        self.tk_text_ltmir2qp.insert(tk.END,re1)
        self.tk_text_ltmir2qp.insert(tk.END,re2)        
    def switch_to_main(self):
        import MSDM5051FinalProjectCode as MSD
        self.withdraw()  # 隐藏窗口1
        MSD.main_window.deiconify()  # 显示主窗口
