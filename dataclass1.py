from dataclasses import dataclass

@dataclass
class Person:
	name: str
	age: int
	city: str


p = Person("Zeeshan", 27, 'Ranchi')
p1 = Person("Zeeshan", 27, 'Ranchi')

print(p)
print(p.name)
print(p.age)
print(p1 == p)