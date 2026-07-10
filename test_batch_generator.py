from torch.utils.data import DataLoader

from src.dataset import TextDataset
from src.tokenizer import CharacterTokenizer


DATASET_PATH = "data/final/dataset.txt"

# Read the dataset
with open(DATASET_PATH, "r", encoding="utf-8") as f:
    text = f.read()

# Create tokenizer
tokenizer = CharacterTokenizer(DATASET_PATH)

# Create dataset
dataset = TextDataset(
    text=text,
    tokenizer=tokenizer,
    context_length=64
)

# Create DataLoader
loader = DataLoader(
    dataset,
    batch_size=4,
    shuffle=True
)

# Get one batch
x, y = next(iter(loader))

print("Input Shape :", x.shape)
print("Target Shape:", y.shape)

print("\nFirst Input:")
print(x[0])

print("\nFirst Target:")
print(y[0])
