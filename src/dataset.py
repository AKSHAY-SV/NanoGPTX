import torch


class TextDataset:

    def __init__(self, text, tokenizer, context_length=64):

        self.text = text
        self.tokenizer = tokenizer
        self.context_length = context_length

        self.data = torch.tensor(
            tokenizer.encode(text),
            dtype=torch.long
        )

    def __len__(self):

        return len(self.data) - self.context_length

    def __getitem__(self, index):

        x = self.data[index:index + self.context_length]

        y = self.data[index + 1:index + self.context_length + 1]

        return x, y
