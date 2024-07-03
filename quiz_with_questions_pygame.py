import pygame
import sys

pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('General Knowledge Quiz')

font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 48)

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

questions = [
    {
        "question": "What is the highest waterfall in the world?",
        "options": ["a) Niagara Falls", "b) Victoria Falls", "c) Angel Falls"],
        "correct": "c"
    },
    {
        "question": "What is the capital of America?",
        "options": ["a) Los Angeles", "b) Washington DC", "c) Chicago"],
        "correct": "b"
    },
    {
        "question": "The Copacabana neighborhood in Brazil is famous for?",
        "options": ["a) Beaches", "b) Festivals", "c) Markets"],
        "correct": "a"
    },
    {
        "question": "What is the name of the pirate flag?",
        "options": ["a) Jolly Roger", "b) Grumpy Codger"],
        "correct": "a"
    },
    {
        "question": "Who built the Acropolis in Athens?",
        "options": ["a) The Romans", "b) The Saxons", "c) The Ancient Greeks"],
        "correct": "c"
    },
    {
        "question": "What are the 'ships of the desert' called?",
        "options": ["a) Camels", "b) Jeep", "c) Pernopter"],
        "correct": "a"
    },
    {
        "question": "On how many hills was Rome built?",
        "options": ["a) Five", "b) Six", "c) Seven"],
        "correct": "c"
    },
    {
        "question": "Which of these Roman emperors was known as 'Divine Caesar'?",
        "options": ["a) Augustus", "b) Nero", "c) Trajan"],
        "correct": "c"
    },
    {
        "question": "What is the name of the famous basilica in Rome, known for its imposing dome?",
        "options": ["a) San Marco", "b) San Giovanni", "c) San Pietro"],
        "correct": "c"
    },
    {
        "question": "Who was the Roman general known for crossing the Alps during the Second Punic War?",
        "options": ["a) Scipio Africanus", "b) Julius Caesar", "c) Hannibal"],
        "correct": "c"
    },
    {
        "question": "Which of these events marked the end of the Roman Republic and the beginning of the Roman Empire?",
        "options": ["a) Assassination of Caligula", "b) Battle of Actium", "c) Declaration of Augustus as 'first citizen'"],
        "correct": "c"
    },
    {
        "question": "What is the name of the hill in Rome where the Capitoline Hill, one of the most important religious and political centers of the ancient city, is located?",
        "options": ["a) Palatine", "b) Aventine", "c) Capitol"],
        "correct": "c"
    },
    {
        "question": "What was the name of the Roman emperor known for codifying imperial laws into a coherent and uniform system?",
        "options": ["a) Justinian", "b) Constantine", "c) Diocletian"],
        "correct": "c"
    },
    {
        "question": "What is the name of the famous Roman circus, known for chariot races and other public spectacles?",
        "options": ["a) Circus Maximus", "b) Colosseum", "c) Pantheon"],
        "correct": "a"
    },
    {
        "question": "What was the name of the first empress of Rome, wife of Claudius and mother of Nero?",
        "options": ["a) Livia", "b) Agrippina", "c) Messalina"],
        "correct": "b"
    },
    {
        "question": "Who was the Roman general known for the conquest of Britain in 43 AD?",
        "options": ["a) Vespasian", "b) Hadrian", "c) Claudius"],
        "correct": "c"
    }
]

current_question = 0
score = 0
total_questions = len(questions)
max_wrong_answers = 3  
wrong_answers = 0 

question_time = 30
time_left = question_time
start_time = pygame.time.get_ticks()

def display_message(text, font, color, center):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=center)
    screen.blit(text_surface, text_rect)

def main():
    global current_question, score, time_left, start_time, wrong_answers
    running = True
    while running:
        screen.fill(white)
        
        if current_question < total_questions and wrong_answers < max_wrong_answers:

            question = questions[current_question]
            display_message(question["question"], big_font, black, (screen_width // 2, 100))

            for i, option in enumerate(question["options"]):
                display_message(option, font, blue, (screen_width // 2, 200 + i * 40))

            elapsed_time = (pygame.time.get_ticks() - start_time) / 1000
            time_left = max(question_time - elapsed_time, 0)

            if time_left < 10:
                time_color = red
            else:
                time_color = black
            display_message(f"Time left: {int(time_left)} seconds", font, time_color, (screen_width // 2, 600))

            if time_left <= 0:
                wrong_answers += 1
                current_question += 1
                start_time = pygame.time.get_ticks()
                continue

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        answer = 'a'
                    elif event.key == pygame.K_b:
                        answer = 'b'
                    elif event.key == pygame.K_c:
                        answer = 'c'
                    else:
                        answer = ''
                    
                    if answer == question["correct"]:
                        score += 1
                    else:
                        wrong_answers += 1
                    current_question += 1
                    start_time = pygame.time.get_ticks()

            if wrong_answers >= max_wrong_answers:
                running = False

        else:
            if wrong_answers >= max_wrong_answers:
                display_message("Game Over", big_font, black, (screen_width // 2, 200))
            else:
                display_message("You answered correctly to " + str(score) + " questions!", big_font, black, (screen_width // 2, 200))
                display_message("You scored " + str(score / total_questions * 100) + "%.", big_font, black, (screen_width // 2, 300))
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
