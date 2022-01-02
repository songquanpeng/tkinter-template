from tkinter import *
from tkinter.ttk import *

from common import ThreadedTask


def main():
    window = Tk()
    window.title('Tkinter Template')
    window.rowconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.geometry('500x300')
    window.resizable(0, 0)

    start_var = IntVar(value=0)
    step_var = IntVar(value=1)
    prompt_var = StringVar(value='>>> ')
    btn_var = StringVar(value='Start')

    frame = Frame(window)
    frame.grid(row=0, column=0, sticky='ns')
    frame.rowconfigure(4, weight=1)

    Label(frame, text='Start:').grid(row=0, column=0, pady=(40, 0))
    Entry(frame, textvariable=start_var).grid(row=0, column=1, pady=(40, 0))
    Label(frame, text='Step:').grid(row=1, column=0)
    Entry(frame, textvariable=step_var).grid(row=1, column=1)
    Label(frame, text='Prompt:').grid(row=2, column=0)
    Entry(frame, textvariable=prompt_var).grid(row=2, column=1)

    text_board = Text(window, font='Consolas -12')
    text_board.grid(row=0, column=1)
    text_board.bind("<Key>", lambda a: "break")  # Make it readonly.

    worker = None
    start_num = start_var.get()

    def on_start_btn_clicked(*_):
        nonlocal worker, start_num
        if worker is None:
            worker = ThreadedTask(text_board, start=start_num, step=step_var.get(), prompt=prompt_var.get())
            worker.start()
            btn_var.set('Stop')
        else:
            worker.stop()
            start_num = worker.current
            worker = None
            btn_var.set('Start')

    def on_clear_btn_clicked(*_):
        text_board.delete('1.0', END)

    start_btn = Button(frame, text='Start', command=on_start_btn_clicked)
    start_btn.grid(row=3, column=0, padx=(40, 20), pady=(30, 40))
    clear_btn = Button(frame, text='Clear', command=on_clear_btn_clicked)
    clear_btn.grid(row=3, column=1, padx=(20, 20), pady=(30, 40))

    mainloop()


if __name__ == '__main__':
    main()
