__author__ = "Ralph Vitug"
__version__ = "1.0.0"

from department.department import Department


class Course:

    """
    Initializes a course object based upon received arguments 
    (if valid).

    args:
    name (str): The name of course
    department (Department): The name of the department in which
    courses exists.
    credit_hours (int): The number of credit hrs sa course has.

    raises:
        Value Error: if any args are invalid raise exception.
    """

    def __init__(self, name:str, department:Department, credit_hours: int):

        if len(name.strip())> 0: # strip removes 
                             # word trailing(white space)
            self.__name = name #name mangling _ClassName._name

        else:
            raise ValueError("Name cannot be blank.")
    
        if isinstance(department, Department):
            self.__department = department
        else:
            raise ValueError("Department is invalid")
    
        if isinstance(credit_hours, int):
            self.__credit_hours = credit_hours
        else:
            raise ValueError("Credit hours must be an int type")
    
    @property
    def name(self) -> str: #Accessor
        return self.__name

    @property
    def department(self) -> Department:
        return self.__department

    @property
    def credit_hours(self) -> int:
        return self.__credit_hours

    def __str__(self) -> str:

        return (f"Course: {self.__name}"
                + f"\nDepartment: "
                f"{self.__department.name.replace('_', ' ').title()}"
                + f"\nCredit Hours: {self.__credit_hours}")
            
