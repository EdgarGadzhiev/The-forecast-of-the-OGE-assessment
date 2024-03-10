import tkinter as tk
from tkinter import messagebox


class GradeCalculator:
        
    def __init__(self, root):
        self.root = root
        self.root.title("Расчет оценки ОГЭ")
        self.root.geometry("720x360")
        self.root.configure(bg='light blue')

        self.questions = [
            "1.Оценка за 1 четверть:",
            "2.Оценка за 2 четверть:",
            "3.Оценка за 3 четверть:",
            "4.Оценка за 4 четверть:",
            "5.Средняя оценка за урок:",
            "6.Итоговая оценка:"
        ]

        self.index = 0
        self.answers = []

        self.label = tk.Label(self.root, text=self.questions[self.index], font=("Arial", 20), bg='light blue', fg='black')
        self.label.place(relx=0.5, rely=0.4, anchor="center")

        self.entry = tk.Entry(self.root, font=("Arial", 16), bg='white', fg='black')
        self.entry.place(relx=0.5, rely=0.5, anchor="center")
    
        self.entry.bind("<Return>", lambda event: self.show_next_question())

        self.next_button = tk.Button(self.root, text="Дальше", command=self.show_next_question, font=("Arial", 14), bg='light blue', fg='black')
        self.next_button.place(relx=0.5, rely=0.6, anchor="center")

    def show_next_question(self):
        answer = self.entry.get()
        if not answer.isdigit() or int(answer) < 2 or int(answer) > 5:
            messagebox.showerror("Ошибка", "Введите численное значение от 2 до 5")
            return
        self.answers.append(int(answer))
        self.index += 1
        if self.index < len(self.questions):
            self.label.config(text=self.questions[self.index])
            self.entry.delete(0, tk.END)
        else:
            self.calculate_average()

    def calculate_average(self):
        average = sum(self.answers) / len(self.answers)
        rounded_average = int(average + 0.5)
        self.root.withdraw()
    
        result_window = tk.Toplevel()
        result_window.title("Оценка ОГЭ")
        result_window.geometry("720x360")
        result_window.configure(bg='light blue')

        result_label = tk.Label(result_window, text=f"Оценка ОГЭ: {rounded_average}", font=("Arial", 20), bg='light blue', fg='black')
        result_label.place(relx=0.5, rely=0.4, anchor="center")

        finish_button = tk.Button(result_window, text="Завершить", command=self.close_windows, font=("Arial", 14), bg='light blue', fg='black')
        finish_button.place(relx=0.5, rely=0.6, anchor="center")

    def close_windows(self):
        self.root.destroy()

def main():
    root = tk.Tk()
    root.configure(bg='light blue')
    app = GradeCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
