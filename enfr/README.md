# enfr

## corpus
- europarl
- common crawl
- undoc
- giga
- newstest (dev 2015)

### to download
- GlobalVoices
- TedTalk
- JRC-Acquis
- EAC
- Tatoeba 

## data clean
```bash
# TBD
```

## normalization
some uniform transformation on the source sequences to identify and protect some specific sequences (for instance url), normalize characters (for instance all types of quotes, unicode variants) or even to normalize some variants (like dates) into unique representation simpler for the translation process
```bash
# TBD
```

## bpe
segment text into subword units
```bash
th tools/learn_bpe.lua -size 32000 -save_bpe /path/to/bpe -tok_mode aggressive -tok_segment_numbers -tok_case_feature < /path/to/input
```

## tokenization
transform the sentence into a sequence of space-separated tokens together with possible features
```bash
th tools/tokenize.lua -bpe_model /path/to/bpe -mode aggressive -segment_numbers -case_feature -joiner_annotate -nparallel 20 < /path/to/input > /path/to/input_tok
```

## preprocess
```bash
th preprocess.lua -train_src /train/src -train_tgt /train/tgt -valid_src /valid/src -valid_tgt /valid/tgt -save_data /save/data -src_vocab_size 50000
```

## train
```bash
th train.lua -layers 4 -word_vec_size 800 -encoder_type brnn -residual -rnn_size 800 -start_decay_at 6 -end_epoch 20 -gpuid 1 -data /load/data -save_model /save/model -log_file /save/log
```

## release
th tools/release_model.lua -gpuid 1 -model /path/model



