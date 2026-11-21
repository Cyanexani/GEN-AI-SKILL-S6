# Assignment - Subword Tokenizer Training

Two small programs that learn a subword vocabulary from the words `low` (5), `lower` (2), `newest` (3) and `widest` (6) by repeatedly merging neighbouring pieces.

- `bpe.py` - Byte Pair Encoding: merges the most frequent pair each step.
- `wordpiece.py` - WordPiece: merges the pair with the highest score, `pair count / (count of first piece * count of second piece)`. Continuation pieces carry a `##` prefix.

## Run
```powershell
python bpe.py
python wordpiece.py
```
No packages or API keys are needed.
