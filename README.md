Use transformers pipeline to run DeepSeek-R1 model (experimental).

Transformers is not supported yet for DeepSeek-R1 model, see
https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B/blob/main/README.md#6-how-to-run-locally.

# Installation.

Install the python requirements.
```bash
cd
python3 -m venv venv_deepseek_transformers
source venv_deepseek_transformers/bin/activate

cd deepseek_transformers
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 -m pip install accelerate
```

# Run

Run the script in the virtual environment.
```bash
cd
source venv_deepseek_transformers/bin/activate

cd deepseek_transformers
python3 main.py
```
The model download is 3.55GB (Compare this size with Ollama download of 1.1GB).

Result on Ubuntu 22.04 (Intel).
```
(venv_deepseek_transformers) (base) guynicholson@Precision5820:~/deepseek_transformers$ python3 main.py
Sliding Window Attention is enabled but not implemented for `sdpa`; unexpected results may be encountered.
Device set to use cuda:0
Prompt: What is the sum of 3 + 2?
I need to find the sum of two numbers: 3 and 2.

First, I will add these two single-digit numbers together.

Adding them gives me a total of 5.
</think>

**Solution:**

To find the sum of \(3 + 2\), follow these simple steps:

1. **Add the Numbers Together:**
   \[
   3 + 2 = 5
   \]

So, the final answer is:
\[
\boxed{5}
\]
Took 2.9 seconds
(venv_deepseek_transformers) (base) guynicholson@Precision5820:~/deepseek_transformers$
```

I tested on latest transformers version 4.51.2 and the same issues duplicate.

# References

* DeepSeek-R1 1.5B model on [huggingface](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B/tree/main).  The `model.safetensors` are 3.55GB.

# Next steps

* [ ] Follow-up when DeepSeek-R1 distilled 1.5B model supports transformers.
