# OVERVIEW OF [https://openai.github.io/openai-agents-python/ref/run/]

Yeh documentation aik AI Agent system ke Runner class ke baare mein hai jo src/agents/run.py file mein defined hai. Main functions teen hain: run, run_sync, aur run_streamed.

## 🔁 run (Asynchronous)
```python

await Runner.run(...)
```

Yeh method aik agent ko async (asynchronous) tareeqe se chalata hai.

### Kaam Kaise Karta Hai:
1. Agent ko input diya jata hai.

2. Agar agent final output dey deyta hai to loop khatam ho jata hai.

3. Agar agent kisi doosray agent ko handoff kar deta hai, to woh agent chalta hai.

4. Agar koi tool call hoti hai, to woh hoti hai aur loop dobara chalta hai.

### Exceptions:
- Agar maximum turns cross ho jayein to MaxTurnsExceeded error aata hai.

- Agar guardrail kisi maslay ki nishandahi kare to GuardrailTripwireTriggered error aata hai.

## ✅ run_sync (Synchronous)
```python

Runner.run_sync(...)
``` 

Yeh method same kaam karta hai lekin synchronous tareeqe se. Yeh async function ke andar kaam nahi karega (e.g. Jupyter notebook, FastAPI, etc). Normal Python scripts ke liye use hota hai.

## 🔄 run_streamed (Streaming Mode)
```python

Runner.run_streamed(...)
```
Yeh version stream mode mein kaam karta hai, yaani output ko realtime mein stream kiya ja sakta hai. Is se aap ko har step ka live feedback milta hai.


## ✅ Parameters (Matlab function ke andar dene wali cheezen)
| Naam	        | Type                          |Kya karta hai (Roman Urdu mein)                   |
|---------------|-------------------------------|--------------------------------------------------|
|starting_agent | Agent[TContext]	            |Pehla agent jisse workflow start hota hai. Yehi   |
|               |                               |main agent hota hai. (Zaroori hai)                |
|input	        |str ya list[TResponseInputItem]|User ka pehla message. String bhi ho sakta hai    |
|               |                               |ya list form mein bhi. (Zaroori hai)              |
|context 	    |TContext ya None	            |Agar aap agent ko koi specific context dena chahte|
|               |                               | hain (e.g., conversation ka state), to yahan den.|
|max_turns	    |int	                        |Kitne turns tak agent chale. Har turn mein agent  |
|               |                               |ya tool call ho sakta hai. Default value hoti hai.|
|hooks          |RunHooks[TContext]             | ya None	Lifecycle ke different points par      |
|               |                               |custom callback functions lagane ke liye. (Jaise  |
|               |                               |agent start, tool call, etc.)                     |
|run_config	    |RunConfig ya None              |Global settings jaise model kaunsi use karni hai, |
|               |                               |guardrails kya lagani hain, etc.                  |
|previous_      |str ya None                    |Agar aap OpenAI Responses API use kar rahe hain   |
|response_id    |                               |to is se aap previous response ko skip kar sakte  |
|               |                               |hain aur continuity maintain hoti hai.            |

## 🔁 max_turns ka matlab:
Agent agar 10 baar run karne ke baad bhi result nahi deta, to error aata hai – taake infinite loop na ban jaye.

### 🎯 Short Example:
```python

result = Runner.run_sync(
    starting_agent=my_agent,
    input="Hello!",
    context=my_context,
    max_turns=5,
    run_config=my_run_config
)
```

## 🔙 Return Values (Yani function kya wapas karta hai)
### 1. ✅ run() aur run_sync() functions:
##### Return type: RunResult

##### Iska matlab:
Jab aap agent ko run karte hain, to jab woh complete ho jata hai (ya kisi aur agent ko handoff karta hai), to ye ek RunResult object wapas karta hai.

#### 💡 RunResult mein kya hota hai?
- output: Last agent ka final jawaab (ya result)

- inputs: Starting input aur tool calls ka data

- guardrail_results: Agar koi guardrails lagi hoti hain to unka result

- handoffs: Agar beech mein agent change hua ho

- steps: Har turn (ya step) ka detail — jaise input, output, tool call, etc.

### 2. ✅ run_streamed() function:
##### Return type: RunResultStreaming

##### Iska matlab:
Ye bhi final result deta hai lekin streaming mode mein deta hai — yani jaise jaise agent kuch bolta jata hai, aap usay live sunn ya dekh sakte hain.

### 💡 RunResultStreaming mein kya hota hai?
- stream_events(): Ek method jisse aap events ko real-time mein stream kar sakte hain.

- final_result: Jab sab complete ho jaye to yahan RunResult mil jata hai.

### 🔁 Summary (Ek line mein):

|Function	     |Return Type	      |Kya deta hai?                       |
|----------------|--------------------|------------------------------------|
|run()           |RunResult           |	Final output + steps + guardrails  |
|run_sync()	     |RunResult           |	Wahi result sync mode mein         |
|run_streamed()	 |RunResultStreaming  |	Streamable events + final result   |

## ⚙️ RunConfig (Settings)
Yeh aik dataclass hai jo pura agent ka behavior control karta hai.

### Important Fields:
- model: Kis AI model ka use karna hai (e.g. GPT-4).

- model_provider: Model ko provide karne wali service (default: OpenAI).

- input_guardrails: Pehle input par security/validation rules.

- output_guardrails: Final output par rules.

- tracing_disabled: Agar True ho to tracing band ho jati hai.

- trace_metadata: Trace ke sath extra data attach karne ke liye.

- workflow_name: Workflow ka naam, jese "Customer Support Agent".

- group_id: Aik group ID agar multiple agents ek hi process ka part hain.











