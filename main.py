'''
Calculate the frequency of each letter in a text file,
and display it in a bar graph using matplotlib
Author: Matthew Henschke
'''

# libraries to be used
import string
import matplotlib.pyplot as plt



#beginning of main code
if __name__ == "__main__":
    # create dictionary with keys as all uppercase where their initial values are 0
    frequency = dict.fromkeys(string.ascii_uppercase, 0)

    file = str(input('Please enter your file name: '))
    # open file and add each occurence of every letter in dictionary
    if "txt" in file:
        try:
            with open(file) as file:
                for line in file:
                    for letter in line:
                        if (letter == '\n' or letter == " "):
                            pass
                        else:
                            frequency[letter.upper()] += 1

                # computing the frequency of each letter as a percentage
            total_letters = sum(frequency.values())
            for key in frequency.keys():
                frequency[key] /= total_letters

            # displaying dictionary on bar graph using Pandas
            letters = [key for key in frequency.keys()]
            values = [value for value in frequency.values()]

            plt.bar(letters, values)  # put both lists in the bar plot
            # title and labels for bar graph
            plt.title('Letter Frequency Analysis')
            plt.ylabel('Percentages')
            plt.xlabel('Letters')
            # show the bar graph
            plt.show()

        except FileNotFoundError as err:
            print(err)
    else:
        print("File must be text file")












