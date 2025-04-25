# Use a pipeline as a high-level helper
import time

from torch import float16
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"

messages = [
    {"role": "user", "content": "What is the sum of 3 + 2?"},
]

tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    trust_remote_code=True,
    padding_side="right"
)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    trust_remote_code=True,
)

# Setup generation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto",
    max_new_tokens=2048,
    temperature=0.6,
    top_p=0.95,
    repetition_penalty=1.15,
    pad_token_id=tokenizer.eos_token_id
)

start_time = time.time()

print(f"Prompt: {messages[0]['content']}")
for out in pipe(messages):
    print(out['generated_text'][-1]['content'])

print(f"Took {(time.time() - start_time):.1f} seconds")
