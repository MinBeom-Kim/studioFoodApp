from rolepermissions.roles import AbstractUserRole

class Teacher(AbstractUserRole):
    available_permissions = {
        
    }

class Child(AbstractUserRole):
    available_permissions = {
        
    }

class Parent(AbstractUserRole):
    available_permissions = {
        
    }