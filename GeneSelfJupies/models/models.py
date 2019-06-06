import pandas as pd
from GeneSelfJupies.models.admix_fraction import admix_fraction
from GeneSelfJupies.models.admix_models import populations

def genderDetect(df):
    '''
    性别判断
    :param df:
    :return:
    '''
    pass

def rarevarDetect():
    pass

def missRateCal(df):
    '''
    缺失率统计
    :param df:
    :return:
    '''

def basisInfo(df):
    '''
    基础基因型信息统计
    :return: dataframe, 位点总数，Het个数，Indel个数（仅查询II,DD,ID），缺失位点数目
    '''
    totalNum = df.shape[0]
    indelNum = 0
    hetNum = 0
    missNum = 0
    indelList = ['II', 'DD', 'ID', 'DI']
    for index, row in df.iterrows():
        try:
            if len(row['genotype']) == 1: # remove haploid snp
                continue
            if row['genotype'] in indelList:
                indelNum += 1
            if row['genotype'][0] != row['genotype'][1]:
                hetNum += 1
            if row['genotype'] == '--':
                missNum += 1
        except Exception as e:
            raise e

    missRate = missNum / float(totalNum)

    basisdf = pd.DataFrame(
        {
            '总的位点数目': [totalNum],
            'indel个数': [indelNum],
            '杂合子个数': [hetNum],
            '缺失个数': [missNum],
            '缺失率': [missRate]
        }
    )
    return basisdf

def ancestryAdmix(df):
    '''

    :param df:
    :return:
    '''





