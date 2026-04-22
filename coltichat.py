import pandas as pd

# Load your data into a DataFrame
df = pd.read_csv('colti_chatbot_data.csv')
#print(df)

print("Coltibot: Hello! I'm your car assistant. How can I help you today?")


while True:
    # Get user input and store the same into a variable
    user_input = input("\n You: ").lower()

    # check if the user wants to exit the chat
    if user_input == 'exit':
        print("Coltibot: Goodbye! Take care of your car!")
        break

    # Create a variable that will store the details structured in the csv file
    found_answer = False

    #come up with a loop that loops through the entire data frame created before
    for index, row in df.iterrows():
        # Clean up the keywords from the csv row
        keywords_list = str(row['Keywords']).split(',')

        # Below we check every keyword in that given row (Keywords)
        for word in keywords_list:
            clean_word = word.strip().lower()

            # If the keyword is inside of the users sentence
            if clean_word in user_input:
                print("Coltibot: " ,row['Response'])
                found_answer = True
                break   # stop looking for other keywords 

        if found_answer:
            break   # stop looking at other answers since we already found a match

    # If we went through the entire/whole csv file and we did not find any match of the keywords, we need to display a default message to the user 

    if not found_answer:
        print("Coltibot: I'm sorry, I don't have an answer for that. Please try asking something else or check your spelling.")    

