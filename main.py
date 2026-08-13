import os #this allows me to clear the screen
import random #this picks random elements of a list
from colorama import Fore #I can change the color of text
import time #This is my equivalent of a wait block
flashcard_archive = [] #the wielder of all flashcards
archive_count = 0 #this counts the number of flashcards 
index = 0 #index variable represents the index of the list
incorrect_writing = 0 #variable

class flashcard: # class for flashcards
  def __init__(self, name, definition):
    self.name = name #name of flashcard goes here
    self.definition = definition #definition of flashcard goes here

def create_flashcard(): #function to create a flashcard
  name = input("Enter vocab word: ")
  if name == "l":
    home()
  definition = input("Enter definition: ")
  if definition == "l":
    home()
  new_flashcard = flashcard(name, definition)
  flashcard_archive.append(new_flashcard)
  os.system("clear")
  print("F L A S H C A R D S", "\n")
  print("Flashcard created.")
  global archive_count
  archive_count += 1

def home(): #function that recalls home screen
  os.system("clear")
  print("F L A S H C A R D S", "\n")
  print(Fore.WHITE + "(" + Fore.RED + "1" + Fore.WHITE + ")",   Fore.BLUE, "Create")
  print(Fore.WHITE + "(" + Fore.RED + "2" + Fore.WHITE + ")",   Fore.LIGHTMAGENTA_EX, "View all flashcards", Fore.WHITE)
  print(Fore.WHITE + "(" + Fore.RED + "3" + Fore.WHITE + ")", Fore.LIGHTGREEN_EX, "Study", Fore.WHITE, "\n")
  action = input("")

  def enter_home():
    print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
    ENTER = input("")
    if ENTER == "":
      os.system("clear")
      home()
  
  if action == "1": #create flashcard
    os.system("clear")
    
    print("F L A S H C A R D S", "\n")
    create_flashcard()
    enter_home()
  
  elif action == "2": #view flashcard
    os.system("clear")
    print("F L A S H C A R D S", "\n")
    global index
    while index < archive_count:
      print(index + 1)
      print(flashcard_archive[index].name)
      print(flashcard_archive[index].definition)
      print("")
      index += 1
    index = 0
    enter_home()
  elif action == "3": #study flashcard
    os.system("clear")
    print("F L A S H C A R D S", "\n")
    print(Fore.WHITE + "(" + Fore.RED + "1" + Fore.WHITE + ")",   Fore.GREEN, "Multiple Choice")
    print(Fore.WHITE + "(" + Fore.RED + "2" + Fore.WHITE + ")",   Fore.LIGHTYELLOW_EX, "Writing")
    print(Fore.WHITE + "(" + Fore.RED + "3" + Fore.WHITE + ")",   Fore.RED, "Test", Fore.WHITE)
    print("")
    study_action = input("")
    if study_action == "1" and archive_count >= 4: # determines if there is enough flashcards to study in multiple choice
      os.system("clear")
      print("F L A S H C A R D S", "\n")
      print("The definition will be shown and select the correct answer out of the few. Must have 4 flashcards or more.")
      print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
      print("Enter (" + Fore.RED + "l" + Fore.WHITE + ") at any time to leave.")
      print("")
      def multiple_choice(): #function for multiple choice
        os.system("clear")
        print("F L A S H C A R D S", "\n")
        study_flashcard_archive = flashcard_archive.copy()
      
        study_flashcard = random.choice(flashcard_archive)
        study_flashcard_archive.remove(study_flashcard)

        study_flashcard2 = random.choice(study_flashcard_archive)
        study_flashcard_archive.remove(study_flashcard2)
  
        study_flashcard3 = random.choice(study_flashcard_archive)
        study_flashcard_archive.remove(study_flashcard3)
        
        study_flashcard4 = random.choice(study_flashcard_archive)
        study_flashcard_archive.remove(study_flashcard4)
    
        correct_study_flashcard_MC = random.choice([study_flashcard, study_flashcard2, study_flashcard3, study_flashcard4])

        def MC_repeat(): #function to repeat multiple choice
          os.system("clear")
          print("F L A S H C A R D S", "\n")
          print(correct_study_flashcard_MC.definition)
          print("")
          print(Fore.WHITE + "(" + Fore.RED + "1" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard.name)
          print(Fore.WHITE + "(" + Fore.RED + "2" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard2.name)
          print(Fore.WHITE + "(" + Fore.RED + "3" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard3.name)
          print(Fore.WHITE + "(" + Fore.RED + "4" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard4.name + Fore.WHITE)
 
          study_guess_MC = input("") #guessing input
          if study_guess_MC == "1" and study_flashcard == correct_study_flashcard_MC:
            print("Correct! ")
            print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
            ENTER = input("")
            if ENTER == "":
              multiple_choice()
            elif ENTER == "l":
              home()
          elif study_guess_MC == "1" and study_flashcard != correct_study_flashcard_MC:
            print("Incorrect.")
            time.sleep(1) #wait block for 1 second
            MC_repeat()
  
          elif study_guess_MC == "2" and study_flashcard2 == correct_study_flashcard_MC:
            print("Correct! ")
            print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
            ENTER = input("")
            if ENTER == "":
              multiple_choice()
            elif ENTER == "l":
              home()
          elif study_guess_MC == "2" and study_flashcard2 != correct_study_flashcard_MC:
            print("Incorrect.")
            time.sleep(1)
            MC_repeat()
      
        
          elif study_guess_MC == "3" and study_flashcard3 == correct_study_flashcard_MC:
            print("Correct! ")
            print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
            ENTER = input("")
            if ENTER == "":
              multiple_choice()
            elif ENTER == "l":
              home()
          elif study_guess_MC == "3" and study_flashcard3 != correct_study_flashcard_MC:
            print("Incorrect.")
            time.sleep(1)
            MC_repeat()
      
          elif study_guess_MC == "4" and study_flashcard4 == correct_study_flashcard_MC:
            print("Correct! ")
            print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
            ENTER = input("")
            if ENTER == "":
              multiple_choice()
            elif ENTER == "l":
              home()
          elif study_guess_MC == "4" and study_flashcard4 != correct_study_flashcard_MC:
            print("Incorrect.")
            time.sleep(1)
            MC_repeat()
          elif study_guess_MC == "l":
            home()
        MC_repeat()
        ENTER = input("")
        if ENTER == "":
          multiple_choice()
      ENTER = input("")
      if ENTER == "":
        multiple_choice()
    elif archive_count < 4:
        print("You need", Fore.LIGHTMAGENTA_EX , 4-archive_count, Fore.WHITE, "more flashcards.")
        print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
        ENTER = input("")
        if ENTER == "":
          home()
      
    elif study_action == "2":
      os.system("clear")
      print("F L A S H C A R D S", "\n")
      print("The definition will be shown and type the corresponding word.")
      print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
      print("Enter (" + Fore.RED + "l" + Fore.WHITE + ") at any time to leave.")
      print("")
      def writing():
        os.system("clear")
        print("F L A S H C A R D S", "\n")
        correct_study_flashcard_writing = random.choice(flashcard_archive)
        def writing_repeat():
          os.system("clear")
          print("F L A S H C A R D S", "\n")
          print("Enter (" + Fore.CYAN + "q" + Fore.WHITE + ") to skip question.", "\n")
          print(correct_study_flashcard_writing.definition)
          writing_guess = input("")
          if writing_guess == correct_study_flashcard_writing.name:
            print("correct!")
            print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
            writing_guess = ""
            ENTER = input("")
            if ENTER == "":       
              writing_guess = ""
              writing()
            elif ENTER == "l":
              home()
          elif writing_guess == "l":
            home()
          elif writing_guess == "q":
            writing()
            writing_guess = ""
          elif writing_guess != correct_study_flashcard_writing.name:
            print("Incorrect.")
            time.sleep(1)
            writing_repeat()

        writing_repeat()
      ENTER = input("")
      if ENTER == "":
        writing()
      elif ENTER == "l":
        home()
    elif study_action == 3:
      os.system("clear")
      print("F L A S H C A R D S", "\n")
      print("A variety of questions will be shown and give the       correct response for all of them.")
      print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
      print("Enter (" + Fore.RED + "l" + Fore.WHITE + ") at any time to leave.")
      print("")
      MC_total = 0
      MC_correct = 0
      writing_total = 0
      writing_correct = 0
      
      while MC_total < 5:
        os.system("clear")
        print("F L A S H C A R D S", "\n")
        study_flashcard_archive = flashcard_archive.copy()
        
        study_flashcard = random.choice(flashcard_archive)
        study_flashcard_archive.remove(study_flashcard)

        study_flashcard2 = random.choice(study_flashcard_archive)
        study_flashcard_archive.remove(study_flashcard2)
  
        study_flashcard3 = random.choice(study_flashcard_archive)
        study_flashcard_archive.remove(study_flashcard3)
          
        study_flashcard4 =     random.choice(study_flashcard_archive)
        study_flashcard_archive.remove(study_flashcard4)

        correct_study_flashcard_MC = random.choice([study_flashcard, study_flashcard2, study_flashcard3, study_flashcard4])

        print(correct_study_flashcard_MC.definition)
        print("")
  
        print(Fore.WHITE + "(" + Fore.RED + "1" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard.name)
        print(Fore.WHITE + "(" + Fore.RED + "2" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard2.name)
        print(Fore.WHITE + "(" + Fore.RED + "3" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard3.name)
        print(Fore.WHITE + "(" + Fore.RED + "4" + Fore.WHITE + ")",   Fore.GREEN, study_flashcard4.name + Fore.WHITE)
        print("")
  
        study_guess_test_MC = input("")

        if study_guess_test_MC == "1" and study_flashcard == correct_study_flashcard_MC:
          MC_total += 1
          MC_correct += 1
        elif study_guess_test_MC == "1" and study_flashcard != correct_study_flashcard_MC:
          MC_total += 1
    
        elif study_guess_test_MC == "2" and study_flashcard2 == correct_study_flashcard_MC:
          MC_total += 1
          MC_correct += 1
        elif study_guess_test_MC == "2" and study_flashcard2 != correct_study_flashcard_MC:
          MC_total += 1
    
        elif study_guess_test_MC == "3" and study_flashcard3 == correct_study_flashcard_MC:
          MC_total += 1
          MC_correct += 1
        elif study_guess_test_MC == "3" and study_flashcard3 != correct_study_flashcard_MC:
          MC_total += 1
    
        elif study_guess_test_MC == "4" and study_flashcard4 == correct_study_flashcard_MC:
          MC_total += 1
          MC_correct += 1
        elif study_guess_test_MC == "4" and study_flashcard4 != correct_study_flashcard_MC:
          MC_total += 1
        else:
          print(Fore.RED, "ERROR", Fore.WHITE)
          time.sleep(1)
          home()
      os.system("clear")
      print("F L A S H C A R D S", "\n")
      print("The definition will be shown and type the corresponding word.")
      print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
      ENTER = input("")
      if ENTER == "":
        while writing_total < 5 and MC_total == 5:
          os.system("clear")
          print("F L A S H C A R D S", "\n")
          correct_study_flashcard_writing = random.choice(flashcard_archive)
          print(correct_study_flashcard_writing.definition)
          writing_guess = input("")
          if writing_guess == correct_study_flashcard_writing.name:
            writing_correct += 1
            writing_total += 1
          if writing_guess != correct_study_flashcard_writing.name:
            writing_total += 1

      os.system("clear")
      print("F L A S H C A R D S", "\n")
      print("Multiple choice correct: " + str(MC_correct) + "/" + str(MC_total))
      print("Writing correct: " + str(writing_correct) + "/" +       str(writing_total))
      print("Click (" + Fore.CYAN + "ENTER" + Fore.WHITE + ") to continue.")
      ENTER = input("")
      if ENTER == "":
        home()

    else:
      print(Fore.RED, "ERROR", Fore.WHITE)
      time.sleep(1)
      home()
    
home()

