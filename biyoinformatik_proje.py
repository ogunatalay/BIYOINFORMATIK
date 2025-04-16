# -*- coding: utf-8 -*-
"""BIYOINFORMATIK PROJE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GXHnYgSmQfFOahqwnVd2qBVoDvdf9-ee
"""

!pip install biopython
#OGÜN ATALAY 

from Bio import SeqIO
from collections import Counter

# 1. SORU A ŞIKKI
# DNA dosyasını okuyup nükleotid sayılarını hesaplayan fonksiyon

def count_nucleotides_without_N(file_path):
    nucleotide_counts = Counter()
    for record in SeqIO.parse(file_path, "fasta"):
        # Belirsiz nükleotidleri filtrele (N'yi dahil etme)
        nucleotide_counts.update(n for n in record.seq if n != "N")
    return nucleotide_counts

# DNA Dosyasını okuyup işlem yap
dna_file = "DNA.fasta"
nucleotide_counts = count_nucleotides_without_N(dna_file)

# Sonuçları ekrana yazdır
print("Nucleotide Counts (excluding N):")
for nucleotide, count in nucleotide_counts.items():
    print(f"{nucleotide}: {count}")

from Bio import SeqIO
from Bio.Seq import Seq

# 1. SORU B ŞIKKI:
#DNA sıralarını RNA'ya çeviren fonksiyon

def convert_to_rna(file_path, output_file):
    with open(output_file, "w") as output_handle:
        for record in SeqIO.parse(file_path, "fasta"):
            # DNA sırasını RNA'ya çevir
            rna_sequence = record.seq.transcribe()
            # Yeni RNA sırasını yaz
            record.seq = rna_sequence
            SeqIO.write(record, output_handle, "fasta")
    print(f"RNA sequences have been saved to {output_file}")

# DNA dosyasını RNA'ya çevir
dna_file = "DNA.fasta"
rna_file = "RNA_Dosyası.fasta"  # Çıkış dosyası adı
convert_to_rna(dna_file, rna_file)

# 1. SORU C ŞIKKI
#DNA sıralarını proteine çevirmek için özel bir fonksiyon

from Bio import SeqIO

# Kendi kodon tablomuzu tanımlayalım
custom_codon_table = {
    'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
    'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
    'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
    'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
    'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
    'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
    'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
    'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
    'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
    'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W'
}

# DNA sıralarını proteine çevirmek için özel bir fonksiyon
def translate_with_custom_codons(dna_sequence):
    protein_sequence = []
    # DNA sırasını 3'erli gruplara ayırarak çevir
    for i in range(0, len(dna_sequence) - len(dna_sequence) % 3, 3):  # Kodonları işleme
        codon = dna_sequence[i:i+3]
        if codon in ('TAA', 'TAG', 'TGA'):  # Stop kodonlarına ulaşıldığında çevirimi durdur
            break
        protein_sequence.append(custom_codon_table.get(codon, 'X'))  # Kodon -> Amino Asit
    return "".join(protein_sequence)

# DNA dosyasındaki sıraları proteine çeviren fonksiyon
def convert_to_protein_with_custom_codons(file_path, output_file):
    with open(output_file, "w") as output_handle:
        for record in SeqIO.parse(file_path, "fasta"):
            protein_sequence = translate_with_custom_codons(str(record.seq))  # DNA -> Protein
            record.seq = protein_sequence
            record.description += " [Translated Protein]"
            SeqIO.write(record, output_handle, "fasta")
    print(f"Protein sequences have been saved to {output_file}")

# DNA dosyasını proteine çevir ve FASTA dosyasına kaydet
dna_file = "DNA.fasta"
protein_file = "Protein_Dosyası.fasta"  # Çıkış dosyası adı
convert_to_protein_with_custom_codons(dna_file, protein_file)

from Bio import SeqIO

# 1. SORU E ŞIKKI
#DNA sıralarının GC içeriğini hesaplayan fonksiyon

def calculate_gc_content(file_path):
    gc_contents = []
    for record in SeqIO.parse(file_path, "fasta"):
        seq = record.seq.upper()  # DNA sırasını büyük harfe çevir
        g_count = seq.count("G")  # G sayısını hesapla
        c_count = seq.count("C")  # C sayısını hesapla
        gc_content = (g_count + c_count) / len(seq) * 100  # GC içeriğini hesapla
        gc_contents.append((record.id, gc_content))
    return gc_contents

# DNA dosyasındaki GC içeriklerini hesapla
dna_file = "DNA.fasta"
gc_contents = calculate_gc_content(dna_file)

# GC içeriklerini ekrana yazdır
print("GC Contents:")
for record_id, gc_content in gc_contents:
    print(f"{record_id}: {gc_content:.2f}%")

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# 1.SORU F ŞIKKI
#DNA dosyasındaki sıraları okuyup global hizalama yapan fonksiyon
def global_alignments(file_path):
    sequences = [record for record in SeqIO.parse(file_path, "fasta")]  # DNA sıralarını listeye al
    alignments = []  # Tüm hizalamaları saklamak için bir liste
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):  # Her bir çift sıralamayı hizala
            seq1 = sequences[i]
            seq2 = sequences[j]
            alignment = pairwise2.align.globalxx(seq1.seq, seq2.seq)  # Global hizalama
            alignments.append((seq1.id, seq2.id, alignment))
    return alignments

# Hizalamaları ekrana yazdırma fonksiyonu
def display_alignments(alignments):
    for seq1_id, seq2_id, alignment in alignments:
        print(f"\nAlignment between {seq1_id} and {seq2_id}:")
        for align in alignment:
            print(format_alignment(*align))  # Hizalamayı formatla ve yazdır

# DNA dosyasını global olarak hizala
dna_file = "DNA.fasta"
alignments = global_alignments(dna_file)

# Hizalamaları ekrana yazdır
display_alignments(alignments)

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# 1. SORU G ŞIKKI
#DNA dosyasındaki sıraları okuyup yerel hizalama yapan fonksiyon
def local_alignments(file_path):
    sequences = [record for record in SeqIO.parse(file_path, "fasta")]  # DNA sıralarını listeye al
    alignments = []  # Tüm hizalamaları saklamak için bir liste
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):  # Her bir çift sıralamayı hizala
            seq1 = sequences[i]
            seq2 = sequences[j]
            alignment = pairwise2.align.localxx(seq1.seq, seq2.seq)  # Yerel hizalama
            alignments.append((seq1.id, seq2.id, alignment))
    return alignments

# Hizalamaları ekrana yazdırma fonksiyonu
def display_alignments(alignments):
    for seq1_id, seq2_id, alignment in alignments:
        print(f"\nLocal Alignment between {seq1_id} and {seq2_id}:")
        for align in alignment:
            print(format_alignment(*align))  # Hizalamayı formatla ve yazdır

# DNA dosyasını yerel olarak hizala
dna_file = "DNA.fasta"
alignments = local_alignments(dna_file)

# Hizalamaları ekrana yazdır
display_alignments(alignments)

from Bio import SeqIO
from collections import Counter

#1. SORU H ŞIKKI
#DNA dizilerinden Pozisyon Sıklık Matrisi hesaplama fonksiyonu
def calculate_pfm(file_path):
    sequences = [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]  # DNA dizilerini listele
    max_length = max(len(seq) for seq in sequences)  # En uzun dizinin uzunluğu
    pfm = []

    # Her pozisyondaki nükleotid frekanslarını hesapla
    for i in range(max_length):
        column = [seq[i] if i < len(seq) else '-' for seq in sequences]  # Kısa dizilere '-' ekle
        counts = Counter(column)  # Nükleotid sayımlarını hesapla
        pfm.append(counts)

    return pfm

# PFM'i ekrana yazdırma fonksiyonu
def display_pfm(pfm):
    print("Position Frequency Matrix (PFM):")
    for i, counts in enumerate(pfm):
        print(f"Position {i + 1}: A={counts.get('A', 0)}, C={counts.get('C', 0)}, G={counts.get('G', 0)}, T={counts.get('T', 0)}, Gap={counts.get('-', 0)}")

# DNA dosyasından PFM hesapla ve ekrana yazdır
dna_file = "DNA.fasta"
pfm = calculate_pfm(dna_file)
display_pfm(pfm)

from Bio import SeqIO
from collections import Counter

#1 SORU İ ŞIKKI Aşağıda, pozisyon sıklık matrisinden (PFM) türetilen PPM'yi hesaplamak için
# Pozisyon Sıklık Matrisi (PFM) Hesaplama
def calculate_pfm(file_path):
    sequences = [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]  # DNA dizilerini listele
    max_length = max(len(seq) for seq in sequences)  # En uzun dizinin uzunluğu
    pfm = []

    # Her pozisyondaki nükleotid frekanslarını hesapla
    for i in range(max_length):
        column = [seq[i] if i < len(seq) else '-' for seq in sequences]  # Kısa dizilere '-' ekle
        counts = Counter(column)  # Nükleotid sayımlarını hesapla
        pfm.append(counts)

    return pfm, len(sequences)

# Pozisyon Sıklık Matrisi'nden (PFM) Pozisyon Olasılık Matrisi (PPM) Hesaplama
def calculate_ppm(pfm, total_sequences):
    ppm = []
    for counts in pfm:
        probabilities = {base: counts[base] / total_sequences for base in "ACGT"}  # Olasılıkları hesapla
        ppm.append(probabilities)
    return ppm

# PPM'yi Görselleştirme
def display_ppm(ppm):
    print("Position Probability Matrix (PPM):")
    for i, probabilities in enumerate(ppm):
        print(f"Position {i + 1}: A={probabilities.get('A', 0):.3f}, C={probabilities.get('C', 0):.3f}, G={probabilities.get('G', 0):.3f}, T={probabilities.get('T', 0):.3f}")

# DNA Dosyasından PFM ve PPM Hesaplama
dna_file = "DNA.fasta"
pfm, total_sequences = calculate_pfm(dna_file)
ppm = calculate_ppm(pfm, total_sequences)

# PPM'yi Yazdır
display_ppm(ppm)

from Bio import SeqIO
from collections import Counter
import math
#1. SORU J ŞIKKI
# Pozisyon Sıklık Matrisi (PFM) Hesaplama
def calculate_pfm(file_path):
    sequences = [str(record.seq) for record in SeqIO.parse(file_path, "fasta")]  # DNA dizilerini listele
    max_length = max(len(seq) for seq in sequences)  # En uzun dizinin uzunluğu
    pfm = []

    # Her pozisyondaki nükleotid frekanslarını hesapla
    for i in range(max_length):
        column = [seq[i] if i < len(seq) else '-' for seq in sequences]  # Kısa dizilere '-' ekle
        counts = Counter(column)  # Nükleotid sayımlarını hesapla
        pfm.append(counts)

    return pfm, len(sequences)

# Pozisyon Sıklık Matrisi'nden (PFM) Pozisyon Olasılık Matrisi (PPM) Hesaplama
def calculate_ppm(pfm, total_sequences):
    ppm = []
    for counts in pfm:
        probabilities = {base: counts[base] / total_sequences for base in "ACGT"}  # Olasılıkları hesapla
        ppm.append(probabilities)
    return ppm

# Pozisyon Olasılık Matrisi'nden (PPM) Pozisyon Ağırlık Matrisi (PWM) Hesaplama
def calculate_pwm(ppm, background_frequency=0.25):
    pwm = []
    for probabilities in ppm:
        weights = {}
        for base in "ACGT":
            prob = probabilities.get(base, 0)
            if prob > 0:
                weights[base] = math.log2(prob / background_frequency)  # PWM formülü
            else:
                weights[base] = -math.inf  # 0 olasılık için -∞
        pwm.append(weights)
    return pwm

# PWM'yi Görselleştirme
def display_pwm(pwm):
    print("Position Weight Matrix (PWM):")
    for i, weights in enumerate(pwm):
        print(f"Position {i + 1}: A={weights.get('A', 0):.3f}, C={weights.get('C', 0):.3f}, G={weights.get('G', 0):.3f}, T={weights.get('T', 0):.3f}")

# DNA dosyasından PFM, PPM ve PWM Hesaplama
dna_file = "DNA.fasta"
pfm, total_sequences = calculate_pfm(dna_file)
ppm = calculate_ppm(pfm, total_sequences)
pwm = calculate_pwm(ppm)

# PWM'yi Yazdır
display_pwm(pwm)

from Bio import SeqIO
import re
#2. soru a şıkkı
# Belirli bir motif deseni arama
def search_motif_in_proteins(file_path, motif):
    results = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequence = str(record.seq)
        matches = [(m.start() + 1, m.group()) for m in re.finditer(motif, sequence)]  # Motif eşleşmeleri
        results.append((record.id, matches))
    return results

# Protein dosyasını ve motif desenini belirle
protein_file = "Protein.fasta"
motif_pattern = r".{5}"  # Herhangi bir 5 uzunluklu motif
motif_results = search_motif_in_proteins(protein_file, motif_pattern)

# Sonuçları ekrana yazdır
for record_id, matches in motif_results:
    print(f"\nProtein ID: {record_id}")
    if matches:
        print("Motif matches found:")
        for position, match in matches:
            print(f"  Position: {position}, Motif: {match}")
    else:
        print("No matches found.")

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#2. SORU B ŞIKKI
# Protein sıralarını okuyup global hizalama yapan fonksiyon
def global_alignments(file_path):
    sequences = [record for record in SeqIO.parse(file_path, "fasta")]  # Protein sıralarını listeye al
    alignments = []  # Tüm hizalamaları saklamak için bir liste
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):  # Her bir çift sıralamayı hizala
            seq1 = sequences[i]
            seq2 = sequences[j]
            alignment = pairwise2.align.globalxx(seq1.seq, seq2.seq)  # Global hizalama
            alignments.append((seq1.id, seq2.id, alignment))
    return alignments

# Hizalamaları ekrana yazdırma fonksiyonu
def display_alignments(alignments):
    for seq1_id, seq2_id, alignment in alignments:
        print(f"\nGlobal Alignment between {seq1_id} and {seq2_id}:")
        for align in alignment[:1]:  # İlk en iyi hizalamayı göster
            print(format_alignment(*align))

# Protein dosyasını global olarak hizala
protein_file = "Protein.fasta"
alignments = global_alignments(protein_file)

# Hizalamaları ekrana yazdır
display_alignments(alignments)

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#2. SORU C ŞIKKI
# Protein sıralarını okuyup yerel hizalama yapan fonksiyon
def local_alignments(file_path):
    sequences = [record for record in SeqIO.parse(file_path, "fasta")]  # Protein sıralarını listeye al
    alignments = []  # Tüm hizalamaları saklamak için bir liste
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):  # Her bir çift sıralamayı hizala
            seq1 = sequences[i]
            seq2 = sequences[j]
            alignment = pairwise2.align.localxx(seq1.seq, seq2.seq)  # Yerel hizalama
            alignments.append((seq1.id, seq2.id, alignment))
    return alignments

# Hizalamaları ekrana yazdırma fonksiyonu
def display_alignments(alignments):
    for seq1_id, seq2_id, alignment in alignments:
        print(f"\nLocal Alignment between {seq1_id} and {seq2_id}:")
        for align in alignment[:1]:  # İlk en iyi hizalamayı göster
            print(format_alignment(*align))

# Protein dosyasını yerel olarak hizala
protein_file = "Protein.fasta"
alignments = local_alignments(protein_file)

# Hizalamaları ekrana yazdır
display_alignments(alignments)

from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
#2. soru d şıkkı

#GLOBAL
# Özelleştirilmiş global hizalama yapan fonksiyon
def global_alignments_with_custom_scores(file_path, match_score, mismatch_penalty, gap_open_penalty, gap_extend_penalty):
    sequences = [record for record in SeqIO.parse(file_path, "fasta")]  # Protein sıralarını listeye al
    alignments = []  # Tüm hizalamaları saklamak için bir liste
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):  # Her bir çift sıralamayı hizala
            seq1 = sequences[i]
            seq2 = sequences[j]
            alignment = pairwise2.align.globalms(
                seq1.seq, seq2.seq,
                match_score, mismatch_penalty,
                gap_open_penalty, gap_extend_penalty
            )
            alignments.append((seq1.id, seq2.id, alignment))
    return alignments

# Global hizalamaları yazdırma
def display_global_alignments(alignments):
    for seq1_id, seq2_id, alignment in alignments:
        print(f"\nGlobal Alignment between {seq1_id} and {seq2_id}:")
        for align in alignment[:1]:  # İlk en iyi hizalamayı göster
            print(format_alignment(*align))

# Özelleştirilmiş parametrelerle global hizalama
protein_file = "Protein.fasta"
global_alignments = global_alignments_with_custom_scores(protein_file, match_score=2, mismatch_penalty=-1, gap_open_penalty=-2, gap_extend_penalty=-0.5)
display_global_alignments(global_alignments)

#LOKAL
# Özelleştirilmiş yerel hizalama yapan fonksiyon
def local_alignments_with_custom_scores(file_path, match_score, mismatch_penalty, gap_open_penalty, gap_extend_penalty):
    sequences = [record for record in SeqIO.parse(file_path, "fasta")]  # Protein sıralarını listeye al
    alignments = []  # Tüm hizalamaları saklamak için bir liste
    for i in range(len(sequences)):
        for j in range(i + 1, len(sequences)):  # Her bir çift sıralamayı hizala
            seq1 = sequences[i]
            seq2 = sequences[j]
            alignment = pairwise2.align.localms(
                seq1.seq, seq2.seq,
                match_score, mismatch_penalty,
                gap_open_penalty, gap_extend_penalty
            )
            alignments.append((seq1.id, seq2.id, alignment))
    return alignments

# Yerel hizalamaları yazdırma
def display_local_alignments(alignments):
    for seq1_id, seq2_id, alignment in alignments:
        print(f"\nLocal Alignment between {seq1_id} and {seq2_id}:")
        for align in alignment[:1]:  # İlk en iyi hizalamayı göster
            print(format_alignment(*align))

# Özelleştirilmiş parametrelerle yerel hizalama
local_alignments = local_alignments_with_custom_scores(protein_file, match_score=3, mismatch_penalty=-2, gap_open_penalty=-5, gap_extend_penalty=-1)
display_local_alignments(local_alignments)