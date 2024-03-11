import tkinter as tk
from tkinter import ttk
import pandas as pd

class MainWindow(tk.Tk):
    def __init__(self):
        columns = ["VehicleType", "DerectionTime_O", "GantryID_O", "DerectionTime_D", "GantryID_D", "TripLength", "TripEnd", "TripInformation"]
        self.data = pd.read_csv('data.csv')
        super().__init__()
        self.__win()
        self.tk_label_lq7ew9f0 = self.__tk_label_lq7ew9f0(self)
        self.tk_button_lq7ez86u = self.__tk_button_lq7ez86u(self)
        self.tk_button_lq7ezj5h = self.__tk_button_lq7ezj5h(self)
        self.tk_button_lq7ezuaj = self.__tk_button_lq7ezuaj(self)
        self.tk_table_lqbqre53 = self.__tk_table_lqbqre53(self)

    def __win(self):
        self.title("Inqury system of Taiwan traffic")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        
    def __tk_label_lq7ew9f0(self,parent):
        label = tk.Label(parent,text="Please choose one of our services",anchor="center", )
        label.place(x=73, y=13, width=449, height=30)
        return label
    def __tk_button_lq7ez86u(self,parent):
        btn = tk.Button(parent, text="search", takefocus=False,command = self.switch_to_window1)
        btn.place(x=89, y=63, width=122, height=30)
        return btn
    def __tk_button_lq7ezj5h(self,parent):
        btn = tk.Button(parent, text="sort", takefocus=False,command = self.switch_to_window2)
        btn.place(x=243, y=63, width=116, height=30)
        return btn
    def __tk_button_lq7ezuaj(self,parent):
        btn = tk.Button(parent, text="join", takefocus=False,command = self.switch_to_window3)
        btn.place(x=393, y=63, width=121, height=31)
        return btn

    def tk_button_update(self):
        self.tk_table.delete(*self.tk_table.get_children())
        for i in range(min(len(self.data),20)):
            row_data = self.data.iloc[i]
            self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
        self.tk_table.place(x=1, y=250, width=599, height=250)
        return self.tk_table

    def __tk_table_lqbqre53(self,parent):
        width = 74
        columns = {"VehicleType": width, "DerectionTime_O": width, "GantryID_O": width, "DerectionTime_D": width,
                   "GantryID_D": width, "TripLength": width, "TripEnd": width, "TripInformation": width}
        self.tk_table = ttk.Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            self.tk_table.heading(text, text=text, anchor='center')
            self.tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        for i in range(20):
            row_data = self.data.iloc[i]
            self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
        self.tk_table.place(x=1, y=250, width=599, height=250)
        return self.tk_table

    def switch_to_window1(self):
        window1 = Window1()
        self.withdraw()  # 隐藏主窗口
        window1.deiconify()  # 显示窗口1
        window1.data = self.data

    def switch_to_window2(self):
        window2 = Window2()
        self.withdraw()  # 隐藏主窗口
        window2.deiconify()  # 显示窗口2
        window2.data = self.data

    def switch_to_window3(self):
        window3 = Window3()
        self.withdraw()  # 隐藏主窗口
        window3.deiconify()  # 显示窗口3
        window3.data = self.data
        

class Window1(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.data = main_window.data
        self.tk_label_lqbr7qjk = self.__tk_label_lqbr7qjk(self)
        self.tk_input_VehicleType = self.__tk_input_lqbr90bp(self)
        self.tk_label_lqbr98fa = self.__tk_label_lqbr98fa(self)
        self.tk_input_DerectionTime_O_from = self.__tk_input_lqbs9air(self)
        self.tk_label_lqbs9row = self.__tk_label_lqbs9row(self)
        self.tk_input_GantryID_O = self.__tk_input_lqbsahmb(self)
        self.tk_label_lqbsalww = self.__tk_label_lqbsalww(self)
        self.tk_input_DerectionTime_D_from = self.__tk_input_lqbsbxo8(self)
        self.tk_label_lqbsc876 = self.__tk_label_lqbsc876(self)
        self.tk_input_TripLength = self.__tk_input_lqbscfli(self)
        self.tk_label_lqbsg8ba = self.__tk_label_lqbsg8ba(self)
        self.tk_input_TripEnd = self.__tk_input_lqbsgvpe(self)
        self.tk_input_DerectionTime_O_to = self.__tk_input_lqbsh5tr(self)
        self.tk_label_lqbshtpb = self.__tk_label_lqbshtpb(self)
        self.tk_label_lqbsi55g = self.__tk_label_lqbsi55g(self)
        self.tk_label_lqbsj8vv = self.__tk_label_lqbsj8vv(self)
        self.tk_label_lqbsjqq7 = self.__tk_label_lqbsjqq7(self)
        self.tk_input_DerectionTime_D_to = self.__tk_input_lqbsjxu6(self)
        self.tk_label_lqbsm29e = self.__tk_label_lqbsm29e(self)
        self.tk_input_GantryID_D = self.__tk_input_lqbsmv90(self)
        self.tk_label_lqbsp6mp = self.__tk_label_lqbsp6mp(self)
        self.tk_button_lqbsr4xf = self.__tk_button_lqbsr4xf(self)
        self.tk_button_lqbsrtak = self.__tk_button_lqbsrtak(self)
        self.tk_button_lqbssvbm = self.__tk_button_lqbssvbm(self)
        self.tk_table_lqbstt9g = self.__tk_table_lqbstt9g(self)

    def __win(self):
        self.title("search")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        
        self.resizable(width=False, height=False)
        

    def __tk_label_lqbr7qjk(self,parent):
        label = tk.Label(parent,text="VehicleType",anchor="center", )
        label.place(x=329, y=8, width=125, height=30)
        return label
    def __tk_input_lqbr90bp(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=465, y=7, width=128, height=30)
        return ipt
    def __tk_label_lqbr98fa(self,parent):
        label = tk.Label(parent,text="DerectionTime_O",anchor="center", )
        label.place(x=9, y=62, width=131, height=30)
        return label
    def __tk_input_lqbs9air(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=212, y=60, width=150, height=30)
        return ipt
    def __tk_label_lqbs9row(self,parent):
        label = tk.Label(parent,text="GantryID_O",anchor="center", )
        label.place(x=10, y=117, width=129, height=30)
        return label
    def __tk_input_lqbsahmb(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=151, y=118, width=121, height=30)
        return ipt
    def __tk_label_lqbsalww(self,parent):
        label = tk.Label(parent,text="DerectionTime_D",anchor="center", )
        label.place(x=10, y=178, width=132, height=30)
        return label
    def __tk_input_lqbsbxo8(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=212, y=178, width=150, height=30)
        return ipt
    def __tk_label_lqbsc876(self,parent):
        label = tk.Label(parent,text="TripLength",anchor="center", )
        label.place(x=10, y=233, width=131, height=30)
        return label
    def __tk_input_lqbscfli(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=147, y=234, width=150, height=30)
        return ipt
    def __tk_label_lqbsg8ba(self,parent):
        label = tk.Label(parent,text="TripEnd",anchor="center", )
        label.place(x=305, y=234, width=131, height=30)
        return label
    def __tk_input_lqbsgvpe(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=445, y=233, width=150, height=30)
        return ipt
    def __tk_input_lqbsh5tr(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=444, y=60, width=150, height=30)
        return ipt
    def __tk_label_lqbshtpb(self,parent):
        label = tk.Label(parent,text="from",anchor="center", )
        label.place(x=150, y=61, width=50, height=30)
        return label
    def __tk_label_lqbsi55g(self,parent):
        label = tk.Label(parent,text="to",anchor="center", )
        label.place(x=372, y=60, width=50, height=30)
        return label
    def __tk_label_lqbsj8vv(self,parent):
        label = tk.Label(parent,text="from",anchor="center", )
        label.place(x=150, y=178, width=50, height=30)
        return label
    def __tk_label_lqbsjqq7(self,parent):
        label = tk.Label(parent,text="to",anchor="center", )
        label.place(x=371, y=178, width=50, height=30)
        return label
    def __tk_input_lqbsjxu6(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=444, y=178, width=148, height=30)
        return ipt
    def __tk_label_lqbsm29e(self,parent):
        label = tk.Label(parent,text="GantryID_D",anchor="center", )
        label.place(x=292, y=117, width=126, height=30)
        return label
    def __tk_input_lqbsmv90(self,parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=443, y=116, width=150, height=30)
        return ipt
    def __tk_label_lqbsp6mp(self,parent):
        label = tk.Label(parent,text="Please enter the corresponding feature to search",anchor="center", )
        label.place(x=11, y=8, width=305, height=30)
        return label
    def __tk_button_lqbsr4xf(self,parent):
        def button_clicked_search():
            df = self.data
            df["DerectionTime_O"] = pd.to_datetime(df["DerectionTime_O"], format="%Y/%m/%d %H:%M:%S")
            df["DerectionTime_D"] = pd.to_datetime(df["DerectionTime_D"], format="%Y/%m/%d %H:%M:%S")

            VehicleType = self.tk_input_VehicleType.get()
            DerectionTime_O_start = self.tk_input_DerectionTime_O_from.get()
            DerectionTime_O_end = self.tk_input_DerectionTime_O_to.get()
            GantryID_O = self.tk_input_GantryID_O.get()
            GantryID_D = self.tk_input_GantryID_D.get()
            DerectionTime_D_start =self.tk_input_DerectionTime_D_from.get()
            DerectionTime_D_end = self.tk_input_DerectionTime_D_to.get()
            TripLength = self.tk_input_TripLength.get()
            TripEnd = self.tk_input_TripEnd.get()

            lst = [VehicleType, DerectionTime_O_start, DerectionTime_O_end, GantryID_O, GantryID_D, DerectionTime_D_start, DerectionTime_D_end, TripLength, TripEnd]
            if pd.Series(lst).isnull().all():
                return df

            mask = True
            if not VehicleType.strip() == "":
                mask &= (df["VehicleType"] == int(VehicleType))
            if not GantryID_O.strip() == "":
                mask &= (df["GantryID_O"] == GantryID_O)
            if not GantryID_D.strip() == "":
                mask &= (df["GantryID_D"] == GantryID_D)
            if not TripLength.strip() == "":
                mask &= (df["TripLength"] == float(TripLength))
            if not TripEnd.strip() == "":
                mask &= (df["TripEnd"] == TripEnd)
            if not DerectionTime_O_start.strip() == "" and not DerectionTime_O_end.strip() == "":
                start_datetime = pd.to_datetime(DerectionTime_O_start, format="%Y/%m/%d %H:%M:%S")
                end_datetime = pd.to_datetime(DerectionTime_O_end, format="%Y/%m/%d %H:%M:%S")
                mask &= (df["DerectionTime_O"] >= start_datetime) & (df["DerectionTime_O"] <= end_datetime)
            elif not DerectionTime_O_start.strip() == "":
                start_datetime = pd.to_datetime(DerectionTime_O_start, format="%Y/%m/%d %H:%M:%S")
                mask &= (df["DerectionTime_O"] >= start_datetime)
            elif not DerectionTime_O_end.strip() == "":
                end_datetime = pd.to_datetime(DerectionTime_O_end, format="%Y/%m/%d %H:%M:%S")
                mask &= (df["DerectionTime_O"] <= end_datetime)
            if not DerectionTime_D_start.strip() == "" and not DerectionTime_D_end.strip() == "":
                start_datetime = pd.to_datetime(DerectionTime_D_start, format="%Y/%m/%d %H:%M:%S")
                end_datetime = pd.to_datetime(DerectionTime_D_end, format="%Y/%m/%d %H:%M:%S")
                mask &= (df["DerectionTime_D"] >= start_datetime) & (df["DerectionTime_O"] <= end_datetime)
            elif not DerectionTime_D_start.strip() == "":
                start_datetime = pd.to_datetime(DerectionTime_D_start, format="%Y/%m/%d %H:%M:%S")
                mask &= (df["DerectionTime_D"] >= start_datetime)
            elif not DerectionTime_D_end.strip() == "":
                end_datetime = pd.to_datetime(DerectionTime_D_end, format="%Y/%m/%d %H:%M:%S")
                mask &= (df["DerectionTime_D"] <= end_datetime)

            filtered_df = df[mask]
            self.data = filtered_df
            self.tk_table.delete(*self.tk_table.get_children())
            for i in range(len(filtered_df)):
                row_data = filtered_df.iloc[i]
                self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
            #self.tk_table.place(x=1, y=250, width=599, height=177)
            self.tk_table.place(x=0, y=320, width=600, height=177)
            return filtered_df

        btn = tk.Button(parent, text="search", takefocus=False, command=button_clicked_search)
        btn.place(x=9, y=280, width=169, height=30)
        return btn
    def __tk_button_lqbsrtak(self,parent):
        btn = tk.Button(parent, text="save", takefocus=False,command=self.savefunction)
        btn.place(x=208, y=280, width=181, height=30)
        return btn
    def __tk_button_lqbssvbm(self,parent):
        btn = tk.Button(parent, text="back", takefocus=False,command = self.switch_to_main)
        btn.place(x=413, y=280, width=181, height=30)
        return btn
    def __tk_table_lqbstt9g(self,parent):
        width = 74
        columns = {"VehicleType":width,"DerectionTime_O":width,"GantryID_O":width,"DerectionTime_D":width,"GantryID_D":width,"TripLength":width,"TripEnd":width,"TripInformation":width}
        self.tk_table = ttk.Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            self.tk_table.heading(text, text=text, anchor='center')
            self.tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        self.tk_table.place(x=0, y=320, width=600, height=177)
        return self.tk_table

    def tk_button_update(self):
        self.tk_table.delete(*self.tk_table.get_children())
        for i in range(len(self.data)):
            row_data = self.data.iloc[i]
            self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
        self.tk_table.place(x=0, y=320, width=600, height=177)
        return self.tk_table

    def savefunction(self):
        df = self.data
        df.to_csv('search.csv', index=False)

    def switch_to_main(self):
        self.withdraw()  # 隐藏窗口1
        main_window.deiconify()  # 显示主窗口
        main_window.data = self.data
        main_window.tk_button_update()


class Window2(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.data = main_window.data
        self.tk_button_lq2hbscl = self.__tk_button_lq2hbscl(self)
        self.tk_table_lq2hdu7q = self.__tk_table_lq2hdu7q(self)
        self.tk_button_lq2hetcm = self.__tk_button_lq2hetcm(self)
        self.tk_button_lq2hfoqp = self.__tk_button_lq2hfoqp(self)
        self.tk_select_box_lq2hmqnm = self.__tk_select_box_lq2hmqnm(self)

    def __win(self):
        self.title("sort")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def __tk_button_lq2hbscl(self, parent):
        btn = tk.Button(parent, text="save", takefocus=False, command=self.savefunction)
        btn.place(x=220, y=160, width=160, height=52)
        return btn

    def __tk_table_lq2hdu7q(self, parent):
        # 表头字段 表头宽度
        width = 74
        columns = {"VehicleType": width, "DerectionTime_O": width, "GantryID_O": width, "DerectionTime_D": width,
                   "GantryID_D": width, "TripLength": width, "TripEnd": width, "TripInformation": width}
        self.tk_table = ttk.Treeview(parent, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            self.tk_table.heading(text, text=text, anchor='center')
            self.tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        for i in range(20):
            row_data = self.data.iloc[i]
            self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
        self.tk_table.place(x=1, y=250, width=599, height=250)
        return self.tk_table

    def __tk_button_lq2hetcm(self, parent):
        def heap_sort(df, selected_row):
            heap = [(value, index) for index, value in enumerate(df[selected_row])]
            n = len(heap)

            for i in range(n // 2 - 1, -1, -1):
                heapify(heap, n, i)

            for i in range(n - 1, 0, -1):
                heap[0], heap[i] = heap[i], heap[0]
                heapify(heap, i, 0)

            sorted_df = df.iloc[[index for _, index in heap]]

            return sorted_df

        def heapify(heap, n, i):
            largest = i
            left_child = 2 * i + 1
            right_child = 2 * i + 2

            if left_child < n and heap[left_child][0] > heap[largest][0]:
                largest = left_child

            if right_child < n and heap[right_child][0] > heap[largest][0]:
                largest = right_child

            if largest != i:
                heap[i], heap[largest] = heap[largest], heap[i]
                heapify(heap, n, largest)

        def button_clicked():
            tk_table = self.tk_select_box_lq2hmqnm
            selected_row = tk_table.get()
            sorted_df = heap_sort(self.data, selected_row)
            self.data = sorted_df
            self.tk_table.delete(*self.tk_table.get_children())
            for i in range(20):
                row_data = sorted_df.iloc[i]
                self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
            self.tk_table.place(x=1, y=250, width=599, height=250)
            return sorted_df

        btn = tk.Button(parent, text="sort", takefocus=False, command=button_clicked)
        btn.place(x=20, y=160, width=161, height=52)
        return btn

    def __tk_button_lq2hfoqp(self, parent):
        btn = tk.Button(parent, text="back", takefocus=False, command=self.switch_to_main)
        btn.place(x=420, y=160, width=166, height=50)
        return btn

    def __tk_select_box_lq2hmqnm(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = (
        "VehicleType", "DerectionTime_O", "GantryID_O", "DerectionTime_D", "GantryID_D", "TripLength", "TripEnd",
        "TripInformation")
        cb.place(x=90, y=40, width=441, height=68)
        return cb

    def savefunction(self):
        df = self.data
        df.to_csv('sort.csv', index=False)

    def switch_to_main(self):
        self.withdraw()  # 隐藏窗口1
        main_window.deiconify()  # 显示主窗口
        main_window.data = self.data
        main_window.tk_button_update()


class Window3(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.data = pd.read_csv('data.csv')
        self.tk_input_VT = self.__tk_input_VT(self)
        self.tk_input_DT_O = self.__tk_input_DT_O(self)
        self.tk_input_GID_O = self.__tk_input_GID_O(self)
        self.tk_input_DT_D = self.__tk_input_DT_D(self)
        self.tk_input_GID_D = self.__tk_input_GID_D(self)
        self.tk_input_TL = self.__tk_input_TL(self)
        self.tk_label_lqbyewgz = self.__tk_label_lqbyewgz(self)
        self.tk_label_lqbyfq6c = self.__tk_label_lqbyfq6c(self)
        self.tk_label_lqbygl3w = self.__tk_label_lqbygl3w(self)
        self.tk_label_lqbymnuv = self.__tk_label_lqbymnuv(self)
        self.tk_label_lqbymp61 = self.__tk_label_lqbymp61(self)
        self.tk_label_lqbymq97 = self.__tk_label_lqbymq97(self)
        self.tk_label_lqbymr9o = self.__tk_label_lqbymr9o(self)
        self.tk_label_lqbymsdx = self.__tk_label_lqbymsdx(self)
        self.tk_input_TE = self.__tk_input_TE(self)
        self.tk_input_TI = self.__tk_input_TI(self)
        self.tk_button_Join = self.__tk_button_Join(self)
        self.tk_button_Back = self.__tk_button_Back(self)
        self.tk_table_join = self.__tk_table_lqbyxnga(self)
        self.tk_button_save = self.__tk_button_Save(self)

    def __win(self):
        self.title("Join")
        # 设置窗口大小、居中
        width = 800
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def __tk_input_VT(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=35, y=85, width=100, height=30)
        return ipt

    def __tk_input_DT_O(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=157, y=85, width=110, height=30)
        return ipt

    def __tk_input_GID_O(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=276, y=85, width=100, height=30)
        return ipt

    def __tk_input_DT_D(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=400, y=85, width=115, height=30)
        return ipt

    def __tk_input_GID_D(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=35, y=200, width=100, height=30)
        return ipt

    def __tk_input_TL(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=157, y=200, width=105, height=30)
        return ipt

    def __tk_label_lqbyewgz(self, parent):
        label = tk.Label(parent, text="VehicleType", anchor="center", )
        label.place(x=35, y=45, width=100, height=30)
        return label

    def __tk_label_lqbyfq6c(self, parent):
        label = tk.Label(parent, text="DerectionTime_O", anchor="center", )
        label.place(x=157, y=45, width=110, height=30)
        return label

    def __tk_label_lqbygl3w(self, parent):
        label = tk.Label(parent, text="GantryID_O", anchor="center", )
        label.place(x=276, y=45, width=100, height=30)
        return label

    def __tk_label_lqbymnuv(self, parent):
        label = tk.Label(parent, text="DerectionTime_D", anchor="center", )
        label.place(x=400, y=45, width=115, height=30)
        return label

    def __tk_label_lqbymp61(self, parent):
        label = tk.Label(parent, text="GantryID_D", anchor="center", )
        label.place(x=35, y=150, width=100, height=30)
        return label

    def __tk_label_lqbymq97(self, parent):
        label = tk.Label(parent, text="TripLength", anchor="center", )
        label.place(x=157, y=150, width=106, height=30)
        return label

    def __tk_label_lqbymr9o(self, parent):
        label = tk.Label(parent, text="TripEnd", anchor="center", )
        label.place(x=276, y=150, width=100, height=30)
        return label

    def __tk_label_lqbymsdx(self, parent):
        label = tk.Label(parent, text="TripInformation", anchor="center", )
        label.place(x=400, y=150, width=115, height=30)
        return label

    def __tk_input_TE(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=276, y=200, width=100, height=30)
        return ipt

    def __tk_input_TI(self, parent):
        ipt = tk.Entry(parent, )
        ipt.place(x=400, y=200, width=115, height=30)
        return ipt

    def __tk_button_Join(self, parent):
        def button_clicked():
            VehicleType = self.tk_input_VT.get()
            DerectionTime_O = self.tk_input_DT_O.get()
            GantryID_O = self.tk_input_GID_O.get()
            GantryID_D = self.tk_input_GID_D.get()
            DerectionTime_D = self.tk_input_DT_D.get()
            TripLength = self.tk_input_TL.get()
            TripEnd = self.tk_input_TE.get()
            TripInformation = self.tk_input_TI.get()
            data_insert = {'VehicleType': VehicleType, 'DerectionTime_O': DerectionTime_O, 'GantryID_O': GantryID_O,
                           'DerectionTime_D': DerectionTime_D, 'GantryID_D': GantryID_D, 'TripLength': TripLength,
                           'TripEnd': TripEnd, 'TripInformation': TripInformation}
            data_judge = {}
            for i in data_insert.keys():
                if data_insert[i] == "":
                    data_insert[i] = 'Nothing'
            pass_judge = 1
            for i in data_insert.keys():
                if i == 'VehicleType':
                    try:
                        data_insert[i] = int(data_insert[i])
                        data_judge[i] = 'valid'
                    except:
                        data_judge[i] = 'invalid'
                        pass_judge = 0
                elif i == 'DerectionTime_O':
                    date_str = ['1', '2', '3']
                    pass_local = 0
                    for j in date_str:
                        if j in data_insert[i]:
                            pass_local = 1
                    if pass_local == 1:
                        data_judge[i] = 'valid'
                    else:
                        data_judge[i] = 'invalid'
                        pass_judge = 0
                elif i == 'DerectionTime_D':
                    date_str = ['1', '2', '3']
                    pass_local = 0
                    for j in date_str:
                        if j in data_insert[i]:
                            pass_local = 1
                    if pass_local == 1:
                        data_judge[i] = 'valid'
                    else:
                        data_judge[i] = 'invalid'
                        pass_judge = 0
                elif i == 'TripLength':
                    try:
                        data_insert[i] = float(data_insert[i])
                        data_judge[i] = 'valid'
                    except:
                        data_judge[i] = 'invalid'
                        pass_judge = 0
                else:
                    data_judge[i] = 'valid'


            if pass_judge == 1:
                self.data = self.data.append(data_insert, ignore_index=True)
                filtered_df = self.data.iloc[-1]
                self.tk_table_join.insert("", 1, text='2', values=tuple(filtered_df))
                # self.tk_table.place(x=1, y=250, width=599, height=177)
                self.tk_table_join.place(x=0, y=320, width=800, height=155)
            else:
                filtered_df = data_insert.values()
                self.tk_table_join.insert("", 1, text='2', values=tuple(filtered_df))
                # self.tk_table.place(x=1, y=250, width=599, height=177)
                self.tk_table_join.place(x=0, y=320, width=800, height=155)
                filtered_df = data_judge.values()
                self.tk_table_join.insert("", 1, text='2', values=tuple(filtered_df))
                # self.tk_table.place(x=1, y=250, width=599, height=177)
                self.tk_table_join.place(x=0, y=320, width=800, height=155)

        btn = tk.Button(parent, text="Join", takefocus=False, command=button_clicked)
        btn.place(x=129, y=258, width=100, height=30)
        return btn

    def __tk_button_Back(self, parent):
        btn = tk.Button(parent, text="Back", takefocus=False, command= self.switch_to_main)
        btn.place(x=345, y=258, width=100, height=30)
        return btn

    def __tk_table_lqbyxnga(self, parent):
        # 表头字段 表头宽度
        columns = {"VehicleType": 119, "DerectionTime_O": 119, "GantryID_O": 79, "DerectionTime_D": 119,
                   "GantryID_D": 79, "TripLength": 79, "TripEnd": 79, "TripInformation": 119}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸

        tk_table.place(x=0, y=320, width=800, height=155)
        return tk_table

    def tk_button_update(self):
        self.tk_table.delete(*self.tk_table.get_children())
        for i in range(len(self.data)):
            row_data = self.data.iloc[i]
            self.tk_table.insert("", i, text=f"Row {i + 1}", values=tuple(row_data))
        self.tk_table.place(x=1, y=250, width=599, height=250)
        return self.tk_table

    def __tk_button_Save(self, parent):
        btn = tk.Button(parent, text="Save", takefocus=False, command= self.savefunction)
        btn.place(x=561, y=258, width=100, height=30)
        return btn
    def savefunction(self):
        df = self.data
        df.to_csv('join.csv', index=False)

    def switch_to_main(self):
        self.withdraw()  # 隐藏窗口1
        main_window.deiconify()  # 显示主窗口
        main_window.data = self.data
        main_window.tk_button_update()

main_window = MainWindow()
# 运行主循环
main_window.mainloop()
