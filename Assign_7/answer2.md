# 🔹 2a. "System prompt" Agent class mein instructions ke naam se kyun hota hai? Aur isay callable (function) bhi kyun bana sakte hain?

## ✅ 1. instructions = System Prompt
Jab aap OpenAI ka AssistantAgent ya RunnableAgent use karte ho, to instructions wohi system prompt hota hai jo agent ko batata hai ke:

- uska role kya hai,

- kis lehje mein baat karni hai,

- aur kis cheez mein madad karni hai.

```python

agent = AssistantAgent(
    name="HelperBot",
    instructions="Tum aik madadgar AI ho.",
    model="gpt-4-turbo"
)
```

Yeh same cheez hai jaise normal API mein:

```python

{"role": "system", "content": "Tum aik madadgar AI ho."}
```

## 🔁 2. Instructions ko callable (function) bhi kyun bana sakte hain?
Agar hum chahain to instructions ko aik function bana sakty hain, taake woh har dafa automatically naye instructions bana sake based on:

- user ka naam,

- waqt,

- messages,

- ya koi external data.

## ✅ Example: Callable Instructions
```python

def dynamic_instructions(context):
    return f"Aap user {context['user_name']} ki madad kar rahe ho. Friendly aur simple raho."

agent = AssistantAgent(
    instructions=dynamic_instructions,
    model="gpt-4-turbo"
)
```

Ab agent har dafa user_name ke mutabiq instructions generate karega.

## 🧠 Summary Table

| Feature	           | Kya karta hai                                                |
|----------------------|--------------------------------------------------------------|
|instructions="..."    | Har dafa aik hi static message (fixed)                       |
|instructions=function | Har dafa new message based on situation (dynamic)            |

#### In short:
Agent class mein instructions system prompt hota hai jo agent ka role define karta hai. Isay callable is liye bana sakte hain taake har baar dynamic instructions generate ki ja sakein based on user context ya situation.

# 🔹 2b. But the user prompt is passed as parameter in the run method of Runner and the method is a classmethod

user ka prompt Runner class ke run() method mein parameter ke tor par diya jata hai. Yeh method @classmethod hota hai taake bina object banaye class level par use kiya ja sake.
