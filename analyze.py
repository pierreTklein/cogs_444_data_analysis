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
