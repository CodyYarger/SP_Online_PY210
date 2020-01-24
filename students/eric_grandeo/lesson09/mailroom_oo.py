#!/usr/bin/env python3

from collections import OrderedDict

#hold all information about a single donor, including thank you letter, donation and donation history
class Donor:
    def __init__(self, name, donations=[]):
        self.name = name
        self.donations = donations

    @property
    def donor(self):
        return {self.name: self.donations}
    
    def add_donation(self, donation=[]):
        self.donations.extend(donation)  

    @property    
    def sum_donations(self):
        self._sum_donations = sum(self.donations)
        return self._sum_donations

    @property
    def num_donations(self):
        self._num_donations = len(self.donations)
        return self._num_donations

    @property
    def avg_donations(self):
        self._avg_donations = self.sum_donations/self.num_donations
        return self._avg_donations

    @property
    def thank_you_letter(self):
        email_dict = dict(name=self.name, donation=int(self.donations[-1]))

        result = """
        Dear {name},
        Thank you very much for the generous donation of ${donation:,.2f}
        It is very much appreciated.
        Respectfully,

        Eric G.
        """.format(**email_dict)

        return result
    
    

#hold all of the donor objects, method to add a new donor, search for a donor, 
#save and reload data, generate reports
class DonorCollection:
    def __init__(self):
        self.donor_list = []

    def add_donor(self, name, amount):

        for donors in self.donor_list:
            if donors.name == name:
                donors.add_donation(amount)
                return
        
        new_donor = Donor(name, amount)
        self.donor_list.append(new_donor)

    @property
    def donor_names(self):
        donor_name = []
        for donor in self.donor_list:
            donor_name.append(donor.name)
        return donor_name

    @property
    def donor_dict(self):
        donor_dict = {}
        for donor in self.donor_list:
            donor_dict.update(donor.donor)
        return donor_dict

    
    def donor_data(self, name):
        for donors in self.donor_list:
            if donors.name == name:
                return donors.donor


    def donor_obj(self, name):
        for donors in self.donor_list:
            if donors.name == name:
                return donors


    @property
    def report_data(self):
        report_data_dict = {}
        for donor in self.donor_list:
            temp_dict = {donor.name: [donor.sum_donations, donor.num_donations, donor.avg_donations]}
            report_data_dict.update(temp_dict)
        sorted_report_data_dict = OrderedDict(sorted(report_data_dict.items(), key=lambda t: t[1], reverse=True))
        return sorted_report_data_dict


    def generate_report(self, sorted_report_data_dict):
        header_row = ("{:<25s}|{:>15s} |{:>10s} | {:>12s}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
        dash_line = "-" * 68
        data_lines = ''
        
        for k,v in sorted_report_data_dict.items():
            data_lines += ("{:<25s}|${:>14,.2f} |{:>10.0f} |${:>12,.2f}".format(k, v[0], v[1], v[2])) + '\n'
        text_to_print = '\n' + header_row + '\n' + dash_line + '\n' + data_lines + '\n'
        return text_to_print


    


