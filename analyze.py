#!/bin/python3
from scipy.stats import mannwhitneyu, median_test
import csv
import numpy as np

def loadCSV(filename_week_1, filename_week_2):
    week_1 = []
    week_2 = []
    with open(filename_week_1, 'r') as f:
        fieldnames = ['numHelped', 'crowdSize', 'sessionsCompleted', 'difficulty', 'comfort']
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for i, row in enumerate(csv_reader):
            if i > 0:
                week_1.append(np.array([float(v) for v in row.values()]))
    with open(filename_week_2, 'r') as f:
        fieldnames = ['numHelped', 'crowdSize', 'sessionsCompleted', 'difficulty', 'comfort']
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for i, row in enumerate(csv_reader):
            if i > 0:
                week_2.append(np.array([float(v) for v in row.values()]))
    return week_1, week_2


def calcMattWhitneyU(week_1, week_2):
    '''
    Run Mann Whitney U test on all 5 variables across week 1 and week 2. 
    week_1, week_2 is of the same format as the output of genData.
    Return the results for all 5 variables.
    '''
    w1_comf, w1_di, w1_comp, w1_cr, w1_nh = [
        [row[i] for row in week_1] for i in range(len(week_1[0]))]
    w2_comf, w2_di, w2_comp, w2_cr, w2_nh = [
        [row[i] for row in week_2] for i in range(len(week_2[0]))]
    nh_mwu = mannwhitneyu(w1_nh, w2_nh)
    cr_mwu = mannwhitneyu(w1_cr, w2_cr)
    comp_mwu = mannwhitneyu(w1_comp, w2_comp)
    di_mwu = mannwhitneyu(w1_di, w2_di)
    comf_mwu = mannwhitneyu(w1_comf, w2_comf)
    table = [
        ('Question', 'Statistic', 'P-Value'),
        ('Number Helped', nh_mwu[0], nh_mwu[1]),
        ('Crowd Size', cr_mwu[0], cr_mwu[1]),
        ('Completed', comp_mwu[0], comp_mwu[1]),
        ('Difficulty', di_mwu[0], di_mwu[1]),
        ('Comfort', comf_mwu[0], comf_mwu[1])
    ]
    print_table("Matt Whitney U Test Results", table)
    return nh_mwu, cr_mwu, comp_mwu, di_mwu, comf_mwu

def print_table(title, table):
    title_length = len(title)
    print("+-" + "-"* title_length + "-+")
    print("| \033[1m" + title + "\033[0m | ")

    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 3)
        for i in range(len(table[0]))
    ]
    row_format = "|".join(["{:>" + str(longest_col) + "}" for longest_col in longest_cols])
    divider = "+" + "+".join([("-" * longest_col) for longest_col in longest_cols]) + "+"
    print(divider)
    for i,row in enumerate(table):
        print("|" + row_format.format(*row) + "|")
        if i == 0:
            print(divider)
    print(divider)

def calcMedianTest(week_1, week_2):
    '''
    Run median test on all 5 variables across week 1 and week 2. 
    week_1, week_2 is of the same format as the output of genData.
    Return the results for all 5 variables.
    '''
    w1_comf, w1_di, w1_comp, w1_cr, w1_nh = [
        [row[i] for row in week_1] for i in range(len(week_1[0]))]
    w2_comf, w2_di, w2_comp, w2_cr, w2_nh = [
        [row[i] for row in week_2] for i in range(len(week_2[0]))]
    nh_mt = median_test(w1_nh, w2_nh)
    cr_mt = median_test(w1_cr, w2_cr)
    comp_mt = median_test(w1_comp, w2_comp)
    di_mt = median_test(w1_di, w2_di)
    comf_mt = median_test(w1_comf, w2_comf)
    return nh_mt, cr_mt, comp_mt, di_mt, comf_mt 


def analyzeExample():
    directory = './sample_data/normal'

    week_1, week_2 = loadCSV('{0}/neg_correlation_week_1'.format(directory), '{0}/neg_correlation_week_2'.format(directory))
    calcMattWhitneyU(week_1, week_2)

    week_1, week_2 = loadCSV('{0}/no_correlation_week_1'.format(directory), '{0}/no_correlation_week_2'.format(directory))
    calcMattWhitneyU(week_1, week_2)

    week_1, week_2 = loadCSV('{0}/pos_correlation_week_1'.format(directory), '{0}/pos_correlation_week_2'.format(directory))
    calcMattWhitneyU(week_1, week_2)


def analyze():
    directory = './data'
    week_1, week_2 = loadCSV('{0}/method_1.csv'.format(directory), '{0}/method_2.csv'.format(directory))
    calcMattWhitneyU(week_1, week_2)

analyze()