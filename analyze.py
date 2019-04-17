#!/bin/python3
from scipy.stats import mannwhitneyu, median_test, rv_discrete
import csv
import numpy as np
import collections 
from functools import reduce
import random



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
    w1_cr, w1_di, w1_comp, w1_comf, w1_nh = [
        [row[i] for row in week_1] for i in range(len(week_1[0]))]
    w2_cr, w2_di, w2_comp, w2_comf, w2_nh = [
        [row[i] for row in week_2] for i in range(len(week_2[0]))]
    nh_mwu = mannwhitneyu(w1_nh, w2_nh)
    cr_mwu = mannwhitneyu(w1_cr, w2_cr)
    comp_mwu = mannwhitneyu(w1_comp, w2_comp)
    di_mwu = mannwhitneyu(w1_di, w2_di)
    comf_mwu = mannwhitneyu(w1_comf, w2_comf)
    table = [
        ('Question', 'U Statistic', 'P-Value'),
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

def pdf(data, minimum=1, maximum=5, laplace=True):
    '''
    Calculates the PDF of the inputted data. Optionally use Laplace Smoothing.
    '''

    pdfs = collections.Counter(data)
    if laplace:
        for i in range(minimum, maximum + 1):
            if pdfs[i] is None:
                pdfs[i] = 1.
            else:
                pdfs[i] += 1.
    return pdfs

# Statistical power
def gen_sample(data, n=1000, minimum=1, maximum=5):
    '''
    Generates a larger sample with the same PDF as the inputted data.
    Minimum and Maximum are the minimum and maximum values of data. Assumes that
    all of the inputted data is integral. 
    '''

    p = pdf(data, minimum, maximum)
    numbers = range(minimum, maximum + 1)
    distribution = []
    for i in numbers:
        distribution.append(p[i])
    total_samples = reduce((lambda x, y: x + y), distribution)
    distribution = map((lambda x: x / total_samples), distribution)
    random_variable = rv_discrete(values=(numbers, distribution))
    return random_variable.rvs(size=n)

def calc_power_one_sample(set_1, set_2, alpha=0.05, num_tests=1000):
    '''
    Calculate the statistical power for two independent groups. 
    - Generates a two larger samples according to the existing PDFs in each of the groups. 
    - Uses Laplace smoothing for unseen variables.
    - Runs the mann whitney u test on some subsample of the generated samples num_tests times, 
    and counts eachc time that the result was insignificant. 
    - Returns Beta.
    '''

    sample_1 = gen_sample(set_1)
    sample_2 = gen_sample(set_2)
    frequency_not_significant = 0
    for i in range(num_tests):
        test_1 = random.sample(sample_1, len(set_1))
        test_2 = random.sample(sample_2, len(set_2))
        stat, pvalue = mannwhitneyu(test_1, test_2)
        if pvalue > alpha:
            frequency_not_significant += 1
    beta = float(frequency_not_significant) / float(num_tests)
    return beta

def calc_power():
    directory = './data'
    week_1, week_2 = loadCSV('{0}/method_1.csv'.format(directory), '{0}/method_2.csv'.format(directory))

    # crowdSize, difficulty, sessionsCompleted, comfort, numHelped
    w1_cr, w1_di, w1_comp, w1_comf, w1_nh = [
            [row[i] for row in week_1] for i in range(len(week_1[0]))]
    w2_cr, w2_di, w2_comp, w2_comf, w2_nh = [
        [row[i] for row in week_2] for i in range(len(week_2[0]))]
        
    beta_cr = calc_power_one_sample(w1_cr, w2_cr)
    beta_di = calc_power_one_sample(w1_di, w2_di)
    beta_comp = calc_power_one_sample(w1_comp, w2_comp)
    beta_comf = calc_power_one_sample(w1_comf, w2_comf)
    beta_nh = calc_power_one_sample(w1_nh, w2_nh)
    table = [
        ('Question', 'Beta', 'Power'),
        ('Number Helped', beta_nh, 1 - beta_nh),
        ('Crowd Size', beta_cr,1 - beta_cr),
        ('Completed', beta_comp, 1 - beta_comp),
        ('Difficulty', beta_di, 1 - beta_di),
        ('Comfort', beta_comf, 1 - beta_comf)
    ]
    print_table("Statistical Power", table)
    return beta_cr, beta_di, beta_comp, beta_comf, beta_nh

calc_power()