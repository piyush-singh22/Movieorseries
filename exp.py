from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

class MentalHealthApp(App):
    main_content = None  # Declare main_content as an instance variable
    responses = {}  # Dictionary to store user's responses
    question_index = 1  # Index to track the current question
    current_question_set = None
    questions = {
        # Student-related questions
        'below_18': {
            1: "How is your sleep?",
            2: "How is Your Appetite?",
            3: "How is your interest in doing your daily work?",
            4: "In the past year, are you drinking alocohol heavily or regularly?",
            5: "how often do you lose focus while performing the task",
            6: "is it difficult for you to stay organize ?",
            7: " is it hard for you to wait for your turn in conversation or activity",
            8: "how frequently do you interact others while they are speaking",
            9: "How often do you experience unwanted thoughts and images that you find difficult to control  ",
            10: "how frequently do you feel compelled to engage in repetive behaviours or actions due to this thoughts?",
            11: "do these obsessions or compulsions interfere with your daily life and causing stress ",
            12: "have you attempt to resist or supress the bad thoughts or compulsions but found it difficult to do so?",
            13: "have you experienced a traumatic evnet that continues to cause you distress or bad thoughts",
            14: "how often do you have nightmares or flashbacks related to traumatic events?",
            15: "do you try to avoid remainders related to the traumatic event?",
            16: "how frequently do you feel difficult sleeping or an exaggarated startle response?",
            17: "how often have you intentionaly harmed yourself physically in the past?",
            18: "have you ever considered to seriously consider harming yourself physically but didnt follow through?",
            19: "how often do you use self harm as a way to cope with emotional pain or distress",
            20: "do you have a plan for self harm or a history of suicidal thoughts"
        },
        # Non-student questions
        '18_to_35': {
            1: "How is your sleep?",
            2: "How is Your Appetite?",
            3: "How is your interest in doing your daily work?",
            4: "In the past year, are you drinking alocohol heavily or regularly?",
            5: "In the past year, are you not getting sleep without alcohol?",
            6: "in the past year, are you getting shaking of hand / body whenever you reduce or stop alcohol?",
            7: " Do you use Beedi/Cigarettes/Gutka or other tobacco products within one hour of getting up from bed in the early morning?",
            8: "In the past few weeks, did you get sudden attacks of fear or anxiety?",
            9: "you have tried to quit using tobacco but find it extremely difficult to stay tobacco-free?",
            10: "you often use tobacco in situations where I know it's not socially acceptable or allowed.?",
            11: "In the past few months, are you often getting tensed/stressed up with no reason or for small trivial reasons?",
            12: "In the past few months, are you unable to control or stop this tension?",
            13: "In the past few weeks, have you been feeling tired all the time?",
            14: "In the past few weeks, have you lost interest or pleasure in your regular daily activities?",
            15: "In the past few weeks, have you been feeling sad/depressed?",
            16: "in the past many months, does this patient have any physical symptoms (listed in diagnostic criterio of Somatization anorder) which is unexplainable with current medical knowledge or with depression/anxiety?",
            17: "In the past many months, has this patient shown signs of 'doctor shopping' (repeatedly consulting you or other doctors) for similar physical symptoms?",
            18: "In the past few weeks, has he/she been talking or smiling to self/hallucination?",
            19: "In the past few weeks, does he/she have poor self-care or wander aimlessly?",
            20:  "In the past few weeks, does he/she have suspiciousness, make big claims, or experience delusions?"




        },
        'above_35':{
            1: "How is your ?",
            2: "How is Your Appetite?",
            3: "How is your interest in doing your daily work?",
            4: "In the past year, are you drinking alocohol heavily or regularly?",
            5: "In the past year, are you not getting sleep without alcohol?",
            6: "in the past year, are you getting shaking of hand / body whenever you reduce or stop alcohol?",
            7: " Do you use Beedi/Cigarettes/Gutka or other tobacco products within one hour of getting up from bed in the early morning?",
            8: "In the past few weeks, did you get sudden attacks of fear or anxiety?",
            9: "you have tried to quit using tobacco but find it extremely difficult to stay tobacco-free?",
            10: "you often use tobacco in situations where I know it's not socially acceptable or allowed.?",
            11: "In the past few months, are you often getting tensed/stressed up with no reason or for small trivial reasons?",
            12: "In the past few months, are you unable to control or stop this tension?",
            13: "In the past few weeks, have you been feeling tired all the time?",
            14: "In the past few weeks, have you lost interest or pleasure in your regular daily activities?",
            15: "In the past few weeks, have you been feeling sad/depressed?",
            16: "in the past many months, does this patient have any physical symptoms (listed in diagnostic criterio of Somatization anorder) which is unexplainable with current medical knowledge or with depression/anxiety?",
            17: "In the past many months, has this patient shown signs of 'doctor shopping' (repeatedly consulting you or other doctors) for similar physical symptoms?",
            18: "In the past few weeks, has he/she been talking or smiling to self/hallucination?",
            19: "In the past few weeks, does he/she have poor self-care or wander aimlessly?",
            20: "In the past few weeks, does he/she have suspiciousness, make big claims, or experience delusions?"


        }
    }

    mental_health_problems = {
        "Schizophrenia": [1, 2, 4, 9, 11],
        "Bipolar Disorder": [3, 5, 7, 8],
        "Clinical Depression": [6, 10, 12, 13],
        "Stress": list(range(14, 19)),
        "Depression": list(range(14, 21)),
        "Borderline Personality Disorder (BPD)": [15, 21, 22]
    }

    addiction_levels = {
        "Safe": (0, 8),
        "Mild Addiction": (9, 13),
        "High Addiction": (14, float('inf'))
    }

    response_options = {
        1: "Never",
        2: "Rarely",
        3: "Sometimes",
        4: "Frequently"
    }

    def build(self):
        # Create the main user interface
        user_interface = self.create_user_interface()
        return user_interface

    def create_user_interface(self):

        user_interface = BoxLayout(orientation='vertical')

        # Top Section: Additional Options
        top_options = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        # Add the "more" button (aligned to the left)
        top_options.add_widget(Button(text='Home', on_press=self.home, size_hint=(0.3, 1)))
        # Create an empty box to push "more" button to the left
        left_space = BoxLayout(size_hint=(0.7, 1))
        top_options.add_widget(left_space)

        # Middle Section: Main Content
        self.main_content = Label(text='\" The mind is its own place and in itself, can make a heaven of hell, a hell of heaven \"', size_hint=(1, 0.6))

        # Text input for user responses (hidden initially)
        self.question_input = TextInput(hint_text='Enter your response here', size_hint=(1.0, 0.1), opacity=0)

        # Next button (hidden initially)
        self.next_button = Button(text='Next', on_press=self.show_questionnaire, size_hint=(0.1, 0.1), opacity=0)

        # Reset button (hidden initially)
        self.reset_button = Button(text='Reset', on_press=self.reset, size_hint=(0.1, 0.1), opacity=0)

        # Start Treatment button
        start_treatment_button = Button(text='Start Survey', on_press=self.start_treatment)

        # Show Location button
        show_location_button = Button(text='Show Specialist', on_press=self.show_location)

        # Bottom Section: Three Functionalities
        bottom_buttons = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        bottom_buttons.add_widget(start_treatment_button)
        bottom_buttons.add_widget(show_location_button)

        user_interface.add_widget(top_options)
        user_interface.add_widget(self.main_content)
        user_interface.add_widget(self.question_input)
        user_interface.add_widget(self.next_button)
        user_interface.add_widget(self.reset_button)
        user_interface.add_widget(bottom_buttons)

        return user_interface

    def start_treatment(self, instance):
        self.main_content.clear_widgets()
        self.main_content.text = ''

        # Show the input field and Next button
        self.question_input.opacity = 1
        self.next_button.opacity = 1
        self.reset_button.opacity = 1
        self.question_input.text = ''  # Clear the input field
        self.question_input.focus = True  # Set focus to the input field

        # Ask the initial question
        self.main_content.text = "What is your age ?"



    def show_questionnaire(self, instance):
        self.main_content.clear_widgets()
        self.main_content.text = ''

        # Get the user's age from the text input field
        age_input = self.question_input.text  # Adjust this based on your UI structure
        try:
            user_age = int(age_input)
        except ValueError:
            # Handle the case where the user enters an invalid age
            self.main_content.text = "Please enter a valid age."
            return

        if user_age < 18:
            self.current_question_set = 'below_18'
        elif 18 <= user_age <= 35:
            self.current_question_set = '18_to_35'
        else:
            self.current_question_set = 'above_35'

        if self.question_index in self.questions[self.current_question_set]:
            question = self.questions[self.current_question_set][self.question_index]
            response_text = f"{question}\n"
            response_text += "Select your response by entering the corresponding number:\n"

            for value, option in self.response_options.items():
                response_text += f"{value}: {option}\n"
            self.main_content.text = response_text

            # Increment the question index for the next question
            self.question_index += 1
        else:
            # User has completed the questionnaire, show responses
            self.reset_button.opacity = 1
            self.show_responses(instance)

    def calculate_total_score(self, responses):
        if self.current_question_set == 'below_18':
            # Calculate total score for users below 18
            score = sum(responses.values())
            if 0 <= score <= 8:
                self.main_content.text = "You are in the safe range."
            elif 8 < score <= 13:
                self.main_content.text = "You have a mild addiction."
            else:
                self.main_content.text = "You have a high addiction."
        else:
            # Calculate total score for users 18 and above
            potential_problems = ["Schizophrenia", "Bipolar Disorder", "Clinical Depression", "Stress", "Depression",
                                  "Borderline Personality Disorder (BPD)"]
            for problem, questions in self.mental_health_problems.items():
                if all(question in responses for question in questions):
                    potential_problems.append(problem)

            if not potential_problems:
                self.main_content.text = "No specific mental health problem detected."
            else:
                result_text = "You may have the following mental health problems:\n"
                for problem in potential_problems:
                    result_text += f"{problem}\n"
                result_text += "For more help, contact a doctor."
                self.main_content.text = result_text



    def convert_response_to_value(self, response):
        try:
            response = int(response)
            if response in self.response_options:
                return response
        except ValueError:
            pass
        return None

    def display_error(self):
        self.main_content.text = "Please enter a valid response (a number from 1 to 4)."

    def on_question_input(self, instance, value):
        response_value = self.convert_response_to_value(value)
        if response_value is not None:
            # Valid response, proceed to the next question
            self.responses[self.question_index] = response_value
            self.question_input.text = ''  # Clear the input field
            self.question_index += 1

            if self.question_index in self.questions[self.current_question_set]:
                question = self.questions[self.current_question_set][self.question_index]
                response_text = f"{question}\n"
                response_text += "Select your response by entering the corresponding number:\n"

                for value, option in self.response_options.items():
                    response_text += f"{value}: {option}\n"

                self.main_content.text = response_text
            else:
                # User has completed the questionnaire, show responses
                self.reset_button.opacity = 1
                self.show_responses(instance)
        else:
            # Invalid response, display an error message
            self.display_error()

    def show_responses(self, instance):
        # Calculate the sum of responses
        response_values = [self.convert_response_to_value(response) for response in self.responses.values()]
        response_sum = sum(response_values)

        # Determine the addiction level
        addiction_level = "Not categorized"
        for level, (lower, upper) in self.addiction_levels.items():
            if lower <= response_sum <= upper:
                addiction_level = level
                break

        # Display the results
        result_text = f"Your addiction level is: {addiction_level}\n"
        self.main_content.text = result_text

        # Additional information based on the addiction level
        if addiction_level == "High Addiction":
            result_text += "It is recommended to seek professional help."
        elif addiction_level == "Mild Addiction":
            result_text += "Consider making positive changes in your life to reduce addiction."
        elif addiction_level == "Safe":
            result_text += "You are in a safe range regarding addiction."

        self.main_content.text = result_text

    def reset(self, instance):
        # Clear existing content
        self.main_content.clear_widgets()

        # Reset the UI to the initial state
        self.question_index = 1
        self.responses = {}
        self.question_input.text = ''
        self.next_button.opacity = 0
        self.reset_button.opacity = 0
        self.question_input.opacity = 0

        # Start the survey again from the first question
        self.start_treatment(instance)

    def home(self, instance):
        # Clear existing content
        self.main_content.clear_widgets()

        self.main_content.text = '\"The mind is its own place and in itself, can make a heaven of hell, a hell of heaven\"'
        self.question_index = 1
        self.responses = {}
        self.question_input.text = ''
        self.next_button.opacity = 0
        self.reset_button.opacity = 0
        self.question_input.opacity = 0

    def show_location(self, instance):

        # Clear existing content
        self.main_content.clear_widgets()
        self.main_content.text = ''
        # Load the data from the CSV file or use sample data
        data = [
            ["Dr. Smith", "Psychiatrist", "123 Main St", "555-1234"],
            ["Dr. Johnson", "Psychologist", "456 Elm St", "555-5678"],
            # Add more rows as needed
        ]

        # Create a new GridLayout to display the data
        layout = GridLayout(cols=4, spacing=25, padding=20, size_hint_y=None)
        layout.bind(minimum_height=layout.setter('height'))

        # Create labels for the table header
        headers = ["Name", "Specialty", "Location", "Contact"]
        for header in headers:
            label = Label(text=header, bold=True, size_hint_x=None, width=200, halign='center')
            layout.add_widget(label)

        # Create labels for the data
        for row in data:
            for item in row:
                label = Label(text=item, size_hint_x=None, width=200, halign='center', padding_x=5)
                layout.add_widget(label)

        # Wrap the GridLayout in a ScrollView for scrolling if needed
        scroll_view = ScrollView(size_hint=(None, None), size=(400, 300), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        scroll_view.add_widget(layout)

        # Add the scroll_view to the main_content
        self.main_content.add_widget(scroll_view)


if __name__ == '__main__':
    MentalHealthApp().run()
