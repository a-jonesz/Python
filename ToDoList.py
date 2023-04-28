from datetime import date

# I have decided to implement the OOP challenge 

# Top level
class ToDoList:
    '''ToDoList has attributes title, owner, and items. Used to keep track
    of things needed to be done'''

    def __init__(self, title, owner):
        self._title = title
        self._owner = owner
        self._items = []

    # SPECIAL FUNCTION: merge
    def merge_lists(self, other):
        for i in other._items:
            self.add_task(i.task, i.due_date, i.assignee)
        self.sort_items()
        return self
    
    # SPECIAL FUNCTION: range
    # Spec did not specify inclusive start/end dates
    def time_range(self, start, end):
        for i in self._items:
            if (i.due_date > start and i.due_date < end):
                print(i)

    # SPECIAL FUNCTION: filter
    def filter(self, f):
        for i in self._items:
            try:
                if (i.f is not None):
                    print(i)
            except:
                print("This is not a valid filter")

    def sort_items(self):
        self._items.sort()

    def add_task(self, task, due_date=None, assignee=None, priority=0):
        self._items.append(Item(task, due_date, assignee, priority))
        self.sort_items()

    def do_task(self, task):
        for i in self._items:
            if i.task == task:
                i.check_off()
    
    def change_task(self, old_task, new_task):
        for i in self._items:
            if i.task == old_task:
                i.task = new_task
    
    def change_date(self, task, new_date):
        for i in self._items:
            if i.task == task:
                i.due_date = new_date
            
    def change_assignee(self, task, new_assignee):
        for i in self._items:
            if i.task == task:
                i.assignee = new_assignee

    def print_items(self):
        for i in self._items:
            print(i)

# Bottom level 
class Item:
    '''An Item is an element of a list, and attribute of the ToDoList.
    The attributes of an Item are the task, due date, assignee, and status
    (whether it has been completed or not)'''
    def __init__(self, task, due_date=None, assignee=None, priority=0):
        self._task = task
        self._due_date = due_date
        self._assignee = assignee
        self._status = 1
        self._priority = priority
    
    def get_task(self):
        return self._task
    
    def set_task(self, new_task):
        self._task = new_task

    task = property(get_task, set_task)
    
    def get_date(self):
        return self._due_date

    def set_date(self, new_date):
        self._due_date = new_date

    due_date = property(get_date, set_date)

    def get_assignee(self):
        return self._assignee
    
    def set_assignee(self, new_assignee):
        self._assignee = new_assignee

    assignee = property(get_assignee, set_assignee)
    
    def check_off(self):
        self._status = 0

    def __str__(self):
        return f"Task: {self._task} | Due Date: {self._due_date} | Assignee: {self._assignee} | Status: {self._status} | Priority: {self._priority}"
    
    def __lt__(self, other):
        return other._priority != 0 or self._due_date < other._due_date

# Testing 
class Main():

    def __init__(self):
        self._my_list = ToDoList("alex's list", "alex")
        # self._my_list.add_task("wash dishes", None, None, 0)
        # self._my_list.add_task("wash dishes", None, None, 1)
        self._my_list.add_task("wash dishes", date(2021,2,22), "dad", 1)
        self._my_list.add_task("clean clothes", date(2019,2,22), "dad")
        
        # self._my_list.time_range(date(2022,2,22), date(2025,2,22))

        self.other_list = ToDoList("anonymous list", "anonymous")
        self.other_list.add_task("take out trash", date(2015, 2, 22), "anonymous")
        self._my_list.merge_lists(self.other_list)

    def run(self):
        self._my_list.print_items()

if __name__ == "__main__":
    Main().run()








