import unicodecsv
import datetime

enrollments_filename = 'enrollments.csv'

## Longer version of code (replaced with shorter, equivalent version below)

# enrollments = []
# f = open(enrollments_filename, 'rb')
# reader = unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
# f.close()

with open(enrollments_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
### Write code similar to the above to load the engagement
### and submission data. The data is stored in files with
### the given filenames. Then print the first row of each
### table to make sure that your code works. You can use the
### "Test Run" button to see the output of your code.

engagement_filename = 'daily_engagement.csv'
submissions_filename = 'project_submissions.csv'

with open(engagement_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)

with open(submissions_filename, 'rb') as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)

#print(daily_engagement[0])

#print(project_submissions[0])


### 

len(enrollments)

unique_enrolled_students = set()
for enrollment in enrollments:
    unique_enrolled_students.add(enrollment['account_key'])
len(unique_enrolled_students)

len(daily_engagement)
unique_engagement_students = set()
for engagement_record in daily_engagement:
    unique_engagement_students.add(engagement_record['account_key'])
len(unique_engagement_students)

#print(daily_engagement[0]['account_key'])

len(project_submissions)
unique_project_submitters = set()
for submission in project_submissions:
    unique_project_submitters.add(submission['account_key'])
len(unique_project_submitters)


###########
def to_date (day):
	if day == '':
		return None
	return datetime.datetime.strptime(day, '%Y-%m-%d')

def to_int (days):
	if days =='':
		return None
	return int(days)

surprising = 0
enrolled_at_least_1_day = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if student not in unique_engagement_students:
        surprising += 1
        days_to_cancel = to_int(enrollment['days_to_cancel'])
        if days_to_cancel == None or days_to_cancel>0:
        	enrolled_at_least_1_day += 1
        #print(enrollment)
        #break

#print(surprising)
#print(enrolled_at_least_1_day)

############

paid_students = {}
for enrollment in enrollments:
    key = enrollment['account_key']
    value = enrollment['join_date']
    dtc = to_int(enrollment['days_to_cancel'])

    if dtc == None or dtc>7:
        paid_students[key] = value

#print(paid_students['448'])
#print(len(paid_students))

#########

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)

print (len(paid_enrollments))
print (len(paid_engagement))
print (len(paid_submissions))

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print(len(paid_engagement_in_first_week))