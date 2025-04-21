from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import load_dataset

model_name = "llama3.2"
model = AutoModelForCausalLM.from_pretrained(model_name, use_fast=True)
tokenizer = AutoTokenizer.from_pretrained(model_name)

dataset = load_dataset("json", data_files="fine_tune_data.jsonl", split="train")


dataset = dataset.train_test_split(test_size=0.1)

#tokenização
def tokenize(example):
    prompt = example["prompt"]
    completion = example["completion"]
    full_input = prompt + completion
    return tokenizer(full_input, truncation=True, padding="max_length", max_length=512)

tokenized = dataset.map(tokenize, batched=False)

# preparar argumentos do treinamento
training_args = TrainingArguments(
    output_dir='./fine_results',
    evaluation_strategy="epoch",
    save_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    report_to="none",
)

# Colador para modelos causal LM
data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

# Rodar o treinamento
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
    tokenizer=tokenizer,
    data_collator=data_collator,
)

trainer.train()