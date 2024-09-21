import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учёт школьной техники")
        self.setGeometry(400, 200, 600, 400)  # Устанавливаем размеры окна
        
        # Создаём главный виджет, который будет центральным в окне
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # Основной вертикальный макет для элементов
        main_layout = QVBoxLayout()

        # 1. Заголовок
        title_label = QLabel("УЧЁТ ШКОЛЬНОЙ ТЕХНИКИ")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; text-align: center;")
        main_layout.addWidget(title_label)

        # 2. Общая статистика
        stats_layout = QVBoxLayout()
        stats_layout.addWidget(QLabel(f"Общее количество устройств: {120}"))
        stats_layout.addWidget(QLabel(f"Исправные устройства: {100}"))
        stats_layout.addWidget(QLabel(f"Требуют ремонта: {15}"))
        stats_layout.addWidget(QLabel(f"Списанные устройства: {5}"))
        main_layout.addLayout(stats_layout)

        # 3. Кнопки для действий
        button_layout = QHBoxLayout()
        add_button = QPushButton("Добавить технику")
        view_button = QPushButton("Просмотреть всё оборудование")
        search_button = QPushButton("Поиск и фильтрация")

        button_layout.addWidget(add_button)
        button_layout.addWidget(view_button)
        button_layout.addWidget(search_button)
        main_layout.addLayout(button_layout)

        # 4. Таблица с последними добавленными устройствами
        table = QTableWidget(3, 4)  # 3 строки и 4 столбца
        table.setHorizontalHeaderLabels(["Название устройства", "Тип", "Дата добавления", "Статус"])

        # Заполнение таблицы
        devices = [
            {"name": "Ноутбук Lenovo", "type": "Ноутбук", "date": "01.09.2024", "status": "Исправен"},
            {"name": "Проектор Epson", "type": "Проектор", "date": "21.08.2024", "status": "Исправен"},
            {"name": "Принтер HP", "type": "Принтер", "date": "15.08.2024", "status": "В ремонте"}
        ]

        for row, device in enumerate(devices):
            table.setItem(row, 0, QTableWidgetItem(device["name"]))
            table.setItem(row, 1, QTableWidgetItem(device["type"]))
            table.setItem(row, 2, QTableWidgetItem(device["date"]))
            table.setItem(row, 3, QTableWidgetItem(device["status"]))

        main_layout.addWidget(table)

        # 5. Версия программы (размещена внизу)
        version_label = QLabel("Версия 1.0")
        version_label.setStyleSheet("font-size: 10px; color: gray;")
        main_layout.addWidget(version_label)

        # Применяем основной макет к виджету
        main_widget.setLayout(main_layout)

# Основная функция для запуска приложения
def application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()

        
        
