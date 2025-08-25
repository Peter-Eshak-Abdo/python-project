
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

    def __str__(self):
        return f"\n Name: {self.name}, ID: {self.member_id}\n"

members = [
    Member("John Doe", "M001"),
    Member("Jane Smith", "M002"),
]
