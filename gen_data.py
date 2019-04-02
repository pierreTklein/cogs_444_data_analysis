import random
import numpy as np
import csv


def createRandEntryPoisson(nh, cr, comp, di, comf):
    '''
    Create a new row of data randomized according to uniform distribution, for all 5 variables.
    nh: Expectation for number of students helped. float.
    cr: Expectation for crowd size. float.
    comp: Expectation for number of tutoring sessions completed. float.
    di: Expectation for difficulty of instruction. float.
    comf: Expectation for comfort level. float.

    Min value at 0, max value at 5.
    '''
    numHelped = int(max(min(np.random.poisson(nh), 5), 0))
    crowd = int(max(min(np.random.poisson(cr), 5), 0))
    completion = int(max(min(np.random.poisson(comp), 5), 0))
    difficulty = int(max(min(np.random.poisson(di), 5), 0))
    comfort = int(max(min(np.random.poisson(comf), 5), 0))
    return np.array([numHelped, crowd, completion, difficulty, comfort])


def createRandEntryUniform(nh, cr, comp, di, comf):
    '''
    Create a new row of data randomized according to uniform distribution, for all 5 variables.
    nh: range for number of students helped. Tuple: [min, max]
    cr: range for crowd size. Tuple: [min, max]
    comp: range for number of tutoring sessions completed. Tuple: [min, max]
    di: range for difficulty of instruction. Tuple: [min, max]
    comf: range for comfort level. Tuple: [min, max]
    '''
    numHelped = random.randint(nh[0], nh[1])
    crowd = random.randint(cr[0], cr[1])
    completion = random.randint(comp[0], comp[1])
    difficulty = random.randint(di[0], di[1])
    comfort = random.randint(comf[0], comf[1])
    return np.array([numHelped, crowd, completion, difficulty, comfort])


# Creates a new row of data (Normal distribution)
def createRandEntryNormal(nh, cr, comp, di, comf):
    '''
    Create a new row of data randomized according to normal distribution, for all 5 variables.
    nh: normal distribution parameters for number of students helped. Tuple: (mu, sigma)
    cr: normal distribution parameters for crowd size. Tuple: (mu, sigma)
    comp: normal distribution parameters for number of tutoring sessions completed. Tuple: (mu, sigma)
    di: normal distribution parameters for difficulty of instruction. Tuple: (mu, sigma)
    comf: normal distribution parameters for comfort level. Tuple: (mu, sigma)
    '''
    numHelped = int(max(min(random.normalvariate(nh[0], nh[1]), 5), 0))
    crowd = int(max(min(random.normalvariate(cr[0], cr[1]), 5), 0))
    completion = int(max(min(random.normalvariate(comp[0], comp[1]), 5), 0))
    difficulty = int(max(min(random.normalvariate(di[0], di[1]), 5), 0))
    comfort = int(max(min(random.normalvariate(comf[0], comf[1]), 5), 0))
    return np.array([numHelped, crowd, completion, difficulty, comfort])

# Generate dataset for both methods (Normal distribution)
def genDataPoisson(lam1, lam2, num_data_pts):
    '''
    lam1: the expecation for the first week.
    lam2: the mean for the second week.
    num_data_pts: the sample size of each week.

    Returns a tuple-- the first item is the data for the first week, and the second item is the data for the second week.
    '''
    week_1 = []
    week_2 = []
    week_1_params = lam1
    week_2_params = lam2
    for i in range(num_data_pts):
        numHelped = week_1_params
        crowd = week_1_params
        completion = week_1_params
        difficulty = week_1_params
        comfort = week_1_params
        week_1.append(createRandEntryPoisson(numHelped, crowd,
                                      completion, difficulty, comfort))
    for i in range(num_data_pts):
        numHelped = week_2_params
        crowd = week_2_params
        completion = week_2_params
        difficulty = week_2_params
        comfort = week_2_params
        week_2.append(createRandEntryPoisson(numHelped, crowd,
                                      completion, difficulty, comfort))
    return np.array(week_1), np.array(week_2)


# Generate dataset for both methods (Normal distribution)
def genDataNormal(mu1, sigma1, mu2, sigma2, num_data_pts):
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
        week_1.append(createRandEntryNormal(numHelped, crowd,
                                      completion, difficulty, comfort))
    for i in range(num_data_pts):
        numHelped = week_2_params
        crowd = week_2_params
        completion = week_2_params
        difficulty = week_2_params
        comfort = week_2_params
        week_2.append(createRandEntryNormal(numHelped, crowd,
                                      completion, difficulty, comfort))
    return np.array(week_1), np.array(week_2)

# Generate dataset for both methods (Uniform distribution)
def genDataUniform(min1, max1, min2, max2, num_data_pts):
    '''
    min1: the lowerbound of the first method.
    max1: the upperbound of the first method.
    min2: the lowerbound of the second method.
    max2: the upperbound of the second method.
    num_data_pts: the sample size of each week.

    Returns a tuple-- the first item is the data for the first week, and the second item is the data for the second week.
    '''
    week_1 = []
    week_2 = []
    week_1_params = [min1, max1]
    week_2_params = [min2, max2]
    for i in range(num_data_pts):
        numHelped = week_1_params
        crowd = week_1_params
        completion = week_1_params
        difficulty = week_1_params
        comfort = week_1_params
        week_1.append(createRandEntryUniform(numHelped, crowd,
                                             completion, difficulty, comfort))
    for i in range(num_data_pts):
        numHelped = week_2_params
        crowd = week_2_params
        completion = week_2_params
        difficulty = week_2_params
        comfort = week_2_params
        week_2.append(createRandEntryUniform(numHelped, crowd,
                                             completion, difficulty, comfort))
    return np.array(week_1), np.array(week_2)



def noCorrelation(num_data_pts, distribution):
    '''
    Generate a dataset with the same mean, variance for both weeks. They are both centered around 2.5, with a standard 
    deviation of 0.833, so that 97% is at 5.
    '''
    if distribution  == 'normal':
        return genDataNormal(2.5, 0.833, 2.5, 0.833, num_data_pts)
    elif distribution == 'uniform':
        return genDataUniform(0, 5, 0, 5, num_data_pts)
    elif distribution == 'poisson':
        return genDataPoisson(2.5, 2.5, num_data_pts)


def positiveCorrelation(num_data_pts, distribution):
    '''
    Generate a dataset where the first week is centered at 2.5, and std. deviation of 0.833. 
    Second week is centered at 4, with a std. deviation of 0.333.
    '''
    if distribution  == 'normal':
        return genDataNormal(2.5, 0.833, 4, 0.333, num_data_pts)
    elif distribution == 'uniform':
        return genDataUniform(0, 4, 1, 5, num_data_pts)
    elif distribution == 'poisson':
        return genDataPoisson(2.5, 4, num_data_pts)

def veryPositiveCorrelation(num_data_pts, distribution):
    '''
    Generate a dataset where the first week is centered at 1, and std. deviation of 0.333. 
    Second week is centered at 4, with a std. deviation of 0.333.
    '''
    if distribution  == 'normal':
        return genDataNormal(1, 0.333, 4, 0.333, num_data_pts)
    elif distribution == 'uniform':
        return genDataUniform(0, 3, 2, 5, num_data_pts)
    elif distribution == 'poisson':
        return genDataPoisson(1, 4, num_data_pts)


def negativeCorrelation(num_data_pts, distribution):
    '''
    Generate a dataset where the first week is centered at 1, and std. deviation of 0.333. 
    Second week is centered at 2.5, with a std. deviation of 0.833.
    '''
    if distribution  == 'normal':
        return genDataNormal(2.5, 0.833, 1, 0.333, num_data_pts)
    elif distribution == 'uniform':
        return genDataUniform(1, 5, 0, 4, num_data_pts)
    elif distribution == 'poisson':
        return genDataPoisson(4, 2.5, num_data_pts)


def veryNegativeCorrelation(num_data_pts, distribution):
    '''
    Generate a dataset where the first week is centered at 4, with a std. deviation of 0.333.
    Second week is centered at 1, and std. deviation of 0.333. 
    '''
    if distribution  == 'normal':
        return genDataNormal(4, 0.333, 1, 0.333, num_data_pts)
    elif distribution == 'uniform':
        return genDataUniform(2, 5, 0, 3, num_data_pts)
    elif distribution == 'poisson':
        return genDataPoisson(4, 1, num_data_pts)


def writeToCSV(filename, week_1, week_2):
    '''
    Write datasets to two files, named <filename>_week_1, and <filename>_week_2. 
    '''
    with open('{0}_week_1'.format(filename), 'w') as f:
        fieldnames = ['numHelped', 'crowdSize', 'sessionsCompleted', 'difficulty', 'comfort']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for data_point in week_1:
            csv_writer.writerow({
                'numHelped': data_point[0],
                'crowdSize': data_point[1],
                'sessionsCompleted': data_point[2],
                'difficulty': data_point[3],
                'comfort': data_point[4],
            })

    with open('{0}_week_2'.format(filename), 'w') as f:
        fieldnames = ['numHelped', 'crowdSize', 'sessionsCompleted', 'difficulty', 'comfort']
        csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
        csv_writer.writeheader()
        for data_point in week_2:
            csv_writer.writerow({
                'numHelped': data_point[0],
                'crowdSize': data_point[1],
                'sessionsCompleted': data_point[2],
                'difficulty': data_point[3],
                'comfort': data_point[4],
            })



for distribution in ['normal', 'uniform', 'poisson']:
    week_1, week_2 = noCorrelation(30, distribution)
    writeToCSV('./sample_data/{}/no_correlation'.format(distribution), week_1, week_2)

    week_1, week_2 = positiveCorrelation(30, distribution)
    writeToCSV('./sample_data/{}/pos_correlation'.format(distribution), week_1, week_2)

    week_1, week_2 = negativeCorrelation(30, distribution)
    writeToCSV('./sample_data/{}/neg_correlation'.format(distribution), week_1, week_2)
