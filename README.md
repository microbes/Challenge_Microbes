# Challenge_Microbes

##Background
Diabetes will be the seventh most common cause of death in 2030, according to the World Health Organization. In 2014, global prevalence of diabetes was estimated to be more than 9%  among adults aged 18+ years. If most hospitals have the necessary medical equipment to treat this disease, some do not have these means.

In this case, the evaluation of hospital stay is an important point to consider. From the patient point of view, it is important to know the length of the stay for cost reasons, and from the hospital point of view, there is various staff, drugs and patient rooms to optimize. Moreover it is well known that a long stay in a hospital can lead to nosocomial pathologies.

Using patient pathologies and their respective diagnoses, predicting the duration of the stay would allow to enhance the hospital organization (in term of staff, room, drugs,...)

With this competition, MicroBES is asking you to join their mission to help hospital with restricted equipment to be more efficient in their organization. Given a dataset of de-identified hospitalization records your challenge is to predict the patient stay, making diabetes treatment more efficient and, ideally, reducing the number of people dying from it.

##Material and method
Data description : The data used in this challenge, is submitted on the behalf of the Center for Clinical and Translational Research, Virginia Commonwealth University. It represents 10 years (1998-2008) of clinical care at 130 US hospitals. The dataset includes 50 features representing patient and hospital outcomes.

Task description : The task is a binary classification problem. Using the train set, it consists in predicting the length of stay for a patient given its diagnosis and its medications. This label consists in two categories : a stay inferior to 7 days or a stay greater or equal to 7 days.

Data Quantity: The data contains 50 attributes such as  patient number, race, gender, age, admission type, number of lab tests performed, etc. And a total of 101766 distinct examples. There’s a total of 4.9% of missing data that needs to be processed. The attributes values are represented either by numerical, boolean or nominal values.

Preprocessing: in order to proceed with the features selection, we’ve firsted start by counting the % of missing data of each attributes, and then deleted the attributes : weight, payer_code, medical_specialty that have respectively : 97%, 53% ,52% of missing data. Other attributes that are irrelevant and need to be deleted are : encounter_id, and patient_nbr.

The original value to predict (length of stay) consisted in the length of the stay in hospital in days. We decided to divide it into two categories :a stay inferior to 7 days or a stay greater or equal to 7 days. Here, we can see in the first plot the number of patients for every length of stay in the original database, the second one shows the distribution after the transformation.
