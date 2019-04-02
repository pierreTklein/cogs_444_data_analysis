from scipy.stats import mannwhitneyu
import csv
import numpy as np

def loadCSV(filename_week_1, filename_week_2):
    week_1 = []
    week_2 = []
    with open(filename_week_1, 'r') as f:
        fieldnames = ['numHelped', 'crowdSize', 'sessionsCompleted', 'difficulty', 'comfort']
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in csv_reader:
            week_1.append(np.array(row.values()))
    with open(filename_week_2, 'r') as f:
        fieldnames = ['numHelped', 'crowdSize', 'sessionsCompleted', 'difficulty', 'comfort']
        csv_reader = csv.DictReader(f, fieldnames=fieldnames)
        for row in csv_reader:
            week_2.append(np.array(row.values()))
    return week_1, week_2


def calcMattWhitneyU(week_1, week_2):
    '''
    Run Mann Whitney U test on all 5 variables across week 1 and week 2. 
    week_1, week_2 is of the same format as the output of genData.
    Return the results for all 5 variables.
    '''
    w1_nh, w1_cr, w1_comp, w1_di, w1_comf = [
        [row[i] for row in week_1] for i in range(len(week_1[0]))]
    w2_nh, w2_cr, w2_comp, w2_di, w2_comf = [
        [row[i] for row in week_2] for i in range(len(week_2[0]))]
    nh_mwu = mannwhitneyu(w1_nh, w2_nh)
    cr_mwu = mannwhitneyu(w1_cr, w2_cr)
    comp_mwu = mannwhitneyu(w1_comp, w2_comp)
    di_mwu = mannwhitneyu(w1_di, w2_di)
    comf_mwu = mannwhitneyu(w1_comf, w2_comf)
    return nh_mwu, cr_mwu, comp_mwu, di_mwu, comf_mwu


directory = './sample_data/normal'

week_1, week_2 = loadCSV('{0}/neg_correlation_week_1'.format(directory), '{0}/neg_correlation_week_2'.format(directory))
print(calcMattWhitneyU(week_1, week_2))

week_1, week_2 = loadCSV('{0}/no_correlation_week_1'.format(directory), '{0}/no_correlation_week_2'.format(directory))
print(calcMattWhitneyU(week_1, week_2))

week_1, week_2 = loadCSV('{0}/pos_correlation_week_1'.format(directory), '{0}/pos_correlation_week_2'.format(directory))
print(calcMattWhitneyU(week_1, week_2))
