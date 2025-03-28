import re
import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--language', type=str, help='The programming language')
    args = parser.parse_args()
    
    with open(args.language + '-dump.html', 'r') as file:
        data = file.read()
        
        # find all the exercise names in https://assets.exercism.org/exercises/resistor-color.svg
        # the exercise names are in the format of "resistor-color"
        exercise_names = re.findall(r'(?<=exercises/)([^.]*)(?=.svg)', data)
        print(exercise_names)

        # renmove duplicates
        exercise_names = list(set(exercise_names))
        print("there are", len(exercise_names), "exercises")


        # write the exercise names to a file
        with open(args.language + '-exercise-names.txt', 'w') as file:
            for name in exercise_names:
                file.write(name + '\n')

        # excecute a shell command 
        for i, name in enumerate(exercise_names):
            os.system(f'exercism download --track={args.language} --exercise={name}')
            os.system('wait')
            # if i == 0:
            #     break

if __name__ == '__main__':
    main()