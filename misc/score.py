def evaluate(solution,prediction):
    if str(type(solution)) == "<class 'pandas.core.frame.DataFrame'>":
        solution = pandastolist(solution)
        
    solution = np.asarray(solution)
    prediction = np.asarray(prediction)
    ones = np.ones_like(solution)
    score = 0
    if (len(solution)!=len(prediction)):
        print("the length of the prediction list must be equal to: "+str(len(solution))+"instead of :"+str(len(prediction)))
        return score
    else:
        TP = float(np.dot((solution + ones),(prediction + ones)))/4.0
        nb_pos = float(np.sum(((solution + ones)/2)))
        TN = float(np.dot((ones-solution),(ones-prediction)))/4.0
        nb_neg = float(len(solution) - nb_pos)
        score = 0.5*(TP/nb_pos + TN/nb_neg)
        return score