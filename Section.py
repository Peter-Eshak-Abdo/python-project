
class Section:
    def __init__(self, category , section_id, count):
        self.category = category
        self.section_id = section_id
        self.count = count
        self.Not_available = False

    def Notavailable(self):
        if not self.Not_available:
            self.Not_available = True
            return True
        return False

    def return_section(self):
        if self.Not_available :
            self.Not_available = False
            return True
        return False

    def __str__(self):
        return f"\nCategory: {self.category}, Section ID From: {self.section_id}, Section ID To: {self.section_id + 999}, Count: {self.count}\n"

sections = [
    Section("Science", 2000, 15200),
    Section("History", 3000, 3600),
]
