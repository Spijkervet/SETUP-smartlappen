from transformers import AutoTokenizer
from transformers import TextDataset, DataCollatorForLanguageModeling
from transformers import Trainer, TrainingArguments, AutoModelWithLMHead


def load_dataset(train_path, test_path, tokenizer):
    train_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=train_path,
        block_size=128)

    test_dataset = TextDataset(
        tokenizer=tokenizer,
        file_path=test_path,
        block_size=128)

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer, mlm=False,
    )
    return train_dataset, test_dataset, data_collator


if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(
        "thomasdehaene/gpt2-large-dutch-finetune-oscar-10m-3epoch")

    train_path = 'train_dataset.txt'
    test_path = 'test_dataset.txt'

    train_dataset, test_dataset, data_collator = load_dataset(
        train_path, test_path, tokenizer)

    model = AutoModelWithLMHead.from_pretrained(
        "thomasdehaene/gpt2-large-dutch-finetune-oscar-10m-3epoch")

    training_args = TrainingArguments(
        output_dir="./gpt2-lyrics",  # The output directory
        overwrite_output_dir=True,  # overwrite the content of the output directory
        num_train_epochs=3,  # number of training epochs
        per_device_train_batch_size=32,  # batch size for training
        per_device_eval_batch_size=64,  # batch size for evaluation
        eval_steps=400,  # Number of update steps between two evaluations.
        save_steps=800,  # after # steps model is saved
        warmup_steps=500,  # number of warmup steps for learning rate scheduler
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
        eval_dataset=test_dataset,
        prediction_loss_only=True,
    )

    trainer.train()
    trainer.save_model()
