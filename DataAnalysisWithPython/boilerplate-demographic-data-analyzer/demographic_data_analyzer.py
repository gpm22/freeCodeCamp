import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    #print(race_count)

    # What is the average age of men?

    men = df[df['sex']=='Male']
    #print(men)
    average_age_men = round(men['age'].mean(),1)

    #print(average_age_men)

    # What is the percentage of people who have a Bachelor's degree?
    
    percentage_bachelors = round(df['education'].value_counts(normalize=True)['Bachelors']*100,1)


    #print(percentage_bachelors)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate
    
    #print(BMD_rich)

    #print(BMD_total)

    #higher_education = round(BMD_rich/BMD_total*100, 1)

    #print(higher_education)

    education = df['education'].value_counts()
    BMD_total = education['Bachelors']+education['Masters']+education['Doctorate']

    education_rich = df[df['salary'] == '>50K']['education'].value_counts()

    BMD_rich = education_rich['Bachelors']+education_rich['Masters']+education_rich['Doctorate']
    rest_total = education.sum() - BMD_total
    rest_rich = education_rich.sum() - BMD_rich

    #lower_education = round(rest_rich/rest_total*100, 1)

    #print(lower_education)

    # percentage with salary >50K
    higher_education_rich = round(BMD_rich/BMD_total*100, 1)
    lower_education_rich = round(rest_rich/rest_total*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    #print(min_work_hours)   

    #print(df.columns)

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K? 

    num_min_workers = df[df['hours-per-week']==min_work_hours]  

    rich_percentage = round(num_min_workers['salary'].value_counts(normalize = True)['>50K']*100,1)
    #num_min_workers[num_min_workers['salary']=='>50K'].()

    #print(rich_percentage)


    # What country has the highest percentage of people that earn >50K?
    countries_richs = df[df['salary']=='>50K']['native-country'].value_counts()

    countries_total = df['native-country'].value_counts()

    countries_percentage = countries_richs/countries_total


    highest_earning_country = countries_percentage.idxmax()

    #print(highest_earning_country)

    highest_earning_country_percentage = round(countries_percentage[highest_earning_country]*100, 1)

    #print(highest_earning_country_percentage)

    # Identify the most popular occupation for those who earn >50K in India.

    Indians = df[df['native-country'] == 'India']
    
    Indians_rich = Indians[Indians['salary'] == '>50K']

    #print(Indians)
    
    top_IN_occupation = Indians_rich['occupation'].value_counts().idxmax()

    #print(top_IN_occupation)

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
