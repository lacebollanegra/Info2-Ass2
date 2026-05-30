from assignment2.user import User

class Professor(User):
    def __init__(self, id : int, name : str, email : str, birth_date : str, birth_place : str, department : str, office : str):
        super().__init__(id,name, email, birth_date, birth_place)
        self.department = department
        self.office = office

    def get_email_signature(self) -> str:
        signature = f"Kind regards,\n{self.name}\n{10 * "-"}\nOffice {self.office}"
        return signature

    @property
    def role(self) -> str:
        return "Professor"
    
    def info(self) -> str:
        return f"Professor-Information:\n{10*"-"}\nID: {self.id}\nName: {self.name}\n Email: {self.email}\n Birtdate: {self.birth_date}\nBirthplace: {self.birth_place}\nDepartment: {self.department}\nOffice: {self.office}"

    

    
    
