import csv

def load(input):
    #All arguments must be arrays of equal length containing respective data
    headers = ['id','lat','long','deposit','timestamp']
    with open('purchase_data.csv','w') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for i in range(len(ids)):
            writer.writerow({'id': input[i][0],'lat': input[i][1],'long': input[i][2],'deposit': input[i][3],'timestamp': input[i][4]})
