# OVERVIEW OF [https://openai.github.io/openai-agents-python/ref/agent/]

### 🔧 ToolsToFinalOutputFunction
Yeh aik function type hai jo 2 cheezen leta hai:

1. RunContextWrapper (jo context hold karta hai)

2. Tool results ki list

Aur return karta hai:
👉 ToolsToFinalOutputResult (jo batata hai ke agent ka final output aagaya ya nahi).

### 📦 ToolsToFinalOutputResult
Yeh aik dataclass hai jisme:

- is_final_output (bool): Agar True hai to iska matlab agent ka kaam khatam ho gaya.

- final_output: Final result, jo kisi bhi type ka ho sakta hai (e.g. string, dict, etc.)

### 🛑 StopAtTools
Yeh aik TypedDict hai jisme:

- stop_at_tool_names: Tools ke naamon ki list hoti hai. Agar koi tool in mein se call ho jaye, to agent dobara run nahi karega.

### ⚙️ MCPConfig
MCP (Model Context Protocol) servers ka configuration hold karta hai:

### convert_schemas_to_strict: 
Agar True ho, to yeh schemas ko strict-mode mein convert karne ki koshish karta hai.

##### ✅ Strict mode ka matlab:
- Only allowed fields: Sirf wahi fields allow hongi jo explicitly schema mein likhi gayi hain.

- Extra fields disallowed: Agar koi extra field input ya output mein milti hai jo schema mein define nahi ki gayi, to error throw hoga.

- Data types ka sakht check: Har field ka data type exactly match hona chahiye (e.g., string mein int nahi chalega).

##### 🧪 Example — Strict vs Loose Mode

###### 🔓 Loose Mode (Default)

```python

class MySchema(TypedDict):
    name: str

data = {"name": "Ali", "age": 25}  # Extra field 'age'

# Loose mode mein yeh data accept ho jata hai
```

###### 🔒 Strict Mode

```python

class MySchema(TypedDict):
    name: str

data = {"name": "Ali", "age": 25}

# Strict mode mein error ayega:
# ❌ Error: Extra field 'age' is not allowed
```

#### ⚙️ Iska Faida Kya Hai?
|    Benefit	              |   Explanation                                                   |
|-----------------------------|-----------------------------------------------------------------|
|✅ Validation ka control   	 |   Agent sirf wahi data accept karega jo sahi format mein ho     |
|✅ Bug prevention	         |   Agar galat ya unwanted field chali gayi to turant error milega|
|✅ Production safety	     |   Production environments mein strict strict validation zyada   |
|                             |    reliable hoti hai                                            |

#### 📌 Kab Use Karna Chahiye?

- Jab aap strict APIs, databases, ya enterprise-level systems ke sath kaam kar rahe ho.

- Jab aap chahte hain ke AI agent ki tool inputs/outputs bilkul predictably validate hoon.

### 🧠 Agent class
Yeh sabse important class hai. Ek Agent aik AI model hai jisko aap instructions, tools, aur guardrails ke sath configure karte hain. Iska use automation aur modular AI workflows mein hota hai.

Kuch important attributes:

#### 🔹 name
Agent ka naam.

#### 🔹 instructions
Yeh "system prompt" hota hai — agent ko batata hai ke usne kya karna hai. Aap ya to:

- Ek simple string de sakte hain

- Ya aik function jo dynamic instructions generate kare

#### 🔹 handoff_description
Yeh aik readable description hoti hai agent ke kaam ki, jab kisi aur tool ko handoff hota hai.

#### 🔹 handoffs
Sub-agents ya secondary agents ki list — agar zarurat ho to yeh unko kaam de sakta hai.

#### 🔹 model
Konsa LLM (jaise GPT-4) use karna hai.

#### 🔹 tools
Agent ke pass available tools ki list.

#### 🔹 mcp_servers
Aise servers jo external tools provide karte hain. Inka lifecycle aap manage karte hain (connect() aur cleanup() functions se).

#### 🔹 input_guardrails & output_guardrails
Rules jo input aur output pe lagte hain (e.g., validation, filters etc.)

#### 🔹 output_type
Agent ka expected output type (e.g., string, dict, ya koi custom schema).

#### 🔹 tool_use_behavior
Agent ka tool use karne ka tareeqa. Yeh kuch options deta hai:

- "run_llm_again": Tool call hone ke baad LLM dobara run karta hai.

- "stop_on_first_tool": Pehla tool call final result ban jata hai.

- ["tool_name1", "tool_name2"]: Agar inme se koi tool call ho, to agent ruk jata hai.

- custom function: Aap apna function de sakte hain jo tool result ko process kare.

#### 🔹 reset_tool_choice
Har tool call ke baad default tool choice pe wapas jata hai taake infinite loop na ho.

### 🔁 clone(**kwargs)
Agent ka duplicate bana ke naye config ke sath use karne ke liye function.

### 🛠️ as_tool(...)
Aap agent ko aik tool mein badal sakte hain, taake doosre agents use call kar saken. Yeh handoff se different hai — yeh sirf aik baar ka call hota hai, conversation handoff nahi hoti.

### 📥 get_system_prompt(...)
Instructions ya prompt jo agent ko diya gaya hai, yeh function usay return karta hai.

### 🧰 get_mcp_tools() & get_all_tools()
Yeh async functions hain:

- get_mcp_tools: MCP servers se tools fetch karta hai.

- get_all_tools: Sab tools (local + MCP) return karta hai.

