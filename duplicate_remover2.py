# -*- coding: utf-8 -*-
import re


def repeat_remover(file_in, file_out):
	"Remove spectra repeat in different clusters and semicolon. This bug will be fixed in the next release."

	with open(file_in, 'r') as f_in, open(file_out, 'w') as f_out:
		seen_spectra = set()
		for line in f_in:

			if '=Cluster=' in line or line.strip() == '':
				seen_spectra = set()
				f_out.write(re.sub(';+', ';', line))

			elif bool(re.match('desname=clusteringBin[0-9]+', line) or re.match('similarity_method=([A-Z])+', line) or re.match('version=spectra-cluster\-\d+\.\d+\.\d+\-([A-Z])+', line) or re.match('threshold=\d+\.\d+', line) or re.match('fdr=\d+', line) or re.match('description=clusteringBin[0-9]+', line)):
				f_out.write(re.sub(';+', ';', line))
			else:
				new_spectrum = line.rstrip().split('=')[-1].split()[0]
				if new_spectrum in seen_spectra:
					continue
				else:
					f_out.write(re.sub(';+', ';', line))
					seen_spectra.add(new_spectrum)


def semicolon_remover(file_input, file_output):
	"Remove repeat semicolon in clustering files"
	with open(file_input, 'r') as f_in, open(file_output, 'w') as f_out:
		for line in f_in:
			file = re.sub(';+', ';', line)
			f_out.write(file)


def main():
	repeat_remover('test2.txt', 'total.clustering_no_semicolon2.txt')


if __name__ == "__main__":
	main()
