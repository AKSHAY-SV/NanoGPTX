from pathlib import Path
import json


class CharacterTokenizer:

    def __init__(self, dataset_path: str):

        self.dataset_path = Path(dataset_path)

        self.text = self.dataset_path.read_text(encoding="utf-8")

        self.characters = sorted(list(set(self.text)))

        self.vocab_size = len(self.characters)

        self.char_to_index = {
            ch: idx for idx, ch in enumerate(self.characters)
        }

        self.index_to_char = {
            idx: ch for idx, ch in enumerate(self.characters)
        }

    def encode(self, text: str):

        return [self.char_to_index[c] for c in text]

    def decode(self, tokens):

        return "".join(
            self.index_to_char[token]
            for token in tokens
        )

    def save_vocab(self, output_file="data/final/vocab.json"):

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(
                self.char_to_index,
                f,
                indent=4,
                ensure_ascii=False
            )


if __name__ == "__main__":

    tokenizer = CharacterTokenizer(
        "data/final/dataset.txt"
    )

    print(f"Vocabulary Size : {tokenizer.vocab_size}")

    sample = "CMOS"

    encoded = tokenizer.encode(sample)

    decoded = tokenizer.decode(encoded)

    print("\nOriginal :", sample)
    print("Encoded  :", encoded)
    print("Decoded  :", decoded)

    tokenizer.save_vocab()
