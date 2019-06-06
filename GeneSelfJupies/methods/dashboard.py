# -*- coding: utf-8 -*-
from ipywidgets import interact, interactive, fixed, interact_manual
from ipywidgets import Layout, Button, Box, FloatText, Textarea, Dropdown, Label, IntSlider
from ipywidgets import HBox, VBox
import ipywidgets as widgets
from IPython.display import display, clear_output
from ipywidgets import Text
import qgrid
from GeneSelfJupies.models import models, admix_models, admix_fraction
import types
import numpy as np

import matplotlib.pyplot as plt
import plotly.offline as py
py.init_notebook_mode(connected=False)
import plotly.graph_objs as go


def analysis(df:str, pcd:dict, *args, **kwargs):
    '''
    分析模块
    '''
    _df = df
    _pcd = pcd
    _out = widgets.Output() #save the current output

    button1 = widgets.Button(
        description='查询',
        button_style='info'
    )

    button2 = widgets.Button(
        description='启动运行',
        button_style='info'
    )

    _id_textbox = widgets.Text(
        value='rs671',
        description='rsID:',
    )

    # style = {'description_width': 'initial'}
    # _tolerance_textbox = widgets.Text(
    #     value='0.001',
    #     description = 'tolerance(default0.001):',
    #     style=style
    # )

    style = {'description_width': 'initial'}
    _tolerance_textbox = widgets.FloatSlider(
        value=0.001,
        min=0,
        max=1,
        step=0.001,
        description='tolerance(default0.001): ',
        disabled=False,
        continuous_update=False,
        orientation='horizontal',
        readout=True,
        readout_format='.1f',
        style=style
    )


    admixmodels = widgets.Dropdown(
        description='模型选择',
        options=admix_models.admixmodels(),
        value='Select'
    )
    admixmodels.set_title = '模型选择'

    # ------------------------------------------------------- #
    @button1.on_click
    def show_on_click(b):
        '''
        显示button1的输入的查询结果
        '''
        with _out:
            clear_output()
            locus = _id_textbox.value
            display(qgrid.show_grid(_df[_df['ID'] == locus], show_toolbar=True))

    # ------------------------------------------------------- #
    @button2.on_click
    def on_button_clicked(b):
        display(models.basisInfo(_df))

    # ------------------------------------------------------- #
    #Ancestry compisition
    def anCal(m, t):
        if m == 'Select':
            print ('请选择祖源模型')
        else:

            admix_frac = np.array(models.admix_fraction(m, _pcd, tolerance=t))
            populations = np.array(models.populations(m))

            #admix_frac = np.array(admix_fraction.admix_fraction(m, _pcd, tolerance=t))
            #populations = np.array(admix_models.populations(m))

            # perform a descending sort of the fractions
            ignore_zeros = True # 忽略0值
            zh = True # 中文显示
            result = m + '\n'

            # Sort the output
            idx = np.argsort(admix_frac)[::-1]
            admix_frac = admix_frac[idx]
            populations = populations[idx]

            labels = []
            sizes = []
            for (i, frac) in enumerate(admix_frac):
                if ignore_zeros and frac < 1e-4: continue
                population_en, population_zh = populations[i]
                if zh == False:  # English
                    population = population_en
                else:  # Chinese
                    population = population_zh
                labels.append(population)
                sizes.append(100 * frac)
                result += '{:s}: {:.2f}%'.format(population, 100 * frac) + '\n'
            result += '\n'

            # print out results
            print(result)

            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
            trace = go.Pie(labels=labels, values=sizes)
            py.iplot([trace], filename=str(m))

    admix = interactive(anCal, m=admixmodels, t=_tolerance_textbox)


    tab1 = VBox(children=[_id_textbox, button1, _out])
    tab2 = VBox(children=[button2])
    tab3 = VBox(children=[admix])

    #tab = widgets.Tab(children=[tab1, tab2])
    tab = widgets.Accordion(children=[tab1, tab2, tab3])
    tab.set_title(0, '位点查询')
    tab.set_title(1, '基础信息统计')
    tab.set_title(2, '祖源构成计算')
    return VBox(children=[tab])

