import random
from scipy.stats import mannwhitneyu
import numpy as np

# Creates a new row of data
def createRandEntry(nh, cr, comp, di, comf):
    '''
    Create a new row of data randomized according to normal distribution, for all 5 datasets.
    nh: normal distribution parameters for number of students helped. Tuple: (mu, sigma)
    cr: normal distribution parameters for crowd size. Tuple: (mu, sigma)
    comp: normal distribution parameters for number of tutoring sessions completed. Tuple: (mu, sigma)
    di: normal distribution parameters for difficulty of instruction. Tuple: (mu, sigma)
    comf: normal distribution parameters for comfort level. Tuple: (mu, sigma)
    '''
    numHelped = random.normalvariate(nh[0], nh[1])
    crowd = random.normalvariate(cr[0], cr[1])
    completion = random.normalvariate(comp[0], comp[1])
    difficulty = random.normalvariate(di[0], di[1])
    comfort = random.normalvariate(comf[0], comf[1])
    return np.array([numHelped, crowd, completion, difficulty, comfort])

# Generate dataset for both methods
def genData(mu1, sigma1, mu2, sigma2, num_data_pts):
    '''
    mu1: the mean of the first method.
    sigma1: the sigma of the first method.
    mu2: the mean of the second method.
    sigma2: the sigma of the second method.
    num_data_pts: the sample size of each week.

    Returns a tuple-- the first item is the data for the first week, and the second item is the data for the second week.
    '''
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
    '''
    Generate a dataset with the same mean, variance for both weeks. They are both centered around 2.5, with a standard 
    deviation of 0.833, so that 97% is at 5.
    '''
    return genData(2.5, 0.833, 2.5, 0.833, num_data_pts)


def positiveCorrelation(num_data_pts):
    '''
    Generate a dataset where the first week is centered at 2.5, and std. deviation of 0.833. 
    Second week is centered at 4, with a std. deviation of 0.333.
    '''
    return genData(2.5, 0.833, 4, 0.333, num_data_pts)


def veryPositiveCorrelation(num_data_pts):
    '''
    Generate a dataset where the first week is centered at 1, and std. deviation of 0.333. 
    Second week is centered at 4, with a std. deviation of 0.333.
    '''
    return genData(1, 0.333, 4, 0.333, num_data_pts)


def negativeCorrelation(num_data_pts):
    '''
    Generate a dataset where the first week is centered at 1, and std. deviation of 0.333. 
    Second week is centered at 2.5, with a std. deviation of 0.833.
    '''
    return genData(1, 0.333, 2.5, 0.833, num_data_pts)


def veryNegativeCorrelation(num_data_pts):
    '''
    Generate a dataset where the first week is centered at 4, with a std. deviation of 0.333.
    Second week is centered at 1, and std. deviation of 0.333. 
    '''
    return genData(4, 0.333, 1, 0.333, num_data_pts)


def calcSignificance(week_1, week_2):
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


week_1, week_2 = noCorrelation(30)
print(calcSignificance(week_1, week_2))

week_1, week_2 = positiveCorrelation(30)
print(calcSignificance(week_1, week_2))

week_1, week_2 = negativeCorrelation(30)
print(calcSignificance(week_1, week_2))
