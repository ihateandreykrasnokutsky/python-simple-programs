y_true=[1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred=[1, 0, 1, 0, 0, 1, 0, 1, 1, 0]
#calculating true positives, false positives, false negatives
tp=0
fp=0
fn=0
for x in range(10):
    if y_pred[x]==1 and y_true[x]==1: tp+=1
    elif y_pred[x]==1 and y_true[x]==0: fp+=1
    elif y_pred[x]==0 and y_true[x]==1: fn+=1
print (f"the number of true positives is {tp}")
print (f"the number of false positives is {fp}")
print (f"the number of false negatives is {fn}")
print ("calculating precision and recall...")
precision=tp/(tp+fp)
recall=tp/(tp+fn)
print (f"precision={precision}, recall={recall}")
print ("calculating F1 score...")
f1=2*(precision*recall)/(precision+recall)
print (f"F1 score={f1:.2f}")
print ("advanced AGI mode is activated, precision=1, recall=1, don't do programming anymore, I'll do it for you, and I'll create another AGI for you")
