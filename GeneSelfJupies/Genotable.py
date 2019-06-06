# -*- coding: utf-8 -*-
from .methods import *
from .methods.dashboard import *
import pandas
import types
import qgrid

class GenoTable():
    def __init__(self, df):
        self._jvds = df
        self.processed_data = {} #applied to admix
        for index, row in self._jvds.iterrows():
            try:
                if len(row['genotype']) == 1: continue
                if len(row) == 4 and row['genotype'][-1] in ['A', 'T', 'G', 'C']:
                    self.processed_data[row['ID']] = row['genotype']
            except Exception as e:
                raise e

    def data2qgrid(self, df):
        if isinstance(df, pandas.DataFrame):
            grid_options = {
                'fullWidthRows': True,
                'syncColumnCellResize': True,
                'forceFitColumns': False,
                'defaultColumnWidth': 180,
                'rowHeight': 28,
                'enableColumnReorder': False,
                'enableTextSelectionOnCells': True,
                'editable': True,
                'autoEdit': False,
                'explicitInitialization': True,
                'maxVisibleRows': 15,
                'minVisibleRows': 8,
                'sortable': True,
                'filterable': True,
                'highlightSelectedCell': False,
                'highlightSelectedRow': True

            }
            return qgrid.show_grid(df, grid_options=grid_options, show_toolbar=True)
        else:
            print ('!')

    def show(self):
        '''
        数据展示， help to explore your dataframe
        :return:
        '''
        return self.data2qgrid(self._jvds)

    def run(self):
        '''
        启动分析
        :return:
        '''
        return analysis(df=self._jvds, pcd=self.processed_data)




