#!/usr/bin/env python3
import sys
from collections import Counter

def read_fasta(path):
    sequences = []



def parse_fastq(path):
    """Extrait les séquences (ligne 2 de chaque bloc de 4)."""
    sequences = []
    with open(path) as f:
        while True:
            header = f.readline()
            if not header:
                break
            seq = f.readline().strip()
            f.readline()  # +
            f.readline()   # qualités
            if seq:
                sequences.append(seq)
    return sequences

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <fichier.fastq>")
        sys.exit(1)
    fastq_path = sys.argv[1]

    print("Lecture du fichier...")
    sequences = parse_fastq(fastq_path)

    total = len(sequences)
    counts = Counter(sequences)
    distinct = len(counts)
    unique = sum(1 for c in counts.values() if c == 1)

    lengths = [len(s) for s in sequences]
    len_min, len_max = min(lengths), max(lengths)
    len_mean = sum(lengths) / len(lengths)

    # Distribution d'abondance : combien de séquences ont 1 occurrence, 2, etc.
    abundance_dist = Counter(counts.values())

    print("\n=== Étude des séquences (ETU) ===\n")
    print(f"Nombre total de reads     : {total}")
    print(f"Séquences distinctes      : {distinct}")
    print(f"Séquences uniques (x1)     : {unique}")
    print(f"\nLongueur : min = {len_min}, max = {len_max}, moyenne = {len_mean:.1f}")
    print("\nDistribution d'abondance (occurrences → nombre de séquences):")
    for occ in sorted(abundance_dist.keys())[:20]:
        print(f"  {occ:6d} occurrence(s) → {abundance_dist[occ]:8d} séquences")
    if len(abundance_dist) > 20:
        print("  ...")
        max_occ = max(abundance_dist.keys())
        print(f"  {max_occ:6d} occurrence(s) → {abundance_dist[max_occ]:8d} séquences")

if __name__ == "__main__":
    main()