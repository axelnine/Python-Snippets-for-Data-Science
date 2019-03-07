def metrics(predicted_values, test_values):
    '''
    This function takes in two lists/arrays
    
    predicted_values: List of values predicted by model
    test_values: List of actual values
    
    It outputs a printed list of metrics like accuracy, precision, recall and f1-score
    
    The function can be modified to return variables instead of printing the outputs
    
    '''
    predicted_values = np.array(predicted_values)
    test_values = np.array(test_values)
    true_positives,true_negatives,false_positives,false_negatives = 0,0,0,0
    
    for i in range(0,len(predicted_values)):
        if (predicted_values[i] == 0 and test_values[i] == 0):
            true_negatives = true_negatives + 1
        elif (predicted_values[i] == 1 and test_values[i] == 1):
            true_positives = true_positives + 1
        elif (predicted_values[i] == 1 and test_values[i] == 0):
            false_positives = false_positives + 1
        else:
            false_negatives = false_negatives + 1
        
    
    accuracy = 100*(true_positives + true_negatives) / (true_positives + true_negatives + false_positives + false_negatives) 
    precision = 100*true_positives / (true_positives + false_positives)
    recall = 100*true_positives / (true_positives + false_negatives)
    f1_score = 2*precision*recall / (precision+recall)
    
    print("Results:\n----------------------------")
    print("Accuracy:", round(accuracy,2), "%")
    print("Precision:", round(precision,2), "%")
    print("Recall:", round(recall,2), "%")
    print("F1 Score:", round(f1_score,2), "%")   

    return None
