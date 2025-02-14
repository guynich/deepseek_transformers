# Use a pipeline as a high-level helper
import time

from transformers import pipeline

messages = [
    {"role": "user", "content": "What is the sum of 3 + 2?"},
]
start_time = time.time()

pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B")

print(f"Prompt: {messages[0]['content']}")
for out in pipe(messages):
    print(out['generated_text'][-1]['content'])

print(f"Took {(time.time() - start_time):.1f} seconds")
