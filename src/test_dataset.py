from pathlib import Path

from tokenizer import CharacterTokenizer
from dataset import TextDataset


DATASET_PATH = "data/final/dataset.txt"

text = Path(DATASET_PATH).read_text(
    encoding="utf-8"
)

tokenizer = CharacterTokenizer(DATASET_PATH)

dataset = TextDataset(
    text,
    tokenizer,
    context_length=32
)

print("Dataset Size :", len(dataset))

x, y = dataset[0]

print("\nInput")

print(x)

print("\nTarget")

print(y)

print("\nDecoded Input")

print(tokenizer.decode(x.tolist()))

print("\nDecoded Target")

print(tokenizer.decode(y.tolist()))
