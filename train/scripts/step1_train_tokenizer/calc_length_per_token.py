import sentencepiece as spm
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("model", type=str, help='Path to the SentencePiece model')
    parser.add_argument("text", type=str, help='Path to your text file')
    parser.add_argument("--max_lines", type=int, default=None, help='The maximum number of lines to read from the text file. If not set, the entire file is read.')
    args = parser.parse_args()
    print(f"{args = }")
    return args

def load_tokenizer(model_path):
    sp = spm.SentencePieceProcessor()
    sp.load(model_path)
    return sp

def tokenize_text(sp, text_path, max_lines=None):
    text = ""
    with open(text_path, 'r', encoding='utf-8') as file:
        for i, line in enumerate(file):
            if max_lines is not None and i >= max_lines:
                break
            text += line
    tokens = sp.encode_as_pieces(text)
    return text, tokens

def calculate_legnth_per_token(original_text, tokens):
    original_length = len(original_text)
    tokenized_length = len(tokens)
    legnth_per_token = original_length / tokenized_length
    return legnth_per_token

def main():
    args = parse_arguments()
    model_path = args.model
    text_path = args.text
    max_lines = args.max_lines

    sp = load_tokenizer(model_path)

    original_text, tokens = tokenize_text(sp, text_path, max_lines)

    legnth_per_token = calculate_legnth_per_token(original_text, tokens)

    print(f'Original Length: {len(original_text)} characters')
    print(f'Tokenized Length: {len(tokens)} tokens')
    print(f'legnth_per_token: {legnth_per_token:.2f}')
    
if __name__ == "__main__":
    main()