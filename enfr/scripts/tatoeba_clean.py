import pandas as pd
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', help='input directory', 
                    type=str, required=True)
parser.add_argument('--output_dir', help='output directory', 
                    type=str, required=True)
args = parser.parse_args()

# load data
dfBase = pd.read_csv(os.path.join(args.input_dir, 'sentences.csv'), sep='\t', header=None, names=['label', 'lang', 'text'])
dfBase = dfBase.set_index('label')
dfLink = pd.read_csv(os.path.join(args.input_dir, 'links.csv'), sep='\t', header=None, names=['ida', 'idb'])

# lang label
label_en = set(dfBase[dfBase['lang']=='eng'].index.tolist())
label_fr = set(dfBase[dfBase['lang']=='fra'].index.tolist())

# lang pair
lang_pair = set()

for r in dfLink.itertuples():
    if r[1] in label_en and r[2] in label_fr:
        lang_pair.add((r[1], r[2]))
    elif r[2] in label_en and r[1] in label_fr:
        lang_pair.add((r[2], r[1]))

lang_enfr = list(lang_pair)

# save data
f_en = open(os.path.join(args.output_dir, 'tatoeba.en'), 'w')
f_fr = open(os.path.join(args.output_dir, 'tatoeba.fr'), 'w')

for t in lang_enfr:
    f_en.write(dfBase.loc[t[0],'text'].strip())
    f_en.write('\n')
    f_fr.write(dfBase.loc[t[1],'text'].strip())
    f_fr.write('\n')
    
f_en.close()
f_fr.close()


