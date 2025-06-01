# TOOL VS FUNCTION CALLING

## 🔧 1. Function Calling kya hai?
Aap ek "function" ko bol rahe hote ho:

"Yeh kaam karo, aur mujhe result do!"

## 📦 Function kya hota hai?
Function ek chhota sa program hota hai jo koi specific kaam karta hai. Jaise:

```python

def add(a, b):
    return a + b
``` 
Jab aap add(2, 3) bolte ho, to function kaam karta hai aur 5 return karta hai.

## ✅ Function Calling ka use kab hota hai?
Jab aap AI (jaise ChatGPT) ko kahte ho:

  “Yeh data lo, is function ko chalao, aur mujhe result do.”

OpenAI ka Function Calling system yeh kaam karta hai:

- Aap natural language mein kuch kehte ho.

- AI automatically decide karta hai: "Haan, mujhe iske liye koi function chalana chahiye."

- AI function ke parameters ko samajh kar correct format mein call karta hai.

## 🎯 Example (Function Calling in OpenAI):
```json

{
  "name": "get_weather",
  "arguments": {
    "location": "Karachi"
  }
}
```
Matlab AI ne samjha: "User ne kaha hai 'Karachi ka mausam kya hai?' To mujhe get_weather function call karna chahiye."

# 🔨 2. Tool Calling kya hai?

Aap AI ko bolte ho:

“Yeh tool use karo, jo kisi external system se connect hota hai, aur kaam karo.”

Yeh tools external systems hotay hain, jaise:

- Browser (search karna)

- Calculator

- Code Interpreter

- Image Editor

- Python tool (coding chalana)

- Web tool (live data lena)

## 🧰 Tool Calling mein kya hota hai?
AI ka brain decide karta hai:

    "Mujhe ek tool ka use karna chahiye jo mujhe OpenAI ne diya hai."

Phir AI:

- Tool call karta hai

- Input bhejta hai (like a query or data)

- Tool result la kar deta hai

- AI us result ko samjha ke user ko explain karta hai

## 🎯 Example (Tool Calling in ChatGPT):
Agar aap kahte hain:

    “Is Excel file ka summary do.”

To AI Python tool ko use karta hai jahan:

- Excel file open hoti hai

- Pandas se data process hota hai

- Summary AI tak wapas aati hai

# 🔍 Ab farq kya hai in dono mein?

| **Point**                         | **Function Calling**                           | **Tool Calling**                                                    |
| --------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------- |
| Kaam kis cheez se hota hai?       | Function (chhoti chhoti tasks)                 | Tools (badi functionalities, jaise search, Python, browser)         |
| Kya user ne banaya?               | Haan, functions user API mein define karta hai | Tools OpenAI ya ChatGPT environment ka part hain                    |
| Kya external system use hota hai? | Nahin, function AI ke andar run hota hai       | Haan, tools external systems ya environments se interact karte hain |
| Ka example?                       | Weather fetch karna via function               | Excel file process karna via Python tool                            |

## 🧠 Ek real life example:
Sochiye aap manager hain.

- Function Calling: Aap office mein kisi employee ko kehte hain:

    "Yeh formula lagao aur mujhe result do."
    (Simple kaam, andar hi andar hota hai.)

- Tool Calling: Aap kehte hain:

    "Accountant ko bolo woh spreadsheet check kare aur mujhe monthly report bheje."
    (Bada kaam, bahar kisi expert ya system ki help leni padti hai.)

## 🤖 Function Calling OpenAI mein kahan use hoti hai?
Jab aap AI agent banate ho jahan woh real-world APIs call kare:

   - e.g., get_flight_status(), book_appointment(), translate_text()

Ye aap khud define karte ho — AI samajh kar function ko call karta hai.

## 🧪 Tool Calling ChatGPT mein kahan use hoti hai?
ChatGPT Plus mein jab AI khud decide karta hai:

- Python tool use kare

- Image editor se kuch kare

- Browser se kuch search kare

## 🧠 1. Function Calling – OpenAI Style Example
#### 🧾 Scenario:
- User kehta hai:

     “Lahore ka mausam batayein.”

- AI smajhta hai:

    Mujhe get_weather naam ka function call karna chahiye.

### 🔧 Step 1: Function Define karein (Python code)
```python

def get_weather(location: str) -> str:
    # Fake weather data
    weather_data = {
        "Lahore": "Garmi hai, 38°C temperature hai",
        "Karachi": "Halka barish, 30°C",
    }
    return weather_data.get(location, "Weather data nahi mila.")
```

### 🤖 Step 2: AI ne samjha aur call kiya:
```python

user_input = "Lahore ka mausam batayein"
if "Lahore" in user_input:
    result = get_weather("Lahore")
    print(f"AI: {result}")
```

#### 🧾 Output:
```makefile

AI: Garmi hai, 38°C temperature hai
```

#### 🔍 Yahan pe:

- AI ne user input samjha

- Correct function ko call kiya

- Argument "Lahore" diya

- Result wapas user ko diya

## 🛠️ 2. Tool Calling – Streamlit + Python Tool Example
#### 📘 Scenario:
- User kehta hai:

    “Yeh data file upload karo aur total calculate karo.”

### 👨‍💻 Streamlit Code (Python Tool Calling jaisa)
```python

import streamlit as st
import pandas as pd

st.title("Tool Calling Demo – CSV Reader")

uploaded_file = st.file_uploader("CSV file upload karein", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df)

    if "Amount" in df.columns:
        total = df["Amount"].sum()
        st.success(f"Total Amount: {total}")
    else:
        st.warning("Amount column nahi mili.")
```
#### 🧾 Output:
- User file upload karta hai

- AI ya app Python tool se Pandas ka use karta hai

- Calculation hoti hai

- Result user ko dikhaya jata hai

### ✅ Summary in 1 Line Each:
- Function Calling: AI directly ek specific chhota task call karta hai — usually aap ke diye hue functions.

- Tool Calling: AI kisi external tool (Python, browser, image tool) ka use karta hai complex ya dynamic kaam ke liye.







