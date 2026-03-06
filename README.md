# 📝 Smart Task Manager (Python)

A fully functional task manager written in pure Python. This project was developed to gain a deep understanding of Object-Oriented Programming (OOP), data persistence (JSON Serialization/Deserialization), and clean Software Architecture, serving as a solid foundation for future Data Science and Machine Learning projects.

## ✨ Features

* **Task Management:** Add, remove, and mark tasks as completed `[X]`.
* **Auto Timestamps:** Background logging of the creation date and time for each task (via the `datetime` module).
* **Data Persistence:** Comprehensive Save/Load system that seamlessly converts Python Objects to a `List.json` file and vice versa.
* **Interactive CLI:** A clean, user-friendly, and error-proof Command Line Interface.

## 🏗️ Architecture

The system is designed strictly following OOP principles, separating the core business logic (Backend) from the presentation layer (UI/Frontend):

* **`Task` (The Model):** The class representing an individual task. It encapsulates its own state (text, date, completion status) and behaviors (e.g., `to_dict()`).
* **`ToDoList` (The Manager):** The class responsible for managing the collection of `Task` objects. It handles File I/O and CRUD operations, abstracting the complexity away from the user (Encapsulation).
* **`main.py` (The Frontend):** The entry point of the application, strictly responsible for routing user inputs and displaying outputs.

🗺️ Roadmap
This project is in active development with the following planned milestones:

[x] Level 1-3: Core Logic, Dictionaries, File I/O & datetime integration.

[x] Level 4: OOP Refactoring (Model-Manager Separation).

[ ] Level 5: Transition from CLI to a Graphical User Interface (GUI) using Tkinter (Event-Driven Programming).

[ ] Level 6: Data Analytics Dashboard (productivity analysis using pandas & matplotlib).

[ ] Level 7: Machine Learning Integration (e.g., Text Classification for automatic task categorization using scikit-learn).

Developed as a Computer Science practice project (4th Year).
