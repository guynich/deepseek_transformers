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
python3 -m pip install -r requirements.txt
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

Result on Ubuntu VM on MacBook Pro 2020 (Intel).
```
(venv_deepseek_transformers) parallels@ubuntu-linux-22-04-02-desktop:~/deepseek_transformers$ python3 main.py
Device set to use cpu
Prompt: What is the sum of 3 + 2?
To solve the problem of adding 3 and 2, I start by identifying the numbers involved,
Took 142.3 seconds
(venv_deepseek_transformers) parallels@ubuntu-linux-22-04-02-desktop:~/deepseek_transformers$ 
```
The model returns some reasoning.  

Issues
* The `<think>` tag is missing. 
* The inference time of 142 seconds is slower than expected.
* The reponse is truncated.

# References

* DeepSeek-R1 1.5B model on [huggingface](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B/tree/main).  The `model.safetensors` are 3.55GB.

# Next steps

* [ ] Follow-up when DeepSeek-R1 distilled 1.5B model supports transformers.
  