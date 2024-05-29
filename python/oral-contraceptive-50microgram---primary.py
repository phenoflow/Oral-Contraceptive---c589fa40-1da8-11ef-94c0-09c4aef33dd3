# Alison K Wright, Evangelos Kontopantelis, Richard Emsley, Ian Buchan, Mamas A Mamas, Naveed Sattar, Darren M Ashcroft, Martin M Rutter, 2024.

import sys, csv, re

codes = [{"code":"47132","system":"gprdproduct"},{"code":"1720","system":"gprdproduct"},{"code":"1348","system":"gprdproduct"},{"code":"443","system":"gprdproduct"},{"code":"5986","system":"gprdproduct"},{"code":"57748","system":"gprdproduct"},{"code":"23211","system":"gprdproduct"},{"code":"25263","system":"gprdproduct"},{"code":"55819","system":"gprdproduct"},{"code":"61465","system":"gprdproduct"},{"code":"2265","system":"gprdproduct"},{"code":"54527","system":"gprdproduct"},{"code":"68515","system":"gprdproduct"},{"code":"23218","system":"gprdproduct"},{"code":"61890","system":"gprdproduct"},{"code":"12631","system":"gprdproduct"},{"code":"59414","system":"gprdproduct"},{"code":"2769","system":"gprdproduct"},{"code":"1466","system":"gprdproduct"},{"code":"56732","system":"gprdproduct"},{"code":"2061","system":"gprdproduct"},{"code":"6431","system":"gprdproduct"},{"code":"61190","system":"gprdproduct"},{"code":"25124","system":"gprdproduct"},{"code":"1613","system":"gprdproduct"},{"code":"56103","system":"gprdproduct"},{"code":"38500","system":"gprdproduct"},{"code":"40650","system":"gprdproduct"},{"code":"54800","system":"gprdproduct"},{"code":"239","system":"gprdproduct"},{"code":"47057","system":"gprdproduct"},{"code":"48570","system":"gprdproduct"},{"code":"58485","system":"gprdproduct"},{"code":"45059","system":"gprdproduct"},{"code":"13810","system":"gprdproduct"},{"code":"10201","system":"gprdproduct"},{"code":"2553","system":"gprdproduct"},{"code":"19131","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('oral-contraceptive-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["oral-contraceptive-50microgram---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["oral-contraceptive-50microgram---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["oral-contraceptive-50microgram---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
