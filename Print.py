import matplotlib.pyplot as plt
import numpy as np
import prettytable

from GeneticAlgorithm import NUMBER_OF_ELITE_LECTURES, TOURNAMENT_SELECTION_SIZE, MUTATION_RATE, POPULATION_SIZE


def print_courses(courses):
    available_courses_table = prettytable.PrettyTable(['Course', 'Modul'])
    for i in range(0, len(courses)):
        modules = courses[i].get_modules()
        temp_str = ""
        for j in range(0, len(modules) - 1):
            temp_str += str(modules[j]) + " | "
        temp_str += str(modules[len(modules) - 1])
        available_courses_table.add_row([courses[i].get_name(), temp_str])
    print(available_courses_table)


def print_modules(courses):
    modules_table = prettytable.PrettyTable(['Initials', 'Modul', 'Lecture(s)'])
    for i in range(0, len(courses)):
        dosens = courses[i].get_dosens()
        temp_str = ""
        for j in range(0, len(dosens) - 1):
            temp_str += str(dosens[j]) + " | "
        temp_str += str(dosens[len(dosens) - 1])
        modules_table.add_row(
            [courses[i].get_number(), courses[i].get_name(), temp_str])
    print(modules_table)


def print_dosens(instructors):
    available_dosens_table = prettytable.PrettyTable(['Initials', 'Lecturer'])
    for i in range(0, len(instructors)):
        available_dosens_table.add_row([instructors[i].get_id(), instructors[i].get_name()])
    print(available_dosens_table)


def print_meeting_times(meeting_times):
    available_meeting_time_table = prettytable.PrettyTable(['Block', 'Time'])
    for i in range(0, len(meeting_times)):
        available_meeting_time_table.add_row([meeting_times[i].get_id(), meeting_times[i].get_time()])
    print(available_meeting_time_table)


def print_generation(schedules):
    generation_table = prettytable.PrettyTable(
        ['#', 'Fitness', 'Number of conflicts', 'Variables [Course, Modul, Room, Lecturer, Time]'])

    for i in range(0, len(schedules)):
        generation_table.add_row([str(i), round(schedules[i].get_fitness(), 3), schedules[i].get_number_of_conflicts(),
                                  schedules[i]])
    print(generation_table)


def print_room(rooms):
    available_rooms_table = prettytable.PrettyTable(['Room ID', 'Capacity'])
    for i in range(0, len(rooms)):
        available_rooms_table.add_row([str(rooms[i].get_number()), str(rooms[i].get_seating_capacity())])
    print(available_rooms_table)


def print_schedule_as_table(schedule):
    classes = schedule.get_lectures()
    table = prettytable.PrettyTable(
        ['Sessions', 'Course (Number of Students)', 'Modul (Initials)', 'Room ID (Capacity)', 'Lecturer (Initials)',
         'Time (Block)'])
    for i in range(0, len(classes)):
        table.add_row([
            str(i),
            classes[i].get_course().get_name() + " (" +
            str(classes[i].get_course().get_number_of_students()) + ")",

            classes[i].get_module().get_name() + " (" +
            classes[i].get_module().get_number() + ")",

            classes[i].get_room().get_number() + " (" + str(
                classes[i].get_room().get_seating_capacity()) + ")",

            classes[i].get_dosen().get_name() + " (" + str(
                classes[i].get_dosen().get_id()) + ")",

            classes[i].get_meeting_time().get_time() + " (" + str(
                classes[i].get_meeting_time().get_id()) + ")"])
    print(table)


def print_current_population(population, generation_number):
    print("\n> Generation # " + str(generation_number))
    print_generation(population.get_schedules())
    print_schedule_as_table(population.get_schedules()[0])


def plot_diagram(conflicts):
    plt.plot(conflicts)
    plt.ylabel("Number of Conflicts")
    plt.yticks(np.arange(0, conflicts[0] + 1, step=1))
    plt.xlabel("Generations")
    plt.Text("NUMBER_OF_ELITE_LECTURES: " + str(NUMBER_OF_ELITE_LECTURES))
    plt.Text("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    plt.Text("MUTATION_RATE: " + str(MUTATION_RATE))
    plt.Text("POPULATION_SIZE: " + str(POPULATION_SIZE))
    plt.show()


def print_stats(generation_number, conflicts, data):
    print("\n")
    print("Generations needed: " + str(generation_number))
    print("--")
    print("Inputs used:")
    print("Number of Lecturers: " + str(len(data.get_dosens())))
    print("Number of Courses: " + str(len(data.get_courses())))
    print("Number of Time Slots: " + str(len(data.get_meeting_times())))
    print("Number of Module: " + str(len(data.get_modules())))
    print("--")
    print("Parameters for the genetic algorithm:")
    print("NUMBER_OF_ELITE_LECTURES: " + str(NUMBER_OF_ELITE_LECTURES))
    print("TOURNAMENT_SELECTION_SIZE: " + str(TOURNAMENT_SELECTION_SIZE))
    print("MUTATION_RATE: " + str(MUTATION_RATE))
    print("POPULATION_SIZE: " + str(POPULATION_SIZE))
    print("--")
    plot_diagram(conflicts)


def print_available_data(data):
    print("> All available data")
    print_courses(data.get_courses())
    print_modules(data.get_modules())
    print_dosens(data.get_dosens())
    print_room(data.get_rooms())
    print_meeting_times(data.get_meeting_times())
