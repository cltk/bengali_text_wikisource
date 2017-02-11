import os, re
import json
import pdb

sourceLink = 'https://bn.wikisource.org/wiki/%E0%A6%AA%E0%A7%8D%E0%A6%B0%E0%A6%A7%E0%A6%BE%E0%A6%A8_%E0%A6%AA%E0%A6%BE%E0%A6%A4%E0%A6%BE'
source = 'Wikisource'

works = [{
	'originalTitle': "পাণ্ডব গীতা",
	'englishTitle': "Pandava Gita",
	'author': "Shashibhusan Purakayasta",
	'source': source,
	'sourceLink': sourceLink,
	'language': 'bengali',
	'text': {},
}, {
	'originalTitle': "শকুন্তলা",
	'englishTitle': "Shakuntala",
	'author': "Rabindranath Tagore",
	'source': source,
	'sourceLink': sourceLink,
	'language': 'bengali',
	'text': {},
}]


def main():

	# Build json docs from txt files
	for root, dirs, files in os.walk("."):
		path = root.split('/')
		for fname in files:
			if fname.endswith('txt'):
				for work in works:
					if path[1] == work['originalTitle']:
						print((len(path) - 1) * '---', os.path.basename(root))
						subwork = int(fname.replace(".txt", "")) -1
						work['text'][subwork] = {}
						text = open(os.path.join(root, fname)).read().splitlines()
						text = [textNode.strip() for textNode in text if len(textNode.strip())]
						for i, textNode in enumerate(text):
							work['text'][subwork][i] = textNode


	for work in works:
		fname = work['source'] + '__' + work['englishTitle'] + '__' + work['author'] + '.json'
		fname = fname.replace(" ", "")
		with open(fname, 'w') as f:
			json.dump(work, f)

if __name__ == '__main__':
	main()
