import sys
import tkinter as tk
from tkinter import PhotoImage, messagebox
from tkinter import ttk
from w_capture_im import ImCaptureWindow
from w_config import ConfigWindow
from w_recog import RecogWindow
from w_registered_list import RegisteredListWindow
from w_result import ResultWindow
from w_base import BaseWindow


class Application(BaseWindow):
    def __init__(self, master=None, auto_start=False):
        super().__init__(master)
        self._capture_window = None
        self._config_window = None
        self._registered_window = None
        self._result_window = None
        self._create_widgets()
        self._auto_start = auto_start
        
        if auto_start:
            self.master.after(500, self._show_recog)
        

    def _create_widgets(self):
        
        padx = 0
        pady = 30
        ipadx = 30
        ipady = 50
        
        #Face Capture Button
        self._button_im = ttk.Button(self._frame_main, text="Face Capture", command=self._show_capture_im)
        self._button_im.grid(column=0, row=0, sticky=tk.EW, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        
        #List Image Face Button
        self._button_reg = ttk.Button(self._frame_main, text="List Images", command=self._show_registered_list)
        self._button_reg.grid(column=2, row=0, sticky=tk.EW, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        
        #Recognition Button
        self._button_rec = ttk.Button(self._frame_main, text="Recognition", command=self._show_recog)
        self._button_rec.grid(column=4, row=0, sticky=tk.EW, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)
        
        #Log Button
        self._button_res = ttk.Button(self._frame_main, text="Log", command=self._show_result)
        self._button_res.grid(column=0, row=1, sticky=tk.EW, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

        #Setting Button
        self._button_conf = ttk.Button(self._frame_main, text="Setting", command=self._show_config)
        self._button_conf.grid(column=2, row=1, sticky=tk.EW, padx=padx, pady=pady, ipadx=ipadx, ipady=ipady)

        self._frame_main.columnconfigure(0, weight=1)
        self._frame_main.columnconfigure(1, minsize=40)
        self._frame_main.columnconfigure(2, weight=1)
        self._frame_main.columnconfigure(3, minsize=40)
        self._frame_main.columnconfigure(4, weight=1)
        for i in range(2):
            self._frame_main.rowconfigure(i, weight=1)
        
        
    def _show_capture_im(self):
        if self._capture_window == None or not self._capture_window.winfo_exists():
            self._capture_window = tk.Toplevel()
            self._capture = ImCaptureWindow(master=self._capture_window)


    def _show_config(self):
        if self._config_window == None or not self._config_window.winfo_exists():
            self._config_window = tk.Toplevel()
            self._config = ConfigWindow(master=self._config_window)
            
            
    def _show_recog(self):
        if self._capture_window == None or not self._capture_window.winfo_exists():
            self._capture_window = tk.Toplevel()
            self._capture = RecogWindow(master=self._capture_window, auto_start=self._auto_start)
            if self._auto_start:
                self._auto_start = False
            
            
    def _show_registered_list(self):
        if self._registered_window == None or not self._registered_window.winfo_exists():
            self._registered_window = tk.Toplevel()
            self._registered_window = RegisteredListWindow(master=self._registered_window)
            
            
    def _show_result(self):
        if self._result_window == None or not self._result_window.winfo_exists():
            self._result_window = tk.Toplevel()
            self._result_window = ResultWindow(master=self._result_window)


if __name__ == "__main__":
    args = sys.argv
    fl = False
    if len(args) > 1 and args[1] == 'catch':
        fl = True
    window = tk.Tk()
    window.title = "Face Recognition"
    app = Application(master=window, auto_start=fl)
    app.mainloop()