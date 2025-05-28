# Q1.  The Agent class has been defined as a dataclass why?

## ✅ Dataclass kya hoti hai?
dataclass Python ka ek special feature hai jo aapko data ko asaani se represent karne ka tareeqa deta hai — bina zyada code likhe.

Aap usay tab use karte hain jab aap sirf data store karna chah rahe ho, jaise:

- Student ka naam, roll number, aur class

- Product ka naam, price, aur quantity

- Kisi aadmi ka profile: naam, email, age

## 🎯 Normal class vs Dataclass
### 🔴 Normal class mein:
Aapko __init__, __repr__, __eq__, waghera manually likhna padta hai.

```python
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def __repr__(self):
        return f"Student(name={self.name}, roll={self.roll})"
```
### ✅ Dataclass mein:
Python yeh sab kaam automatically kar deta hai!

```python
from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll: int
```

Bas itna likhne se:

- __init__() method ban jata hai

- __repr__() method automatic ban jata hai

- __eq__() (comparison) bhi ban jata hai

### 📦 Real-Life Example: Product
```python
from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

# Use karna
item1 = Product("Laptop", 1200.99, 5)
item2 = Product("Mouse", 25.50, 10)

print(item1)
# Output: Product(name='Laptop', price=1200.99, quantity=5)
```

## 🔧 Faide (Benefits) of Dataclass

| Feature                    | Faida                                           |
|----------------------------|-------------------------------------------------|
| `__init__` auto banta hai  | Kam code, zyada kaam                            |
| `__repr__` auto banta hai  | Pretty printing                                 |
| `__eq__` auto banta hai    | Comparison asaan                                |
| Mutability support         | Aap chahein to object change bhi kar sakte hain |

## 🧠 Extra: Frozen dataclass (immutable)
Agar aap chahte hain ke object change na ho, to frozen=True likh sakte hain:

```python
@dataclass(frozen=True)
class User:
    username: str
    email: str
```

## 📘 Summary (Asaan Alfaaz mein):

"@dataclass ek shortcut hai jo aapko data rakhne ke liye class banana asaan banata hai. Aapko manually functions likhne ki zarurat nahi padti — Python khud sab kuch handle karta hai."

# Q1.  The Agent class has been defined as a dataclass why?

Jab hum Agent class ko @dataclass se define karte hain, to iska matlab hai:

- Yeh class sirf data ko represent kar rahi hai (behavior nahi).

- Hum chahte hain ke Python automatic tareeqe se is class ke liye __init__, __repr__, aur __eq__ jaise methods khud banaye.

- Humari code writing chhoti aur readable ban jaye.

#### In short:
@dataclass se hum ek saf, seedhi, aur fast class banate hain jo sirf values store karti hai — jaise naam, type, kaam, aur tools of the agent.

### 📦 Example Without @dataclass:

```python
class Agent:
    def __init__(self, name, role, tools):
        self.name = name
        self.role = role
        self.tools = tools

    def __repr__(self):
        return f"Agent(name={self.name}, role={self.role}, tools={self.tools})"
```
Ye kaafi boring aur repetitive code hai. Har time __init__ aur __repr__ likhna padta hai.

### ✅ Same Example With @dataclass:

```python
from dataclasses import dataclass
from typing import List

@dataclass
class Agent:
    name: str
    role: str
    tools: List[str]
```

#### 🎯 Is mein:

- __init__ automatically ban gaya

- __repr__ bhi mil gaya

- Hum objects ko asaani se print, compare, aur access kar sakte hain

### 🧪 Test the Dataclass:

```python

agent1 = Agent("Researcher", "Info Gatherer", ["Google", "Docs"])
agent2 = Agent("Writer", "Content Creator", ["Notion", "Grammarly"])

print(agent1)
# Output: Agent(name='Researcher', role='Info Gatherer', tools=['Google', 'Docs'])
```
## 🛠️ Use-case in Agents SDK:
Jab hum Agents SDK jese systems bana rahe hote hain:

- Har agent ke paas data hota hai (name, function, tools, state, etc.)

- Hume un agents ko easily create, update, aur compare karna hota hai

- Is liye @dataclass best choice hoti hai!

## 🧠 Final Summary:
Agent class ko @dataclass is liye banaya jata hai taake hum asaani se data store aur manage kar saken, bina extra methods likhe. Yeh clean aur efficient code writing ka tareeqa hai.
