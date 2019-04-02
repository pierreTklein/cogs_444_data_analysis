import random
from scipy.stats import mannwhitneyu
import numpy as np

def createRandEntry(nh, cr, comp, di, comf):
    numHelped = random.normalvariate(nh[0], nh[1])
    crowd = random.normalvariate(cr[0], cr[1])
    completion = random.normalvariate(comp[0], comp[1])
    difficulty = random.normalvariate(di[0], di[1])
    comfort = random.normalvariate(comf[0], comf[1])
    return np.array([numHelped, crowd, completion, difficulty, comfort])


def genData(mu1, sigma1, mu2, sigma2, num_data_pts):
    week_1 = []
    week_2 = []
    week_1_params = [mu1, sigma1]
    week_2_params = [mu2, sigma2]
    for i in range(num_data_pts):
        numHelped = week_1_params
        crowd = week_1_params
        completion = week_1_params
        difficulty = week_1_params
        comfort = week_1_params
        week_1.append(createRandEntry(numHelped, crowd,
                                      completion, difficulty, comfort))
    for i in range(num_data_pts):
        numHelped = week_2_params
        crowd = week_2_params
        completion = week_2_params
        difficulty = week_2_params
        comfort = week_2_params
        week_2.append(createRandEntry(numHelped, crowd,
                                      completion, difficulty, comfort))
    return np.array(week_1), np.array(week_2)


def noCorrelation(num_data_pts):
    return genData(2.5, 0.833, 2.5, 0.833, num_data_pts)


def positiveCorrelation(num_data_pts):
    return genData(2.5, 0.833, 4, 0.333, num_data_pts)


def veryPositiveCorrelation(num_data_pts):
    return genData(1, 0.333, 4, 0.333, num_data_pts)


def negativeCorrelation(num_data_pts):
    return genData(1, 0.333, 2.5, 0.833, num_data_pts)


def veryNegativeCorrelation(num_data_pts):
    return genData(4, 0.333, 1, 0.333, num_data_pts)


def calcSignificance(week_1, week_2):
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


week_1, week_2 = noCorrelation(30)
print(calcSignificance(week_1, week_2))

week_1, week_2 = positiveCorrelation(30)
print(calcSignificance(week_1, week_2))

week_1, week_2 = negativeCorrelation(30)
print(calcSignificance(week_1, week_2))
