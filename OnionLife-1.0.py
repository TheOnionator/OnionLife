import random
import math


WorldList = []
World_Food_Production = 100


def generate_initial_organisms(amount, world_list):

    Gene_Size = 10
    Gene_Movement_Speed = 10
    Gene_Metabolic_Rate = 10
    Gene_Reproduction_Rate = 10
    Gene_Mutation_Rate = 10

    x = range(amount)

    for n in x:
        world_list.append([])

        world_list[n].append([])
        world_list[n].append([])

        world_list[n][0].append("Size")
        world_list[n][0].append(Gene_Size)
        world_list[n][0].append("Movement_Speed")
        world_list[n][0].append(Gene_Movement_Speed)
        world_list[n][0].append("Metabolic_Rate")
        world_list[n][0].append(Gene_Metabolic_Rate)
        world_list[n][0].append("Reproduction_Rate")
        world_list[n][0].append(Gene_Reproduction_Rate)
        world_list[n][0].append("Mutation_Rate")
        world_list[n][0].append(Gene_Mutation_Rate)

        world_list[n][1].append("Health")
        world_list[n][1].append(Gene_Size*10)
        world_list[n][1].append("Food_Consumption")
        world_list[n][1].append((Gene_Size*Gene_Metabolic_Rate + Gene_Movement_Speed)/10)
        world_list[n][1].append("Food_Gathering")
        world_list[n][1].append((Gene_Size/5)*Gene_Movement_Speed)
        world_list[n][1].append("Max_Food_Bar")
        world_list[n][1].append(Gene_Size*50)
        world_list[n][1].append("Food_Bar")
        world_list[n][1].append(Gene_Size*50/2)
        world_list[n][1].append("Life_Span")
        world_list[n][1].append(400/Gene_Metabolic_Rate)
        world_list[n][1].append("Age")
        world_list[n][1].append(0)
        world_list[n][1].append("Generation")
        world_list[n][1].append(0)



generate_initial_organisms(10, WorldList)

print(WorldList)


def evolution(ticks, total_food_production, world_list):

    Time = range(ticks)
    World_Food_Consumption = 0

    born = 0
    died = 0

    for a in Time:
        starvation = 0
        old = 0

        for element in world_list:
            World_Food_Consumption += element[1][3]

        for element in world_list:

            element[1][13] += 1

            if element[1][9] + (element[1][5] - element[1][3]) <= 0:
                world_list.remove(element)
                starvation += 1
                died += 1
            if element[1][13] >= element[1][11]:
                world_list.remove(element)
                old += 1
                died += 1
            else:
                # if there is a surplus food in the world
                if total_food_production > World_Food_Consumption:
                    # if the food bar is less than max
                    if (element[1][9] + (element[1][5] - element[1][3])) < element[1][7]:
                        # add surplus food left over from consumption
                        element[1][9] += (element[1][5] - element[1][3])
                    # if the food bar is full
                    if (element[1][9] + (element[1][5] - element[1][3])) > element[1][7]:


                        Gene_Size = element[0][1]
                        Gene_Movement_Speed = element[0][3]
                        Gene_Metabolic_Rate = element[0][5]
                        Gene_Reproduction_Rate = element[0][7]
                        Gene_Mutation_Rate = element[0][9]

                        Stat_Generation = element[1][15] + 1




                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Size *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Size = 100
                        if Mutagen_Random == 2:
                            Gene_Size *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Size = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Movement_Speed *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Movement_Speed * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Movement_Speed = 100
                        if Mutagen_Random == 2:
                            Gene_Movement_Speed *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Movement_Speed = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Metabolic_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Metabolic_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Metabolic_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Metabolic_Rate = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Reproduction_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Reproduction_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Reproduction_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Reproduction_Rate = 0.1



                        world_list.append([])

                        n = len(world_list)-1

                        world_list[n].append([])
                        world_list[n].append([])

                        world_list[n][0].append("Size")
                        world_list[n][0].append(Gene_Size)
                        world_list[n][0].append("Movement_Speed")
                        world_list[n][0].append(Gene_Movement_Speed)
                        world_list[n][0].append("Metabolic_Rate")
                        world_list[n][0].append(Gene_Metabolic_Rate)
                        world_list[n][0].append("Reproduction_Rate")
                        world_list[n][0].append(Gene_Reproduction_Rate)
                        world_list[n][0].append("Mutation_Rate")
                        world_list[n][0].append(Gene_Mutation_Rate)


                        world_list[n][1].append("Health")
                        world_list[n][1].append(Gene_Size*10)
                        world_list[n][1].append("Food_Consumption")
                        world_list[n][1].append((Gene_Size*Gene_Metabolic_Rate + Gene_Movement_Speed)/10)
                        world_list[n][1].append("Food_Gathering")
                        world_list[n][1].append((Gene_Size/5)*Gene_Movement_Speed)
                        world_list[n][1].append("Max_Food_Bar")
                        world_list[n][1].append(Gene_Size*50)
                        world_list[n][1].append("Food_Bar")
                        world_list[n][1].append(Gene_Size*50/2)
                        world_list[n][1].append("Life_Span")
                        world_list[n][1].append(400/Gene_Metabolic_Rate)
                        world_list[n][1].append("Age")
                        world_list[n][1].append(0)
                        world_list[n][1].append("Generation")
                        world_list[n][1].append(Stat_Generation)

                        element[1][9] = Gene_Size*50/2

                        born += 1

                if World_Food_Consumption > total_food_production:
                    # if the food bar is less than max
                    if (element[1][9] + (element[1][5] - element[1][3])) < element[1][7]:
                        # add surplus food left over from consumption
                        element[1][9] += ((element[1][5] - element[1][3]) * total_food_production/World_Food_Consumption)
                    # if the food bar is full
                    if (element[1][9] + (element[1][5] - element[1][3])) > element[1][7]:


                        Gene_Size = element[0][1]
                        Gene_Movement_Speed = element[0][3]
                        Gene_Metabolic_Rate = element[0][5]
                        Gene_Reproduction_Rate = element[0][7]
                        Gene_Mutation_Rate = element[0][9]

                        Stat_Generation = element[1][15] + 1




                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Size *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Size = 100
                        if Mutagen_Random == 2:
                            Gene_Size *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Size = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Movement_Speed *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Movement_Speed * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Movement_Speed = 100
                        if Mutagen_Random == 2:
                            Gene_Movement_Speed *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Size * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Movement_Speed = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Metabolic_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Metabolic_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Metabolic_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Metabolic_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Metabolic_Rate = 0.1

                        Mutagen_Random = random.randint(1, 4)
                        if Mutagen_Random == 1:
                            Gene_Reproduction_Rate *= (1 + 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 + 1/10*(Gene_Mutation_Rate/10)) > 100:
                            Gene_Reproduction_Rate = 100
                        if Mutagen_Random == 2:
                            Gene_Reproduction_Rate *= (1 - 1/10*(Gene_Mutation_Rate/10))
                        if Gene_Reproduction_Rate * (1 - 1/10*(Gene_Mutation_Rate/10)) < 0.1:
                            Gene_Reproduction_Rate = 0.1



                        world_list.append([])

                        n = len(world_list)-1

                        world_list[n].append([])
                        world_list[n].append([])

                        world_list[n][0].append("Size")
                        world_list[n][0].append(Gene_Size)
                        world_list[n][0].append("Movement_Speed")
                        world_list[n][0].append(Gene_Movement_Speed)
                        world_list[n][0].append("Metabolic_Rate")
                        world_list[n][0].append(Gene_Metabolic_Rate)
                        world_list[n][0].append("Reproduction_Rate")
                        world_list[n][0].append(Gene_Reproduction_Rate)
                        world_list[n][0].append("Mutation_Rate")
                        world_list[n][0].append(Gene_Mutation_Rate)


                        world_list[n][1].append("Health")
                        world_list[n][1].append(Gene_Size*10)
                        world_list[n][1].append("Food_Consumption")
                        world_list[n][1].append((Gene_Size*Gene_Metabolic_Rate + Gene_Movement_Speed)/10)
                        world_list[n][1].append("Food_Gathering")
                        world_list[n][1].append((Gene_Size/5)*Gene_Movement_Speed)
                        world_list[n][1].append("Max_Food_Bar")
                        world_list[n][1].append(Gene_Size*50)
                        world_list[n][1].append("Food_Bar")
                        world_list[n][1].append(Gene_Size*50/2)
                        world_list[n][1].append("Life_Span")
                        world_list[n][1].append(400/Gene_Metabolic_Rate)
                        world_list[n][1].append("Age")
                        world_list[n][1].append(0)
                        world_list[n][1].append("Generation")
                        world_list[n][1].append(Stat_Generation)

                        element[1][9] = Gene_Size*50/2

                        born += 1



        print("Tick", a+1, " - ", len(world_list), "Creatures", World_Food_Consumption, "  ", starvation, "Died of Starvation  ", old, "Died of Old Age")
        World_Food_Consumption = 0


    size_change = 0
    speed_change = 0
    metabolism_change = 0


    if world_list[-1][0][1] > 10:
        size_change = (world_list[-1][0][1] / 10) * 100 - 100
    if world_list[-1][0][1] < 10:
        size_change = (100 - (world_list[-1][0][1] / 10) * 100) * -1

    if world_list[-1][0][3] > 10:
        speed_change = (world_list[-1][0][3] / 10) * 100 - 100
    if world_list[-1][0][3] < 10:
        speed_change = (100 - (world_list[-1][0][3] / 10) * 100) * -1

    if world_list[-1][0][5] > 10:
        metabolism_change = (world_list[-1][0][5] / 10) * 100 - 100
    if world_list[-1][0][5] < 10:
        metabolism_change = (100 - (world_list[-1][0][5] / 10) * 100) * -1

    food_surplus = round(world_list[-1][1][5] / world_list[-1][1][3], 2)
    lifetime_offspring = math.floor(round((world_list[-1][1][5] - world_list[-1][1][3])/(world_list[-1][1][7]/2)*world_list[-1][1][11], 3))

    size_change = round(size_change, 2)
    speed_change = round(speed_change, 2)
    metabolism_change = round(metabolism_change, 2)

    print("")
    print(world_list[-1])
    print("")

    print("Newest Organism", "-", "Generation", world_list[-1][1][15])
    print("Size ", size_change, "%")
    print("Speed ", speed_change, "%")
    print("Metabolism ", metabolism_change, "%")
    print("Food Surplus", str(food_surplus) + "x", " ", "Gain -", round(world_list[-1][1][5] - world_list[-1][1][3], 2))
    print("Lifetime Offspring", lifetime_offspring)

    print("")

    print(born, "Born")
    print(died, "Died")


evolution(1000, World_Food_Production, WorldList)
