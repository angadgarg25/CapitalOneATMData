import csv

def load(ids,lats,longs,prices,times):
    #All arguments must be arrays of equal length containing respective data
    headers = ['id','lat','long','price','timestamp']
    with open('purchase_data.csv','w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for i in range(len(ids)):
            writer.writerow({'id': ids[i],'lat': lats[i],'long': longs[i],'price': prices[i],'timestamp': times[i]})
