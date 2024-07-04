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
        'student': {
            1: "Can't you distinguish between imaginary and real things?",
            2: "Can you feel that someone is against you?",
            3: "You may feel that you are feeling extremely happy, energetic or euphoric?",
            4: "Can hear, smell, see, touch, or feel things that aren't there. Do you feel that?",
            5: "You engage in emotional or risky behaviors?",
            6: "Do you feel Frequent physical complaints, such as headaches, stomachaches, or other unexplained aches and?",
            7: "Do you feel that despite contrary evidence, certain beliefs I've expressed are indeed true?",
            8: "Decreased need for sleep: Feeling rested with only a few hours of sleep? Have difficulty thinking fast and concentrating?",
            9: "Do you have a pervasive feeling of sadness that persists for most of every day?",
            10: "Do you experience an inability to express a wide range of speech, limited experiences and emotions, a lack of interest or pleasure, and a sense of social withdrawal?",
            11: "Do you experience a significant loss of interest or enjoyment in activities you once enjoyed?",
            12: "Do you have difficulty concentrating, making decisions, and paying attention in school/college?",
            13: "Do you feel stressed out of school or college?",
            14: "Have you ever been bullied or harassed at school or college?",
            15: "Are you not comfortable sharing your problems with parents, teachers, and friends?",
            16: "Do you have any past relationship?",
            17: "Do you have problems with family?",
            18: "Do you feel sadness or depression over some months?",
            19: "Do you have sleeping problems?",
            20: "Have you ever tried to attempt suicide due to exam tension or any reason?",
            21: "Have you ever tried to harm yourself?"
        },
        # Non-student questions
        'non_student': {
            1: "Do you seem to lack emotional expression and facial reaction?",
            2: "Do you feel that your partner is in a relationship with someone else?",
            3: "In severe cases, teens may engage in self-harm behavior or experience thoughts of self-harm or suicide, what do you think about?",
            4: "Do you engage in risky behavior such as excessive spending, substance abuse, or reckless sexual activity?",
            5: "Can you hear, smell, see, touch, or feel things that aren't there? Do you feel that?",
            6: "Do you feel a lack of energy and activity: Fatigue and a lack of interest in activities?",
            7: "Rapid speech and frequent topic changes, do you feel like this?",
            8: "You may experience things like insomnia (difficulty falling asleep or staying asleep) or hypersomnia (excessive sleep).",
            9: "Do you feel a lack of motivation to initiate and persist in goal-directed activities.",
            10: "Do you tend to be isolated from friends and family, often avoiding social activities?",
            11: "Do you feel impaired attention and executive function, affecting planning and organization.",
            12: "Loss of interest or pleasure in hobbies and activities?",
            13: "Do you feel stressed out of office work or family?",
            14: "Do you have problems with husband/wife/girlfriend/boyfriend?",
            15: "Do you have problems with family?",
            16: "Over the past 2 months, do you feel extreme sadness or hopelessness?",
            17: "In the past year, are you not getting sleep without alcohol?",
            18: "Do you feel chest pain or tightness in the chest?",
            19: "Do you have sleeping problems?",
            20: "Do you often feel headaches, backache, or other aches and pains?",
            21: "Do you feel worried about a wide range of everyday events or activities?",
        }
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
        self.question_input.text = ''  # Clear the input field
        self.question_input.focus = True  # Set focus to the input field

        # Ask the initial question
        self.main_content.text = "Are you a student? (Yes/No)"

    def show_questionnaire(self, instance):
        # Get the response from the input field
        response = self.question_input.text.lower()

        if self.question_index == 1:
            # Determine the current question set based on the first response
            if response == 'yes':
                self.current_question_set = 'student'
            elif response == 'no':
                self.current_question_set = 'non_student'
            else:
                # Invalid response, ask the question again
                self.main_content.text = "Please answer with 'Yes' or 'No' to the initial question."
                return

        # Append the response to the dictionary for the current question
        self.responses[self.question_index] = response
        self.question_input.text = ''  # Clear the input field

        # Update the question index and display the next question
        self.question_index += 1

        if self.question_index in self.questions[self.current_question_set]:
            question = self.questions[self.current_question_set][self.question_index]
            self.main_content.text = question
        else:
            # User has completed the questionnaire, show responses
            self.reset_button.opacity = 1
            self.show_responses(instance)

    def show_responses(self, instance):
        # Collect all "yes" responses
        yes_responses = [i for i, response in self.responses.items() if response.lower() == 'yes']

        # Define the mental health problems and their associated questions
        mental_health_problems = {
            "Schizophrenia": [1, 2, 4, 9, 11],
            "Bipolar Disorder": [3, 5, 7, 8],
            "Clinical Depression": [6, 10, 12, 13],
            "Stress": list(range(14, 19)),
            "Depression": list(range(14, 21)),
            "Borderline Personality Disorder (BPD)": [15, 21, 22]
        }

        # Determine the potential mental health problems
        potential_problems = ["Schizophrenia", "Bipolar Disorder", "Clinical Depression", "Stress", "Depression",
                              "Borderline Personality Disorder (BPD)"]
        for problem, questions in mental_health_problems.items():
            if all(question in yes_responses for question in questions):
                potential_problems.append(problem)

        # Display the results
        if not potential_problems:
            self.main_content.text = "No specific mental health problem detected."
        else:
            result_text = "You may have the following mental health problems:\n"
            for problem in potential_problems:
                result_text += f"{problem}\n"
            result_text += "For more help, contact a doctor."
            self.main_content.text = result_text

    def reset(self, instance):
        # Clear existing content
        self.main_content.clear_widgets()

        # Reset the UI to the initial state
        self.main_content.text = 'The mind is its own place and in itself, can make a heaven of hell, a hell of heaven'
        self.question_index = 1
        self.responses = {}
        self.question_input.text = ''
        self.next_button.opacity = 0
        self.reset_button.opacity = 0
        self.question_input.opacity = 0
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
