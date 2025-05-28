# Q3. What is the purpose of the Runner class?

Runner class ka purpose yeh hai ke yeh agents ka workflow run karne ka zimma uthata hai. Yani, jab aap ek agent banate hain jo kisi input ka response deta hai — to us agent ko run karne, uska jawab lene, aur agar zarurat ho to agle agent ko handoff karne ka kaam Runner karta hai.

### 📌 Simplify:
- Aap Runner.run() ya Runner.run_sync() ya Runner.run_streamed() ko use karke apna agent chala sakte hain.

- Yeh automatically har step handle karta hai: input lena, agent se jawab lena, tool call karna, ya agle agent ko dena.

- Agar agent ka final output mil jaye to loop khatam ho jata hai.

- Agar limit exceed ho jaye ya koi rule tod diya jaye to exception raise hoti hai.

### 🔧 Example Situation:
Aap ne ek Customer Support Agent banaya hai — ab aap chahte hain ke user ka sawal le kar agent jawab de, aur zarurat ho to doosray expert agent ko forward kare. Is poore process ko manage karna Runner ka kaam hai.

# 4. What are generics in Python? Why we use it for TContext?  

## 🔷 Generics kya hotay hain Python mein?
Python mein generics ka matlab hota hai ke aap kisi class ya function ko general bana saktay hain taake wo different types ke sath kaam kar sakein, bina baar baar nayi class banaye.

Ye typing module ka hissa hai — jese:

```python

from typing import TypeVar, Generic

T = TypeVar('T')
```

Iska matlab: T ek placeholder hai kisi bhi type ke liye — jaise str, int, dict, ya custom class.

### 🤔 TContext ka use kyun kiya jaata hai?
TContext ek generic type hai jo represent karta hai agent ke context ka data — yani wo data jo agent ke har turn ya response mein istemal hota hai.

### ✅ Iska faida ye hota hai:
- Har agent ka apna custom context ho sakta hai.

- Aap strongly typed support de sakte ho taake bugs avoid ho.

- Code reusability aur flexibility milti hai.

#### 💡 Example:
```python

from typing import TypeVar, Generic

TContext = TypeVar('TContext')

class Agent(Generic[TContext]):
    def __init__(self, context: TContext):
        self.context = context
```

Agar kisi agent ka context ek dictionary ho:

```python

agent = Agent[dict]({"user_id": 123, "session": "xyz"})
```

Agar kisi aur agent ka context ek custom class ho:

```python

class CustomContext:
    user_id: int
    token: str

agent = Agent[CustomContext](CustomContext())
```

### 📌Summary:
- Generics aisi technique hai jisme aap class/function ko flexible bana dete ho taake wo har type ke data ke sath kaam karein.

- TContext ko use karne ka matlab ye hai ke har agent ko uska apna context data diya ja sake — jaise ke user info, session, ya aur koi environment data.

- Is se code modular, clean aur type-safe ban jata hai.
