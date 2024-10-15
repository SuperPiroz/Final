
#En Task klass som representerar varje inviduell punkt på todo listan. 
#punkterna på listan kommer vara ordnade efter númmer, beskrivning och en deadline,
# som tex: " 4, "Gå till tvättstugan", "2024-10-14 " 

class Task:
    def __init__(self, task_id, category, dead_line=None ):
        self.task_id = task_id #En unik identiferar för varje punkt på listan
        self.category = category #En beskrivning av punkten 
        self.dead_line = dead_line #när detta ska vara klart ett mål datum helt enkelt
        self.compleated=False# en markör som visar om det är slutfört eller inte. 

    def display_task_details(self): #Funktion för att visa punktens detaljer 
        status = "Compleated" if self.compleated else "Not Compleated"
        print(f"Task ID: {self.task_id}, Description: {self.category}, Due Date: {self.dead_line}, Status: {status}")

    def complete_task(self): #Funktion för at merkara en uppgift som klar
        self.completed = True

# Den här klassen hanterar en samling med uppgifter istället för enskilda uppgifter   
class Todo_list: 
    def __init__(self):
        self.tasks = {} # En dict för att lagra dom olika punkterna på, där task_id fungerar som en nyckel
      
    def add_task(self, task):# Funktion för att lägga till uppgifter på listan
        self.tasks[task.task_id] = task 
        print (f"Youre To-do is now added: {task.category}.") 
        
    def remove_task (self, task_id):# Funktion för att ta bort en task 
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Youre To-do: {task_id} is now removed.")# Återger att den tagit bort
        else:
            print(f"Youre to do {task_id}was not found.")# Återger att punkten inte fanns med på listan.
 
    def display_tasks(self): # en display tasks så att man kan se hela listan 
        print("These are the tasks in the to doi list:")
        for task in self.tasks.values(): #En forloop som går över alla punkter i listan 
            task.display_task_details()
    
    def mark_complete(self, task_id):# Funktion för att markera en punkt som klar eller ej
      if task_id in self.tasks:
         self.tasks[task_id].complete_task()
         print(f"Youre To-do: {task_id}, is now marked as complete.")      
      else:
          print(f"Youre To-do: {task_id} was not found")


#skapar några punkter
task1 = Task(1, "Gå ut med hunden","2024-10-12")
task2 = Task(2, "Gå till tvättstugan", "2024-10-14")

#skapar en to do lista a to-do list
ToDoList = Todo_list()

#lägger till dom 2 punkterna ovan i min lista
ToDoList.add_task(task1)
ToDoList.add_task(task2)

# Visa listan 
ToDoList.display_tasks()

# Markera dom olika punkterna som klara elle ej
ToDoList.mark_complete(1)
ToDoList.mark_complete(2)
