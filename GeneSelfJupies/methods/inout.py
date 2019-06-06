# -*- coding: utf-8 -*-
import pandas as pd
from GeneSelfJupies.Genotable import GenoTable

_cached_loaddata = None


def calc_skiprows(path):
    '''
    计算 skiprows（读取需要去掉的注释行，行数）
    :return:    int        行数
    '''
    skiprows = 0
    with open(path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line.startswith('#'):
                break
            skiprows += 1
    return skiprows

def import_data(path):
    '''

    :param path: 原始raw基因文件，23andme-format
    :return: GenoTable对象
    '''
    skiprows = calc_skiprows(path)
    global _cached_loaddata
    if _cached_loaddata is None:
        _cached_loaddata = pd.read_csv(path, sep='\t', skiprows=skiprows, dtype=str, header=None)
    _cached_loaddata.rename(columns = {0:'ID', 1:'contig', 2:'position', 3:'genotype'}, inplace = True)

    return GenoTable(_cached_loaddata)

def get_value(defValue=None):
    try:
        return _cached_loaddata
    except KeyError:
        return defValue
