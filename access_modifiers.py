"""
- python has no real access modifiers
- but it has 3 access levels by conventions:
 public -> name (accessable everywhere in the program)
 protected -> _name (internal user)
 private -> __name (name-mangled to avoid accidental overriding)
"""

class parent:
    def __init__(self):
        self.name="myName"      # accessible throughout the program
        self._name="myName"     # accessible throughout the program,but it just indicates that its for internal use only(use it only if you know what you’re doing; it may change or break without notice)
        self.__name="myName"    # accessible throughout the program, but it prevents child classes from accidentally overriding it 

obj=parent()
print(obj.name)   
print(obj._name)
print(obj.__name)  # cant access             
print(obj._parent__name)  # mangling method 
    
print(dir(obj))  # this function tells about the methods/function can be executed on this object



""" _name:
- this is just a convention to indicate for internal use only
- it does not enforce it but  just acts as a warning
- if we use it, then the code may break later
"""

""" __name :
- python internally converts it into __classname__name internally
- so if child class can't override it because internally names become different __parentclass__name and __childclass_name
- we can't access it directly, must access it using mangling method
"""

""" __classname__name:
- This is "NAME MANGLING"  
- this concept is used to protect class-private and superclass-private 
attributes from being overwriting accidently it can be accesed only in a specific method only
"""