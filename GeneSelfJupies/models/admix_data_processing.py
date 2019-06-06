import csv
import numpy as np
import os
from GeneSelfJupies.models import models, admix_models, admix_fraction

# convert alleles information of a model to a dict
def read_model(model):
    # obtain model file names
    snp_file_name = admix_models.snp_file_name(model)
    frequency_file_name = admix_models.frequency_file_name(model)

    # read SNPs
    snp = []
    minor_alleles = []
    major_alleles = []

    with open(
            os.path.join(os.path.dirname(__file__), 'data/' + snp_file_name),
            'r') as snp_file:
        snp_file = csv.reader(snp_file, delimiter=' ')
        for row in snp_file:
            snp.append(row[0])
            minor_alleles.append(row[1])
            major_alleles.append(row[2])

    # read frequency matrix
    frequency = []
    with open(
            os.path.join(
                os.path.dirname(__file__), 'data/' + frequency_file_name),
            'r') as frequency_file:
        frequency_file = csv.reader(frequency_file, delimiter=' ')
        for row in frequency_file:
            frequency.append([float(f) for f in row])

    return np.array(snp), np.array(minor_alleles), np.array(
        major_alleles), np.array(frequency)