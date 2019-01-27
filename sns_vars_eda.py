# -*- coding: utf-8 -*-

import warnings
warnings.filterwarnings("always")
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from matplotlib.ticker import StrMethodFormatter
from matplotlib import style
style.use("fivethirtyeight")
# sns.set(style="white", color_codes=True)
plt.style.use("ggplot")


def sns_continuous_distplot(data, x, facet=None, ggtitle=None):
    '''
    plot for single continuous variable [by a string var facet]

    Parameters
    ----------
    data : [dataframe]
        pandas dataframe
    x : [string]
        variable name in string
    facet : [string], optional
        plot by facet [description](the default is None)
    ggtitle : [string], optional
        string to plot in caption (the default is None)

    Returns
    -------
    [object]
        a seaborn object
    '''

    if ggtitle is None:
        if facet is None:
            ggtitle = "Distribution of {}".format(x)
        else:
            ggtitle = "Distribution of {} by {}".format(x, facet)
            col_wrap = np.ceil(np.sqrt(data[facet].unique().__len__()))

    kde_kws = {'lw': 1.5}
    if facet is None:
        # ref: http://seaborn.pydata.org/examples/many_facets.html
        p = sns.distplot(a=data[x], color='#ff4125', kde_kws=kde_kws, axlabel=False).set_title(ggtitle)
    else:
        p = sns.FacetGrid(data, col=facet, hue=facet, col_wrap=col_wrap)
        p = p.map(sns.distplot, x, kde_kws=kde_kws)
        p.fig.suptitle(ggtitle)
        plt.subplots_adjust(top=0.9)  # ref: https://www.programcreek.com/python/example/96204/seaborn.FacetGrid
    plt.ticklabel_format(style='scientific', scilimits=(0, 4))
    return p


def sns_continuous_continuous_scatter(data, x, y, facet=None, ggtitle=None):
    '''
    plot for continuous with continuous variable [by a string var facet]

    Parameters
    ----------
    data : [dataframe]
        pandas dataframe
    x : [string]
        variable name in string
    y : [string]
        variable name in string
    facet : [string], optional
        plot by facet [description](the default is None)
    ggtitle : [type], optional
        string to plot in caption (the default is None)

    Returns
    -------
    [object]
       a seaborn object
    '''

    if ggtitle is None:
        if facet is None:
            ggtitle = "ScatterPlot of {} vs {}".format(x, y)
        else:
            ggtitle = "ScatterPlot of {} vs {} by {}".format(x, y, facet)
            col_wrap = np.ceil(np.sqrt(data[facet].unique().__len__()))

    line_kws = {'lw': 1.5}
    if facet is None:
        p = sns.regplot(data[x], data[y], line_kws=line_kws).set_title(ggtitle)
    else:
        p = sns.FacetGrid(data, col=facet, hue=facet, col_wrap=col_wrap)
        p = p.map(sns.regplot, x, y, line_kws=line_kws)
        p.fig.suptitle(ggtitle)
        plt.subplots_adjust(top=0.9)
    plt.ticklabel_format(style='scientific', scilimits=(0, 4))
    return p


def sns_factor_continuous_boxplot(data, x, y=None, facet=None, ggtitle=None):
    '''
    plot for factor with continuous variable [by a string var facet]

    Parameters
    ----------
    data : [dataframe]
        pandas dataframe
    x : [string]
        variable name in string
    y : [string]
        variable name in string
    facet : [string], optional
        plot by facet [description](the default is None)
    ggtitle : [type], optional
        string to plot in caption (the default is None)

    Returns
    -------
    [object]
       a seaborn object
    '''
    if ggtitle is None:
        if facet is None:
            if y:
                ggtitle = "Boxplot of {} vs {}".format(x, y)
            else:
                ggtitle = "Boxplot of {}".format(x)
        else:
            if y:
                ggtitle = "Boxplot of {} vs {} by {}".format(x, y, facet)
            else:
                ggtitle = "Boxplot of {} by {}".format(x, facet)
            col_wrap = np.ceil(np.sqrt(data[facet].unique().__len__()))

    linewidth = 1
    if facet is None:
        if y:
            p = sns.boxplot(data[x], data[y], linewidth=linewidth).set_title(ggtitle)
        else:
            p = sns.boxplot(data[x], linewidth=linewidth).set_title(ggtitle)
    else:
        p = sns.FacetGrid(data, col=facet, col_wrap=col_wrap)
        if y:
            p = p.map(sns.boxplot, x, y, linewidth=linewidth)
        else:
            p = p.map(sns.boxplot, x, linewidth=linewidth)
        p.fig.suptitle(ggtitle)
        plt.subplots_adjust(top=0.9)
    return p


def sns_factor_continuous_barplot(data, y, x=None, facet=None, ggtitle=None):
    '''
    plot for factor with continuous variable [by a string var facet]

    Parameters
    ----------
    data : [dataframe]
        pandas dataframe
    x : [string]
        variable name in string
    y : [string]
        variable name in string
    facet : [string], optional
        plot by facet [description](the default is None)
    ggtitle : [type], optional
        string to plot in caption (the default is None)

    Returns
    -------
    [object]
       a seaborn object
    '''
    if ggtitle is None:
        if facet is None:
            if y:
                ggtitle = "Barplot of {} vs {}".format(y, x)
            else:
                ggtitle = "Barplot of {}".format(y)
        else:
            if y:
                ggtitle = "Barplot of {} vs {} by {}".format(y, x, facet)
            else:
                ggtitle = "Barplot of {} by {}".format(y, facet)
            col_wrap = np.ceil(np.sqrt(data[facet].unique().__len__()))

    linewidth = 1
    if facet is None:
        if x:
            p = sns.barplot(data[x], data[y], linewidth=linewidth).set_title(ggtitle)
        else:
            p = sns.barplot(data[x], linewidth=linewidth).set_title(ggtitle)
    else:
        p = sns.FacetGrid(data, col=facet, col_wrap=col_wrap)
        if x:
            p = p.map(sns.barplot, x, y, linewidth=linewidth)
        else:
            p = p.map(sns.barplot, x, linewidth=linewidth)
        p.fig.suptitle(ggtitle)
        plt.subplots_adjust(top=0.9)
    return p


def sns_factor_countplot(data, x, facet=None, ggtitle=None):
    '''
    plot for factor with continuous variable [by a string var facet]

    Parameters
    ----------
    data : [dataframe]
        pandas dataframe
    x : [string]
        variable name in string
    y : [string]
        variable name in string
    facet : [string], optional
        plot by facet [description](the default is None)
    ggtitle : [type], optional
        string to plot in caption (the default is None)

    Returns
    -------
    [object]
       a seaborn object
    '''
    if ggtitle is None:
        if facet is None:
            ggtitle = "Countplot of {}".format(x)
        else:
            ggtitle = "Countplot of {} by {}".format(x, facet)
            col_wrap = np.ceil(np.sqrt(data[facet].unique().__len__()))

    if facet is None:
        p = sns.countplot(data[x]).set_title(ggtitle)
    else:
        p = sns.FacetGrid(data, col=facet, col_wrap=col_wrap)
        p.map(sns.countplot, x)
        p.fig.suptitle(ggtitle)
        plt.subplots_adjust(top=0.9)
    return p


if __name__ == "__main__":
    df = pd.read_csv("./tests/train.csv").fillna(0)
    print("df: ", df.shape)
    cat_df = df.select_dtypes(include='object')
    print("cat_df: ", cat_df.shape)
    num_df = df.select_dtypes(include='number')
    print("num_df: ", num_df.shape)
    # sns_continuous_distplot(df, "SalePrice")
    # sns_continuous_distplot(df, "SalePrice", "OverallQual")
    # sns_continuous_continuous_scatter(df, "YearBuilt", "SalePrice")
    # sns_continuous_continuous_scatter(df, "YearBuilt", "SalePrice", "OverallQual")
    # sns_continuous_continuous_boxplot(df, "SalePrice")
    # sns_factor_continuous_boxplot(df, "OverallQual", "SalePrice")
    # sns_factor_continuous_boxplot(df, "YearBuilt", "SalePrice", "OverallQual")
    # sns_factor_countplot(df, "OverallQual")
    # sns_factor_countplot(df, "YearBuilt", "OverallQual")
    # sns_factor_continuous_barplot(df, x="OverallQual", y="SalePrice")
    sns_factor_continuous_barplot(df, x="YearBuilt", y="SalePrice", facet="OverallQual")
    plt.show()
