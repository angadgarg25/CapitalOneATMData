import csv

def load(ids,lats,longs,deposits,times):
    #All arguments must be arrays of equal length containing respective data
    headers = ['id','lat','long','deposit','timestamp']
    with open('purchase_data.csv','w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for i in range(len(ids)):
            writer.writerow({'id': ids[i],'lat': lats[i],'long': longs[i],'deposit': deposits[i],'timestamp': times[i]})
